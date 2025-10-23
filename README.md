# 🧾 Credit Card Statement PDF Parser

A Python-based tool that automatically extracts key information from credit card statement PDFs for major issuers such as **Chase, Amex, Citi, HDFC, and SBI**.
It works on both **text-based PDFs** and **scanned PDFs** (via OCR fallback).

-----

## 📌 Features

✅ Supports **5 major issuers**

  - Chase
  - American Express
  - Citi
  - HDFC Bank
  - SBI Card

✅ Extracts **5 Key Data Points**

  - Card Variant
  - Card Last 4 Digits
  - Billing Cycle
  - Payment Due Date
  - Total/New Balance

✅ Supports **real-world PDFs**
✅ **OCR fallback** for scanned statements
✅ **Interactive PDF selection** (no manual path input)
✅ Outputs **clean JSON data**

-----

## 🗂️ Folder Structure

```plaintext
pdf_parser_project/
│
├── main_processor.py           # Main application file
│
├── /parsers/           # Individual issuer parsers
│   ├── chase_extractor.py
│   ├── amex_extractor.py
│   ├── citi_extractor.py
│   ├── hdfc_extractor.py
│   └── sbi_extractorpy
│
├── requirements.txt    # Dependencies list
└── README.md           # Documentation
```

-----

## ⚙️ Installation

### Step 1: Clone or Download Repository

```bash
git clone https://github.com/yourusername/pdf_pro.git
cd pdf_parser_project
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If you plan to use OCR (for scanned PDFs), also install:

```bash
pip install pytesseract pdf2image pillow
```

### 🧩 External Setup (Optional for OCR)

🖼️ **Poppler**

  - **Windows:**
      - Download from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows)
      - Extract and add the `bin` folder to your system `PATH`.
      - *Example PATH: `C:\poppler-24.07.0\Library\bin`*

🔠 **Tesseract OCR**

  - **Windows:**
      - Download from [Tesseract OCR Releases](https://www.google.com/search?q=https://github.com/UB-Mannheim/tesseract/wiki)
      - Add the installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your system `PATH`.

-----

## 🚀 Usage

Run the Parser:

```bash
python parser.py
```

A file picker window will open — select the credit card statement PDF you want to parse.

Then, the tool will:

1.  Detect the issuer automatically
2.  Extract relevant data points
3.  Display results as formatted JSON

### 🧾 Example Output

```json
{
  "card_variant": "REWARDS",
  "card_last4": "1234",
  "billing_cycle": "12/03/18 - 01/01/19",
  "payment_due_date": "01/25/2019",
  "new_balance": "1,245.00",
  "issuer": "chase",
  "used_ocr": false,
  "raw_text_snippet": "Manage your account online: ..."
}
```

-----

## 🧠 How It Works

1.  User selects PDF file via GUI.
2.  Text extraction attempted via `pdfplumber`.
3.  If extraction fails → OCR using `pdf2image` + `pytesseract`.
4.  Issuer detected using keyword search.
5.  Issuer-specific parser extracts target fields.
6.  Results displayed in JSON format.

### 🔍 Error Handling

| Scenario | Action |
| :--- | :--- |
| Invalid or missing file | Shows error message |
| Scanned PDF | Automatically switches to OCR |
| Unsupported issuer | Returns `"issuer": "unknown"` |
| Missing libraries | Displays clear installation hint |

-----

## 🧮 Dependencies

| Library | Purpose |
| :--- | :--- |
| `pdfplumber` | Text extraction from PDFs |
| `pytesseract` | OCR for scanned PDFs |
| `pdf2image` | Converts PDF to image for OCR |
| `Pillow` | Image processing |
| `rich` | Colored JSON output |
| `tkinter` | GUI for file selection |

-----

## 💡 Future Enhancements

  - Add more issuers (Axis, ICICI, etc.)
  - Build a web UI with Flask
  - Add summary report generation
  - Integrate with finance management tools

-----

## 👨‍💻 Author

  - **Developed by:** Runmay
  - **Course:** M.Sc. Computer Science
  - **Submission Date:** 23rd October
