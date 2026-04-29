# Reinforcement Learning and Language Models - Conceptual Final Exam Guide

This version is designed for understanding ideas, tradeoffs, and intuition first, with very little formula emphasis.

## 1) Big Picture

Language models and reinforcement learning both deal with decision-making under uncertainty:

- In language modeling, the system chooses likely next words.
- In reinforcement learning, the agent chooses likely good actions.
- In both cases, better decisions come from better representations and better handling of uncertainty.

## 2) N-grams: What They Are and Why They Matter

An n-gram model predicts the next word using only a short window of previous words.

- **Unigram:** ignores context; fast but shallow.
- **Bigram:** uses one previous word; improves local flow.
- **Trigram:** uses two previous words; often improves grammar.

Core insight: As context length grows, local quality improves, but data sparsity gets worse.

## 3) Smoothing: The Main Intuition

Smoothing is about handling things the model has not seen before.

- Without smoothing, unseen word combinations get impossible probability.
- With smoothing, unseen cases stay possible (small probability), which is more realistic.
- Add-one is easy but can distort common events.
- Add-alpha is usually more balanced and practical.

Exam tip: If asked "why smoothing?", the best answer is "to prevent zero-probability failures on unseen patterns."

## 4) Perplexity and Cross-Entropy (Deeper Intuition)

Think of both as "how wrong or uncertain is the model on real language data?"

### Cross-Entropy: Average Surprise per Token

- **Cross-entropy** measures how surprised a model is by the true next word.
- If the model gives high probability to correct words, cross-entropy is low.
- If it assigns low probability to correct words, cross-entropy is high.

Exam-safe mental model:

- Low cross-entropy = "the model usually expects what actually happens."
- High cross-entropy = "the model is often surprised by the real text."

### Perplexity: Uncertainty in an Interpretable Form

- **Perplexity** is a transformed version of cross-entropy that is easier to interpret.
- It can be read as the model's "effective number of plausible next choices."
- Lower perplexity means sharper, more confident next-token predictions.

Quick intuition examples:

- Perplexity near 1: model is very certain and usually correct.
- Perplexity around 10: model behaves like it is choosing among about 10 likely options.
- Very high perplexity: predictions are diffuse or frequently wrong.

### How They Relate

- They encode the same core information.
- If cross-entropy goes down, perplexity also goes down.
- Perplexity is often preferred for communication; cross-entropy is often preferred in optimization and theory.

Exam phrasing: "Perplexity is an exponential view of cross-entropy, so both rank models similarly on the same dataset."

### Why We Still Need Caution

Lower cross-entropy/perplexity is usually good, but not a complete quality guarantee:

- A model can improve perplexity yet still produce bland or generic outputs.
- Better next-token prediction may not fully capture reasoning quality, factuality, or safety.
- Metric gains on one domain may not transfer to very different domains.

So these are **intrinsic** metrics: excellent for model comparison and iteration, but incomplete for real-world usefulness.

### Common Exam Traps

- Saying perplexity "proves" better translation/chat quality.
- Comparing perplexity across tokenizations or datasets as if they were directly equivalent.
- Ignoring that rare tokens and domain shift can inflate both metrics.

### What to Say in a Short Answer

"Cross-entropy measures average surprise on true tokens. Perplexity is the same signal in a more interpretable scale of prediction uncertainty. Lower is generally better for language modeling, but these intrinsic metrics should be paired with task-level evaluation before claiming real-world superiority."

## 5) Intrinsic vs Extrinsic Evaluation

- **Intrinsic evaluation:** tests the model directly (fast, cheap, good for iteration).
- **Extrinsic evaluation:** tests impact on a real task like translation or speech recognition (more realistic, slower, expensive).

Exam framing: intrinsic tells you "model quality in isolation"; extrinsic tells you "real-world usefulness."

## 6) Representations: One-Hot vs Embeddings

- **One-hot vectors** treat words as unrelated IDs.
- **Dense embeddings** place semantically related words closer together.

Why embeddings are better conceptually:

- They encode similarity and patterns.
- They reduce dimensionality.
- They transfer better to downstream tasks.

## 7) Word2Vec (Skip-gram) Intuition

Skip-gram learns a word representation by asking:
"Given this center word, what nearby words should appear?"

As training proceeds:

- Words with similar contexts become close in vector space.
- Frequent words can dominate, so practical training tricks (like negative sampling) make learning more efficient.

## 8) Static Embeddings: Strength and Limitation

