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
