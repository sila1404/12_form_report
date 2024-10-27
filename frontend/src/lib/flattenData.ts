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

export function flatten8ColumnsData(data: ReportResponseType) {
  const result: any[] = [];
  data?.data.forEach((detail) => {
    result.push({
      "Account Code": detail[0],
      Item: detail[1],
      "Balance Forward Debit": detail[2],
      "Balance Forward Credit": detail[3],
      "Movement in the month Debit": detail[4],
      "Movement in the month Credit": detail[5],
      "Closing Balance Debit": detail[6],
      "Closing Balance Credit": detail[7],
    });
  });

  return result;
}
