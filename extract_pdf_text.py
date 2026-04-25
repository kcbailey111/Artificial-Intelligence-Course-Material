#!/usr/bin/env python3
"""
Extract text from all PDF files in the repository.
Outputs .txt files in an extracted_text/ folder for easy reading or sharing.

Optional OCR (ocrmypdf) helps when PDFs are image-based (e.g. slides exported as
pictures). ocrmypdf adds a searchable text layer; this script then reads it
with pypdf.

External dependencies for OCR (not installed by pip alone):
  - Tesseract OCR: https://github.com/tesseract-ocr/tesseract
  - Ghostscript: https://www.ghostscript.com/

  Windows: install Tesseract and Ghostscript, then ensure both are on PATH
  (e.g. winget install UB-Mannheim.TesseractOCR, ArtifexSoftware.GhostScript).

Usage:
  python extract_pdf_text.py
      Default: direct text extraction only (no OCR).

  python extract_pdf_text.py --ocr
      Run OCR on every PDF before extracting text (slower).

  python extract_pdf_text.py --ocr-if-sparse
      OCR only when direct extraction yields little text (good for mixed repos).

  python extract_pdf_text.py --ocr-force
      Like --ocr but force_ocr=True (rasterize all pages; use for image-only PDFs).

  python extract_pdf_text.py --ocr --only "Final Exam Material"
      Limit to PDFs whose path contains this substring (case-insensitive).
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("Error: pypdf is required. Install with: pip install pypdf")
    sys.exit(1)


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""
    reader = PdfReader(pdf_path)
    text_parts: list[str] = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_parts.append(text)
    return "\n\n".join(text_parts)


def _page_count(pdf_path: Path) -> int:
    try:
        return len(PdfReader(pdf_path).pages)
    except Exception:
        return 1


def is_sparse_extraction(pdf_path: Path, text: str, min_chars_per_page: float) -> bool:
    """Heuristic: PDF may be mostly images if very little text per page."""
    stripped = text.strip()
    if not stripped:
        return True
    pages = max(1, _page_count(pdf_path))
    return len(stripped) < min_chars_per_page * pages


def run_ocrmypdf(
    input_pdf: Path,
    output_pdf: Path,
    *,
    force_ocr: bool = False,
    languages: str = "eng",
) -> None:
    """
    Add an OCR text layer with ocrmypdf. Raises on failure.

    Uses the stable positional API (input, output, **kwargs) for compatibility
    across ocrmypdf 16.x and 17.x. ``languages`` may be a Tesseract language
    string such as ``eng`` or ``eng+fra``.
    """
    try:
        import ocrmypdf
    except ImportError as e:
        raise RuntimeError(
            "ocrmypdf is not installed. Run: pip install ocrmypdf\n"
            "You also need Tesseract and Ghostscript on PATH."
        ) from e

    exit_code = ocrmypdf.ocr(
        str(input_pdf.resolve()),
        str(output_pdf.resolve()),
        deskew=True,
        progress_bar=False,
        language=languages,
        force_ocr=force_ocr,
    )

    ok = exit_code == 0
    try:
        from ocrmypdf import ExitCode

        if exit_code == ExitCode.ok:
            ok = True
    except ImportError:
        pass
    if not ok:
        raise RuntimeError(f"ocrmypdf failed with exit code: {exit_code!r}")


def extract_with_optional_ocr(
    pdf_path: Path,
    *,
    use_ocr: bool,
    ocr_if_sparse: bool,
    force_ocr: bool,
    sparse_min_chars_per_page: float,
) -> tuple[str, str]:
    """
    Returns (extracted_text, method) where method is 'direct', 'ocr', or 'ocr_sparse'.
    """
    direct = extract_text_from_pdf(pdf_path)

    need_ocr = use_ocr or (
        ocr_if_sparse and is_sparse_extraction(pdf_path, direct, sparse_min_chars_per_page)
    )

    if not need_ocr:
        return direct, "direct"

    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    try:
        run_ocrmypdf(pdf_path, tmp_path, force_ocr=force_ocr)
        ocr_text = extract_text_from_pdf(tmp_path)
        return ocr_text, "ocr_force" if force_ocr else "ocr"
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Run OCR on every PDF before text extraction",
    )
    parser.add_argument(
        "--ocr-if-sparse",
        action="store_true",
        help="Run OCR only when direct extraction yields little text per page",
    )
    parser.add_argument(
        "--ocr-force",
        action="store_true",
        help="Use ocrmypdf force_ocr (all pages rasterized; for image-only PDFs)",
    )
    parser.add_argument(
        "--sparse-threshold",
        type=float,
        default=40.0,
        metavar="N",
        help="With --ocr-if-sparse: OCR if total chars < N * page_count (default: 40)",
    )
    parser.add_argument(
        "--only",
        type=str,
        default="",
        help="Process only PDFs whose path contains this substring (case-insensitive)",
    )
    args = parser.parse_args()

    use_ocr = args.ocr or args.ocr_force
    ocr_if_sparse = args.ocr_if_sparse

    script_dir = Path(__file__).resolve().parent
    output_dir = script_dir / "extracted_text"
    output_dir.mkdir(exist_ok=True)

    pdf_files = [
        p
        for p in script_dir.rglob("*.pdf")
        if ".git" not in p.parts and "extracted_text" not in p.parts
    ]

    only = args.only.strip().lower()
    if only:
        pdf_files = [p for p in pdf_files if only in str(p).lower()]

    if not pdf_files:
        print("No PDF files found.")
        return

    if use_ocr and ocr_if_sparse:
        mode = "OCR on all PDFs (--ocr); --ocr-if-sparse is redundant when combined"
    elif use_ocr:
        mode = "OCR on all PDFs"
    elif ocr_if_sparse:
        mode = "OCR only when direct text is sparse (--ocr-if-sparse)"
    else:
        mode = "direct extraction only"
    print(f"Found {len(pdf_files)} PDF(s). Mode: {mode}\n")

    for pdf_path in sorted(pdf_files):
        txt_name = pdf_path.stem + ".txt"
        txt_path = output_dir / txt_name

        try:
            text, method = extract_with_optional_ocr(
                pdf_path,
                use_ocr=use_ocr,
                ocr_if_sparse=ocr_if_sparse,
                force_ocr=args.ocr_force,
                sparse_min_chars_per_page=args.sparse_threshold,
            )
            txt_path.write_text(text, encoding="utf-8")
            tag = f"[{method}]"
            print(f"  [OK] {tag} {pdf_path.name} -> extracted_text/{txt_name}")
        except Exception as e:
            print(f"  [ERR] {pdf_path.name}: {e}")

    print(f"\nDone. Text saved to: {output_dir}")


if __name__ == "__main__":
    main()
