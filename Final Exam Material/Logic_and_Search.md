# Logic and Search - Final Exam Study Guide

This guide condenses Logic and Search into quick-review tables, core ideas, and deeper exam reasoning patterns.

## 1) High-Yield Topic Map

| Topic | What to Know | Typical Exam Ask |
|---|---|---|
| Propositional Logic | Syntax, semantics, entailment, CNF, resolution | Convert to CNF, prove entailment |
| Uninformed Search | BFS, DFS, UCS, IDS tradeoffs | Pick algorithm by constraints |
| Informed Search | Heuristics, admissible vs consistent, A* | Prove/argue optimality conditions |
| First-Order Logic | Quantifiers, unification, forward/backward chaining | Translate English <-> FOL |
| Optimization Search | Hill climbing, simulated annealing, genetic algorithms | Identify local-optimum fixes |

## 1.5) Unifying Mental Model

- **Logic** answers "what must be true?" using formal inference.
- **Search** answers "how do we find a good/optimal action sequence?"
- Many exam questions combine both: represent knowledge correctly first, then choose inference/search method.
- Typical failure mode: correct concept, wrong assumptions (e.g., using non-admissible heuristic but claiming A* optimality).

## 2) Core Definitions (Must Memorize)

| Concept | Definition |
|---|---|
| Soundness | If system proves `phi`, then `phi` is true (`KB ⊢ phi => KB ⊨ phi`) |
| Completeness | If `phi` is true, system can prove it (`KB ⊨ phi => KB ⊢ phi`) |
| Admissible Heuristic | Never overestimates true cost to goal |
| Consistent Heuristic | Satisfies triangle inequality: `h(n) <= c(n,n') + h(n')` |
| Dominating Heuristic | Heuristic `h2` dominates `h1` if both admissible and `h2(n) >= h1(n)` for all `n` |

### Critical Distinctions (Frequently Tested)

- **Validity vs satisfiability:** valid means true in all models; satisfiable means true in at least one model.
- **Entailment (`⊨`) vs derivability (`⊢`):** semantic truth vs proof-system consequence.
- **Knowledge base consistency:** inconsistent KB can entail everything (principle of explosion in classical logic).

## 3) Search Algorithms Cheat Table

| Algorithm | Complete? | Optimal? | Time | Space | Best Use |
|---|---|---|---|---|---|
| BFS | Yes | Yes (unit or monotone edge costs) | `O(b^d)` | `O(b^d)` | Shallow solutions |
| DFS | No (in infinite depth) | No | `O(b^m)` | `O(bm)` | Very low memory |
| UCS | Yes (`epsilon > 0`) | Yes | `O(b^(C*/epsilon))` | `O(b^(C*/epsilon))` | Non-uniform costs |
| IDS | Yes | Yes (unit costs) | `O(b^d)` | `O(bd)` | Unknown depth + low memory |
| A* | Yes (admissible) | Yes (with standard conditions) | Exponential worst-case | Exponential | Good heuristic available |
| IDA* | Yes | Yes (admissible) | Exponential + re-expansion | DFS-like | A* but memory-limited |
| Beam | Usually no | No | `O(kd)` | `O(k)` | Fast approximate search |

### Selection Heuristic (What to write on exam)

1. If costs differ, prefer **UCS/A*** over BFS/IDS.
2. If memory is constrained, prefer **IDS/IDA*/DFS variants**.
3. If optimality is mandatory, reject greedy/beam unless stated acceptable.
4. If heuristic quality is strong, A* typically dominates uninformed alternatives in practice.

## 4) Logic Conversion Patterns

| English Pattern | Correct FOL Pattern |
|---|---|
| "All A are B" | `forall x (A(x) => B(x))` |
| "Some A are B" | `exists x (A(x) and B(x))` |
| "No A are B" | `forall x (A(x) => not B(x))` or `not exists x (A(x) and B(x))` |
| "Everyone loves someone" | `forall x exists y Loves(x,y)` |
| "Someone is loved by everyone" | `exists y forall x Loves(x,y)` |

### Quantifier Order Trap (Must Know)

- `forall x exists y Loves(x,y)`: each person may love a different person.
- `exists y forall x Loves(x,y)`: one specific person is loved by everyone.
- Same symbols, different meaning; quantifier order is semantically critical.

## 5) Resolution / CNF Checklist

