import openpyxl
# see excel file
wb = openpyxl.load_workbook('example.xlsx')
print (type(wb))