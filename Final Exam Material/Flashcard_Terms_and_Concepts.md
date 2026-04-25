# Flashcard Terms and Concepts (Logic + Search)

Use each line as a front/back flashcard pair: **Term -> Definition**.

## A) Logic Foundations

- **Proposition** -> A statement that is either true or false.
- **Knowledge Base (KB)** -> A set of facts and rules an agent uses for reasoning.
- **Inference** -> Deriving new statements from known statements.
- **Entailment (`KB ⊨ phi`)** -> `phi` is true in every model where `KB` is true.
- **Provability (`KB ⊢ phi`)** -> `phi` can be derived using formal inference rules.
- **Soundness** -> If `KB ⊢ phi`, then `KB ⊨ phi` (no false conclusions).
- **Completeness** -> If `KB ⊨ phi`, then `KB ⊢ phi` (can derive all true conclusions).
- **Validity** -> A formula true in every possible model.
- **Satisfiable** -> True in at least one model.
- **Unsatisfiable** -> True in no model.
- **CNF (Conjunctive Normal Form)** -> AND of OR-clauses.
- **Resolution** -> Rule that derives new clauses to prove entailment by contradiction.

## B) First-Order Logic (FOL)

- **Predicate** -> A relation/property (e.g., `Student(x)`).
- **Quantifier (`forall`)** -> "For all" objects in the domain.
- **Quantifier (`exists`)** -> "There exists" at least one object.
- **Unification** -> Finding substitutions that make expressions match.
- **Substitution** -> Replacing variables with terms.
- **Forward Chaining** -> Data-driven inference from known facts to new facts.
- **Backward Chaining** -> Goal-driven inference working backward from query.
- **`forall x exists y ...` vs `exists y forall x ...`** -> Not equivalent; quantifier order changes meaning.

## C) Search Problem Setup

- **State Space** -> All possible states reachable in the problem.
- **Initial State** -> Starting state of the agent.
- **Goal Test** -> Condition used to decide if a state is a solution.
- **Successor Function** -> Rules for generating next states.
- **Path Cost (`g(n)`)** -> Total cost from start to node `n`.
- **Branching Factor (`b`)** -> Average number of successors per state.
- **Solution Depth (`d`)** -> Depth of the shallowest goal.
- **Maximum Depth (`m`)** -> Maximum depth of search tree.

## D) Uninformed + Informed Search

- **BFS** -> Expands shallowest nodes first; complete, optimal with unit costs.
- **DFS** -> Expands deepest nodes first; low memory, not generally complete/optimal.
- **UCS** -> Expands node with lowest path cost; complete/optimal with positive step costs.
- **IDS** -> Repeated depth-limited DFS; BFS-like completeness with DFS-like memory.
- **Greedy Best-First Search** -> Chooses lowest `h(n)`; often fast, not optimal.
- **A\*** -> Chooses lowest `f(n)=g(n)+h(n)`; optimal with admissible heuristic.
- **IDA\*** -> Iterative deepening on `f`-cost thresholds; lower memory than A*.
- **Beam Search** -> Keeps top `k` nodes at each depth; fast but may miss optimal path.

## E) Heuristics

- **Heuristic (`h(n)`)** -> Estimate of cost from node `n` to goal.
- **Admissible Heuristic** -> Never overestimates true remaining cost (`h(n) <= h*(n)`).
- **Consistent Heuristic** -> Satisfies triangle inequality (`h(n) <= c(n,n') + h(n')`).
- **Dominating Heuristic** -> Better informed admissible heuristic; usually fewer expansions.
- **Heuristic Error** -> Difference between estimate and true remaining cost.

## F) Optimization / Local Search

- **Hill Climbing** -> Move to better neighbor; can get stuck in local optima.
- **Local Optimum** -> Better than nearby states but not globally best.
- **Plateau** -> Region where neighboring states have equal value.
- **Simulated Annealing** -> Sometimes accepts worse moves to escape local optima.
- **Cooling Schedule** -> Rule for reducing exploration probability over time.
- **Genetic Algorithm** -> Population-based search using selection, crossover, mutation.
- **Mutation** -> Random variation to increase diversity.
- **Elitism** -> Keep best candidates across generations.

## G) High-Priority: Exploration vs Exploitation

- **Exploration** -> Trying uncertain actions to gain information about their value.
- **Exploitation** -> Choosing the currently best-known action for immediate reward.
- **Exploration-Exploitation Tradeoff** -> Balancing short-term reward vs long-term learning.
- **Under-Exploration Risk** -> Prematurely committing to suboptimal choices.
- **Over-Exploration Risk** -> Wasting time on poor actions, lowering short-term reward.
- **Regret** -> Reward gap between chosen actions and the best possible action.
- **Cumulative Regret** -> Total performance loss over time due to imperfect choices.
- **Multi-Armed Bandit** -> Simplified setting for studying exploration vs exploitation.
- **Stationary Environment** -> Reward distributions stay the same over time.
- **Non-Stationary Environment** -> Reward distributions change over time.

## H) Exploration Strategies (Flashcard Must-Know)

- **Epsilon-Greedy** -> Exploit with probability `1-epsilon`, explore randomly with `epsilon`.
- **Decaying Epsilon** -> Start with more exploration, reduce exploration over time.
- **Optimistic Initialization** -> Start with high value estimates to encourage early exploration.
- **UCB (Upper Confidence Bound)** -> Choose action maximizing estimate + uncertainty bonus.
- **Thompson Sampling** -> Sample from posterior belief and pick best sampled action.
- **Softmax/Boltzmann Exploration** -> Sample actions by probability proportional to estimated value.
- **Random Restarts** -> Re-run search from different starts to improve global exploration.

## I) Quick Compare Cards

- **BFS vs DFS** -> BFS is complete/optimal (unit costs), DFS uses much less memory.
- **UCS vs A\*** -> UCS uses only `g(n)`; A* uses `g(n)+h(n)` to guide search.
- **Admissible vs Consistent** -> Admissible: never overestimate; Consistent: admissible + monotonic.
- **Exploration vs Exploitation** -> Learn better options vs maximize known reward now.
- **Local Search vs Systematic Search** -> Local search optimizes current state; systematic search tracks paths/tree.

## J) Mini Formula Cards

- **A\* Evaluation** -> `f(n) = g(n) + h(n)`
- **Admissibility Condition** -> `h(n) <= h*(n)`
- **Consistency Condition** -> `h(n) <= c(n,n') + h(n')`
- **Epsilon-Greedy Policy** -> Explore with `epsilon`, exploit with `1-epsilon`

