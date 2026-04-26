# Comprehensive Final Exam Flashcards

Based on:
- `Logic_and_Search.md`
- `Machine_Learning.md`
- `Other_Topics.md`
- `Reinforcement_Learning_and_Language_Models.md`

Format: **Front: Back**

## Logic and Search

- What is soundness?: If `KB ⊢ phi`, then `KB ⊨ phi` (proved statements are true).
- What is completeness?: If `KB ⊨ phi`, then `KB ⊢ phi` (all true statements are provable).
- What makes a heuristic admissible?: It never overestimates the true cost to goal: `h(n) <= h*(n)`.
- What makes a heuristic consistent?: It satisfies triangle inequality: `h(n) <= c(n,n') + h(n')`.
- What is a dominating heuristic?: An admissible heuristic that is always greater/equal to another admissible heuristic.
- BFS: completeness and optimality?: Complete; optimal with unit/monotone edge costs.
- DFS: main tradeoff?: Very low memory but not generally complete/optimal in infinite-depth spaces.
- UCS: when is it optimal?: With strictly positive step costs (`epsilon > 0`).
- IDS: key benefit?: BFS-like completeness with DFS-like memory usage.
- A*: evaluation function?: `f(n) = g(n) + h(n)`.
- Why is A* often memory-heavy?: It stores many frontier/explored nodes.
- Beam search: main risk?: Can prune away the optimal path.
- Translate "All A are B" to FOL.: `forall x (A(x) => B(x))`.
- Translate "Some A are B" to FOL.: `exists x (A(x) and B(x))`.
- Why is quantifier order important?: `forall x exists y` is not equivalent to `exists y forall x`.
- CNF conversion first step?: Eliminate `=>` and `<=>`.
- CNF proof by resolution ending condition?: Derive empty clause to prove entailment.
- Hill climbing common failure mode?: Gets stuck at local optima/plateaus.
- Simulated annealing advantage?: Can escape local optima by occasionally accepting worse moves.
- Genetic algorithm core operators?: Selection, crossover, mutation.

## Machine Learning

- High train + high validation error indicates what?: High bias (underfitting).
- Low train + high validation error indicates what?: High variance (overfitting).
- Underfitting common fix?: Increase model capacity/features.
- Overfitting common fixes?: Regularization, more data, pruning/simplification.
- Accuracy is most suitable when?: Classes are balanced and error costs are similar.
- Precision is prioritized when?: False positives are costly.
- Recall is prioritized when?: False negatives are costly.
- F1 is useful when?: You need a balance between precision and recall.
- Why use PR-AUC over ROC-AUC?: PR-AUC is more informative for rare positive classes.
- Accuracy formula?: `(TP + TN) / (TP + TN + FP + FN)`.
- Precision formula?: `TP / (TP + FP)`.
- Recall formula?: `TP / (TP + FN)`.
- Specificity formula?: `TN / (TN + FP)`.
- F1 formula?: `2 * (Precision * Recall) / (Precision + Recall)`.
- MCC formula intuition?: Correlation-style balanced metric using all confusion matrix terms.
- What does SMOTE do?: Synthesizes new minority samples by interpolation.
- Key SMOTE pipeline rule?: Split first; apply SMOTE only to training data.
- Why can SMOTE hurt precision?: Better minority coverage can increase false positives.
- What are class weights?: Higher penalty for minority-class errors during training.
- What is threshold moving?: Adjust decision cutoff to trade precision vs recall.
- SHAP global summary shows what?: Overall feature impact across dataset.
- SHAP local waterfall/force plot shows what?: Feature contributions for one prediction.
- SHAP sign meaning?: Positive pushes prediction up; negative pushes down.
- Common imbalance pitfall?: Reporting only accuracy.
- Common leakage pitfall?: Applying SMOTE before train/test split.

## Other Topics (Games and Decision-Making)

