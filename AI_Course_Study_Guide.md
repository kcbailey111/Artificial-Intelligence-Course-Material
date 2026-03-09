# CSC-343: Artificial Intelligence — Comprehensive Study Guide

A consolidated study guide covering all course topics: Uninformed Search, Informed Search, Advanced Search, Propositional Logic, First-Order Logic, and NLP Before LLMs.

---

## Table of Contents

1. [Uninformed Search](#1-uninformed-search)
2. [Informed Search](#2-informed-search)
3. [Advanced Search (Optimization)](#3-advanced-search-optimization)
4. [Propositional Logic](#4-propositional-logic)
5. [First-Order Logic](#5-first-order-logic)
6. [NLP Before LLMs](#6-nlp-before-llms)

---

## 1. Uninformed Search

### Core Concepts

**Frontier**
- The set of nodes that have been generated but not yet expanded.
- Represents the boundary between explored and unexplored parts of the search space.
- How you select the next node (FIFO, LIFO, priority) defines the search strategy and its properties.

**Tree Search vs. Graph Search**
| | Tree Search | Graph Search |
|---|---|---|
| Explored set | No | Yes |
| Same state added multiple times? | Yes | No |
| When to use | Memory is critical; revisiting might help | Avoid redundant work; have memory for explored set |

**Completeness & Optimality**
- **Complete**: Finds a solution if one exists.
- **Optimal**: Finds the least-cost (or shortest) solution when costs matter.

### Algorithms

| Algorithm | Frontier Type | Order of Expansion | Complete? | Optimal? | Time | Space |
|-----------|---------------|--------------------|-----------|----------|------|-------|
| **BFS** | Queue (FIFO) | By depth | Yes (finite spaces) | Yes (uniform cost) | O(b^d) | O(b^d) |
| **DFS** | Stack (LIFO) | By depth (deep first) | No (infinite) | No | O(b^m) | O(bm) |
| **UCS** | Priority queue | By path cost g(n) | Yes | Yes | O(b^d) | O(b^d) |
| **IDS** | Stack (repeated) | By depth limit | Yes | Yes (uniform cost) | O(b^d) | O(bd) |

- **BFS**: Explores level by level; first goal found has minimum depth.
- **DFS**: Uses less memory; can find a solution quickly if goals are deep; may follow one path indefinitely in infinite spaces.
- **UCS**: Expands in order of increasing **path cost**, not depth. Depth and cost differ when edge costs vary.
- **IDS**: Repeated depth-limited searches with increasing limits. Redundant work at shallow levels is acceptable because most nodes are at deeper levels.

### Key Formulas

**Nodes generated (tree with branching factor b, solution at depth d):**
$$\text{Total nodes} = \frac{b^{d+1} - 1}{b - 1}$$

**Example:** b=4, d=5 → (4^6 - 1)/(4-1) = 1365 nodes.

### Important Facts

- In **graph search**, a node goes to the explored set when it is **expanded** (removed from the frontier), not when first generated.
- DFS uses O(bm) space, **not** O(b^d).
- IDS has the same asymptotic time complexity as BFS: O(b^d).

---

## 2. Informed Search

### Core Concepts

**Heuristic h(n)**
- Estimate of the cost from node n to the goal.
- **Admissible**: h(n) ≤ h*(n) for all n (never overestimates).
- **Consistent (monotonic)**: h(n) ≤ c(n, n′) + h(n′) for all successors n′.
- If consistent → admissible. Admissible does **not** imply consistent.

**Evaluation function**
- **A***: f(n) = g(n) + h(n), where g(n) = cost from start to n.
- **Greedy Best-First**: f(n) = h(n) only.
- **Weighted A***: f(n) = g(n) + w·h(n), w > 1; trades optimality for speed.

**Heuristic dominance**
- h₂ dominates h₁ if h₂(n) ≥ h₁(n) for all n.
- A dominating heuristic expands fewer nodes and is preferred when admissible.

### Why Admissibility Matters

If h overestimates for some nodes, A* can expand a suboptimal path first and return a non-optimal solution. Admissibility guarantees optimality.

### 8-Puzzle Heuristics

| Heuristic | Definition | Dominance |
|-----------|------------|-----------|
| **Misplaced tiles** (h₁) | Number of tiles not in goal position | — |
| **Manhattan distance** (h₂) | Sum of horizontal + vertical distances per tile | h₂ dominates h₁ |
| **Row/column** (h₃) | Tiles not in goal row + not in goal column | Compare per state |

### Beam Search

- Keeps only the top-k nodes by f(n) at each level.
- k=1 → equivalent to Greedy Best-First.
- **Not** complete or optimal; can prune the optimal path.
- Cannot infer inadmissibility from a suboptimal solution.

### Important Facts

- A* is optimal if h is admissible (consistency not required for optimality).
- If A* expands node n, then f(n) ≤ C*, where C* is the optimal cost.
- Weighted A* with w=2: solution cost at most 2× optimal (when h admissible).

---

## 3. Advanced Search (Optimization)

### When to Use What

| Use optimization (hill climbing, SA, GA) when | Use path-finding (A*) when |
|----------------------------------------------|----------------------------|
| No explicit start/goal; optimizing f(x) | Clear start and goal |
| Maximizing/minimizing objective (scheduling, TSP, tuning) | Path cost defines solution quality |
| Configuration search | Sequence of actions from start to goal |

### Hill Climbing

**Local optima**
- A state better than all neighbors but worse than the global optimum.
- Hill climbing stops when no neighbor improves f(x); it never accepts worse moves.

**Neighbor definition**
- **Small neighborhood**: Fewer options, faster steps, more likely to get stuck.
- **Large neighborhood**: More options, better escape from local optima, slower per step.

**Variants**
- **Random restart**: Multiple runs from random starts; with enough restarts, can find global optimum with probability → 1.
- ** plateau**: If all neighbors have equal f(x), standard hill climbing stops (or needs tie-breaking).

### Simulated Annealing

**Acceptance probability** (maximizing f):
$$P = e^{-\frac{|f(\text{current}) - f(\text{neighbor})|}{T}}$$

- **High T**: P ≈ 1 → more exploration (random walk).
- **Low T**: P ≈ 0 for worse moves → exploitation (like hill climbing).
- **T → 0**: Becomes hill climbing.
- **T → ∞**: Pure random walk.

**Cooling schedule**
- Controls how T decreases over time.
- **Too fast**: Behaves like hill climbing; may get stuck in local optimum.
- **Purpose**: Enough exploration early, then convergence to a good solution.

### Genetic Algorithms

- **Population**: Multiple candidate solutions.
- **Crossover**: Combines two parents; exploits good building blocks.
- **Mutation**: Random changes; adds diversity and helps escape local optima.
- **Elitism**: Keeps best individual(s) in the next generation; avoids losing the best solution.

**Why GA can beat hill climbing**
- Multiple regions explored in parallel.
- Mutation and crossover can escape local optima.
- Not tied to a single current state.

### 2-Opt (TSP)

- Reversing a contiguous segment of the tour yields a valid tour (Hamiltonian cycle).
- Larger neighborhoods do **not** guarantee better solutions; they increase cost per step.

### Important Facts

- A* uses **more** memory than hill climbing and GAs (O(b^d) frontier).
- Hill climbing finds the global optimum if there is only one local optimum.
- Higher mutation rate does **not** always improve convergence; too high disrupts good solutions.

---

## 4. Propositional Logic

### Core Concepts

**Validity vs. Soundness**
- **Valid**: If premises were true, the conclusion would be true (correct logical form).
- **Sound**: Valid **and** all premises are true. Soundness is what we want for reliable conclusions.

**Satisfiability**
- **Satisfiable**: Some assignment makes the formula true.
- **Tautology**: True in all models.
- **Unsatisfiable**: False in all models.
- If φ is a tautology, then ¬φ is unsatisfiable. (Satisfiable vs. ¬φ is a separate issue.)

**Entailment vs. Derivation**
- **KB ⊨ α**: α is true in every model where KB is true (entailment).
- **KB ⊢ α**: α can be derived from KB by the inference system (derivation).
- **Soundness**: If KB ⊢ α then KB ⊨ α.
- **Completeness**: If KB ⊨ α then KB ⊢ α. Soundness and completeness are independent.

### Representation

**CNF (Conjunctive Normal Form)**
- Conjunction of clauses; each clause is a disjunction of literals.
- Uses: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ D).

**Horn clauses & Definite clauses**
- **Horn clause**: At most one positive literal.
- **Definite clause**: Exactly one positive literal: A₁ ∧ … ∧ Aₙ ⇒ B.
- Forward and backward chaining require definite clauses.

### Inference Rules

**Modus Ponens**
- From P and P ⇒ Q, derive Q.

**Resolution**
- From (A ∨ B) and (¬A ∨ C), derive (B ∨ C).
- **Resolution refutation**: To show KB ⊨ α, show that KB ∧ ¬α is unsatisfiable (derive empty clause ∅).

**Important**: If we cannot derive ∅, we **cannot** conclude entailment.

### Forward vs. Backward Chaining

| | Forward Chaining | Backward Chaining |
|---|---|---|
| Direction | Data-driven (facts → goal) | Goal-driven (goal → facts) |
| Start | Known facts | Query |
| Prefer when | Many facts, broad inference | Specific goal, small relevant subset |

- Both require definite clauses; both terminate on finite KBs.
- Forward chaining is **not** complete for full propositional logic (e.g., cannot derive P∨Q from {P∨Q} with Horn-clause rules).
- Negated literals in clauses complicate forward/backward chaining (need semantics for negation).

### Enumeration

- Truth tables: 2^n rows for n propositional symbols.
- Time complexity: O(2^n) — intractable for large n.

### Logical Equivalences

- (P ⇒ Q) ≡ (¬Q ⇒ ¬P) (contrapositive)
- (P ∨ ¬P) is a tautology; can be removed from CNF.
- P ⇔ Q ≡ (P⇒Q) ∧ (Q⇒P) ≡ (¬P∨Q) ∧ (¬Q∨P)

---

## 5. First-Order Logic (FOL)

### Why FOL?

Propositional logic cannot compactly express objects, relations, and quantifiers. FOL adds:
- Terms (constants, variables, functions)
- Predicates
- Quantifiers: ∀ (universal), ∃ (existential)

### Terms vs. Sentences

- **Term**: Object-denoting expression (e.g., x, Father(John)).
- **Sentence**: Truth-valued formula (e.g., Bird(Tweety), ∀x Bird(x) ⇒ Has_Feathers(x)).

### Unification

**Goal**: Find a substitution θ such that expressions become identical.
- **MGU (Most General Unifier)**: A substitution that unifies with the fewest constraints.
- **Occurs check**: Prevents X = f(X), which would create infinite terms. If variable X appears in term t and X ≠ t, unification fails.

**Examples**
- Unify P(X, a) and P(b, X): Fails (X would need to be both a and b).
- Unify X with g(A, X): Fails (occurs check).
- Likes(X, Ice_Cream) and Likes(John, Y): θ = {X/John, Y/Ice_Cream}.
- Parent(X, Father(X)) and Parent(Alice, Y): θ = {X/Alice, Y/Father(Alice)}.
- F(X, g(X)) and F(g(Y), Y): Fails (occurs check).

### Universal Instantiation

- From ∀x P(x), derive P(c) for any ground term c.
- Enables applying Modus Ponens with universally quantified rules.

### Generalized Modus Ponens

- Combines unification and Universal Instantiation with Modus Ponens.
- From ∀x Bird(x) ⇒ Has_Feathers(x) and Bird(Tweety), unify x/Tweety and derive Has_Feathers(Tweety).

### Forward Chaining in FOL

- Start from facts, apply rules using unification.
- **Not** goal-directed; derives all possible facts.
- Different from propositional forward chaining in that unification matches variables to constants/terms.

### Prolog

- **Backtracking**: When a goal fails, Prolog backtracks to try alternative clauses.
- **append/3**: append([], L, L). append([H|T1], L2, [H|T3]) :- append(T1, L2, T3).
- Trace queries by recursive pattern matching and backtracking.

### Quantifier Notes

- ∀X ∃Y Loves(X, Y) ≠ ∃Y ∀X Loves(X, Y).
- ∀x ¬P(x) ≡ ¬∃x P(x) (De Morgan for quantifiers).

---

## 6. NLP Before LLMs

### Symbolic vs. Statistical NLP

| Symbolic/Rule-based | Statistical |
|---------------------|-------------|
| Hand-crafted rules and lexicons | Patterns learned from data |
| Explicit linguistic knowledge | Probabilities from corpora |
| Brittle on unexpected input | More robust to variation and noise |

### Data Sparsity

- Number of n-grams grows as |V|^n.
- Most sequences have zero or few counts; we cannot memorize all probabilities.
- **Markov assumption**: Limit context to n-1 words to make estimation feasible.

### N-gram Language Models

**Maximum Likelihood Estimation (MLE)**
$$P(w_n | w_{n-1}) = \frac{\text{Count}(w_{n-1}, w_n)}{\text{Count}(w_{n-1})}$$

**Smoothing**
- **Add-1 (Laplace)**: P = (Count + 1) / (Count(context) + |V|). Often overestimates unseen events.
- **Add-k** (k < 1): Less probability mass to unseen events than add-1.

**Sentence probability (bigram)**
$$P(w_1 \ldots w_n) = P(w_1|\text{START}) \cdot \prod_{i=2}^{n} P(w_i|w_{i-1}) \cdot P(\text{END}|w_n)$$

### Evaluation

**Cross-entropy** (bits per word):
$$H = -\frac{1}{N} \sum_{i=1}^{N} \log_2 P(w_i | \text{context})$$

**Perplexity**
$$\text{Perplexity} = 2^H = 2^{\text{cross-entropy}}$$

- Lower cross-entropy → lower perplexity → better model.
- Perplexity ≈ effective number of equally likely choices per word.

### Log-Likelihood

- Products of many small probabilities cause underflow.
- log(∏ p_i) = Σ log(p_i) avoids underflow and is monotonic, so maximizing log-likelihood = maximizing likelihood.

### Word Embeddings

**Distributional hypothesis**
- “You shall know a word by the company it keeps.”
- Words in similar contexts have similar meanings.

**Word2Vec**
- **Skip-gram**: Center word → predict context words. Generates (center, context) pairs.
- **CBOW**: Context words → predict center word.
- Each word has two vectors: center (input) and context (output); final embedding often uses the center vector.

**Window size**
- Larger: longer-range dependencies, more topical/semantic.
- Smaller: local syntax, immediate neighbors.
- Window 2: 2 words left and right of center.

**Cosine similarity**: -1 to 1; values near 1 mean similar direction (similar meaning).

### Limitations of Word2Vec

1. One vector per word — no sense disambiguation; homonyms share representation.
2. Limited word order/syntax; only context windows.
3. Weak handling of negation, compositionality, and complex semantics.

### One-Hot Vectors

- Orthogonal; cosine similarity 0 between different words.
- Do **not** capture semantic similarity.

---

## Study Tips

1. **Uninformed Search**: Practice tracing BFS, DFS, UCS, IDS with frontier/explored set and the node-count formula.
2. **Informed Search**: Compute 8-puzzle heuristics, check admissibility, and trace A* with f-values.
3. **Advanced Search**: Identify local optima, compute acceptance probabilities for SA, and choose the right algorithm for problem type.
4. **Propositional Logic**: Practice resolution refutation, CNF conversion, and forward/backward chaining.
5. **First-Order Logic**: Practice unification (including occurs check) and forward chaining with Generalized Modus Ponens.
6. **NLP**: Compute MLE and smoothed probabilities, cross-entropy, perplexity, and Skip-gram (center, context) pairs.

---

*Good luck on your exam!*
