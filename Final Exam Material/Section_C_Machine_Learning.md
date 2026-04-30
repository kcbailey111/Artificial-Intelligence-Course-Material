# Section C — Machine Learning

Topics below expand **bias–variance**, **precision / recall / F1**, and **CNN vs GNN structure** (aligned with sample-style “evaluate a proposal” questions). Full study guide: `Machine_Learning.md`.

---

## Bias–variance tradeoff

### Picture

From finite data, error on new data has several sources. The classic **bias–variance** story (often with squared error) separates:

- **Bias:** systematic error—model family **too simple** or **wrong structure** for the truth.  
- **Variance:** sensitivity to training **noise**—small data changes → large model changes.

**Exam shorthand:** high bias ≈ **underfitting**; high variance ≈ **overfitting**.

### Bias

Mismatch between the **best fit in your hypothesis class** and the **true** pattern, even with infinite data. **Symptom:** **high training error** (model cannot fit signal). Examples: linear model for strongly nonlinear boundary; tiny tree for heavy feature interactions.

### Variance

How much the fit **wiggles** when the training sample changes. **Symptom:** **low train, high validation** error. Examples: deep unrestricted trees; high-capacity nets, little data, weak regularization.

### Complexity curve (conceptual)

More complexity: bias often **down**, variance **up**. Total error often **U-shaped** vs complexity. Real life adds optimization, label noise, misspecification—bias–variance is an **organizing story**, not a theorem for every loss.

### Train vs validation patterns

| Pattern | Diagnosis | Levers |
|--------|-----------|--------|
| High train, high val | Underfit / bias | More capacity, better features, less excessive regularization, train longer if under-trained |
| Low train, high val | Overfit / variance | Regularization, more data, simpler model, early stopping, ensembles |
| Low train, low val | Reasonable fit | Threshold / calibration for deployment metric |

### Regularization

L2/L1, dropout, depth limits, etc. usually **cut variance**; too much can **raise bias**.

### More data

Typically **reduces variance**; does **not** fix wrong model class (**bias**) until you change representation or hypothesis class.

### Metrics vs loss

You may minimize **log loss** but care about **F1** or cost-weighted error—good bias–variance on loss still needs **threshold tuning** and **task metrics**.

### Short template

**Bias** is underfitting: rigid model, often poor on both train and val. **Variance** is overfitting: fits noise, strong train but weak val. Fix bias with useful capacity/features; fix variance with regularization, data, or simpler models—always validate on held-out data.

---

## Precision, recall, and F1

### Confusion matrix (binary)

|  | Predicted + | Predicted − |
|--|------------|-------------|
| **Actual +** | TP | FN |
| **Actual −** | FP | TN |

### Precision

\(\text{Precision} = TP / (TP + FP)\) — among **positive predictions**, fraction correct.

**High precision** ⇒ few false positives. Matches **costly false alarms**. If \(TP+FP=0\), precision **undefined** (libraries may return 0).

### Recall

\(\text{Recall} = TP / (TP + FN)\) — among **actual positives**, fraction found (**sensitivity** / TPR).

**High recall** ⇒ few false negatives. Matches **costly misses**.

### Accuracy trap

\(\text{Accuracy} = (TP+TN)/\text{total}\). With **rare positives**, predicting always negative yields high accuracy and **zero recall**. Prefer **precision/recall** or **PR-AUC** when imbalance matters.

### Threshold tradeoff

Higher threshold → usually fewer positives → often **higher precision, lower recall**; lower threshold does the reverse. Precision/recall are **operating-point** quantities unless the exam fixes a threshold.

### F1

\(F1 = 2PR/(P+R)\) — harmonic mean of precision and recall. Reasonable when you want a **balance** on the **positive class** in imbalanced settings. **Not** enough when costs are **asymmetric** (use cost-sensitive objectives).

### ROC-AUC vs PR-AUC

**ROC-AUC:** ranking across thresholds (TPR vs FPR); can look optimistic with huge negatives. **PR-AUC:** often better for **rare positives**. Neither replaces domain **cost** analysis.

### Worked example

\(TP=30, FP=10, FN=10, TN=50\): precision = recall = F1 = 0.75; accuracy = 0.80. With ~2% positives, “always negative” ≈ 98% accuracy and useless detection.

### Template: choose a metric

State **class balance** and **which error is costlier**. Costly FP → emphasize **precision** + recall floor. Costly FN → **recall** + acceptable precision. **F1** for balanced positive-class focus. Always mention **validation threshold tuning**.

---

## CNN grid structure vs GNN graph structure

### Shared idea

Both **update a representation using neighbors**: convolutional neighborhoods on a grid vs **message passing** on a graph.

### What CNNs assume

Images: **regular grid**, meaningful **spatial locality**, **translation**-style sharing. Local patches match edges, textures; filters reuse across positions.

### What graphs are

**Nodes and edges** (atoms/bonds, users/social links, papers/citations). **No** canonical axis like an image; **degrees** vary. **Connectivity**, not a 2D lattice, defines “near.”

### Adjacency matrix caveat

Any finite graph has an adjacency matrix, but **row/column order** is a **labeling choice**. Permuting node IDs **permutes** the matrix without changing the graph. A CNN on that matrix treats **index positions** like spatial coordinates—locality is in **index space**, not necessarily **graph distance**.

### GNN message passing

Per node \(v\): aggregate messages from **graph neighbors** (sum/mean/max), update \(v\)’s embedding. Permutation-invariant aggregation ⇒ **equivariance** to consistent relabeling: structure is preserved, not an arbitrary layout.

### Molecules and “CNN on a graph matrix”

Chemistry depends on **bonds** and attributes; many valid orderings of the same molecule exist. Raw matrix + CNN lacks the **relational** inductive bias of **GNNs**; specialized encodings help but GNNs align more directly with **topology**.

### Shared limitations (exam “evaluate”)

Both **compress neighborhoods** into fixed vectors; deep stacks risk **over-smoothing** or missing long-range structure; both can **memorize** spurious patterns. “GNN > CNN for graphs” is about **correct structure**, not unlimited power.

### Sample-exam paragraph

CNNs encode **Euclidean grid locality** and translation; images fit that. Graphs encode **relational** neighborhoods; adjacency matrices are **label-dependent**, so convolution in matrix indices is not the same as convolution on **intrinsic** graph neighborhoods. **GNN message passing** aggregates true neighbors and respects relabeling structure, so it is the natural default for molecular or network data, though both methods summarize neighborhoods and can lose long-range detail without careful design.

---

## See also

- `Machine_Learning.md` — SMOTE, SHAP, calibration, model families, regularization table.
