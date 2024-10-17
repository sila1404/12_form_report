import {
  Table,
  TableBody,
  TableCell,
  TableRow,
  TableHeader,
  TableHead,
} from "./components/ui/table";
import ReportHeader from "./components/ReportHeader";

function App() {
  return (
    <main className="flex justify-center pt-7">
      <div className="grid place-items-center w-8/12 p-8 shadow-lg border-2 border-neutral-800">
        <ReportHeader reportMessage="ຂໍ້ມູນຖານະການເງິນ"/>
        <Table className="border border-neutral-800 shadow-xl">
          <TableHeader>
            <TableRow className="divide-x border border-neutral-800 divide-y divide-neutral-800">
              <TableHead className="text-center font-bold">ລາຍການ</TableHead>
              <TableHead className="text-center font-bold">ຈໍານວນເງິນ (ກີບ)</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow className="bg-slate-300 border border-neutral-800 divide-x divide-neutral-800 font-bold">
              <TableCell>1. ເງິນສົດ ແລະ ເງິນຝາກຢູ່ທະນາຄານກາງ</TableCell>
              <TableCell className="text-right">Total</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>1.1 ເງິນສົດ ແລະ ທີ່ຖືວ່າຄືເງິນສົດ</TableCell>
              <TableCell className="text-right">1.132.541.000</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>1.2 ເງິນຝາກບໍ່ມີກຳນົດ</TableCell>
              <TableCell className="text-right">2.324.000</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>1.3 ເງິນຝາກມີກຳນົດ</TableCell>
              <TableCell className="text-right">12.232.458.000</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </div>
    </main>
  );
}

export default App;
