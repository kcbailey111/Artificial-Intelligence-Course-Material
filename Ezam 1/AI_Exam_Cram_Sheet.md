# AI Course Exam Cram Sheet

Quick reference for CSC-343 topics: Uninformed Search, Informed Search, Advanced Search, Propositional Logic, First-Order Logic, and NLP Before LLMs.

---

## 1. Uninformed Search

### Core Concepts
- **Frontier**: Nodes generated but not yet expanded. Defines the search strategy.
- **Tree vs Graph Search**: Tree can revisit states; Graph uses an explored set, each state at most once.
- **Explored set**: Node added when **expanded** (removed from frontier), not when first generated.

### Algorithms
| Algorithm | Selection | Complete? | Optimal? | Space |
|-----------|-----------|-----------|----------|-------|
| BFS | FIFO | Yes (finite) | Yes (uniform cost) | O(b^d) |
| DFS | LIFO | No (infinite) | No | O(bm) |
| UCS | Min g(n) | Yes | Yes | O(b^d) |
| IDS | Depth-limited DFS, increasing limit | Yes | Yes | O(bd) |

### Key Facts
- DFS not complete in infinite state spaces (can go down one path forever).
- BFS complete in finite state spaces (explores level by level).
- UCS expands by path cost g(n), **not** depth.
- IDS: redundant shallow work acceptable; most nodes are at deepest level.
- BFS space O(b^d); DFS space O(bm).

### Formulas
- BFS nodes: (b^(d+1) − 1)/(b − 1)
- DFS nodes: (b^(m+1) − 1)/(b − 1)

---

## 2. Informed Search

### Heuristics
- **Admissible**: h(n) ≤ h*(n) for all n. Never overestimates true cost.
- **Consistent**: h(n) ≤ c(n,n') + h(n') for all n,n'. Implies admissible.
- **Dominance**: h₂ dominates h₁ if h₂(n) ≥ h₁(n) for all n, and > for some n. Prefer dominating heuristic (fewer expansions).

### A* and Variants
- **A***: f(n) = g(n) + h(n). Optimal if h admissible (consistency not required for optimality).
- **Greedy Best-First**: Select by h(n) only. Not optimal.
- **Weighted A***: f(n) = g(n) + w·h(n). Solution cost ≤ w·C* when h admissible.
- **Beam Search**: Keep top k nodes per level. Neither complete nor optimal (pruning can remove optimal path).

### 8-Puzzle Heuristics
- h₁ = Misplaced Tiles
- h₂ = Manhattan Distance (dominates h₁ and h₃)
- h₃ = Not in goal row + not in goal column

### Key Facts
- Overestimating h → A* can return suboptimal solution.
- If A* expands n, then f(n) ≤ C*.
- Consistent ⇒ admissible; admissible ⇏ consistent.
- Straight-line distance: admissible and consistent.
- Beam k=1 ≠ Greedy Best-First (different mechanics).
- Anytime algorithms do not require admissible heuristic.

---

## 3. Advanced Search (Optimization)

### When to Use
- **Path-finding (A*)**: Explicit start/goal, need path.
- **Optimization (HC, SA, GA)**: Find best configuration, maximize/minimize f(x).

### Hill Climbing
- **Local optima**: Stuck at state better than neighbors but worse than global optimum.
- **Neighbor tradeoff**: Small = fast but more local optima; Large = better solutions, slower.
- **Random restart**: With enough restarts, prob. of finding global opt → 1.

### Simulated Annealing
- **P(worse move) = e^(-Δ/T)**
- **Exploration vs Exploitation**: High T → exploration; Low T → exploitation.
- **Cooling**: If T drops too fast → behaves like hill climbing, gets stuck.
- T→0: hill climbing. T→∞: random walk.

### Genetic Algorithms
- **Crossover**: Combines parents; exploits good building blocks.
- **Mutation**: Random change; explores new regions.
- **Elitism**: Keep best individual(s); prevents losing good solution.
- Population allows parallel exploration of search space.

### Key Facts
- A* uses more memory than HC/GA.
- Hill climbing optimal only if single local optimum.
- 2-opt: reversing tour segment gives valid tour.
- Larger neighborhood ≠ always better (more cost, still local optima).
- High mutation rate ≠ faster convergence (can disrupt solutions).

---

## 4. Propositional Logic

### Validity vs Soundness
- **Valid**: If premises true → conclusion true (form correct).
- **Sound**: Valid AND all premises true. AI needs sound reasoning.

