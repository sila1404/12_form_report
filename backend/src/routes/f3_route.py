from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
import pandas as pd
from services import F3

f3_route = APIRouter(prefix="/reports")

@f3_route.get("/f3")
def get_f3_report(req: Request):
    """
    Retrieve the F3 report based on the uploaded DataFrame.

    Returns:
        JSON response containing the F3 report data.
    """
    df_report: pd.DataFrame = getattr(req.app.state, "df_report", None)

    # Check if the DataFrame exists
    if df_report is None:
        return JSONResponse(
            content={"error": "No report available. Please upload the file first."},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    
    f3 = F3(df_report)
    

    try:
        f3_report1 = f3.first_report()
        total = f3_report1['total']
        report_1 = f3_report1['report_1']
        report_2 = f3_report2['report_2']

        f3_report2 = f3.second_report()
        total_2 = f3_report2['total']
        report_2_1 = f3_report2['report_1']
        report_2_2 = f3_report2['report_2']
        report_2_4 = f3_report2['report_4']

        f3_report9 = f3.nineth_report()
        total_9 = f3_report9['total']
        report_9_2 = f3_report9['report_2'] 

        f3_report10 = f3.tenth_report()
        total_10 = f3_report10['total']
        report_10_1 = f3_report10['report1']

        f3_report15 = f3.fifteenth_report()
        total_15 = f3_report15['total']
        report_15_2 = f3_report15['report_2']
        report_15_3 = f3_report15['report_3']
        report_15_4 = f3_report15['report_4']

        f3_report16 = f3.sixteenth_report()
        total_16 = f3_report16['total']
        report_16_1 = f3_report16['report_1']
        report_16_2 = f3_report16['report_2']

        f3_report17 = f3.seventeenth_report()
        total_17 = f3_report17['total']
        report_17_1 = f3_report17['report_1']

        f3_report18 = f3.eigthteenth_report()
        total_18  = f3_report18['total']
        report_18_1 = f3_report18['report_1']
        report_18_2 = f3_report18['report_2']
        reprot_18_3 = f3_report18['report_3']

        f3_report19 = f3.nineteenth_report()
        total_19 = f3_report19['total']
        report_19_1 = f3_report19['report_1']
        reprot_19_2 = f3_report19['report_2']

        f3_report21 = f3.twenty_first_report()
        total_21 = f3_report21['total']
        report_21_1 = f3_report21['report_1']

        response_data = {
        "colums": ["ລາຍການ", "ຈຳນວນເງິນ (ກີບ)"],
        "data":[
             ["1. ລາຍຮັບດອກເບ້ຍ ແລະ ທີ່ຖືຄືວ່າດອກເບ້ຍ",total],
             ["1.1 ລາຍຮັບຈາກການເຄື່ອນໄຫວລະຫວ່າງທະນາຄານ",report_1],
             ["1.2 ລາຍຮັບຈາກການເຄື່ນໄຫວຈາກລູກຄ້າ", report_2],
             ["1.3 ລາຍຮັບຈາກຫຼັກຊັບຊື້ໂດຍມີສັນຍາຂາຍຄືນ", 0],
             ["1.4 ລາຍຮັບຈາກການລົງທຶນໃນຫຼັກຊັບທີ່ໃຫ້ລາຍໄດ້ຄົງທີ່",0],
             ["1.5 ລາຍດອກເບ້ຍ ແລະ ທີ່ຖືວ່າຄືດອກເບ້ຍອື່ນໆ", 0],

             ["2. ລາຍຈ່າຍດອກເບ້ຍ ແລະ ທີ່ຖືວ່າຄືດອກເບ້ຍ",total_2],
             ["2.1 ລາຍຈ່າຍໃນການເຄື່ອນໄຫວລະຫວ່າງທະນາຄານ", report_2_1],
             ["2.2 ລາຍຈ່າຍໃນການເຄື່ອນໄຫວກັບລູກຄ້າ",report_2_2 ],
             ["2.3 ລາຍຈ່າຍໃນການຂາຍຫຼັກຊັບໂດຍມີສັນຍາຊື້ຄືນ",0 ],
             ["2.4 ລາຍຈ່າຍໃນການຈຳໜ່າຍຮຸ້ນກູ້ ແລະ ໃບຢັ້ງຢືນກູ້ຢືມເງິນ", report_2_4],
             ["2.5 ດອກເບ້ຍ ແລະ ທີ່ຖືວ່າຄືດອກເບ້ຍອື່ນໆ", 0 ],

             ["3. ກຳໄລ ຫຼື ຂາດທຶນສຸດທິກ່ຽວກັບການຊື້ຂາຍຄໍາ (+/-)", 0 ],
             ["3.1 ລາຍຮັບທີ່ພົວພັນກັບວັດຖຸມີຄ່າ", 0],
             ["3.2 ລາຍຈ່າຍກ່ຽວກັບຄໍາ ແລະ ວັດຖຸມີຄ່າ", 0 ],

             ["4. ລາຍຮັບຈາກສິນເຊື່ອເຊົ່າຊື້ ແລະ ໃຫ້ເຊົ່າໂດຍມີທາງເລືອກຊື້", 0],
             ["4.1 ລາຍຮັບຈາກສິນເຊື່ອເຊົ່າຊື້້",0] ,
             ["4.2 ກ່ຽວກັບສິນເຊື່ອເຊົ່າຊື້",0],
             
             ["5. ລາຍຈ່າຍກ່ຽວກັບສິນເຊື່ອເຊົ່າຊື້ ແລະ ໃຫ້ເຊົ່າໂດຍມີທາງເລືອກຊື້ (-)",0],
             [" 5.1 ລາຍຈ່າຍກ່ຽວກັບສິນເຊື່ອເຊົ່າຊື້ ",0],

             ["6. ລາຍຮັບຈາກການໃຫ້ເຊົ່າທຳມະດາ", 0 ],
             ["6.1 ລາຍຮັບຈາກການໃຫ້ເຊົ່າທຳມະດາ",0 ],
             ["6.2 ກ່ຽວກັບການໃຫ້ເຊົ່າທໍາມະດາ", 0 ],

             ["7. ລາຍຈ່າຍກ່ຽວກັບການໃຫ້ເຊົ່າທຳມະດາ (-)",0],
             [" 7.1 ລາຍຈ່າຍກ່ຽວກັບການໃຫ້ເຊົ່າທຳມະດາ",0],
            
             ["8. ລາຍຮັບເງິນປັນຜົນ",0],
             ["8.1 ເງິນປັນຜົນ ແລະ ລາຍຮັບປະເພດດຽວກັນ",0],
             ["8.2 ເງິນປັນຜົນຈາກເງິນໃຫ້ກູ້ຢຶມສໍາຮອງ",0],

             ["9. ລາຍຮັບຄ່າທຳນຽມ ແລະ ຄ່າບໍລິການການເງິນ",total_9],
             ["9.1 ລາຍຮັບຄ່າທຳນຽມທີ່ພົວພັນກັບການເຄື່ອນໄຫວລະຫວ່າງສະຖາບັນການເງິນ",0],
             ["9.2 ລາຍຮັບຄ່າທຳນຽມທີ່ພົວພັນກັບການເຄື່ອນໄຫວກັບລູກຄ້າ",report_9_2],
             ["9.3 ລາຍຮັບຄ່າທຳນຽມຕ່າງໆກ່ຽວກັບຫຼັກຊັບ ແລະ ເອກະສານອະນຸພັນ",0],
             ["9.4 ລາຍຮັບຄ່າທຳນຽມໃນການແລກປ່ຽນເງິນຕາຕ່າງປະເທດ",0],
             ["9.5 ລາຍຮັບຈາກການບໍລິການທາງດ້ານການເງິນ",0],

             ["10. ລາຍຈ່າຍຄ່າທຳນຽມ ແລະ ຄ່າບໍລິການການເງິນ (-)",total_10],
             ["10.1 ລາຍຈ່າຍຄ່າທຳນຽມທີ່ພົວພັນກັບການເຄື່ອນໄຫວລະຫວ່າງສະຖາບັນການເງິນ",report_10_1],
             ["10.2 ລາຍຈ່າຍຄ່າທຳນຽມທີ່ພົວພັນກັບການເຄື່ອນໄຫວກັບລູກຄ້າ", 0],
             ["10.3 ລາຍຈ່າຍຄ່າທຳນຽມຕ່າງໆກ່ຽວກັບຫຼັກຊັບ ແລະ ເອກະສານອະນຸພັນ",0],
             ["10.4 ລາຍຈ່າຍຄ່າທຳນຽມໃນການແລກປ່ຽນເງິນຕາຕ່າງປະເທດ",0],
             ["10.5 ລາຍຈ່າຍຈາກການບໍລິການທາງດ້ານການເງິນ",0],

             ["11. ກຳໄລ ຫຼື ຂາດທຶນຈາກຫຼັກຊັບເພື່ອຄ້າ (+/-)",0],
             ["11.1 ລາຍຮັບກ່ຽວກັບຫຼັກຊັບເພື່ອຄ້າ",0],
             ["11.2 ລາຍຈ່າຍກ່ຽວກັບຫຼັກຊັບເພື່ອຄ້າ",0],

             ["12. ກຳໄລ ຫຼື ຂາດທຶນຈາກຫຼັກຊັບຊື້ເພື່ອຂາຍ (+/-)",0],
             ["12.1 ລາຍຮັບກ່ຽວກັບຂາຍຫຼັກຊັບຊື້ເພື່ອຂາຍ",0],
             ["12.2 ລາຍຈ່າຍກ່ຽວກັບຂາຍຫຼັກຊັບຊື້ເພື່ອຂາຍ",0],

             ["13. ກຳໄລ ຫຼື ຂາດທຶນຈາກການແລກປ່ຽນເງິນຕາຕ່າງປະເທດ (+/-)",0],
             ["13.1 ກໍາໄລຈາກການແລກປ່ຽນເງິນຕາຕ່າງປະເທດ",0],
             ["13.2 ຂາດທຶນຈາກການແລກປ່ຽນເງິນຕາຕ່າງປະເທດ",0],

             ["14. ກຳໄລ ຫຼື ຂາດທຶນຈາກເຄື່ອງມືອະນຸພັນ (+/-)",0],
             ["14.1 ລາຍຮັບທີ່ພົວພັນກັບເອກະສານອະນຸພັນ",0],
             ["14.2 ລາຍຈ່າຍກ່ຽວກັບເອກະສານການເງິນມີກໍານົດ",0],

             ["15. ລາຍຮັບອື່ນໆໃນທຸລະກິດ",total_15],
             ["15.1 ລາຍຮັບຈາກຄໍາໝັ້ນສັນຍາດ້ານຫຼັກຊັບ ແລະ ຄໍາໝັ້ນສັນຍາອື່ນໆ",0],
             ["15.2. ລາຍຮັບອື່ນໆຈາກການທຸລະກິດສະຖາບັນການເງິນ",report_15_2],
             [""]

        ]
        }

        