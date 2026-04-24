# Search Algorithms — Time & Space Complexity Reference

**Notation:** `b` = branching factor | `d` = depth of shallowest goal | `m` = maximum depth | `C*` = optimal solution cost | `ε` = minimum edge cost

---

## Tree Search vs Graph Search

Tree Search and Graph Search are two **implementation strategies** for the same algorithms (BFS, DFS, UCS, A*, etc.). They differ in whether states can be revisited.

| Strategy | Frontier | Explored Set | State Visits |
|----------|----------|--------------|--------------|
| **Tree Search** | Nodes to expand | None | Same state can be added multiple times via different paths |
| **Graph Search** | Nodes to expand | States already expanded | Each state expanded at most once |

### Key Details

- **Explored set**: A node is added when it is **expanded** (removed from frontier), not when first generated.
- **Tree Search**: Lower memory (no explored set), but redundant work—may expand same state repeatedly.
- **Graph Search**: Avoids redundant work; higher memory (stores explored set). Time/space complexities in the tables below typically assume graph search.
- **When to use**: Tree Search when memory is critical; Graph Search when you want to avoid revisiting states and have sufficient memory.

---

## Uninformed Search

| Algorithm | Selection | Time | Space | Complete | Optimal |
|-----------|-----------|------|-------|----------|---------|
| **Breadth-First (BFS)** | FIFO (queue) | O(b^d) | O(b^d) | Yes (finite spaces) | Yes (uniform cost) |
| **Depth-First (DFS)** | LIFO (stack) | O(b^m) | O(bm) | No (infinite spaces) | No |
| **Depth-Limited (DLS)** | LIFO, limit L | O(b^L) | O(bL) | Yes if d ≤ L | No |
| **Iterative Deepening (IDS)** | DLS, L=0,1,2,… | O(b^d) | O(bd) | Yes | Yes (uniform cost) |
| **Uniform-Cost (UCS)** | Min g(n) | O(b^(1 + ⌊C*/ε⌋)) | O(b^(1 + ⌊C*/ε⌋)) | Yes | Yes |

### Details

- **BFS**: Explores level by level. Stores full frontier. Space dominates for wide, shallow trees.
- **DFS**: Goes deep first. Stores current path + unexplored siblings → O(bm). Not complete in infinite state spaces.
- **UCS**: Expands by path cost g(n), not depth. ε = smallest edge cost.
- **IDS**: Repeated depth-limited search; re-expands shallow nodes. Same time as BFS, much lower space.

### Node Count Formulas

- Nodes explored to depth d: **(b^(d+1) − 1) / (b − 1)**
- IDS total (up to depth d): ~**b^d** dominant term; shallow re-expansion adds constant factor

---

## Informed Search

| Algorithm | Evaluation | Time | Space | Complete | Optimal |
|-----------|------------|------|-------|----------|---------|
| **A*** | f(n) = g(n) + h(n) | O(b^d) worst case | O(b^d) | Yes | Yes (if h admissible) |
| **Greedy Best-First** | h(n) only | O(b^m) worst case | O(b^m) | No | No |
| **Beam Search** | Top k by f or h per level | Depends on k | O(k × depth) | No | No |
| **Weighted A*** | f = g + w·h | Same as A* | Same as A* | Yes | Cost ≤ w·C* |

### Notes

- **A***: With admissible h, expands only nodes with f(n) ≤ C*. Typically expands fewer nodes than UCS.
- **Greedy Best-First**: Uses h(n) only; often fast but can miss optimal path.
- **Beam Search**: Prunes to k nodes per level; neither complete nor optimal.
- **Weighted A***: w > 1 speeds search but solution cost can be up to w × optimal.

---

## Local Search / Optimization

| Algorithm | Data Stored | Time per Iteration | Space | Complete | Optimal |
|-----------|-------------|--------------------|-------|----------|---------|
| **Hill Climbing** | Current state + neighbors | O(neighbors) | O(state) | No | No |
| **Simulated Annealing** | Current state + neighbors | O(neighbors) | O(state) | Yes (with appropriate schedule) | No (probabilistic) |
| **Genetic Algorithm** | Population of N | O(N × (crossover + mutation)) | O(N × state) | No | No |
| **Random Restart Hill Climbing** | Same as Hill Climbing | R × HC time | O(state) | Prob. → 1 with enough restarts | Prob. → 1 |

### Notes

- **Hill Climbing**: Can get stuck in local optima. No exploration of worse states.
- **Simulated Annealing**: P(accept worse) = e^(-Δ/T). High T → exploration; low T → exploitation.
- **Genetic Algorithm**: Population size N fixed. Time ~ generations × N × fitness cost.
- **A* vs HC/GA**: A* needs O(b^d) memory; hill climbing and GA use O(1) or O(N) state storage.

---

## Summary

| Metric | BFS | DFS | UCS | IDS | A* | Hill Climbing |
|--------|-----|-----|-----|-----|-----|---------------|
| **Time** | O(b^d) | O(b^m) | O(b^(1+⌊C*/ε⌋)) | O(b^d) | O(b^d) | O(iter × neighbors) |
| **Space** | O(b^d) | O(bm) | O(b^(1+⌊C*/ε⌋)) | O(bd) | O(b^d) | O(state) |
