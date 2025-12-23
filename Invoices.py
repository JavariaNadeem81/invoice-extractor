import os
import re
import pdfplumber
import pandas as pd
from datetime import datetime
# Note: Ensure you have pdf2image and pytesseract installed if you need OCR fallback
import pytesseract 
from pdf2image import convert_from_path
 
# Path configurations
INPUT_FOLDER = 'PDF_Invoice_Folder'
OUTPUT_FILE = 'comprehensive_invoices_.csv'

def get_text_from_pdf(path):
    """Extracts text from PDF (digital only in this version)."""
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            # Safely extract text within the 'with' block to avoid 'seek of closed file' error
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def parse_invoice_data(text):
    """Uses robust regex to extract fields from raw text."""
    data = {
        "Invoice_Number": "N/A",
        "Date": "N/A",
        "Total_Amount": "N/A",
        "Order_ID": "N/A" 
    }
    
    # 1. Capture multiple possible Total labels
    total_match = re.search(r"(?:Total|Amount Due|Balance)[:\s]*\$?\s?([\d,]+\.\d{2})", text, re.IGNORECASE)
    if total_match:
        data["Total_Amount"] = total_match.group(1)

    # 2. Capture specific Order ID if present
    order_id_match = re.search(r"Order ID\s?:?\s*(\w+-\w+-\w+-\w+)", text, re.IGNORECASE)
    if order_id_match:
        data["Order_ID"] = order_id_match.group(1)
        # Assuming Order ID is the primary ID for these docs
        data["Invoice_Number"] = order_id_match.group(1)
        
    # 3. Handle Date formats: Text (Nov 10 2012) AND Numeric (11/10/2012)
    date_match = re.search(r"(?:Date|Issued)[:\s]*([a-zA-Z]{3}\s\d{1,2}\s\d{4}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text, re.IGNORECASE)
    if date_match:
        date_str = date_match.group(1)
        try:
            # Try parsing 'Nov 10 2012'
            dt_obj = datetime.strptime(date_str, '%b %d %Y')
            data["Date"] = dt_obj.strftime('%Y-%m-%d')
        except ValueError:
            # Fallback for '11/10/2012' type dates
            data["Date"] = date_str
            
    return data

# Main execution logic
results = []
if os.path.exists(INPUT_FOLDER):
    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(INPUT_FOLDER, filename)
            print(f"Processing: {filename}")
            try:
                raw_text = get_text_from_pdf(file_path)
                invoice_info = parse_invoice_data(raw_text)
                invoice_info["Source_File"] = filename
                results.append(invoice_info)
            except Exception as e:
                print(f"Critical error on {filename}: {e}")

    # Export to comprehensive CSV
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Successfully processed {len(results)} invoices to {OUTPUT_FILE}")
