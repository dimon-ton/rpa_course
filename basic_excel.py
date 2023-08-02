from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import subprocess

exel_file = Workbook()
work_sheet = exel_file.active

data = [['ชนิด', 'สีใบ', 'ความสูง'], 
        ['ต้นมะม่วง', 'สีเขียว', 5],
        ['ต้นกล้วย', 'สีเหลือง', 3],
        ['ต้นซากุระ', 'สีม่วง', 4]]

for d in data:
    work_sheet.append(d)


value = Reference(work_sheet, min_col=3, max_col=3, min_row=2, max_row=4)
cat = Reference(work_sheet, min_col=1, max_col=1, min_row=2, max_row=4)

chart = BarChart()
chart.title = "ความสูงของต้นไม้"
chart.y_axis.title = 'ความสูงของต้นไม้ (เมตร)'
chart.x_axis.title = 'ชนิดของต้นไม้'
chart.legend = None




chart.add_data(value)
work_sheet.add_chart(chart, 'E5')

chart.set_categories(cat)


exel_file.save('basic_excel.xlsx')


# open file
subprocess.Popen('basic_excel.xlsx', shell=True)