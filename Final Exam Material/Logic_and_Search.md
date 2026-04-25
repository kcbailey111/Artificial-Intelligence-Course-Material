# Logic and Search - Final Exam Study Guide

This guide condenses the Logic and Search material into quick-review tables, core ideas, and practice prompts.

## 1) High-Yield Topic Map

| Topic | What to Know | Typical Exam Ask |
|---|---|---|
| Propositional Logic | Syntax, semantics, entailment, CNF, resolution | Convert to CNF, prove entailment |
| Uninformed Search | BFS, DFS, UCS, IDS tradeoffs | Pick algorithm by constraints |
| Informed Search | Heuristics, admissible vs consistent, A* | Prove/argue optimality conditions |
| First-Order Logic | Quantifiers, unification, forward/backward chaining | Translate English <-> FOL |
| Optimization Search | Hill climbing, simulated annealing, genetic algorithms | Identify local-optimum fixes |

## 2) Core Definitions (Must Memorize)

| Concept | Definition |
|---|---|
| Soundness | If system proves `phi`, then `phi` is true (`KB ⊢ phi => KB ⊨ phi`) |
| Completeness | If `phi` is true, system can prove it (`KB ⊨ phi => KB ⊢ phi`) |
| Admissible Heuristic | Never overestimates true cost to goal |
| Consistent Heuristic | Satisfies triangle inequality: `h(n) <= c(n,n') + h(n')` |
| Dominating Heuristic | Heuristic `h2` dominates `h1` if both admissible and `h2(n) >= h1(n)` for all `n` |

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

## 4) Logic Conversion Patterns

| English Pattern | Correct FOL Pattern |
|---|---|
| "All A are B" | `forall x (A(x) => B(x))` |
| "Some A are B" | `exists x (A(x) and B(x))` |
| "No A are B" | `forall x (A(x) => not B(x))` or `not exists x (A(x) and B(x))` |
| "Everyone loves someone" | `forall x exists y Loves(x,y)` |
| "Someone is loved by everyone" | `exists y forall x Loves(x,y)` |

## 5) Resolution / CNF Checklist

1. Eliminate `=>` and `<=>`.
2. Push negations inward (DeMorgan + double-negation).
3. Distribute `or` over `and`.
4. Remove tautological clauses.
5. Add negated query and resolve to contradiction.

If empty clause is derived, entailment is proven.

## 6) Heuristic Search: What to Compare

| Property | Why It Matters |
|---|---|
| Admissibility | Guarantees optimal A* solution |
| Consistency | Avoids reopen logic; more efficient graph search |
| Dominance | Fewer expansions with stronger admissible heuristic |
| Memory Use | A* is often memory bottleneck |

## 7) Optimization Methods Quick Compare

| Method | Strength | Weakness | Fix/Variant |
|---|---|---|---|
| Hill Climbing | Simple, fast | Local optima | Random restarts / stochastic |
| Simulated Annealing | Escapes local optima | Sensitive to cooling schedule | Geometric cooling (e.g. 0.99) |
| Genetic Algorithm | Strong global exploration | Many hyperparameters | Elitism + tuned mutation |

## 8) Common Exam Traps

- Confusing validity vs soundness.
- Treating implication as causation.
- Assuming `forall x exists y` equals `exists y forall x`.
- Using non-admissible heuristic and claiming A* optimality.
- Using DFS when completeness is required in potentially infinite depth.

## 9) Rapid Review Prompts

1. Why does admissibility imply A* optimality?
2. Give an example where greedy best-first fails.
3. Convert "No student is both absent and excused" to FOL.
4. Explain why beam search can discard optimal paths.
5. State one scenario where IDS is better than BFS.

## 10) Last-Minute Formula Sheet

- `f(n) = g(n) + h(n)` (A*)
- `h(n) <= h*(n)` (admissible)
- `h(n) <= c(n,n') + h(n')` (consistent)
- `MCC = (TP*TN - FP*FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN))`

