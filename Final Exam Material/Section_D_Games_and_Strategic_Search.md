# Section D — Games & strategic search

> **Note:** The official CSC-343 outline lists **Section D as redacted** on the public PDF. This file collects **adversarial search** material that often appears in AI courses alongside **Section A (search)** or as a fourth unit—see your syllabus. Broader game-theory terms: `Other_Topics.md`.

---

## Minimax search

### When it applies

**Minimax** targets **two-player, zero-sum, perfect-information** games: alternating moves, both see full state, one player’s gain is the other’s loss (up to sign).

**Contrast:** single-agent shortest-path search is not minimax unless you explicitly model an **adversary**.

### MAX and MIN nodes

- **MAX** nodes: choose move to **maximize** backed-up value.  
- **MIN** nodes: choose move to **minimize** backed-up value (from MAX’s score convention).

Leaves (or depth-limited evaluations) carry **utilities** for MAX.

### Backup rule

- **MAX** node value = **max** of children.  
- **MIN** node value = **min** of children.

Root move leading to best value for MAX is the minimax choice if both play **optimally**.

**Exam phrasing:** each side assumes the opponent plays **best for themselves** (worst for you in zero-sum games).

### What “optimal” means here

**Optimal under optimal play:** in finite perfect-information zero-sum games, deviating from minimax lets a rational opponent exploit you. Against a **weak** human, minimax is a conservative baseline, not necessarily the highest-scoring practical strategy.

### Complexity

Time often **\(O(b^d)\)** for branching `b` and depth `d` (plies)—motivates **alpha–beta**, **depth limits**, **evaluation functions**.

### Depth limits and evaluation

When the tree is too deep, cut off and use a **static evaluation** at frontier nodes. **Horizon effect:** danger just beyond the cutoff is invisible → blunders.

### Chance (optional)

**Expectiminimax:** **chance** nodes take **expected value** over random outcomes (dice). Minimax is the no-chance special case.

### Short template

Minimax backs up **max** at MAX and **min** at MIN, encoding optimal adversarial play in zero-sum perfect-information games. It is usually exponential in depth, so real systems use limits, evaluation functions, and **alpha–beta** pruning.

---

## Alpha–beta pruning

### Goal

Skip branches that **cannot change** the minimax value at an ancestor—**same result** as minimax (under standard tree assumptions), **fewer expansions**.

### Alpha and beta

During depth-first minimax with pruning:

- **α:** best value MAX can **guarantee** so far on this path (MAX’s “floor”).  
- **β:** bound representing what MIN can still **allow** (MIN’s side of the negotiation).

**Memory aid:** if MIN finds a line **≤ α**, MAX already had something better elsewhere—**prune** MIN’s remaining children. If MAX finds a line **≥ β**, MIN will block it—**prune** MAX’s remaining children. (Exact α/β cutoff wording follows your textbook.)

### Guarantees

With **ideal move ordering**, many fewer nodes are visited (often taught as roughly **\(O(b^{d/2})\)** best case vs **\(O(b^d)\)** naive—details depend on assumptions). **Root move** matches minimax for same depth, same leaf evaluation, deterministic tree model.

### Move ordering

Pruning helps when **refutations** appear early—hence **killer moves**, history heuristic, etc. in game programs.

### Caveats

**Transpositions** (same state via multiple paths) may need **transposition tables** / graph-aware treatment so pruning stays sound. **Depth-limited** search still suffers **evaluation error** and horizon issues.

### Short template

Alpha–beta maintains **α** and **β** along the path and **cuts** subtrees that cannot affect the backed-up minimax value. It is **algorithmically equivalent** to minimax on the same model but faster; quality still depends on **move ordering** and, under depth limits, on **evaluation function** accuracy.

---

## See also

- `Other_Topics.md` — Nash equilibrium, dominant strategies, zero-sum matrices, procedure steps.  
- `Section_A_Logic_and_Search.md` — single-agent search (BFS, UCS, A*, IDS, etc.).
