# Other Topics - Final Exam Study Guide

This section captures material adjacent to the core categories, especially games and decision-making frameworks, with deeper exam-focused intuition.

## 1) Topic Map

| Topic | Core Idea | Exam Angle |
|---|---|---|
| Game Theory Basics | Strategic interaction among rational agents | Identify equilibrium outcomes |
| Zero-sum Games | One player's gain is another's loss | Minimax reasoning |
| Minimax Search | Optimal play under adversarial setting | Build game tree decisions |
| Alpha-Beta Pruning | Prune irrelevant minimax branches | Analyze pruning effects |
| Mixed Strategies | Randomized action selection | Compute expected utility |

## 1.5) Why This Topic Matters

- Multi-agent settings differ from single-agent optimization because outcome quality depends on **opponent actions**.
- In adversarial problems, "best move" means best under **worst-case rational response**, not average-case.
- Game-theoretic tools formalize strategic stability, while search tools compute practical decisions in trees.
- Exam questions often combine concepts: e.g., "find Nash in matrix, then reason about minimax in tree form."

## 2) Core Terms

| Term | Meaning |
|---|---|
| Strategy | Complete action plan in game |
| Payoff | Utility received from outcome |
| Nash Equilibrium | No player benefits by unilateral deviation |
| Dominant Strategy | Best action regardless of opponent action |
| Saddle Point | Stable pure-strategy solution in zero-sum matrix |

### High-Value Clarifications

- **Dominant strategy vs Nash equilibrium:** a dominant strategy is about one player's action quality across all opponent moves; Nash is about mutual best responses.
- **Pure vs mixed strategy:** pure picks one action with probability `1`; mixed randomizes with non-zero probabilities.
- **Zero-sum:** if utilities are `(u, -u)`, maximizing one is minimizing the other exactly.
- **Common-payoff/cooperative games:** not zero-sum; minimax logic does not directly apply the same way.

## 3) Minimax and Alpha-Beta Quick Compare

| Method | Guarantee | Time (worst) | Main Benefit |
|---|---|---|---|
| Minimax | Optimal adversarial play | `O(b^d)` | Correct game-theoretic choice |
| Alpha-Beta | Same minimax result | Up to `O(b^(d/2))` with ideal ordering | Major speedup |

### Complexity Intuition

- `b` = branching factor (moves per position), `d` = search depth.
- Exponential growth is why heuristics, pruning, and move ordering are essential.
- Alpha-beta improves effective depth reachable under fixed compute, not theoretical optimality.
- In real systems, iterative deepening + good ordering can yield large practical gains.

## 4) Minimax Procedure (Exam Steps)

1. Expand game tree to depth limit or terminal states.
2. Evaluate terminal/leaf utilities.
3. Back up values: max at MAX nodes, min at MIN nodes.
4. Choose root action with best backed-up value.

### When Full Search Is Impossible

| Constraint | Standard Fix | Tradeoff |
|---|---|---|
| Tree too large | Depth-limited minimax | Horizon effect risk |
| Expensive leaves | Heuristic evaluation | Approximation error |
| Fixed time budget | Iterative deepening | Repeated work, but better anytime behavior |
| Tactical traps | Quiescence extensions | More compute in volatile positions |

### Horizon Effect (Exam Phrase)

- A bad event just beyond depth limit can be hidden from the agent.
- Mitigate with better evaluation and selective extension in unstable/tactical states.

## 5) Alpha-Beta Intuition

| Bound | Meaning | Prune Condition |
|---|---|---|
| `alpha` | Best value MAX can force so far | At MIN node, if value `<= alpha`, prune |
| `beta` | Best value MIN can force so far | At MAX node, if value `>= beta`, prune |

Node ordering quality strongly affects pruning effectiveness.

### Alpha-Beta Invariant (Important)

- Alpha-beta pruning is **sound** because pruned branches cannot influence ancestor decisions given current bounds.
- Therefore, final root choice is identical to plain minimax with same depth/evaluation.
- If exam asks "what changed?": **nodes expanded changed, decision quality did not** (assuming same evaluation and depth).

