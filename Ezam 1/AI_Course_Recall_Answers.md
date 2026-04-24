# CSC-343: AI Course — Recall Practice Answers

---

## 1. Uninformed Search

1. **Frontier**: The set of nodes that have been generated but not yet expanded. It represents the boundary between explored and unexplored parts of the search space.

2. In graph search, a node goes to the explored set when it is **expanded** (removed from the frontier), not when first generated.

3. **Completeness**: The algorithm finds a solution if one exists.

4. **Optimality**: The algorithm finds the least-cost (or shortest) solution when costs matter.

5. BFS uses a **queue (FIFO)** and expands nodes by depth (level by level).

6. DFS uses a **stack (LIFO)** and expands nodes by depth (deep first).

7. **UCS** orders by path cost **g(n)**, while BFS orders by depth. When edge costs vary, depth ≠ cost.

8. **b** = branching factor, **m** = maximum depth of the search tree, **d** = depth of the shallowest goal.

9. IDS has the same asymptotic time complexity as BFS: **O(b^d)**.

10. **Total nodes** = (b^(d+1) − 1) / (b − 1).

11. Use tree search when **memory is critical** and revisiting states might help. Use graph search when you have memory and want to avoid redundant work.

12. DFS is **not complete** in infinite state spaces and **not optimal**.

---

## 2. Informed Search

1. **Heuristic h(n)**: An estimate of the cost from node n to the goal.

2. **Admissible**: h(n) ≤ h*(n) for all n (never overestimates). It guarantees A* is **optimal**.

3. **Consistent (monotonic)**: h(n) ≤ c(n, n′) + h(n′) for all successors n′. Yes, consistent implies admissible.

4. No. Admissible does **not** imply consistent.

5. **f(n) = g(n) + h(n)**, where g(n) = cost from start to n.

6. **f(n) = h(n)** only.

7. **h₂ dominates h₁** if h₂(n) ≥ h₁(n) for all n. The dominating heuristic expands fewer nodes (when admissible).

8. **Misplaced tiles** (h₁) and **Manhattan distance** (h₂). Manhattan distance dominates misplaced tiles.

9. **f(n) = g(n) + w·h(n)** with w > 1. Trades **optimality** for **speed** (w=2: cost at most 2× optimal when h admissible).

10. **f(n) ≤ C***, where C* is the optimal cost.

11. Beam search is **not complete** and **not optimal**; it can prune the optimal path.

12. **No.** Beam search can prune the optimal path; you cannot infer inadmissibility from a suboptimal result.

---

## 3. Advanced Search (Optimization)

1. Use optimization (hill climbing, SA, GA) when there is **no explicit start/goal**, when you are **maximizing/minimizing an objective** (e.g., scheduling, TSP, tuning), or when it’s **configuration search**. Use A* when there is a clear start and goal and path cost defines solution quality.

2. **Local optimum**: A state that is better than all neighbors but worse than the global optimum.

3. No. Hill climbing never accepts a worse move; it stops when no neighbor improves f(x).

4. **Random restart**: Run hill climbing from multiple random starts. With enough restarts, the probability of finding the global optimum approaches 1.

5. **High T**: P ≈ 1 → more exploration (random walk). **Low T**: P ≈ 0 for worse moves → exploitation (like hill climbing).

6. **P = e^(-|f(current) − f(neighbor)| / T)** (for maximizing f).

7. With **too fast** cooling, SA behaves like hill climbing and may get stuck in a local optimum.

8. **Crossover**: Combines two parents; exploits good building blocks. **Mutation**: Random changes; adds diversity and helps escape local optima.

9. **Elitism**: Keeping the best individual(s) in the next generation to avoid losing the best solution.

10. GAs maintain a **population** and explore multiple regions in parallel; **mutation and crossover** can escape local optima; they are not tied to a single current state.

11. **2-opt**: Reversing a contiguous segment of the tour to produce a valid Hamiltonian cycle (another valid tour).

12. **No.** Too high mutation can disrupt good solutions; it does not always improve convergence.

13. A* uses **more** memory (O(b^d) frontier); hill climbing uses much less.

---

## 4. Propositional Logic

1. **Valid**: If the premises were true, the conclusion would be true (correct logical form). **Sound**: Valid **and** all premises are true; soundness is what we want for reliable conclusions.

2. **Satisfiable**: Some assignment makes it true. **Unsatisfiable**: False in all models. **Tautology**: True in all models.

3. If φ is a tautology, then **¬φ is unsatisfiable**.

4. **KB ⊨ α** (entailment): α is true in every model where KB is true.

