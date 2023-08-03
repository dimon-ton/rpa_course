from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import subprocess
import random
import os

excel_folder = os.path.join(os.getcwd(), 'excel_file')

for i in range(1, 101):

    exel_file = Workbook()
    work_sheet = exel_file.active


    data = [['ชนิด', 'สีใบ', 'ความสูง'], 
            ['ต้นมะม่วง', 'สีเขียว', random.randint(3,30)],
            ['ต้นกล้วย', 'สีเหลือง', random.randint(3,30)],
            ['ต้นซากุระ', 'สีม่วง', random.randint(3,30)]]

    for d in data:
        work_sheet.append(d)


  

    number = i

    excel_name = 'data_no_graph{}.xlsx'.format(number)
    excel_path = os.path.join(excel_folder, excel_name)

    exel_file.save(excel_path)
