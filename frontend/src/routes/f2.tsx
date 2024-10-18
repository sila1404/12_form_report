import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { createFileRoute } from "@tanstack/react-router"
import ReportHeader from "@/components/ReportHeader";

export const Route = createFileRoute('/f2')({
  component: ReportF2
})

function ReportF2() {
  return (
    <main className="flex justify-center pt-7">
      <div className="grid place-items-center w-8/12 p-8 shadow-lg border-2 border-neutral-800">
        <ReportHeader reportMessage="ຂໍ້ມູນຖານະການເງິນ" />
        <Table className="border border-neutral-800 shadow-xl">
          <TableHeader>
            <TableRow className="divide-x border border-neutral-800 divide-y divide-neutral-800">
              <TableHead className="text-center font-bold">ລາຍການ</TableHead>
              <TableHead className="text-center font-bold">
                ຈໍານວນເງິນ (ກີບ)
              </TableHead>
            </TableRow>
          </TableHeader>
          <TableBody className="divide-y divide-neutral-800">
            {/* start report 1 */}
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
            {/* end report 1 */}
            {/* start report 2 */}
            <TableRow className="bg-slate-300 divide-x divide-neutral-800 font-bold">
              <TableCell>2. ໜີ້ຕ້ອງຮັບຈາກສະຖາບັນການເງິນອື່ນ</TableCell>
              <TableCell className="text-right">Total</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>2.1 ເງິນຝາກບໍ່ມີກຳນົດ</TableCell>
              <TableCell className="text-right">1.132.541.000</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>2.2 ເງິນຝາກມີກຳນົດ</TableCell>
              <TableCell className="text-right">2.324.000</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>2.3 ເງິນໃຫ້ກູ້ຢືມ ແລະ ເງິນລ່ວງໜ້າສຸດທິ</TableCell>
              <TableCell className="text-right">12.232.458.000</TableCell>
            </TableRow>
            {/* end report 2 */}
            {/* start report 3 */}
            <TableRow className="bg-slate-300 divide-x divide-neutral-800 font-bold">
              <TableCell>3. ຫຼັກຊັບຊື້ໂດຍມີສັນຍາຂາຍຄືນ</TableCell>
              <TableCell className="text-right">Total</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>3.1 ຫຼັກຊັບຊື້ໂດຍມີສັນຍາຂາຍຄືນ</TableCell>
              <TableCell className="text-right">1.132.541.000</TableCell>
            </TableRow>
            <TableRow className="divide-x divide-neutral-800">
              <TableCell>3.2 ໜີ້ຕ້ອງຮັບທວງຍາກ ແລະ ລາຍການອື່ນໆ</TableCell>
              <TableCell className="text-right">2.324.000</TableCell>
            </TableRow>
            {/* end report 3 */}
          </TableBody>
        </Table>
      </div>
    </main>
  );
}

