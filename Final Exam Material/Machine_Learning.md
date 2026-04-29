# Machine Learning - Final Exam Study Guide

This guide consolidates supervised learning, evaluation metrics, class imbalance, and explainability into exam-ready tables and deeper "why this matters" notes.

## 1) High-Yield Topic Map

| Topic | Key Concepts | Typical Question Type |
|---|---|---|
| Supervised Learning | Bias-variance, model families, regularization | Compare model tradeoffs |
| Evaluation Metrics | Accuracy, precision, recall, F1, ROC-AUC, PR-AUC | Pick metric for scenario |
| Imbalance + SMOTE | Minority class handling, thresholding | Improve recall without huge FP |
| Explainable AI (SHAP) | Global/local feature contribution | Interpret model decisions |

## 1.5) Core Learning Theory in 3 Minutes

- **Supervised learning objective:** Learn a function `f(x)` from labeled pairs `(x, y)` that generalizes to unseen data.
- **Generalization:** Low training error is not enough; you care about low expected error on future samples.
- **Empirical Risk Minimization (ERM):** Minimize average training loss, then control overfitting with regularization/validation.
- **Loss vs metric:** You optimize a differentiable loss (e.g., log loss), but report task-aligned metrics (e.g., F1, PR-AUC).
- **No free lunch intuition:** No single model is best for all distributions; match model assumptions to data structure.

## 2) Model Family Comparison

| Model | Strengths | Weaknesses | Best When |
|---|---|---|---|
| Linear/Logistic Regression | Interpretable, fast, stable | Limited nonlinear expressiveness | Baselines, tabular linear trends |
| Decision Tree | Nonlinear, intuitive rules | High variance/overfitting | Need clear rule-based explanation |
| Random Forest | Strong out-of-box, robust | Less interpretable | General tabular tasks |
| SVM | Strong margins, good on medium data | Sensitive to scaling/kernel choices | Clear separation with tuned kernels |
| Neural Nets | Flexible function approximation | Data/computation hungry | Complex patterns and larger data |

### Model Selection Heuristics (Exam Framing)

- Start with a **simple baseline** (logistic/linear regression) to set a reference.
- If you see clear nonlinear boundaries or interactions, move to **trees/ensembles**.
- If data is high-dimensional but medium-sized with good separation, consider **SVM**.
- If feature engineering is hard and data volume is large, consider **neural networks**.
- Always pair choice with constraints: interpretability, latency, compute budget, and class imbalance sensitivity.

### Regularization Cheat Notes

| Method | Effect | Typical Use |
|---|---|---|
| L2 (Ridge / weight decay) | Shrinks weights smoothly | Default anti-overfit option |
| L1 (Lasso) | Drives some weights to zero | Sparse/feature selection behavior |
| Elastic Net | Mix of L1 + L2 | Correlated features + sparsity |
| Early stopping | Stops before overfit in iterative learners | Neural nets, boosted trees |
| Dropout | Randomly drops activations | NN regularization via model averaging effect |

## 3) Bias-Variance Quick Table

| Symptom | Likely Issue | Typical Fix |
|---|---|---|
| High train error + high val error | High bias (underfit) | Increase model capacity/features |
| Low train error + high val error | High variance (overfit) | Regularization, more data, pruning |
| Train and val both strong | Good fit | Tune threshold/calibration for objective |

### Bias-Variance Intuition

- **Bias** is error from too-rigid assumptions (model too simple).
- **Variance** is error from sensitivity to training noise (model too flexible).
- As complexity increases: bias tends to decrease, variance tends to increase.
- Best performance is near the minimum of validation error, not training error.

### Fast Diagnosis Pattern

1. Compare train vs validation curves.
2. If both bad: add features, richer model, or reduce over-regularization.
3. If train excellent but validation poor: simplify model, regularize, or increase data.
4. Re-check with cross-validation to reduce split luck.

## 4) Metric Selection by Goal

| Scenario | Prefer | Why |
|---|---|---|
| Balanced classes, equal costs | Accuracy | Simple overall correctness |
| False positives are costly | Precision | Reduce false alarms |
| False negatives are costly | Recall | Catch as many positives as possible |
| Need balance precision/recall | F1 | Harmonic compromise |
| Ranking quality across thresholds | ROC-AUC | Threshold-independent ranking |
| Rare positive class | PR-AUC | More informative under imbalance |

### Metric Choice by Business Cost

