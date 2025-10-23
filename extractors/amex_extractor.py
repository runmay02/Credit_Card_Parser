import re

def extract_amex_details(raw_content):
    """
    Parses the raw text from an American Express statement to find key details.
    """
    extracted_info = {}

    # Find the card type (e.g., PLATINUM, GOLD)
    variant_match = re.search(r'(PLATINUM|GOLD|REWARDS)', raw_content, re.I)
    extracted_info["card_type"] = variant_match.group(1).upper() if variant_match else None

    # Find the last 4 digits of the card
    last4_match = re.search(r'Card Ending In\s*(\d{4})', raw_content, re.I)
    extracted_info["last_four_digits"] = last4_match.group(1) if last4_match else None

    # Find the billing cycle dates
    period_match = re.search(r'Statement Period[:\s]*([\d/]+\s*-\s*[\d/]+)', raw_content, re.I)
    extracted_info["statement_period"] = period_match.group(1) if period_match else None

    # Find the payment due date
    due_date_match = re.search(r'Payment Due Date[:\s]*([\d/]+)', raw_content, re.I)
    extracted_info["due_date"] = due_date_match.group(1) if due_date_match else None

    # Find the total amount due
    balance_match = re.search(r'New Balance[:\s]*\$?([\d,]+\.\d{2})', raw_content, re.I)
    extracted_info["total_due"] = balance_match.group(1) if balance_match else None

    return extracted_info
