# CSC-343 Mock Final Exam Questions (Sample-Style)

These questions follow the same style as the sample: conceptual evaluation, argument critique, and required components.

## Section A — Logic and Search

### Mock A1
A student claims: "If a heuristic is admissible, then graph-search A* never needs to reopen a node, so consistency is optional and mostly theoretical." Evaluate this claim.

Your answer must address:
- The difference between admissibility and consistency, and why consistency is stronger;
- A concrete graph-search scenario where an admissible but inconsistent heuristic causes node reopenings or inefficient behavior; and
- Whether A* optimality can still hold, and under what implementation conditions.

### Mock A2
A team uses beam search for route planning because it is "basically A* but faster." They report excellent runtime and conclude beam search is the best default for all large search problems. Evaluate this conclusion.

Your answer must address:
- How beam width affects completeness and optimality;
- A specific case where beam search discards the optimal path early; and
- A principled criterion for choosing between A*, IDA*, and beam search under memory constraints.

### Mock A3
An engineer argues that "UCS is always better than BFS because it handles general costs, so BFS is obsolete." Evaluate this argument.

Your answer must address:
- Conditions under which BFS and UCS behave identically;
- Why BFS may be preferred in practice despite UCS being more general; and
- A problem structure where UCS is strictly necessary for correctness.

## Section B — Reinforcement Learning and Language Models

### Mock B1
In a multi-armed bandit system, a manager sets `epsilon = 0` after only 200 interactions because one action currently has the highest average reward. They argue this maximizes business value immediately, so exploration is no longer needed. Evaluate this decision.

Your answer must address:
- The exploration-exploitation tradeoff and the risk of premature exploitation;
- How regret can grow under under-exploration; and
- One strategy (e.g., decaying epsilon, UCB, Thompson sampling) that could improve long-term performance.

### Mock B2
A language model with slightly worse perplexity is rejected, even though it performs better on a downstream summarization task. A reviewer says this is impossible because "lower perplexity always means better model quality." Evaluate this claim.

Your answer must address:
- What perplexity does and does not measure;
- Why intrinsic metrics can diverge from extrinsic task outcomes; and
- A concrete modeling choice that can improve task performance without improving perplexity much.

### Mock B3
A practitioner switches from add-alpha smoothing to no smoothing in a trigram model because "seen trigrams are what matter in realistic text." Evaluate this reasoning.

Your answer must address:
- Why sparsity worsens with larger n-grams;
- What zero probabilities imply for sequence likelihood and evaluation; and
- When simple smoothing may still outperform a no-smoothing model in practice.

## Section C — Machine Learning

### Mock C1
A classifier for medical screening has 97% accuracy, and the team declares it deployment-ready. The positive class prevalence is 2%. Evaluate this conclusion.

Your answer must address:
- Why accuracy can be misleading under class imbalance;
- Which metrics should be prioritized and why (precision, recall, PR-AUC, F1); and
- One thresholding or training intervention to better match clinical risk.

### Mock C2
A student applies SMOTE to the full dataset before splitting into train and test, obtains strong results, and claims SMOTE is clearly superior. Evaluate this claim.

Your answer must address:
- Why this pipeline creates leakage;
- How the evaluation should be redesigned; and
- A realistic tradeoff between recall gains and precision loss after proper SMOTE use.

### Mock C3
A model's SHAP plots look intuitive, so the team treats the explanations as proof that the model is valid and fair. Evaluate this inference.

Your answer must address:
- What SHAP explanations capture (and what they do not);
- Why explanation quality does not guarantee predictive reliability or fairness; and
- One additional validation step needed before deployment.

## Section D — Integrative / "Other Topics" Style

### Mock D1
In a two-player zero-sum game, a developer proposes replacing minimax with a one-step greedy policy because "it wins quickly against weak opponents." Evaluate this proposal.

Your answer must address:
- Why local tactical gain can differ from minimax-optimal play;
- A game-tree pattern where shallow greed loses to deeper strategy; and
- When alpha-beta pruning improves tractability without changing decision quality.

### Mock D2
A normal-form game has no dominant strategies. A classmate concludes there can be no Nash equilibrium and that rational play is undefined. Evaluate this statement.

Your answer must address:
- Why dominant strategies are not required for Nash equilibrium;
- How best responses are used to locate equilibria; and
- Why mixed strategies may be necessary in some games.

### Mock D3
An AI team says adversarial search and ML are unrelated because one is "symbolic" and the other is "statistical." Evaluate this framing.

Your answer must address:
- One shared idea between minimax evaluation and learned value estimation;
- One important difference in assumptions or guarantees; and
- A practical system (e.g., self-play) where both paradigms interact.

## Optional Short-Answer Drill (2–4 sentences each)

1. Explain a case where admissibility is not enough to make A* graph search efficient.
2. Give one real-world example where recall should be prioritized over precision.
3. Why can lower cross-entropy fail to improve a downstream generation task?
4. What is one failure mode shared by hill climbing and gradient-based optimization?
5. Why does better move ordering matter for alpha-beta pruning?

