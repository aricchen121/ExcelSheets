import openpyxl
# Look at sheets in excel file
wb = openpyxl.load_workbook('example.xlsx')
print (wb.sheetnames)

# Find name of third worksheet
sheet = wb['Sheet3']
print (sheet)

#Find only name of third worksheet
print(sheet.title)

# Show active sheet in excel
anotherSheet = wb.active
print (anotherSheet)