# Invoice PDF Data Extraction Project

## Overview
This project automates the extraction of key invoice information from **digital PDF invoices** and consolidates the results into a structured CSV file.  
It is designed for scalability, clarity, and real-world business use cases such as finance reporting, auditing, and record keeping.

The script processes multiple invoices in bulk, applies robust pattern matching, and outputs a clean dataset ready for analysis.

---

## Objectives
- Extract invoice data from PDF files
- Standardize unstructured text into tabular format
- Reduce manual data entry effort
- Enable downstream analytics and reporting

---

## Extracted Fields
The script attempts to extract the following information:
- **Invoice Number** (derived from Order ID when applicable)
- **Order ID**
- **Invoice Date**
- **Total Amount**
- **Source File Name**

Missing or unavailable values are safely marked as `N/A`.

---

## Project Structure

├── invoices_2025/ # Input folder containing PDF invoices
├── comprehensive_invoices_updated.csv # Output file
├── invoice_parser.py # Main Python script
├── README.md
├── .gitignore


---

## Technologies Used
- Python
- pdfplumber
- pandas
- regex (re)
- datetime
- os

*(Optional OCR support can be added using `pdf2image` and `pytesseract` for scanned PDFs.)*

---

## How It Works
1. Reads all PDF files from the input directory
2. Extracts raw text from each PDF
3. Applies regex-based parsing for invoice fields
4. Normalizes date formats where possible
5. Aggregates results into a CSV file

---

## Usage
1. Place all invoice PDFs inside the `invoices_2025` folder
2. Run the script:
   ```bash
   python invoice_parser.py
The output CSV will be generated in the project root

Limitations

Current version supports digital PDFs only

Scanned invoices require OCR integration

Date normalization supports common formats

Future Enhancements

OCR fallback for scanned documents

Currency detection

Vendor name extraction

Logging and error reports

CLI argument support

Author

Developed as a practical automation project to demonstrate Python scripting, text parsing, and data extraction workflows.
