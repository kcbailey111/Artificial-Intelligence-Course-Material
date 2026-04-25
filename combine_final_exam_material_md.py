#!/usr/bin/env python3
"""Build category markdown files from extracted_text/*.txt (Final Exam Material)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "extracted_text"
OUT_DIR = ROOT / "Final Exam Material"
FENCE = "`" * 3


def read_txt(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8", errors="replace")


def build_doc(title: str, intro: str, parts: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", "", intro, ""]
    for heading, fname in parts:
        body = read_txt(fname).rstrip()
        pdf_name = fname.replace(".txt", ".pdf")
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(f"*Extracted from PDF: `{pdf_name}`*")
        lines.append("")
        lines.append(FENCE)
        lines.append(body)
        lines.append(FENCE)
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    intro = (
        "This document was generated from text extracted from the **Final Exam Material** folder. "
        "Slide PDFs may have imperfect reading order; formulas and diagrams appear as plain text."
    )

    logic = build_doc(
        "Logic and Search",
        intro
        + " Topics: propositional logic, uninformed and informed search, first-order logic, advanced search/optimization.",
        [
            ("Propositional Logic", "1 Propositonal Logic (1).txt"),
            ("Uninformed Search", "2 Uninformed Search.txt"),
            ("Informed Search", "3 Informed Search.txt"),
            ("First-Order Logic", "4 First-Order Logic.txt"),
            ("Advanced Search (Optimization)", "5 Advanced Search (Optimization).txt"),
        ],
    )

    rl_lm = build_doc(
        "Reinforcement Learning and Language Models",
        intro
        + " This bundle includes **NLP Before LLMs** (language modeling and statistical NLP). "
        "There is no standalone Reinforcement Learning deck in *Final Exam Material*; "
        "RL is mentioned briefly in the supervised learning overview and as motivation in the games deck.",
        [("NLP Before LLMs", "6 NLP Before LLMs.txt")],
    )

    ml = build_doc(
        "Machine Learning",
        intro
        + " Topics: supervised learning (linear models to neural networks), evaluation metrics, "
        "class imbalance (SMOTE), explainability (SHAP).",
        [
            (
                "Supervised Learning: Linear Models to Neural Networks",
                "9 Supervised Learning From Linear Models to Neural Networks.txt",
            ),
            ("Evaluation Metrics (deck 1)", "10 Evaluation Metrics.txt"),
            ("Evaluation Metrics (deck 2)", "11 Evaluation Metrics.txt"),
            ("Handling Class Imbalance with SMOTE", "12 Handling Class Imbalance with SMOTE.txt"),
            ("Explainable AI — SHAP", "13 Explainable AI -- SHAP.txt"),
        ],
    )

    other = build_doc(
        "Other Topics (outside the three exam themes)",
        intro
        + " Material that does not map cleanly to **Logic and Search**, "
        "**Reinforcement Learning and Language Models**, or **Machine Learning**.",
        [("Games and Game Theory", "7 Games and Game Theory.txt")],
    )

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "Logic_and_Search.md").write_text(logic, encoding="utf-8")
    (OUT_DIR / "Reinforcement_Learning_and_Language_Models.md").write_text(rl_lm, encoding="utf-8")
    (OUT_DIR / "Machine_Learning.md").write_text(ml, encoding="utf-8")
    (OUT_DIR / "Other_Topics.md").write_text(other, encoding="utf-8")
    print("Wrote:", OUT_DIR / "Logic_and_Search.md")
    print("Wrote:", OUT_DIR / "Reinforcement_Learning_and_Language_Models.md")
    print("Wrote:", OUT_DIR / "Machine_Learning.md")
    print("Wrote:", OUT_DIR / "Other_Topics.md")


if __name__ == "__main__":
    main()
