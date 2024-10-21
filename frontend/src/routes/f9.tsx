import { useEffect, useState } from "react";
import { createFileRoute } from "@tanstack/react-router";
import axios from "axios";
import ReportHeader from "@/components/ReportHeader";
import DownloadButton from "@/components/DownloadButton";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import { formatNumber } from "@/lib/formatNumberWithComma";

export const Route = createFileRoute("/f9")({
  component: ReportF9,
});

type ReportF9Response = {
  Account_Code: number[];
  Item: string[];
  Balance_Forward_Debit: number[];
  Balance_Forward_Credit: number[];
  Movement_in_the_month_Debit: number[];
  Movement_in_the_month_Credit: number[];
  Closing_Balance_Debit: number[];
  Closing_Balance_Credit: number[];
};

function ReportF9() {
  const [reportData, setReportData] = useState<ReportF9Response>();
  const [errMsg, setErrMsg] = useState("");

  useEffect(() => {
    const getF9Report = async () => {
      try {
        const { data, status } = await axios.get(
          "http://127.0.0.1:8000/reports/f9"
        );

        if (status === 200) {
          setReportData(data);
        }
      } catch (error) {
        if (axios.isAxiosError(error) && error.response) {
          setErrMsg(error.response.data.error);
        }
      }
    };

    getF9Report();
  }, []);

  if (!reportData) {
    return <div>{errMsg}</div>;
  }

  // Get the headers from the object keys (as strings)
  const headers = Object.keys(reportData) as Array<keyof ReportF9Response>;

  function flattenData(data: ReportF9Response | undefined) {
    return data?.Account_Code.map((_, i) => ({
      "Account Code": data.Account_Code[i],
      Item: data.Item[i],
      "Balance Forward Debit": data.Balance_Forward_Debit[i],
      "Balance Forward Credit": data.Balance_Forward_Credit[i],
      "Movement in the month Debit": data.Movement_in_the_month_Debit[i],
      "Movement in the month Credit": data.Movement_in_the_month_Credit[i],
      "Closing Balance Debit": data.Closing_Balance_Debit[i],
      "Closing Balance Credit": data.Closing_Balance_Credit[i],
    }));
  }

  return (
    <>
      <main className="flex justify-center pt-7">
        <div className="grid place-items-center w-9/12 p-8 shadow-lg border-2 border-neutral-800">
          <ReportHeader reportMessage="ຂໍ້ມູນການດຸ່ນດ່ຽງບັນຊີ 06 ຫ້ອງ" />
          <Table className="border border-neutral-800 shadow-xl">
            <TableHeader>
              <TableRow className="divide-x border border-neutral-800 divide-y divide-neutral-800">
                {headers.map((header, idx) => (
                  <TableHead className="text-center font-bold" key={idx}>
                    {header.replace(/_/g, " ")}
                  </TableHead>
                ))}
              </TableRow>
            </TableHeader>
            <TableBody>
              {reportData?.Account_Code.map((_, rowIndex) => (
                <TableRow
                  key={rowIndex}
                  className="divide-x divide-neutral-800"
                >
                  {headers.map((header, colIndex) => (
                    <TableCell
                      key={header}
                      className={
                        typeof reportData[header][rowIndex] === "number" &&
                        colIndex !== 0
                          ? "text-right"
                          : "text-left"
                      }
                    >
                      {typeof reportData[header][rowIndex] === "number" &&
                      colIndex !== 0
                        ? formatNumber(reportData[header][rowIndex])
                        : reportData[header][rowIndex]}
                    </TableCell>
                  ))}
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
        <DownloadButton
          data={flattenData(reportData)}
          fileName="Report_F09"
          sheetName="Report F9"
        />
      </main>
    </>
  );
}
