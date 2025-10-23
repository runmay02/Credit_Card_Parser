import os
import json
import pdfplumber
import tkinter as tk
from tkinter import filedialog

# Optional OCR dependencies
try:
    import pytesseract
    from PIL import Image
    from pdf2image import convert_from_path
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False

from rich import print_json

from parsers.chase_parser import parse_chase
from parsers.amex_parser import parse_amex
from parsers.citi_parser import parse_citi
from parsers.hdfc_parser import parse_hdfc
from parsers.sbi_parser import parse_sbi


# ---- Extract text from PDF ----
def extract_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text, False
    except Exception:
        if not OCR_AVAILABLE:
            raise RuntimeError("Text extraction failed and OCR not available.")
        images = convert_from_path(pdf_path, dpi=300)
        text_chunks = [pytesseract.image_to_string(img) for img in images]
        return "\n".join(text_chunks), True


# ---- Detect issuer ----
def detect_issuer(text):
    t = text.lower()
    if "chase" in t:
        return "chase"
    elif "american express" in t or "amex" in t:
        return "amex"
    elif "citi" in t:
        return "citi"
    elif "hdfc" in t:
        return "hdfc"
    elif "sbi card" in t or "state bank" in t:
        return "sbi"
    else:
        return "unknown"


# ---- Main runner ----
def main():
    # Open file dialog to choose PDF
    root = tk.Tk()
    root.withdraw()  # Hide Tkinter window
    pdf_path = filedialog.askopenfilename(
        title="Select PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not pdf_path:
        print("No file selected. Exiting.")
        return

    print(f"\n[+] Selected file: {pdf_path}\n")

    text, used_ocr = extract_text(pdf_path)
    issuer = detect_issuer(text)

    parsers = {
        "chase": parse_chase,
        "amex": parse_amex,
        "citi": parse_citi,
        "hdfc": parse_hdfc,
        "sbi": parse_sbi,
    }

    extractor = parsers.get(issuer)
    if extractor is None:
        data = {}
    else:
        data = extractor(text)

    data["issuer"] = issuer
    data["used_ocr"] = used_ocr
    data["raw_text_snippet"] = text[:700]

    json_str = json.dumps(data, indent=2)
    print_json(json_str)


if __name__ == "__main__":
    main()
