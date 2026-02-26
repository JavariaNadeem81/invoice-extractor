import os
import tkinter as tk
from tkinter import filedialog  # Needed for the file picker
import sys
import pandas as pd
 
# 1. Pop-up to pick the file
tk.Tk().withdraw() 
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

if file_path:
    df = pd.read_csv(file_path)
    
    # 2. Your original Excel setup
    writer = pd.ExcelWriter('Automated_Report.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Daily Report', index=False)

    # 3. Your original formatting
    worksheet = writer.sheets['Daily Report']
    for i, col in enumerate(df.columns):
        column_len = max(df[col].astype(str).str.len().max(), len(col)) + 2
        worksheet.set_column(i, i, column_len)

    writer.close()
    print("Success! Your Formatted report is ready.")
else:
    print("No file was selected.")