- What is a strategy in game theory?: Complete action plan for every possible situation.
- What is payoff?: Utility from an outcome.
- What is Nash equilibrium?: No player can improve by unilateral deviation.
- What is a dominant strategy?: Best action regardless of opponent action.
- What is a saddle point?: Stable pure-strategy equilibrium in a zero-sum matrix.
- Minimax objective?: Choose action assuming opponent also plays optimally.
- Minimax worst-case time?: `O(b^d)`.
- Alpha-beta pruning guarantee?: Same final move/value as minimax.
- Alpha-beta best impact?: Significant pruning; up to about `O(b^(d/2))` with ideal ordering.
- What is `alpha`?: Best value MAX can guarantee so far.
- What is `beta`?: Best value MIN can guarantee so far.
- MIN-node prune condition?: If current value `<= alpha`, prune.
- MAX-node prune condition?: If current value `>= beta`, prune.
- Why does move ordering matter?: Better ordering increases pruning and reduces search cost.
- Common alpha-beta misconception?: It changes optimal move choice (it does not).
- Why remove dominated strategies?: Simplifies matrix and highlights candidate equilibria.

## Reinforcement Learning and Language Models

- Chain rule for language modeling?: `P(w1...wn) = product_i P(wi | w1...w(i-1))`.
- Markov assumption in n-grams?: Approximate with limited history: `P(wi|history) approx P(wi|last k words)`.
- Unigram limitation?: No context, weak coherence.
- Bigram vs trigram?: Trigram captures more local grammar but has more sparsity.
- Why is smoothing needed?: Prevent zero probabilities for unseen n-grams.
- Add-one smoothing downside?: Often over-smooths frequent events.
- Add-alpha smoothing benefit?: Better balance than add-one when tuned.
- Cross-entropy meaning?: Average surprise/negative log likelihood per token.
- Perplexity meaning?: Effective branching uncertainty; lower is better.
- Intrinsic evaluation example?: Cross-entropy/perplexity on held-out text.
- Extrinsic evaluation example?: Downstream task performance (e.g., ASR/MT).
- One-hot vectors weakness?: Sparse, high-dimensional, poor semantic similarity.
- Dense embeddings benefit?: Capture semantic similarity in low-dimensional vectors.
- Skip-gram input and target?: Input center word; predict nearby context words.
- Why negative sampling in Word2Vec?: Efficiently approximates full softmax training.
- Static embedding limitation?: Same vector regardless of sentence context.

## Exploration vs Exploitation (High Priority)

- What is exploration?: Trying uncertain actions to gather information.
- What is exploitation?: Choosing the currently best-known action for immediate reward.
- Core tradeoff?: Short-term reward now vs better decisions later.
- Under-exploration risk?: Premature convergence to a suboptimal policy/action.
- Over-exploration risk?: Excessive short-term losses from too much random behavior.
- What is regret?: Difference between received reward and reward of best possible action.
- What is cumulative regret?: Total regret over many decisions.
- What is epsilon-greedy?: Exploit with probability `1-epsilon`, explore randomly with `epsilon`.
- Why decay epsilon?: Explore early, exploit more as certainty grows.
- What is optimistic initialization?: Start with high value estimates to induce early exploration.
- What is UCB intuition?: Pick high estimated value plus uncertainty bonus.
- What is Thompson sampling intuition?: Sample plausible action values and choose the sampled best.
- Stationary vs non-stationary environments?: Fixed reward distributions vs changing reward distributions.
- How does this connect to search?: Similar tradeoff between broad search (explore) and best-known path focus (exploit).
- How does this connect to LM uncertainty?: Probabilistic uncertainty supports informed exploration decisions.

## Quick Formula Cards

- A* formula: `f(n) = g(n) + h(n)`.
- Admissibility condition: `h(n) <= h*(n)`.
- Consistency condition: `h(n) <= c(n,n') + h(n')`.
- Precision formula: `TP / (TP + FP)`.
- Recall formula: `TP / (TP + FN)`.
- F1 formula: `2PR/(P+R)`.
- Cross-entropy formula: `CE = -(1/n) sum_i log P(wi|context)`.
- Perplexity formula: `Perplexity = 2^CE`.

