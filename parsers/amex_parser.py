import re

def parse_amex(text):
    data = {}
    data["card_variant"] = re.search(r'(PLATINUM|GOLD|REWARDS)', text, re.I)
    data["card_variant"] = data["card_variant"].group(1).upper() if data["card_variant"] else None

    data["card_last4"] = re.search(r'Card Ending In\s*(\d{4})', text, re.I)
    data["card_last4"] = data["card_last4"].group(1) if data["card_last4"] else None

    data["billing_cycle"] = re.search(r'Statement Period[:\s]*([\d/]+\s*-\s*[\d/]+)', text, re.I)
    data["billing_cycle"] = data["billing_cycle"].group(1) if data["billing_cycle"] else None

    data["payment_due_date"] = re.search(r'Payment Due Date[:\s]*([\d/]+)', text, re.I)
    data["payment_due_date"] = data["payment_due_date"].group(1) if data["payment_due_date"] else None

    data["new_balance"] = re.search(r'New Balance[:\s]*\$?([\d,]+\.\d{2})', text, re.I)
    data["new_balance"] = data["new_balance"].group(1) if data["new_balance"] else None

    return data