| Domain Example | Costlier Error | Primary Metric | Secondary Checks |
|---|---|---|---|
| Cancer screening | False negative | Recall / Sensitivity | PR-AUC, confusion matrix by threshold |
| Spam filter | False positive | Precision | Recall floor, user complaint rate |
| Fraud detection | Usually FN, but FP also costly | PR-AUC + Recall@K | Precision at operating threshold |
| Credit default ranking | Ranking quality | ROC-AUC | Calibration and KS/lift curves |

### Threshold vs Ranking (Common Exam Trap)

- **AUC metrics** evaluate ranking quality across thresholds.
- **Precision/Recall/F1** depend on a chosen threshold.
- A model can have better ROC-AUC but worse F1 at a default threshold of `0.5`.
- Therefore, compare at optimized thresholds when objective is operational classification.

### Accuracy vs Precision (Deep Dive)

| Aspect | Accuracy | Precision |
|---|---|---|
| What it measures | Overall fraction of correct predictions | Of predicted positives, fraction truly positive |
| Formula | `(TP + TN) / Total` | `TP / (TP + FP)` |
| Sensitive to class imbalance? | Yes, can look high from majority class correctness | Less sensitive to TN volume; focuses on positive prediction quality |
| Best when | Classes/costs are balanced | False positives are expensive |
| Fails when | Rare positives or unequal error costs | Model predicts almost no positives (can inflate precision with low coverage) |

#### Intuition

- **Accuracy asks:** "How often am I correct overall?"
- **Precision asks:** "When I raise an alert, how often am I right?"
- In skewed datasets, a model can be "accurate" by mostly predicting majority class, while being operationally useless.
- Precision is action-oriented for systems where each positive prediction triggers costly intervention.

#### Imbalance Example (Why Accuracy Can Mislead)

Dataset: 1,000 samples, only 20 positives (2% prevalence).

- Model A predicts all samples as negative:
  - `TP=0, FP=0, TN=980, FN=20`
  - Accuracy = `980/1000 = 98%`
  - Precision = undefined/treated as `0` (no positive predictions)
  - Operational value for detecting positives: poor.

- Model B predicts 30 positives, 12 are correct:
  - `TP=12, FP=18, TN=962, FN=8`
  - Accuracy = `(12+962)/1000 = 97.4%` (lower than Model A)
  - Precision = `12/30 = 40%`
  - Recall = `12/20 = 60%`
  - Usually far more useful despite slightly lower accuracy.

#### Threshold Effect on Precision

- Raising decision threshold usually:
  - decreases number of predicted positives,
  - increases precision (fewer false positives),
  - may reduce recall (miss more true positives).
- Lowering threshold does the opposite.
- So precision is not a fixed model property; it is an operating-point property.

#### Exam-Style Interpretation Template

1. Report class balance and business cost of false positives.
2. If positives are rare, down-weight accuracy in your conclusion.
3. Use precision (and recall/PR-AUC) at the chosen threshold.
4. Justify tradeoff in domain terms (e.g., alert fatigue, review cost).

## 5) Confusion Matrix and Formulas

| Metric | Formula |
|---|---|
| Accuracy | `(TP + TN) / (TP + TN + FP + FN)` |
| Precision | `TP / (TP + FP)` |
| Recall (TPR) | `TP / (TP + FN)` |
| Specificity (TNR) | `TN / (TN + FP)` |
| F1 | `2 * (Precision * Recall) / (Precision + Recall)` |
| MCC | `(TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))` |

### Worked Mini Example

Suppose:
- `TP = 30`, `FP = 10`, `TN = 50`, `FN = 10`

Then:
- Accuracy = `(30+50)/100 = 0.80`
- Precision = `30/(30+10) = 0.75`
- Recall = `30/(30+10) = 0.75`
- F1 = `2*(0.75*0.75)/(0.75+0.75) = 0.75`

If positives were rare (say 5%), the same accuracy could hide poor recall. This is why imbalance-aware metrics matter.

### Accuracy and Precision Edge Cases

- **High accuracy + low precision:** often many true negatives with too many false alarms among predicted positives.
- **High precision + low recall:** model is conservative; positive predictions are reliable but many positives are missed.
- **No predicted positives (`TP+FP=0`):** precision is undefined; many libraries return `0` by convention.
- **Compare models fairly:** evaluate precision at matched recall or matched review budget, not arbitrary thresholds.

## 6) Handling Class Imbalance (SMOTE + Friends)