### Key Definitions
- **Complete**: KB ⊨ α ⇒ KB ⊢ α (can derive every entailed sentence).
- **Sound**: KB ⊢ α ⇒ KB ⊨ α (only derives entailed sentences).
- **Satisfiable**: True in some model. **Tautology**: True in all. **Unsatisfiable**: False in all.

### Inference
- **Forward chaining**: Data-driven; from facts, apply rules until goal.
- **Backward chaining**: Goal-driven; from query, prove premises.
- **Resolution refutation**: Prove KB ⊨ α by showing KB ∧ ¬α unsatisfiable (derive ∅).
- **Horn clauses**: At most one positive literal. Forward/backward chaining use definite clauses.

### Formulas
- P ⇒ Q ≡ ¬Q ⇒ ¬P (contrapositive)
- P ⇔ Q ≡ (P⇒Q) ∧ (Q⇒P) ≡ (¬P∨Q) ∧ (¬Q∨P)
- Truth table: 2^n rows → O(2^n) complexity

### Key Facts
- Valid with false premises possible.
- φ satisfiable ⇏ ¬φ unsatisfiable (both can be satisfiable).
- φ tautology ⇒ ¬φ unsatisfiable.
- Resolution: if cannot derive ∅, query **not** entailed.
- (P ∨ ¬P) is tautology; can remove from CNF.
- Modus ponens alone is **not** complete for propositional logic.
- Completeness ⇏ Soundness (independent).

---

## 5. First-Order Logic

### Terms vs Sentences
- **Term**: Object (constant, variable, function). Example: Father(john).
- **Sentence**: Truth-valued formula (predicate + connectives + quantifiers).

### Unification
- Find θ such that two expressions become identical.
- **Occurs check**: Reject X = t if X occurs in t (prevents infinite terms).
- Example: P(X,a) and P(b,X) → need X=b and X=a → fails unless a=b.

### Quantifiers
- ∀X∃Y Loves(X,Y) ≠ ∃Y∀X Loves(X,Y) (order matters).
- ∀X (Student(X) ∧ Smart(X)) = "Everything is student and smart."
- ∀X (Student(X) → Smart(X)) = "All students are smart."
- ∀x ¬P(x) ≡ ¬∃x P(x)

### Inference
- **Universal Instantiation (UI)**: ∀v α ⇒ α[v/t] for any term t.
- **Generalized Modus Ponens (GMP)**: Unify rule premises with facts, conclude θ(conclusion).

### Prolog
- **Backtracking**: DFS over search space; try choice, on failure try next.
- Father(John) is term if Father is function, sentence if predicate.

---

## 6. NLP Before LLMs

### Symbolic vs Statistical
- **Symbolic**: Hand-crafted rules, brittle.
- **Statistical**: Learn from data, more robust to variation.

### N-Grams & Sparsity
- **Data sparsity**: |V|^n possible n-grams; most never seen.
- **Markov assumption**: Limit context to n-1 words to reduce parameters.
- **Bigram**: P(w_n | w_{n-1}). **Unigram**: P(w) only—no grammar/order.

### Smoothing
- **MLE**: P(w|w_prev) = Count(w_prev, w) / Count(w_prev)
- **Add-1 (Laplace)**: (Count + 1) / (Count + |V|). Overestimates unseen.
- **Add-k** (k<1): Less mass to unseen events.

### Perplexity & Cross-Entropy
- **Perplexity = 2^(cross-entropy)** (or e^CE with ln)
- Lower = better model. Perplexity 100 ≈ 100 equally likely choices.

### Word Embeddings
- **Distributional hypothesis**: "You shall know a word by the company it keeps."
- **Skip-gram**: Two vectors per word (center, context).
- **Log-likelihood**: Avoids numerical underflow (product → sum).

### Word2Vec Limitations
- One vector per word (no sense disambiguation).
- No explicit word order/syntax.
- Limited negation, compositionality.

### Key Facts
- Similar context → similar vectors ("doctor"/"nurse"); co-occurrence ("king"/"throne") may differ.
- One-hot: orthogonal, no semantic similarity.
- Cosine similarity: 1 = similar, -1 = opposite.

---

## Quick Reference: Algorithm Choice

| Problem | Algorithm |
|---------|-----------|
| Path from start to goal | A*, UCS, BFS |
| Smooth landscape, good start | Hill Climbing |
| Rugged landscape, escape local opt | Simulated Annealing |
| Huge combinatorial space | GA or SA |
| Single smooth peak | Hill Climbing |
