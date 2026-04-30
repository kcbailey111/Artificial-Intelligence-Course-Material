# Section B — Reinforcement Learning and Language Models

Topics below match common final prompts (including **cross-entropy / perplexity** and **train–test interpretation**). Lighter overview: `Reinforcement_Learning_and_Language_Models.md`. Exploration: `Exploration_vs_Exploitation.md`.

---

## Cross-entropy and perplexity

### Autoregressive language modeling

A language model assigns probabilities to the next token given context:

\[
P(w_t \mid w_{1}, \ldots, w_{t-1})
\]

Training maximizes likelihood of observed next tokens, i.e. minimizes average **negative log-likelihood** / cross-entropy on the training distribution.

### Cross-entropy: average surprise on true tokens

At each step the model outputs a distribution over the vocabulary; the **true** next token is one outcome.

- High predicted probability for what actually happens → **low** cross-entropy (not surprised).  
- Low predicted probability for what happens → **high** cross-entropy (surprised).

Per-step loss is commonly \(\ell_t = -\log \hat{p}_t(w_t)\); **average** cross-entropy is the average of \(\ell_t\). Use one **log base** consistently; perplexity formulas must match (natural log: \(\text{PP} = e^{\text{CE}}\); bits: \(\text{PP} = 2^{\text{CE}}\)).

Minimizing average CE on training data is (up to constants) **maximum likelihood** for the next-token model.

### Perplexity

\(\text{PP} = \exp(\text{CE})\) when CE uses **natural log**.

**Interpretation:** roughly the **effective number of equally likely next choices** the model acts as if it has.

- PP near 1: very peaked / confident on that data.  
- PP ~20: uncertainty like ~20-way uniform choice.  
- Very large PP: diffuse or often wrong on held-out text.

CE is best for **optimization and theory**; PP is often easier to **communicate**.

### Same ranking

On the **same** corpus and tokenization, lower CE ⇔ lower PP (monotonic). Neither ranks models on **different** tokenizations or domains in a directly comparable way.

### What CE/PP do and do not certify

Better test CE usually means better **statistical fit** to next-token prediction on that text. It does **not** alone guarantee factuality, reasoning, safety, alignment, or success on **downstream** tasks (translation, QA, etc.)—pair **intrinsic** metrics with **extrinsic** evaluation.

### Short template

**Cross-entropy** is average negative log probability of the true next tokens (surprise under the model). **Perplexity** is an exponential rescaling—same ranking on a fixed setup, easier human interpretation. Both are incomplete proxies for real-world usefulness.

---

## Train vs test performance, generalization, and “overfitting”

### Generalization

A model **generalizes** when it does well on **new** data from a similar process to training. For LMs, low held-out **CE / perplexity** is a common proxy—not the same as deployment success.

### Overfitting

**Overfitting:** the model fits training **idiosyncrasies** (noise, spurious patterns) and suffers on new data. Typical pattern: training loss improves, validation/test loss **worsens** or stalls. It is a **degree** and **trend**, not a single noisy step.

### Why “train CE down, test CE up ⇒ stop” can be too hasty

- **Small test sets:** tiny CE moves can be **sampling noise**.  
- **Train/test mismatch:** topic, era, style differ.  
- **Optimization noise:** batch-level training vs finite holdout.  
- **Objective mismatch:** a slightly worse test CE checkpoint can be **better** on summarization faithfulness, code execution, instruction following, etc.—**perplexity ≠ task success**. Name a **concrete downstream** task when the exam asks.

### What strengthens an overfitting claim

Growing train–test gap over **many** checkpoints, worse on **multiple** held-outs, worse **task** metrics, calibration issues—not a one-time blip alone.

### Underfitting (contrast)

High **train and test** error: model too weak or over-regularized. Fix: capacity, features, less excessive regularization, or more training if under-trained.

### Early stopping

Stop when validation metric stops improving—regularizes iterative training. **Best** checkpoint by CE may not be best by **business** metric.

### Paragraph template

A train/test CE gap is **consistent with** overfitting but not always sufficient: finite-test noise, split mismatch, and metric mismatch can move test CE slightly without making the model worse for every goal. Judge **trends**, extra validation, and **task-level** metrics; lower perplexity does not automatically mean better reasoning or factuality.

---

## Policy vs value in reinforcement learning

### Interaction loop

Each step: observe \(s_t\), choose \(a_t\), get reward \(r_t\) and \(s_{t+1}\). Objective: maximize **expected return** (often discounted).

### Policy

**Policy** \(\pi(a \mid s)\): how the agent **chooses** actions (deterministic or stochastic). This is **behavior**.

### Value functions

Under policy \(\pi\):

- **\(V^\pi(s)\):** expected return from \(s\) if you follow \(\pi\) afterward.  
- **\(Q^\pi(s,a)\):** expected return if you take \(a\) in \(s\), then follow \(\pi\).

**Optimal** \(\pi^*\), \(V^*\), \(Q^*\): best achievable (under standard MDP assumptions).

| Object | Question it answers |
|--------|---------------------|
| **Policy** | What action to take? |
| **Value** | How good is this state or action for future reward? |

Many algorithms **learn values to improve the policy**, or **optimize the policy** directly.

### Method families (high level)

- **Value-based:** learn \(Q\) or \(V\); act ε-greedy (or similar) w.r.t. estimates.  
- **Policy-based:** parameterize \(\pi_\theta\); policy gradients adjust \(\theta\).  
- **Actor–critic:** policy (actor) + value (critic) for lower variance / guidance.

### Exploration vs exploitation

Policies can explore or exploit; value estimates guide **which** uncertainties matter. See `Exploration_vs_Exploitation.md`.

### Confusions to avoid

- Policy ≠ **reward function** (environment supplies rewards).  
- Q-learning primarily learns **Q**, then implies a greedy policy.  
- In theory \(Q^*\) identifies optimal actions; practice uses **approximation** and exploration.

### Short template

A **policy** is the agent’s action-selection rule; **value functions** estimate long-run return from states or state–action pairs under a policy. Algorithms use values to rank actions and improve behavior, or adjust the policy parameters directly—the distinction is **behavior** vs **long-run forecasts**.

---

## See also

- `Reinforcement_Learning_and_Language_Models.md` — n-grams, smoothing, embeddings, bigger picture.  
- `Machine_Learning.md` — metric vs training loss (analogy for CE vs downstream tasks).