| Technique | What It Does | Tradeoff |
|---|---|---|
| Random oversampling | Duplicates minority points | Can overfit duplicates |
| Random undersampling | Removes majority points | Throws away information |
| SMOTE | Synthesizes minority samples via interpolation | Can create ambiguous border points |
| Class weights | Penalize minority errors more | Needs objective-aware tuning |
| Threshold moving | Changes decision cutoff | Requires calibration/validation |

### Why SMOTE Works (and When It Fails)

- SMOTE creates synthetic minority samples along line segments between minority neighbors.
- It helps models see a less skewed class prior during training.
- It may hurt when minority class is noisy, multimodal, or heavily overlapping with majority class.
- Borderline-SMOTE/SMOTEENN variants try to focus on informative edges or clean noisy regions.

### Alternative Imbalance Strategies

| Strategy | Best For | Caveat |
|---|---|---|
| Focal loss | Hard/rare examples in deep models | Extra hyperparameter tuning |
| Balanced Random Forest | Tree-based tabular tasks | Still requires threshold tuning |
| Anomaly detection framing | Extremely rare positives | Labels/assumptions may not fit |
| Cost-sensitive learning | Explicit error costs available | Need trustworthy cost estimates |

## 7) SMOTE Exam Checklist

1. Split train/validation first.
2. Apply SMOTE only to training split.
3. Refit model and compare recall/precision/F1/PR-AUC.
4. Tune threshold after training.
5. Verify no leakage from preprocessing order.

**Pipeline order reminder (leakage-safe):**
1. Train/validation split
2. Fit scaler/encoder on train only
3. Transform train/validation
4. Apply SMOTE on transformed train only
5. Train model
6. Evaluate on untouched validation

## 8) Explainable AI (SHAP) Quick Reference

| SHAP View | Purpose | Interpretation |
|---|---|---|
| Global summary plot | Overall feature impact | Higher absolute SHAP = stronger influence |
| Dependence plot | Feature effect by value | Shows nonlinearities/interactions |
| Local force/waterfall plot | Single prediction explanation | Feature pushes toward/away from output |

SHAP sign convention: positive SHAP values push prediction higher (toward positive class score), negative values push lower.

### SHAP Interpretation Rules

- SHAP explains the model you trained; it does **not** prove causal effects.
- Global importance = average absolute SHAP values across samples.
- Local explanation = additive contribution from each feature around a baseline expected output.
- Correlated features can split contribution in unintuitive ways; check domain consistency.

### Quick SHAP Workflow for Exams

1. Validate model quality first (if model is weak, explanation is less useful).
2. Use global plot to identify strongest drivers.
3. Use dependence plot for directionality/nonlinearity.
4. Use local waterfall/force to justify one prediction.
5. State one caveat (correlation, data shift, non-causality).

## 9) Common Pitfalls

- Reporting only accuracy on imbalanced data.
- Applying SMOTE before train/test split (data leakage).
- Comparing models at different thresholds unfairly.
- Using SHAP explanations without validating baseline model quality.
- Treating correlation-based feature importance as causation.
- Ignoring calibration when probabilities are used for decisions.

## 9.5) Calibration (Often Tested Indirectly)

- **Calibration question:** If model outputs `0.8`, do ~80% of those cases actually turn positive?
- A model can rank well (high AUC) but be poorly calibrated.
- Use reliability curves / Brier score / Expected Calibration Error (ECE) checks.
- Methods: Platt scaling (sigmoid) and isotonic regression on validation data.
- If downstream policy uses risk thresholds, calibration is critical.

## 10) Last-Minute Review Drill

1. When is PR-AUC more informative than ROC-AUC?
2. Why can recall improve while precision drops after SMOTE?
3. What does a large positive SHAP value for `Feature X` mean on one sample?
4. Give one underfitting and one overfitting mitigation strategy.
5. Why can two models with similar AUC have different business performance?
6. When would you optimize threshold for F1 vs recall-at-precision-constraint?
7. Why might a calibrated model be preferred over a slightly higher-AUC model?

## 11) Rapid Answer Templates (For Written Questions)

### "Choose the best metric"

1. Identify class balance and error costs.
2. State primary metric and why it aligns with cost.
3. Add one secondary metric to prevent blind spots.
4. Mention threshold tuning and validation protocol.

### "Improve performance on minority class"

1. Baseline confusion matrix + PR-AUC.
2. Apply class weights or SMOTE (train only).
3. Tune threshold for target objective.
4. Re-evaluate precision-recall tradeoff and calibration.

### "Interpret this prediction with SHAP"

1. Start from baseline expected prediction.
2. List top positive and negative SHAP contributors.
3. Conclude net direction and confidence caveat.
4. Note that explanation is model-based, not causal.

