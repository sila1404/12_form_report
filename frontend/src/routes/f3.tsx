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
import { ReportResponseType } from "./f9";
import { getReportData } from "@/lib/getReportData";
import { formatNumber } from "@/lib/formatNumberWithComma";
import { flatten2ColumnsData } from "@/lib/flattenData";
import DownloadButton from "@/components/DownloadButton";

export const Route = createFileRoute("/f3")({
  loader: async () => {
    const result = await getReportData("/f3");

    return {
      reportData: result.data.response_data as ReportResponseType,
      message: result.data.message,
    };
  },
  component: () => {
    const { message, reportData } = Route.useLoaderData();

    if (!reportData) {
      return <div>{message}</div>;
    }


    return (
      <main className="flex justify-center pt-7">
        <div className="grid place-items-center w-9/12 p-8 shadow-lg border-2 border-neutral-800">
          <ReportHeader reportMessage="ຂໍ້ມູນຜົນການດໍາເນີນງານ" />
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
            data={flatten2ColumnsData(reportData)}
            fileName="Report_F3"
            sheetName="Report F3"
          />
        </div>
      </main>
    );
  },
});
