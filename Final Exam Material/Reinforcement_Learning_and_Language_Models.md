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

## 4) Perplexity and Cross-Entropy (Concept Only)

Think of these as confidence-quality signals:

- **Cross-entropy:** average surprise of the model on real text.
- **Perplexity:** how uncertain the model is when picking next words.

Lower values usually mean the model predicts text better, but lower perplexity does not always guarantee better downstream task performance.

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

