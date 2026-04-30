# Section A — Logic and Search

In-depth review for **CSC-343-style** questions: tie together **definitions**, **completeness / optimality**, **time / space**, and **problem structure** (costs, depth, heuristics). For logic (FOL, resolution, CNF), see `Logic_and_Search.md`.

---

## Search: shared vocabulary

### State, actions, transitions

- A **state** is a snapshot of the world relevant to the problem.
- An **action** moves from one state to a **successor**.
- A **solution** is usually an **action sequence** (a path) from the start state to a **goal state**.

### Path cost vs depth

- **Depth** counts steps (or levels) along a path.
- **Path cost** sums **step costs** along the path. If every action costs `1`, depth and cost align. If costs differ, **cheap deep paths** can beat **shallow expensive paths**.

### Tree search vs graph search

Implementations differ in whether you remember **states you already expanded**:

| Style | Explored set | Effect |
|------|--------------|--------|
| **Tree search** | None | The same state can be reached again via different paths; more redundant work, sometimes less bookkeeping. |
| **Graph search** | Yes | Each state is expanded at most once (under standard conventions); less redundant work, more memory. |

**Exam point:** The *algorithm name* (BFS, UCS, A*) refers to **what you expand next**. Tree vs graph refers to **duplicate handling**.

### Completeness vs optimality (search sense)

These words also appear in **logic** (proof systems). In **search**, they mean:

| Term | Meaning |
|------|---------|
| **Complete** | If *any* solution exists (finite branching, no pathological zero-cost loops), the algorithm is guaranteed to **eventually find a solution**. |
| **Optimal** | When the algorithm returns a solution, that solution has **minimum path cost** among all solutions (under the stated assumptions). |

**Common exam mistake:** mixing “complete” with “explores everything.” BFS can be complete without visiting the entire state space—it stops when it dequeues a goal.

---

## Uninformed search (no heuristic)

Notation: `b` = branching factor; `d` = depth of shallowest goal; `m` = max depth; `C*` = optimal solution cost; `ε` = minimum positive edge cost.

### Breadth-first search (BFS)

**Frontier:** FIFO—expand the **oldest** (shallowest-not-yet-expanded) node.

| Property | Typical statement |
|----------|-------------------|
| Complete? | **Yes** (finite `b`, finite goal depth) |
| Optimal? | **Yes** if **all step costs are equal** (positive). With unequal costs, BFS by **depth** is **not** guaranteed minimum-**cost**. |
| Time / space | `O(b^d)` |

**Use when:** fewest steps (unit costs), shallow goals, frontier memory acceptable. **Avoid when:** non-uniform costs (prefer UCS) or frontier too large.

### Depth-first search (DFS)

**Frontier:** LIFO—expand the **newest** child first.

| Property | Typical statement |
|----------|-------------------|
| Complete? | **No** in general (infinite depth). Graph search on finite graphs changes behavior. |
| Optimal? | **No** in general. |
| Time | `O(b^m)` worst case |
| Space | `O(bm)`—main advantage |

**Use when:** memory tight, any path helps, or as part of **IDS**. **Avoid when:** optimality or completeness is required in bad infinite branches.

### Depth-limited search (DLS)

DFS with depth cap `L`. Complete only if `d ≤ L`. Building block for **IDS**.

### Iterative deepening (IDS)

Run DLS with `L = 0, 1, 2, …` until a goal is found.

| Property | Typical statement |
|----------|-------------------|
| Complete? | **Yes** (like BFS, under standard assumptions) |
| Optimal? | **Yes** for **unit costs** (shallowest = cheapest) |
| Time | `O(b^d)` (same order as BFS; extra constant factor from re-expansion) |
| Space | `O(bd)` |

**Exam trap:** With **unequal** costs, shallow ≠ cheap. A goal at depth 2 with cost 100 can be returned before a cost-5 goal at depth 4; **UCS** optimizes **total cost**, not depth.

### Uniform-cost search (UCS)

**Frontier:** always smallest **`g(n)`** (path cost from start).

