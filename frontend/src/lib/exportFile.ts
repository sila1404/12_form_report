import * as XLSX from "xlsx"
import { saveAs } from "file-saver"

export function exportToExcel(data: any, sheetName:string, fileName: string) {
  // Convert JSON data to a sheet
  const worksheet = XLSX.utils.json_to_sheet(data);

  // Create a workbook and add the worksheet
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, `${sheetName}`);

  // Export the Excel file
  XLSX.writeFile(workbook, `${fileName}.xlsx`);
};

export function exportToCSV(data: any, fileName: string) {
    // Convert JSON data to a sheet
    const worksheet = XLSX.utils.json_to_sheet(data);

    // Convert worksheet data to CSV
    const csv = XLSX.utils.sheet_to_csv(worksheet)
    
    // Add BOM (Byte Order Mark) for UTF-8
    const bom = '\uFEFF'; // UTF-8 BOM
    const csvWithBOM = bom + csv;
  
    // Export the CSV file
    saveAs(new Blob([csvWithBOM], {type: "text/csv;charset=utf-8;"}), `${fileName}.csv`)
}