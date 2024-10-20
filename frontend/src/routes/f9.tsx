import ReportHeader from "@/components/ReportHeader";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { createFileRoute } from "@tanstack/react-router";
import axios from "axios";
import { useState, useEffect } from "react";

import { formatNumber } from "@/lib/formatNumberWithCommas";
import DownloadButton from "@/components/DownloadButton";

export const Route = createFileRoute("/f9")({
  component: ReportF9,
});

type ReportF9Response = {
  Account_Code: number;
  Item: string;
  Balance_Forward_Debit: number;
  Balance_Forward_Credit: number;
  Movement_in_the_month_Debit: number;
  Movement_in_the_month_Credit: number;
  Closing_Balance_Debit: number;
  Closing_Balance_Credit: number;
};

function ReportF9() {
  const [reportData, setReportData] = useState<ReportF9Response[]>();

  useEffect(() => {
    const getF9Report = async () => {
      const { data, status } = await axios.get(
        "http://127.0.0.1:8000/reports/f9"
      );

      if (status === 200) {
        setReportData(data);
      }
    };

    getF9Report();
  }, []);

  return (
    <>
    <main className="flex justify-center pt-7">
    <div className="grid place-items-center w-9/12 p-8 shadow-lg border-2 border-neutral-800">
      <ReportHeader reportMessage="ຂໍ້ມູນການດຸ່ນດ່ຽງບັນຊີ 06 ຫ້ອງ" />
      <Table className="border border-neutral-800 shadow-xl">
        <TableHeader>
          <TableRow className="divide-x border border-neutral-800 divide-y divide-neutral-800">
            <TableHead className="text-center font-bold">
              Account Code
            </TableHead>
            <TableHead className="text-center font-bold">Item</TableHead>
            <TableHead className="text-center font-bold">
              Balance Forward Debit
            </TableHead>
            <TableHead className="text-center font-bold">
              Balance Forward Credit
            </TableHead>
            <TableHead className="text-center font-bold">
              Movement in the month Debit
            </TableHead>
            <TableHead className="text-center font-bold">
              Movement in the month Credit
            </TableHead>
            <TableHead className="text-center font-bold">
              Closing Balance Debit
            </TableHead>
            <TableHead className="text-center font-bold">
              Closing Balance Credit
            </TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {reportData?.map((data, index) => (
            <TableRow key={index} className="divide-x divide-neutral-800">
              <TableCell>{data.Account_Code}</TableCell>
              <TableCell>{data.Item}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Balance_Forward_Debit)}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Balance_Forward_Credit)}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Movement_in_the_month_Debit)}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Movement_in_the_month_Credit)}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Closing_Balance_Debit)}</TableCell>
              <TableCell className="text-right">{formatNumber(data.Balance_Forward_Credit)}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      </div>
      <DownloadButton data={reportData} fileName="Report_F02" sheetName="Report F2" />
    </main>
    </>
  );
}