1. Eliminate `=>` and `<=>`.
2. Push negations inward (DeMorgan + double-negation).
3. Distribute `or` over `and`.
4. Remove tautological clauses.
5. Add negated query and resolve to contradiction.

If empty clause is derived, entailment is proven.

### CNF Conversion Pitfalls

- Forgetting standardization apart for quantified variables.
- Skipping Skolemization details before dropping existential quantifiers.
- Distributing incorrectly: `A or (B and C)` becomes `(A or B) and (A or C)`.
- Not preserving logical equivalence (or equisatisfiability where appropriate).

## 6) Heuristic Search: What to Compare

| Property | Why It Matters |
|---|---|
| Admissibility | Guarantees optimal A* solution |
| Consistency | Avoids reopen logic; more efficient graph search |
| Dominance | Fewer expansions with stronger admissible heuristic |
| Memory Use | A* is often memory bottleneck |

### Why Consistency Helps A*

- With consistent `h`, `f(n)=g(n)+h(n)` is nondecreasing along paths.
- This implies once a node is expanded in graph search, its best path is finalized.
- Result: fewer reopen operations and cleaner optimality argument.

### Dominance in One Line

If `h2` dominates `h1` and both are admissible, A* with `h2` expands no more nodes than with `h1` (except ties).

## 7) Optimization Methods Quick Compare

| Method | Strength | Weakness | Fix/Variant |
|---|---|---|---|
| Hill Climbing | Simple, fast | Local optima | Random restarts / stochastic |
| Simulated Annealing | Escapes local optima | Sensitive to cooling schedule | Geometric cooling (e.g. 0.99) |
| Genetic Algorithm | Strong global exploration | Many hyperparameters | Elitism + tuned mutation |

### Optimization Intuition

- Hill climbing is local and greedy; excellent speed, weak global guarantees.
- Simulated annealing adds controlled uphill moves to escape local traps.
- Genetic algorithms maintain population diversity, reducing single-start bias.
- Choose by landscape shape: smooth/local -> hill climb; rugged/multimodal -> SA/GA.

## 8) Common Exam Traps

- Confusing validity vs soundness.
- Treating implication as causation.
- Assuming `forall x exists y` equals `exists y forall x`.
- Using non-admissible heuristic and claiming A* optimality.
- Using DFS when completeness is required in potentially infinite depth.
- Confusing UCS with BFS when action costs are unequal.
- Assuming greedy best-first is optimal because it uses heuristics.

## 8.5) Worked Micro Example (A* vs Greedy)

Suppose two frontier nodes:
- Node A: `g=8`, `h=1`, so `f=9`
- Node B: `g=3`, `h=7`, so `f=10`

Greedy best-first picks smaller `h` -> Node A.
A* picks smaller `f` -> Node A here, but if A had `g=12,h=1` (`f=13`) and B stayed (`f=10`), A* picks B while greedy still picks A. This is why greedy can be faster yet non-optimal.

## 9) Rapid Review Prompts

1. Why does admissibility imply A* optimality?
2. Give an example where greedy best-first fails.
3. Convert "No student is both absent and excused" to FOL.
4. Explain why beam search can discard optimal paths.
5. State one scenario where IDS is better than BFS.
6. Why does consistency reduce node reopenings in A* graph search?
7. Give one example where UCS is required over BFS.

## 10) Last-Minute Formula Sheet

- `f(n) = g(n) + h(n)` (A*)
- `h(n) <= h*(n)` (admissible)
- `h(n) <= c(n,n') + h(n')` (consistent)
- `MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))`

## 11) Rapid Answer Templates (Written Questions)

### "Choose a search algorithm"

1. State path-cost model (unit vs non-uniform).
2. State requirements (complete/optimal/memory/time).
3. Select algorithm matching constraints.
4. Justify with one complexity and one guarantee statement.

### "Argue A* optimality"

1. State admissibility (and consistency for graph-search efficiency).
2. Define `f(n)=g(n)+h(n)`.
3. Explain why goal popped from frontier has minimal path cost under assumptions.
4. Mention caveat if heuristic is non-admissible.

### "Translate English to FOL"

1. Define predicates clearly.
2. Decide quantifier scope/order first.
3. Write formula and sanity-check with plain-language paraphrase.
4. Flag ambiguous wording if multiple formalizations are possible.

