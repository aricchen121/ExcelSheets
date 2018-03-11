import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

# get cell A1 and its value
print (sheet['A1'])
print (sheet['A1'].value)

#get cell B1 and its value
#print Apples
c = sheet['B1']
print (c.value)

print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)