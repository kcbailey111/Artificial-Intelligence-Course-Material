#!/usr/bin/env python3
"""
Extract text from all PDF files in the repository.
Outputs .txt files in an extracted_text/ folder for easy reading or sharing.
"""

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: pypdf is required. Install with: pip install pypdf")
    sys.exit(1)


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(pdf_path)
    text_parts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)
    return "\n\n".join(text_parts)


def main():
    # Use the script's directory as the root to search
    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir / "extracted_text"
    output_dir.mkdir(exist_ok=True)

    # Find all PDFs (exclude .git and extracted_text)
    pdf_files = [
        p
        for p in script_dir.rglob("*.pdf")
        if ".git" not in p.parts and "extracted_text" not in p.parts
    ]

    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF(s). Extracting text...\n")

    for pdf_path in sorted(pdf_files):
        txt_name = pdf_path.stem + ".txt"
        txt_path = output_dir / txt_name

        try:
            text = extract_text_from_pdf(pdf_path)
            txt_path.write_text(text, encoding="utf-8")
            print(f"  [OK] {pdf_path.name} -> extracted_text/{txt_name}")
        except Exception as e:
            print(f"  [ERR] {pdf_path.name}: {e}")

    print(f"\nDone. Text saved to: {output_dir}")


if __name__ == "__main__":
    main()
