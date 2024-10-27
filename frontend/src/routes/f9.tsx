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

import { formatNumber } from "@/lib/formatNumberWithComma";
import { getReportData } from "@/lib/getReportData";
import { flatten8ColumnsData } from "@/lib/flattenData";

export type ReportResponseType = {
  columns: Array<string>;
  data: Array<Array<string | number>>;
};

export const Route = createFileRoute("/f9")({
  loader: async () => {
    const result = await getReportData("/f9");

    return {
      reportData: result.data.response_data as ReportResponseType,
      message: result.data.message,
    };
  },
  component: () => {
    const { reportData, message } = Route.useLoaderData();

    if (!reportData) {
      return <div>{message}</div>;
    }

    return (
      <>
        <main className="flex justify-center pt-7">
          <div className="grid place-items-center w-9/12 p-8 shadow-lg border-2 border-neutral-800">
            <ReportHeader reportMessage="ຂໍ້ມູນການດຸ່ນດ່ຽງບັນຊີ 06 ຫ້ອງ" />
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
                {reportData?.data.map((data, rowIndex) => (
                  <TableRow
                    key={rowIndex}
                    className="divide-x divide-neutral-800"
                  >
                    {data.map((detail, colIndex) => (
                      <TableCell
                        key={colIndex}
                        className={
                          typeof detail === "number" && colIndex !== 0
                            ? "text-right"
                            : "text-left"
                        }
                      >
                        {typeof detail === "number" && colIndex !== 0
                          ? formatNumber(detail)
                          : detail}
                      </TableCell>
                    ))}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
          <DownloadButton
            data={flatten8ColumnsData(reportData)}
            fileName="Report_F09"
            sheetName="Report F9"
          />
        </main>
      </>
    );
  },
});
