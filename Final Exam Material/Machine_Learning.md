# Machine Learning - Final Exam Study Guide

This guide consolidates supervised learning, evaluation metrics, class imbalance, and explainability into exam-ready tables.

## 1) High-Yield Topic Map

| Topic | Key Concepts | Typical Question Type |
|---|---|---|
| Supervised Learning | Bias-variance, model families, regularization | Compare model tradeoffs |
| Evaluation Metrics | Accuracy, precision, recall, F1, ROC-AUC, PR-AUC | Pick metric for scenario |
| Imbalance + SMOTE | Minority class handling, thresholding | Improve recall without huge FP |
| Explainable AI (SHAP) | Global/local feature contribution | Interpret model decisions |

## 2) Model Family Comparison

| Model | Strengths | Weaknesses | Best When |
|---|---|---|---|
| Linear/Logistic Regression | Interpretable, fast, stable | Limited nonlinear expressiveness | Baselines, tabular linear trends |
| Decision Tree | Nonlinear, intuitive rules | High variance/overfitting | Need clear rule-based explanation |
| Random Forest | Strong out-of-box, robust | Less interpretable | General tabular tasks |
| SVM | Strong margins, good on medium data | Sensitive to scaling/kernel choices | Clear separation with tuned kernels |
| Neural Nets | Flexible function approximation | Data/computation hungry | Complex patterns and larger data |

## 3) Bias-Variance Quick Table

| Symptom | Likely Issue | Typical Fix |
|---|---|---|
| High train error + high val error | High bias (underfit) | Increase model capacity/features |
| Low train error + high val error | High variance (overfit) | Regularization, more data, pruning |
| Train and val both strong | Good fit | Tune threshold/calibration for objective |

## 4) Metric Selection by Goal

| Scenario | Prefer | Why |
|---|---|---|
| Balanced classes, equal costs | Accuracy | Simple overall correctness |
| False positives are costly | Precision | Reduce false alarms |
| False negatives are costly | Recall | Catch as many positives as possible |
| Need balance precision/recall | F1 | Harmonic compromise |
| Ranking quality across thresholds | ROC-AUC | Threshold-independent ranking |
| Rare positive class | PR-AUC | More informative under imbalance |

## 5) Confusion Matrix and Formulas

| Metric | Formula |
|---|---|
| Accuracy | `(TP + TN) / (TP + TN + FP + FN)` |
| Precision | `TP / (TP + FP)` |
| Recall (TPR) | `TP / (TP + FN)` |
| Specificity (TNR) | `TN / (TN + FP)` |
| F1 | `2 * (Precision * Recall) / (Precision + Recall)` |
| MCC | `(TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))` |

## 6) Handling Class Imbalance (SMOTE + Friends)

| Technique | What It Does | Tradeoff |
|---|---|---|
| Random oversampling | Duplicates minority points | Can overfit duplicates |
| Random undersampling | Removes majority points | Throws away information |
| SMOTE | Synthesizes minority samples via interpolation | Can create ambiguous border points |
| Class weights | Penalize minority errors more | Needs objective-aware tuning |
| Threshold moving | Changes decision cutoff | Requires calibration/validation |

## 7) SMOTE Exam Checklist

1. Split train/validation first.
2. Apply SMOTE only to training split.
3. Refit model and compare recall/precision/F1/PR-AUC.
4. Tune threshold after training.
5. Verify no leakage from preprocessing order.

## 8) Explainable AI (SHAP) Quick Reference

| SHAP View | Purpose | Interpretation |
|---|---|---|
| Global summary plot | Overall feature impact | Higher absolute SHAP = stronger influence |
| Dependence plot | Feature effect by value | Shows nonlinearities/interactions |
| Local force/waterfall plot | Single prediction explanation | Feature pushes toward/away from output |

SHAP sign convention: positive SHAP values push prediction higher (toward positive class score), negative values push lower.

## 9) Common Pitfalls

- Reporting only accuracy on imbalanced data.
- Applying SMOTE before train/test split (data leakage).
- Comparing models at different thresholds unfairly.
- Using SHAP explanations without validating baseline model quality.

## 10) Last-Minute Review Drill

1. When is PR-AUC more informative than ROC-AUC?
2. Why can recall improve while precision drops after SMOTE?
3. What does a large positive SHAP value for `Feature X` mean on one sample?
4. Give one underfitting and one overfitting mitigation strategy.

