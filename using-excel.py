import xlrd
book = xlrd.open_workbook("using-excel.xls")
sheet = book.sheet_by_index(0)

for i in range(0, 13):
    print(sheet.cell_value(0, i), end='')
