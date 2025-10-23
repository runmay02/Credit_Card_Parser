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
    OCR_CAPABLE = True
except ImportError:
    OCR_CAPABLE = False

from rich import print_json

# Import the new extractor functions
from extractors.chase_extractor import extract_chase_details
from extractors.amex_extractor import extract_amex_details
from extractors.citi_extractor import extract_citi_details
from extractors.hdfc_extractor import extract_hdfc_details
from extractors.sbi_extractor import extract_sbi_details


def get_text_from_pdf(file_location):
    """
    Extracts text from a PDF file.
    Tries direct text extraction first, then falls back to OCR if needed.
    """
    try:
        # Try standard text extraction
        with pdfplumber.open(file_location) as pdf_document:
            full_text = "\n".join(page.extract_text() or "" for page in pdf_document.pages)
        if full_text.strip():
            return full_text, False  # Return text, ocr_used = False
    except Exception as e:
        print(f"Standard text extraction failed: {e}")
        if not OCR_CAPABLE:
            raise RuntimeError("Text extraction failed and OCR libraries are not installed.")

    # Fallback to OCR if standard extraction fails or yields no text
    if not OCR_CAPABLE:
        raise RuntimeError("PDF is likely an image, but OCR libraries are not installed.")

    print("Standard extraction failed or returned empty. Attempting OCR...")
    try:
        images = convert_from_path(file_location, dpi=300)
        ocr_segments = [pytesseract.image_to_string(img) for img in images]
        full_text = "\n".join(ocr_segments)
        return full_text, True  # Return text, ocr_used = True
    except Exception as ocr_error:
        print(f"OCR extraction also failed: {ocr_error}")
        raise RuntimeError(f"Both standard and OCR extraction failed for: {file_location}")


def identify_bank_from_text(raw_content):
    """
    Analyzes the text to identify the bank/issuer.
    """
    content_lower = raw_content.lower()
    if "chase" in content_lower:
        return "chase"
    elif "american express" in content_lower or "amex" in content_lower:
        return "amex"
    elif "citi" in content_lower:
        return "citi"
    elif "hdfc" in content_lower:
        return "hdfc"
    elif "sbi card" in content_lower or "state bank" in content_lower:
        return "sbi"
    else:
        return "unknown"


def run_processor():
    """
    Main execution function.
    Prompts user for a file, processes it, and prints the extracted data.
    """
    # Open file dialog to choose PDF
    gui_root = tk.Tk()
    gui_root.withdraw()  # Hide the main Tkinter window
    selected_file = filedialog.askopenfilename(
        title="Select PDF statement file",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not selected_file:
        print("No file was selected. Exiting.")
        return

    print(f"\n[+] Processing file: {selected_file}\n")

    try:
        document_content, ocr_was_used = get_text_from_pdf(selected_file)
    except Exception as e:
        print(f"[!] Error: {e}")
        return

    detected_bank = identify_bank_from_text(document_content)

    # Map of detected bank names to their corresponding parser functions
    bank_parsers_map = {
        "chase": extract_chase_details,
        "amex": extract_amex_details,
        "citi": extract_citi_details,
        "hdfc": extract_hdfc_details,
        "sbi": extract_sbi_details,
    }

    # Get the correct parser function for the detected bank
    chosen_parser = bank_parsers_map.get(detected_bank)

    if chosen_parser is None:
        print(f"No parser found for detected bank: '{detected_bank}'")
        final_data = {}
    else:
        print(f"Using '{detected_bank}' parser...")
        final_data = chosen_parser(document_content)

    # Add metadata to the final output
    final_data["detected_bank"] = detected_bank
    final_data["ocr_was_used"] = ocr_was_used
    final_data["content_snippet"] = document_content[:700].strip()

    # Convert the final data to a JSON string and print it
    output_json = json.dumps(final_data, indent=2)
    print_json(output_json)


if __name__ == "__main__":
    run_processor()
