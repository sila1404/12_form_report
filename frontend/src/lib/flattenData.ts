import { ReportResponseType } from "@/routes/f9";

export function flatten2ColumnsData(data: ReportResponseType) {
  const result: any[] = [];
  data?.data.forEach((detail) => {
    result.push({
      Item: detail[0],
      "Amount (KIP)": detail[1],
    });
  });

  return result;
}