5. **KB ⊢ α** (derivation): α can be derived from KB by the inference system.

6. **Soundness**: If KB ⊢ α then KB ⊨ α. **Completeness**: If KB ⊨ α then KB ⊢ α. They are independent.

7. **CNF**: Conjunction of clauses; each clause is a disjunction of literals. Example: (A ∨ B) ∧ (¬A ∨ C) ∧ (¬B ∨ D).

8. **Horn clause**: At most one positive literal. **Definite clause**: Exactly one positive literal: A₁ ∧ … ∧ Aₙ ⇒ B.

9. **Definite clauses**.

10. **Modus Ponens**: From P and P ⇒ Q, derive Q.

11. From (A ∨ B) and (¬A ∨ C) derive **(B ∨ C)**.

12. Show that **KB ∧ ¬α is unsatisfiable** (derive the empty clause ∅).

13. **No.** If we cannot derive ∅, we cannot conclude entailment.

14. **Forward chaining**: Data-driven (facts → goal). **Backward chaining**: Goal-driven (goal → facts).

15. **O(2^n)** — 2^n rows for n propositional symbols.

16. Contrapositive of P ⇒ Q: **¬Q ⇒ ¬P**.

---

## 5. First-Order Logic

1. Propositional logic cannot compactly express **objects, relations, and quantifiers**. FOL adds terms, predicates, and quantifiers.

2. **Constants** (e.g., John), **variables** (e.g., x), **functions** (e.g., Father(John)).

3. **MGU** = Most General Unifier. A substitution that unifies with the fewest constraints.

4. **Occurs check**: If variable X appears in term t and X ≠ t, unification fails (prevents X = f(X) and infinite terms).

5. **No.** X would need to be both a and b, which is impossible.

6. **No.** Occurs check fails: X appears in g(A, X).

7. **θ = {X/John, Y/Ice_Cream}**.

8. **Universal Instantiation**: From ∀x P(x), derive P(c) for any ground term c.

9. **Generalized Modus Ponens** combines unification, Universal Instantiation, and Modus Ponens to apply universally quantified rules (e.g., Bird(x) ⇒ Has_Feathers(x) with Bird(Tweety) → Has_Feathers(Tweety)).

10. **No.** FOL forward chaining is not goal-directed; it derives all possible facts.

11. Prolog **backtracks** to try alternative clauses when a goal fails.

12. **No.** ∀X ∃Y Loves(X,Y) = everyone loves someone; ∃Y ∀X Loves(X,Y) = someone is loved by everyone. Order matters.

13. **∀x ¬P(x) ≡ ¬∃x P(x)**.

---

## 6. NLP Before LLMs

1. **Symbolic**: Brittle on unexpected input. **Statistical**: More robust to variation and noise.

2. **Data sparsity**: The number of n-grams grows as |V|^n; most sequences have zero or few counts, so we cannot memorize all probabilities.

3. **Markov assumption**: Limit context to the previous n−1 words to make estimation feasible.

4. **P(w_n | w_{n-1}) = Count(w_{n-1}, w_n) / Count(w_{n-1})**.

5. Add 1 to the count in the numerator; add |V| (vocabulary size) to the denominator. P = (Count + 1) / (Count(context) + |V|).

6. **P(w_1 … w_n) = P(w_1|START) · ∏_{i=2}^{n} P(w_i|w_{i-1}) · P(END|w_n)**.

7. **H = −(1/N) Σ log₂ P(w_i | context)**. **Lower** is better.

8. **Perplexity = 2^H** = 2^(cross-entropy). Lower perplexity = better model; it approximates the effective number of equally likely choices per word.

9. Products of many small probabilities cause **underflow**. log(∏ p_i) = Σ log(p_i) avoids underflow and is monotonic.

10. **“You shall know a word by the company it keeps.”** Words in similar contexts tend to have similar meanings.

11. **Skip-gram**: Center word → predict **context** words.

12. **CBOW**: Context words → predict **center** word.

13. **Larger window**: Longer-range dependencies, more topical/semantic. **Smaller window**: Local syntax, immediate neighbors.

14. Cosine similarity near 1 means **similar direction** → **similar meaning**.

15. **No.** One-hot vectors are orthogonal; cosine similarity is 0 between different words; they do not capture semantic similarity.

16. (1) One vector per word — no sense disambiguation; homonyms share representation. (2) Limited word order/syntax; only context windows. (3) Weak handling of negation, compositionality, and complex semantics.

---

*Answers correspond to the questions in AI_Course_Recall_Questions.md.*