### Tiny Pruning Example

At a MIN node, if current best value becomes `3` while ancestor MAX already has `alpha = 5`, then MIN can do no better than `3` for MAX. Since MAX already has a guaranteed `5` elsewhere, this branch is irrelevant and can be pruned.

## 6) Normal-Form Game Matrix Checklist

- Identify each player's action set.
- Fill payoff pairs carefully `(u1, u2)`.
- Remove strictly dominated strategies if present.
- Locate mutual best responses (candidate Nash equilibria).
- Distinguish pure vs mixed equilibria.

### Best-Response Method (Reliable for Exams)

1. Mark Player 1 best responses for each action of Player 2.
2. Mark Player 2 best responses for each action of Player 1.
3. Intersections are pure Nash equilibria.
4. If none exist, solve for mixed equilibrium by making opponents indifferent.

### Mixed Strategy 2x2 Recipe

For player probabilities `p` and `q`:
- Choose `p` so opponent's expected payoff from their two actions is equal.
- Choose `q` so your expected payoff from your two actions is equal.
- Solve linear equations, then verify probabilities in `[0,1]`.

## 7) Common Mistakes

- Confusing dominant strategy with equilibrium.
- Forgetting that multiple Nash equilibria can exist.
- Claiming alpha-beta changes the final move choice (it should not).
- Mixing utility scales between players in zero-sum setup.
- Assuming "random play" means mixed equilibrium (must satisfy indifference conditions).
- Forgetting tie cases where multiple best responses produce multiple equilibria.

## 7.5) Solved Micro Example (Pure Nash)

Payoff matrix (Player 1 rows, Player 2 columns):

|   | L | R |
|---|---|---|
| U | (2,1) | (0,0) |
| D | (1,0) | (3,2) |

- Player 1 best responses: to `L` -> `U` (2 > 1), to `R` -> `D` (3 > 0)
- Player 2 best responses: to `U` -> `L` (1 > 0), to `D` -> `R` (2 > 0)
- Intersections: `(U,L)` and `(D,R)` are both Nash equilibria.

## 8) Rapid Practice Prompts

1. Why does alpha-beta never change minimax optimality?
2. Give an example of a game with no dominant strategy but with Nash equilibrium.
3. How does better move ordering change search cost?
4. When do mixed strategies become necessary?
5. Why can a game have multiple Nash equilibria, and why is selection hard?
6. Explain horizon effect in one sentence and one mitigation.
7. In a zero-sum game, why does maximin equal minimax at equilibrium?

## 9) Cross-Topic Links

- **To informed search:** both minimax and A* rely on evaluation functions under constraints.
- **To optimization:** local vs global optima intuition helps reason about strategic landscapes.
- **To ML/RL:** self-play and policy/value estimation connect adversarial search to learning systems.

## 10) RL + Game Search Connection (Deeper Link)

- Classical minimax assumes known rules and explicit search.
- RL can learn value/policy approximations from self-play when full tree search is infeasible.
- Modern systems often combine both:
  - Search for lookahead at decision time.
  - Learned value/policy networks for guidance and evaluation.
- Exam framing: search gives exact short-horizon reasoning; learning gives scalable generalization.

## 11) Rapid Answer Templates (Written Questions)

### "Find Nash equilibrium"

1. State players and actions.
2. Mark best responses for each player.
3. Report intersections (pure NE) or solve indifference equations (mixed NE).
4. Add one-sentence interpretation of strategic stability.

### "Explain alpha-beta benefit"

1. Define alpha and beta bounds.
2. State prune conditions at MAX/MIN nodes.
3. Explain same minimax outcome, fewer node evaluations.
4. Mention move ordering as key determinant of speedup.

### "When use mixed strategy?"

1. No stable pure strategy profile (or predictable pure play gets exploited).
2. Randomization keeps opponent indifferent across responses.
3. Compute equilibrium probabilities via expected utility equality.
4. Note mixed equilibrium gives expected, not deterministic, outcomes.

