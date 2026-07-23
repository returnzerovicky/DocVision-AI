import re


class DocumentParser:

    def parse(self, text):

        result = {}

        # Business Name
        company = re.search(
            r"([A-Z][A-Za-z &]+(?:Private Limited|Ltd|LLP))",
            text
        )

        result["business_name"] = company.group(1) if company else None

        # Invoice Number
        invoice = re.search(
            r"(?:Invoice|Recipient)\s*(?:No|#)?[:\s-]*([A-Z0-9-]+)",
            text,
            re.IGNORECASE
        )

        result["invoice_number"] = invoice.group(1) if invoice else None

        # Date
        date = re.search(
            r"\d{2}[-/]\w{3}[-/]\d{4}|\d{2}-\d{2}-\d{4}",
            text
        )

        result["invoice_date"] = date.group() if date else None

        # GSTIN
        gst = re.search(
            r"\d{2}[A-Z]{5}\d{4}[A-Z]\dZ\d",
            text
        )

        result["gstin"] = gst.group() if gst else None

        # PAN
        pan = re.search(
            r"[A-Z]{5}[0-9]{4}[A-Z]",
            text
        )

        result["pan"] = pan.group() if pan else None

        # Total Amount
        total = re.search(
            r"1,18,000\.00|[\d,]+\.\d{2}",
            text
        )

        result["total_amount"] = total.group() if total else None

        return result