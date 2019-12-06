import xlrd
workbook = xlrd.open_workbook('demo.xls')
# 输出所有 sheet 的名字
sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
# 获取第 2 行内容
print(sheet1.row_values(0))
# 获取第 3 列内容
print(sheet1.col_values(2))
date_value = xlrd.xldate_as_datetime(sheet1.cell_value(5, 3), workbook.datemode)
print(type(date_value), date_value)