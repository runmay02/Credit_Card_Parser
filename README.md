# 🧾 PDF Statement Parser

This project is a **Python-based PDF statement parser** that automatically extracts, analyzes, and summarizes key details (like billing info, balances, issuer details, etc.) from credit card statements.  
It supports multiple issuers (Chase, Amex, Citi, HDFC, and SBI) and includes OCR fallback for scanned PDFs.

---

## 🚀 Features

- 📂 **Interactive file upload:** Select a PDF file via a file picker (no need to type paths).  
- 🧠 **Automatic issuer detection:** Identifies the credit card issuer (Chase, Amex, Citi, HDFC, SBI).  
- 🔍 **Text extraction:** Uses `pdfplumber` for text-based PDFs and `pytesseract` OCR for scanned ones.  
- 🧾 **Custom parsers:** Each issuer has its own parser logic for structured data extraction.  
- 💡 **Rich JSON output:** Displays formatted JSON with extracted information.

---

## 📁 Folder Structure

pdf_pro/
│
├── parser.py # Main script to run the parser
│
├── /parsers/ # Individual issuer parsers
│ ├── chase_parser.py
│ ├── amex_parser.py
│ ├── citi_parser.py
│ ├── hdfc_parser.py
│ └── sbi_parser.py
│
├── /requirements.txt # Required dependencies
└── /README.md # Documentation


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/pdf_pro.git
cd pdf_pro


python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux


pip install -r requirements.txt


🧩 Dependencies

The following Python libraries are required:

pdfplumber — Extracts text from text-based PDFs

pytesseract — Performs OCR on scanned PDFs (optional)

pdf2image — Converts PDF pages to images for OCR

Pillow — Required by pdf2image

rich — Displays pretty JSON output

tkinter — Used for file picker (comes with Python standard library)


🧠 Usage

Run the script:

python parser.py


A file picker will appear.
Choose any credit card statement PDF, and the script will:

Extract text (or OCR scanned PDFs)

Detect the issuer

Parse structured data

Display results in JSON format

🧾 Example Output
{
  "card_variant": "REWARDS",
  "billing_cycle": "12/03/18 - 01/01/19",
  "payment_due_date": "27",
  "new_balance": "1,245.00",
  "issuer": "chase",
  "used_ocr": false,
  "raw_text_snippet": "Manage your account online: ..."
}

🧑‍💻 Extending the Project

To add support for a new bank or issuer:

Create a new parser file in /parsers/ (e.g., icici_parser.py)

Implement a function:

def parse_icici(text):
    data = {
        "card_variant": "...",
        "billing_cycle": "...",
        # ...
    }
    return data


Register it in parser.py under the parsers dictionary.


💬 Author

Your Name
📧 runmaystudy@gmail.com

💻 GitHub: runmay02


