# Reinforcement Learning and Language Models - Final Exam Study Guide

This guide focuses on the NLP-before-LLMs content and the language-model foundations that appear in your exam themes.

## 1) Topic Snapshot

| Topic | Core Idea | Exam Focus |
|---|---|---|
| N-gram Language Models | Predict next word from limited context | Bigram/trigram formulas |
| Smoothing | Avoid zero probabilities | Add-one vs add-alpha |
| Perplexity | Intrinsic LM quality metric | Interpret lower-is-better |
| Embeddings | Dense semantic vectors | One-hot vs learned vectors |
| Word2Vec / Skip-gram | Predict context from center word | Objective intuition |

## 2) Essential Formulas

| Formula | Meaning |
|---|---|
| `P(w1...wn) = product_i P(wi | w1...w(i-1))` | Chain rule for LM |
| `P(wi | history) approx P(wi | last k words)` | Markov assumption |
| `P_add-alpha = (count(ngram)+alpha)/(count(prefix)+alpha|V|)` | Smoothed probability |
| `CE = -(1/n) sum_i log P(wi | context)` | Cross-entropy on sequence |
| `Perplexity = 2^CE` | Effective branching uncertainty |

## 3) N-gram Model Comparison

| Model | Conditions On | Pros | Limits |
|---|---|---|---|
| Unigram | No context | Very simple baseline | No syntax/coherence |
| Bigram | Previous 1 word | Better local fluency | Weak long-range context |
| Trigram | Previous 2 words | Better grammar | Data sparsity increases |

## 4) Smoothing Cheat Table

| Method | Benefit | Risk |
|---|---|---|
| No smoothing | Preserves observed counts | Unseen n-grams get zero probability |
| Add-one | Eliminates zeros easily | Over-smooths frequent events |
| Add-alpha (`0 < alpha < 1`) | Better balance in practice | Needs tuning |

## 5) Evaluation: Intrinsic vs Extrinsic

| Evaluation Type | Measures | Strength | Weakness |
|---|---|---|---|
| Intrinsic | CE / perplexity on held-out text | Fast comparison | May not predict downstream gains |
| Extrinsic | End-task quality (ASR/MT/etc.) | Most realistic | Expensive and slow |

## 6) Embeddings: Quick Concepts

| Representation | Dimension | Semantic Similarity? | Notes |
|---|---|---|---|
| One-hot | `|V|` (very high) | No | Sparse, orthogonal |
| Dense embeddings | 50-300 typical | Yes | Learned from context statistics |

## 7) Word2Vec (Skip-gram) in One Minute

- **Input:** center word.
- **Output target:** nearby context words.
- **Objective:** maximize probability of true context words.
- **Result:** words with similar contexts get nearby vectors.
- **Optimization tricks:** negative sampling, subsampling frequent words.

## 8) Common Mistakes

- Saying lower perplexity always guarantees better downstream tasks.
- Forgetting that sparsity worsens as `n` increases.
- Confusing co-occurrence with true semantics in all cases.
- Treating static embeddings as context-aware (they are not).

## 9) Fast Recall Questions

1. Why does smoothing become more important for larger n-grams?
2. Why can unigram output look plausible but incoherent?
3. What does perplexity represent intuitively?
4. Why are one-hot vectors poor for semantic similarity?

## 10) Link to RL Theme

While this folder has no dedicated RL slide deck, exam connections usually appear via:

- **Policy as next-action prediction** parallels sequence prediction.
- **Exploration/exploitation** parallels uncertainty and probabilistic modeling.
- **Value of representation learning** appears in both NLP embeddings and RL state representations.

