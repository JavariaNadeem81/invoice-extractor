import pandas as pd
 #create simple dataframe
data = {
        'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
        'Product': ['Widget A', 'Widget B', 'Widget C', 'Widget D', 'Widget E'],
        'Sales': [1200.50, 850.00, 2100.75, 4500.25, 3000.00],
        'Quantity': [10, 5, 18, 20, 12]
 }

df = pd.DataFrame(data)

# create a pandas Excel writer using XlsxlWriter as the engine
file_name = 'Sales_REport_.xlsx'
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

#Convert the dataframe to an XlsxWriter Excel object
df.to_excel(writer, sheet_name= 'Monthly  Report', index=False)

#Get the xlsxwriter workbook and worksheet objects
workbook = writer.book
worksheet = writer.sheets['Monthly  Report']

#Define some custom formates 
header_fromat = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',
    'fg_color': '#D7E4BC',
    'border': 1
})

currencey_format = workbook.add_format({'num_format': '$#,##0.00'})
#Apply formating
#Overwrite the headers with the custom format
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_fromat)

#Format the sales column as currency
worksheet.set_column('C:C', 15, currencey_format)

#Set column width for readability
worksheet.set_column('A:A', 15)
worksheet.set_column('D:D', 20)

#close the Pandas Excel writer and output the Excel file
writer.close()

print(f"Report '{file_name}' generated successfully.")