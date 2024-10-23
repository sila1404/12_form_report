import { useEffect, useState } from "react";
import { createFileRoute } from "@tanstack/react-router";
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

import { ReportResponseType } from "./f9";

import { getReportData } from "@/lib/getReportData";
import { formatNumber } from "@/lib/formatNumberWithComma";

export const Route = createFileRoute("/f2")({
  component: () => {
    const [reportData, setReportData] = useState<ReportResponseType>();
    const [errMsg, setErrMsg] = useState("");

    useEffect(() => {
      const fetchData = async () => {
        const result = await getReportData("/f2");
        if (result.status === 200) {
          setReportData(result.data);
        } else {
          setErrMsg(result.message);
        }
      };

      fetchData();
    }, []);

    if (!reportData) {
      return <div>{errMsg}</div>;
    }

    function flattenData(data: ReportResponseType) {
      const result: any[] = [];
      data?.data.forEach((detail) => {
        result.push({
          Item: detail[0],
          "Amount (KIP)": detail[1],
        });
      });

      return result;
    }

    return (
      <main className="flex justify-center pt-7">
        <div className="grid place-items-center w-9/12 p-8 shadow-lg border-2 border-neutral-800">
          <ReportHeader reportMessage="ຂໍ້ມູນຖານະການເງິນ" />
          <Table className="border border-neutral-800 shadow-xl">
            <TableHeader>
              <TableRow className="divide-x border border-neutral-800 divide-y divide-neutral-800">
                {reportData?.columns.map((colmunsName, index) => (
                  <TableHead key={index} className="text-center font-bold">
                    {colmunsName}
                  </TableHead>
                ))}
              </TableRow>
            </TableHeader>
            <TableBody>
              {reportData?.data.map((data, index) => (
                <TableRow
                  key={index}
                  className="border border-neutral-800 divide-x divide-neutral-800"
                >
                  {data.map((detail, index) => (
                    <TableCell
                      key={index}
                      className={
                        typeof detail === "number" ? "text-right" : "text-left"
                      }
                    >
                      {typeof detail === "number"
                        ? formatNumber(detail)
                        : detail}
                    </TableCell>
                  ))}
                </TableRow>
              ))}
            </TableBody>
          </Table>
          <DownloadButton
            data={flattenData(reportData)}
            fileName="Report_F2"
            sheetName="Report F2"
          />
        </div>
      </main>
    );
  },
});
