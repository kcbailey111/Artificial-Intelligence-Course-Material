# Other Topics - Final Exam Study Guide

This section captures material that is adjacent to the core categories, especially games and decision-making frameworks.

## 1) Topic Map

| Topic | Core Idea | Exam Angle |
|---|---|---|
| Game Theory Basics | Strategic interaction among rational agents | Identify equilibrium outcomes |
| Zero-sum Games | One player's gain is another's loss | Minimax reasoning |
| Minimax Search | Optimal play under adversarial setting | Build game tree decisions |
| Alpha-Beta Pruning | Prune irrelevant minimax branches | Analyze pruning effects |
| Mixed Strategies | Randomized action selection | Compute expected utility |

## 2) Core Terms

| Term | Meaning |
|---|---|
| Strategy | Complete action plan in game |
| Payoff | Utility received from outcome |
| Nash Equilibrium | No player benefits by unilateral deviation |
| Dominant Strategy | Best action regardless of opponent action |
| Saddle Point | Stable pure-strategy solution in zero-sum matrix |

## 3) Minimax and Alpha-Beta Quick Compare

| Method | Guarantee | Time (worst) | Main Benefit |
|---|---|---|---|
| Minimax | Optimal adversarial play | `O(b^d)` | Correct game-theoretic choice |
| Alpha-Beta | Same minimax result | Up to `O(b^(d/2))` with ideal ordering | Major speedup |

## 4) Minimax Procedure (Exam Steps)

1. Expand game tree to depth limit or terminal states.
2. Evaluate terminal/leaf utilities.
3. Back up values: max at MAX nodes, min at MIN nodes.
4. Choose root action with best backed-up value.

## 5) Alpha-Beta Intuition

| Bound | Meaning | Prune Condition |
|---|---|---|
| `alpha` | Best value MAX can force so far | At MIN node, if value `<= alpha`, prune |
| `beta` | Best value MIN can force so far | At MAX node, if value `>= beta`, prune |

Node ordering quality strongly affects pruning effectiveness.

## 6) Normal-Form Game Matrix Checklist

- Identify each player's action set.
- Fill payoff pairs carefully `(u1, u2)`.
- Remove strictly dominated strategies if present.
- Locate mutual best responses (candidate Nash equilibria).
- Distinguish pure vs mixed equilibria.

## 7) Common Mistakes

- Confusing dominant strategy with equilibrium.
- Forgetting that multiple Nash equilibria can exist.
- Claiming alpha-beta changes the final move choice (it should not).
- Mixing utility scales between players in zero-sum setup.

## 8) Rapid Practice Prompts

1. Why does alpha-beta never change minimax optimality?
2. Give an example of a game with no dominant strategy but with Nash equilibrium.
3. How does better move ordering change search cost?
4. When do mixed strategies become necessary?

## 9) Cross-Topic Links

- **To informed search:** both minimax and A* rely on evaluation functions under constraints.
- **To optimization:** local vs global optima intuition helps reason about strategic landscapes.
- **To ML/RL:** self-play and policy/value estimation connect adversarial search to learning systems.