- Strength: compact and semantically meaningful representations.
- Limitation: the same word gets the same vector in every sentence.

So static embeddings capture general meaning but not context-specific meaning.

## 9) Common Exam Mistakes

- Claiming perplexity alone proves end-task superiority.
- Forgetting that larger n-grams increase sparsity.
- Assuming co-occurrence always equals deep semantics.
- Treating static embeddings as fully context-aware.

## 10) RL Connections to Mention in Answers

Even if the question is mostly about language models, these links are often rewarded:

- **Uncertainty handling:** both LM prediction and RL action selection manage uncertainty.
- **Exploration vs exploitation:** RL's action tradeoff parallels choosing among uncertain next-token possibilities.
- **Representation learning:** embeddings in NLP and state features in RL both improve decision quality.

## 11) Quick Concept Checks

1. Why do n-gram models improve local fluency but struggle with long-range meaning?
2. Why is smoothing more important as model context size increases?
3. Why can a model with good perplexity still fail on a downstream task?
4. Why are embeddings generally better than one-hot vectors for semantic tasks?

## 12) Reinforcement Learning Core Setup (Exam Essential)

In RL, an agent learns by acting in an environment and receiving rewards:

- **State (s):** what the agent currently observes.
- **Action (a):** a choice the agent can make now.
- **Reward (r):** immediate feedback after action.
- **Policy (pi):** mapping from state to action (or action probabilities).

Core exam idea: RL is **sequential decision-making**. The quality of an action depends on long-term consequences, not just immediate reward.

## 13) Exploration vs Exploitation

- **Exploration:** try uncertain actions to learn better strategies.
- **Exploitation:** choose currently best-known action for immediate gain.

Why this matters:

- Too much exploitation can trap the agent in a suboptimal strategy.
- Too much exploration wastes time on poor actions.
- Good learning usually starts with more exploration and shifts toward exploitation.

## 14) MDP, Return, and Discounting

Most RL tasks are framed as a **Markov Decision Process (MDP)** with:

- states, actions, transition dynamics, and rewards.
- the **Markov property**: next state depends on current state/action, not full history.

The agent maximizes **expected cumulative discounted reward**:

- Discount factor gamma controls horizon:
  - high gamma -> more future-oriented behavior
  - low gamma -> more immediate-reward behavior
- Discounting is motivated by uncertainty and delayed value.

Exam phrasing: "Discounting balances short-term reward with long-term planning."

## 15) Value Functions and Bellman Intuition

- **V^pi(s):** how good it is to be in state s under policy pi.
- **Q^pi(s, a):** how good it is to take action a in state s under policy pi.

Practical intuition:

- V tells overall goodness of a state.
- Q supports action selection directly.
- Bellman recursion says value = immediate reward + discounted next value.

Optimality idea:

- Optimal policy pi* picks actions with highest expected long-term value.
- Bellman optimality formalizes this via a max over actions.

## 16) Model-Based vs Model-Free RL

### Model-Based Dynamic Programming

When transition/reward model is known:

- **Value Iteration:** repeatedly update state values with Bellman max backup, then extract policy.
- **Policy Iteration:** alternate policy evaluation and policy improvement.

Conceptual tradeoff:

- Value iteration is often simpler per loop.
- Policy iteration often converges in fewer outer loops and keeps explicit intermediate policies.

### Model-Free Learning (Unknown Model)

When transition probabilities/rewards are unknown, learn from interaction:

- **Q-learning** learns Q(s,a) directly from sampled experience.
- Common action rule: **epsilon-greedy** (mostly exploit, sometimes explore).
- Update intuition: move old Q estimate toward observed reward + discounted best future Q.

Key exam distinction:

- Value/policy iteration need model knowledge.
- Q-learning does not need model equations, only experience tuples (s, a, r, s').

## 17) High-Value RL Mistakes to Avoid

- Confusing **state value V** with **action value Q**.
- Saying exploration is only useful early (it is often needed throughout, though reduced).
- Ignoring delayed rewards and treating RL like one-step classification.
- Claiming model-free means "no environment interaction" (it is the opposite).

## 18) RL + Language Model Link (Modern Context)

A useful bridge for conceptual exam answers:

- Language generation is a sequence of token actions.
- Reward can encode human preference or task quality.
- RL-style fine-tuning can shift models from "likely text" toward "useful/aligned behavior."

This is the same core RL principle: optimize long-term objective through feedback-driven policy improvement.
