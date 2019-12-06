import matplotlib.pyplot as plt
import xlwings as xw

wb = xw.Book()  # 创建新的工作簿
sht = wb.sheets['sheet1']
# wb = xw.Book('demo.xlsx')  # 连接当前工作路径的工作簿
# # wb = xw.Book(r'C:\path\to\file.xlsx')  # Windows下用raw string构建路径连接指定工作簿
# sht = wb.sheets['test_sheet']
# sht.range('A1').value = 'Foo 1'
# print(sht.range('A1').value) # Foo 1

# print(wb)
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)

wb.save('test.xlsx')
wb.close()