| Property | Typical statement |
|----------|-------------------|
| Complete? | Yes if step costs **≥ ε > 0** |
| Optimal? | **Yes** (minimum path cost) |
| Time / space | `O(b^(1 + ⌊C*/ε⌋))` style |

**Relation to BFS:** if every action costs `1`, `g` equals depth ⇒ **same ordering as BFS**. **Use UCS** whenever costs differ and you need cheapest solutions.

---

## Informed search

Heuristic `h(n)` estimates remaining cost to goal (match your course’s convention).

### Greedy best-first

Expand smallest `h(n)` only. Often fast; **not optimal** in general.

### A*

Expand smallest **`f(n) = g(n) + h(n)`**.

- **Admissible** `h` (never overestimates) ⇒ **optimal** (standard tree-search claim; graph search adds consistency / reopening details).
- **`h ≡ 0`** ⇒ **f = g** ⇒ behaves like **UCS**.

A* is **goal-directed UCS** with optimality conditions on `h`, not “magic BFS.”

### Iterative deepening A* (IDA*)

Cutoff on **`f`**, not depth—memory-limited A*.

### Beam search

Keep top-`k` nodes per level. **Not** complete or optimal; approximate under tight budgets.

---

## How algorithms mimic each other

| Situation | What becomes equivalent / similar |
|-----------|-----------------------------------|
| Unit costs | **BFS ≈ UCS** ordering by `g` |
| Low memory + unit-cost optimality | **IDS** mimics BFS’s shallow-first preference via repeated DFS |
| No heuristic | **A* with `h=0`** ≡ **UCS** |
| Good admissible heuristic | **A*** resembles greedy on `h` but **`g`** limits greedy failures |

**Nuance:** “Mimic” is **same expansion preference under special cases**, not identical runtime—IDS pays **re-expansion**; UCS uses a **priority queue**.

---

## How they differ — decision axes

1. **Optimality target:** fewest steps (unit costs: BFS/IDS) vs **minimum cost** (UCS/A*).
2. **Memory:** DFS / IDS / IDA* vs large frontiers (BFS, UCS, A*).
3. **Heuristic:** none (uninformed) vs **admissible/consistent** (A*).
4. **Space shape:** infinite depth hurts DFS; zero-cost cycles hurt UCS unless ruled out.

---

## Exam checklist: choose an algorithm

1. Costs: uniform vs general positive.  
2. Need: any path vs cheapest vs fewest steps.  
3. Completeness required?  
4. Memory budget—`O(b^d)` frontier feasible?  
5. Heuristic: admissible? consistent?  
6. Tree vs graph search; goal test on generate vs dequeue (**match lecture**).

Defend one choice with **one guarantee + one complexity + one structural reason**.

---

## Quick contrasts

1. **BFS vs UCS:** same when costs uniform; UCS generalizes cost-optimality.  
2. **BFS vs IDS:** same unit-cost optimality idea; IDS saves space, pays time.  
3. **IDS vs UCS:** IDS optimizes **depth**; UCS optimizes **cost**—different when costs vary.  
4. **UCS vs A*:** A* adds `h`; `h=0` gives UCS ordering.  
5. **Greedy vs A*:** greedy ignores `g`; A* balances `g` and `h`.

---

## Sample exam tone (IDS vs BFS claim)

Iterative deepening repeats depth-limited searches so shallow nodes are tried first, giving **optimal fewest-step** solutions under **uniform costs** while using memory closer to **DFS** than BFS’s frontier. When **step costs differ**, minimizing **edges** first is not minimizing **total cost**, so depth-first methods can return a shallow expensive goal while a cheaper deep goal exists; then **UCS** or **A*** (admissible `h`) is appropriate. Algorithm choice should follow **problem structure**, especially the **cost model**, not blanket “IDS is always better.”

---

## See also

- `Logic_and_Search.md` — propositional/FOL, resolution, A* admissibility vs consistency, local search.  
- `Ezam 1/Search_Algorithms_Reference.md` — complexity tables.
