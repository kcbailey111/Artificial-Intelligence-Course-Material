# CSC-343: AI Course — Recall Practice Questions

Use these questions for active recall. Cover the answers and try to answer from memory before checking.

---

## 1. Uninformed Search

1. What is the **frontier** in search, and what does it represent?

2. In graph search vs. tree search, when is a node added to the **explored set**?

3. What does **completeness** mean for a search algorithm?

4. What does **optimality** mean for a search algorithm?

5. Which frontier structure does BFS use, and in what order does it expand nodes?

6. Which frontier structure does DFS use, and in what order does it expand nodes?

7. What is the key difference between UCS and BFS in terms of what they order by?

8. DFS uses O(bm) space, not O(b^d). What do b, m, and d represent?

9. IDS repeats depth-limited search with increasing limits. What is its asymptotic time complexity compared to BFS?

10. Write the formula for total nodes in a tree with branching factor b and solution at depth d.

11. Under what condition would you prefer **tree search** over **graph search**?

12. Is DFS complete in infinite state spaces? Optimal?

---

## 2. Informed Search

1. What is a **heuristic h(n)** in the context of informed search?

2. Define **admissible** heuristic. What property does it guarantee for A*?

3. Define **consistent (monotonic)** heuristic. Does consistent imply admissible?

4. Does admissible imply consistent?

5. Write the evaluation function f(n) for A* search.

6. Write the evaluation function for **Greedy Best-First** search.

7. What does **heuristic dominance** mean? If h₂ dominates h₁, which expands fewer nodes?

8. Name the two classic 8-puzzle heuristics and state which dominates the other.

9. What does **Weighted A*** use for f(n)? What does w > 1 trade off?

10. If A* uses admissible h and expands node n, what can you say about f(n) relative to C*?

11. Beam search keeps only the top-k nodes by f(n). Is it complete? Optimal?

12. Can beam search returning a suboptimal solution prove that the heuristic is inadmissible?

---

## 3. Advanced Search (Optimization)

1. When should you use **hill climbing / SA / GA** instead of A*?

2. Define **local optimum** in the context of hill climbing.

3. Does hill climbing ever accept a worse move?

4. How does **random restart** hill climbing help find the global optimum?

5. In simulated annealing, what happens when temperature T is high vs. low?

6. Write the acceptance probability formula for simulated annealing (maximizing f).

7. If the cooling schedule is **too fast**, what behavior does SA exhibit?

8. In genetic algorithms, what is the role of **crossover**? Of **mutation**?

9. What does **elitism** mean in GAs?

10. Why can GAs escape local optima when hill climbing cannot?

11. What is the 2-opt move in TSP?

12. Does a higher mutation rate in GAs always improve convergence?

13. Compare A* vs. hill climbing in terms of memory use.

---

## 4. Propositional Logic

1. What is the difference between **valid** and **sound**?

2. When is a formula **satisfiable**? **Unsatisfiable**? A **tautology**?

3. If φ is a tautology, what can you say about ¬φ?

4. What does KB ⊨ α mean (entailment)?

5. What does KB ⊢ α mean (derivation)?

6. Define **soundness** of an inference system. What about **completeness**?

7. What is **CNF** (Conjunctive Normal Form)? Give an example.

8. What is a **Horn clause**? A **definite clause**?

9. Forward and backward chaining require what type of clauses?

10. State the **Modus Ponens** rule.

11. In **resolution**, from (A ∨ B) and (¬A ∨ C) what do you derive?

12. For **resolution refutation** to show KB ⊨ α, what must you show about KB ∧ ¬α?

13. If we cannot derive the empty clause, can we conclude entailment?

14. What is the direction of forward chaining (data-driven or goal-driven)? Backward chaining?

15. What is the time complexity of truth-table enumeration for n propositional symbols?

16. Write the contrapositive of P ⇒ Q.

---

## 5. First-Order Logic

1. Why do we need FOL over propositional logic?

2. What are the three kinds of **terms** in FOL?

3. What does **MGU** stand for, and what property does it have?

4. What is the **occurs check** in unification? Why is it needed?

5. Does P(X, a) unify with P(b, X)? Why or why not?

6. Does X unify with g(A, X)? Why or why not?

7. Unify Likes(X, Ice_Cream) and Likes(John, Y). What is θ?

8. What is **Universal Instantiation**?

9. Describe **Generalized Modus Ponens** and what it combines.

10. Is forward chaining in FOL goal-directed?

11. In Prolog, what happens when a goal fails (backtracking)?

12. Are ∀X ∃Y Loves(X, Y) and ∃Y ∀X Loves(X, Y) equivalent? Explain.

13. State De Morgan’s law for quantifiers: ∀x ¬P(x) ≡ ?

---

## 6. NLP Before LLMs

1. Contrast **symbolic** and **statistical** NLP in terms of how they handle unexpected input.

2. What is **data sparsity** in n-gram models? How does vocabulary size affect it?

3. What does the **Markov assumption** say about context?

4. Write the MLE formula for bigram probability P(w_n | w_{n-1}).

5. In **Add-1 (Laplace)** smoothing, what is added to the numerator and denominator?

6. Write the formula for sentence probability in a bigram model (with START and END).

7. What is **cross-entropy** in bits per word? Lower is better or worse?

8. What is **perplexity**, and how does it relate to cross-entropy?

9. Why do we use **log-likelihood** instead of raw likelihood for long sequences?

10. State the **distributional hypothesis** for word meaning.

11. In **Skip-gram**, does the model predict context from center, or center from context?

12. In **CBOW**, what does the model predict?

13. What does a larger **window size** in Word2Vec capture vs. a smaller one?

14. If two words have cosine similarity near 1, what does that mean?

15. Do **one-hot** vectors capture semantic similarity? Why or why not?

16. Name three limitations of Word2Vec.

---

*Total: 100+ recall questions across all topics.*
