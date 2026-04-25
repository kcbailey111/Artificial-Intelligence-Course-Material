# Logic and Search

This document was generated from text extracted from the **Final Exam Material** folder. Slide PDFs may have imperfect reading order; formulas and diagrams appear as plain text. Topics: propositional logic, uninformed and informed search, first-order logic, advanced search/optimization.

## Propositional Logic

*Extracted from PDF: `1 Propositonal Logic (1).pdf`*

```
Brief History of Logic in AI

It has been the persistent backbone of AI, evolving to meet new challenges while 
remaining central to how we build intelligent systems.
Logic is not just a historical artifact.
“Persistent backbone of AI” “Persistent backbone”

Logic & AI: Historical Context
Dartmouth Conference (Summer 1956)
• Established symbolic reasoning as AI's core 
approach: intelligence through manipulation of logical 
symbols
• Set the “logic can capture thinking” paradigm that 
dominated AI for 30+ years
• Created the research agenda focused on formal 
reasoning, theorem proving, and rule-based systems
Proposal
"We propose that a 2-month, 10-person study of artificial intelligence be carried out... The study is 
to proceed on the basis of the conjecture that every aspect of learning or any other feature of 
intelligence can in principle be so precisely described that a machine can be made to simulate it."

Key Logic-in-AI Milestones I
Logic Theorist (1956) - Newell & Simon
• First program to prove mathematical theorems using logical reasoning
• Demonstrated that machines could perform formal logical deduction
LISP (“List Processing”) (1958) - John McCarthy
• Symbolic Processing: LISP was designed for manipulating symbols rather than numbers, making it ideal for AI 
tasks like logical reasoning and language understanding.
• Code-as-Data (Homoiconicity): LISP treats code and data interchangeably, allowing programs to manipulate 
their own structure—a powerful feature for AI and metaprogramming.
• Recursion-Friendly: LISP supports recursive functions naturally, which is essential for many AI algorithms.
• Prefix Notation (Polish Notation): Uses fully parenthesized prefix notation, e.g., (+ 2 3) instead of 2 +  3.
• Garbage Collection: One of the first languages to include automatic memory management.
• Extensibility: Users can define new control structures and language features, making it highly adaptable.
• Influence: It became the dominant language for symbolic AI research for decades.

Key Logic-in-AI Milestones II
Expert Systems Era (1970s-1980s)
• Rule-based systems using “IF-THEN” 
logical reasoning
MYCIN: Stanford (1970s)
• Purpose: Diagnose bacterial infections and recommend 
antibiotics.
• Rule-Based System: Used hundreds of “IF-THEN” rules 
to simulate expert reasoning.
• Knowledge Representation: Encoded medical expertise 
as logical rules.
• Inference Engine: Applied backward chaining to deduce 
conclusions from symptoms.
• Uncertainty Handling: Introduced certainty factors to 
manage probabilistic reasoning.
• Impact: Demonstrated expert-level decision-making in 
real-world domains like medicine.
DENDRAL: Stanford (1960s)
• Purpose: Assist chemists in identifying molecular 
structures from mass spectrometry data.
• Domain-Specific Expert System: Focused on organic 
chemistry, particularly structural analysis.
• Rule-Based Reasoning: Used encoded chemical 
knowledge and inference rules to generate 
hypotheses.
• Knowledge Engineering Breakthrough: Pioneered 
techniques for capturing expert knowledge in a formal 
system.
• Impact: Demonstrated that expert systems could 
outperform human experts in narrow domains.
Proved logical reasoning could solve real-world problems; 
established knowledge representation as encoding logical rules; 
showed logic could capture expert human reasoning

Key Logic-in-AI Milestones III
Logic Programming with Prolog (1970s)
• Programming language where you write logical facts and rules, computer ‘searches’ logical conclusions
• Made logic itself the programming paradigm: showed computation as logical inference
• Influenced AI knowledge representation
inOrder([]).
inOrder([A, B | T]) :- A =< B, inOrder([B|T]).
inOrder([_]).
Empty list is ordered.
A list containing 1 element is sorted.
Check if the first two list 
elements are ordered.
Check that the tail of the 
original list is ordered.
naiveSort(L1, L2) :- perm(L1, L2), inOrder(L2).

Key Logic-in-AI Milestones IV
The Logical Reasoning Challenge (1980s Crisis):
• Problem: Pure logical systems couldn't handle uncertainty, incomplete information, or common-sense 
reasoning
• Forced development of fuzzy logic and probabilistic reasoning (expanding what “logic” means in AI)
SAT/SMT Solvers (2000s-present)
• Extremely efficient programs that solve logical satisfiability problems
• Shows logical reasoning can scale to millions of variables; used in 
software verification, planning, scheduling
Automated Theorem Proving
• AI systems that prove mathematical theorems using formal logic.
• Demonstrates machine reasoning can surpass humans in formal domains; verifies critical software and 
hardware
SAT: Solving logical boolean formulas
SMT: Boolean logic, but reasoning over integers.

Symbolic (Logic-based)
• “Top-Down” Approach: Intelligence through 
manipulation of symbols and rules
• Explicit knowledge representation: We tell the 
computer what we know
• Rule-based reasoning: Follows logical steps 
humans can trace
• Explainable decisions: Can precisely explain “why” 
it reached a conclusion
• Good for structured domains: Excels where rules 
are clear (chess, theorem proving, legal reasoning)
Core assumption: Intelligence is symbol manipulation
Two Paradigms: Symbolic vs Connectionist Approaches
We have two fundamentally different philosophies about how intelligence works.
Connectionist (Neural Networks)
• “Bottom-Up” Approach: Intelligence 
emerges from learning patterns
• Learning from data: Discovers patterns we 
might not see
• Pattern recognition: Excels at finding 
subtle statistical regularities
• Statistical inference: Makes decisions 
based on learned associations
• Good for perceptual tasks: Handles messy 
real-world data (vision, speech, language)
Core assumption: Intelligence emerges from 
interconnected simple units
Integrating paradigms: Neurosymbolic AI
Reasoning
Explanation Adaptation
Learning
 cat
(Recent Trend)

Key Logic-in-AI Milestones V
Neurosymbolic AI (2020s)
• Combining neural networks with logical reasoning (e.g., AlphaGeometry)
• Merges pattern recognition with logical deduction; represents the future where logic remains essential 
even in the neural age
LLMs and Logical Reasoning
• Large language models showing emergent logical reasoning abilities
• Suggests statistical learning can acquire logical structure; raises questions about 
whether logic is learned or programmed
LRMs (Large Reasoning Models): designed for complex reasoning, combining symbolic 
logic with neural networks.
• Unlike LLMs, they focus on deductive, inductive, and mathematical reasoning
• Provide explanations of each step taken facilitating analysis and human verification.

Introduction to logic
• Arguments, validity, soundness, entailment
Propositional logic
• Sentences, semantics, inference
Inference methods
• Enumeration
• Fundamental rules: Modus ponens
• Forward chaining (data-driven reasoning)
• Backward chaining (goal-driven reasoning)
• Resolution (CNF conversion and resolution rule)
• Soundness and completeness of inference systems
Topics in Logic and Propositional Logic

Arguments
Logic is the study of correct reasoning: how to 
draw valid conclusions from given information.
Our Challenge: How do we formalize “correct 
reasoning”?
Before we can automate reasoning, we must understand 
three key concepts that define what makes reasoning correct.
Definition. An argument is a set of sentences (premises) and a conclusion.
Premises
Sarah has a student ID.
All students must have student 
IDs to enter the library.
Sarah entered the library.
Conclusion Jake will be late for his 8am class.
If you hit the snooze button more than 
twice, you will be late for your 8am class.
Jake hit the snooze button four times this 
morning.

Validity and Soundness
Definition. An argument is valid if, assuming all its 
premises are true, the conclusion must also be true.
Premises
My phone needs 
charging.
All smartphones need 
charging. My phone is a 
smartphone.
Conclusion Dr. Alvin gives easy exams.
All professors give easy exams.
Dr. Alvin is a professor.
ValidValid?
Definition. An argument is sound if it 
is valid and all premises are actually true.
Sound means the conclusion is not only logically 
guaranteed but also factually correct.
Validity is about the form of the argument—not whether 
the premises are actually true. Even an argument with false 
premises can be valid if the conclusion logically follows.
SoundSound?
Valid
No
Jessica is a student.
Some students have iPhones. 
Jessica has an iPhone. 
No
No

Entailment
Definition. 𝐴 ⊨  𝐵 if and only 
if in every interpretation 
where 𝐴 is true, 𝐵 is also true.
𝐴 It is raining heavily.
𝐵
(Whenever it rains heavily, 
the ground must be wet.)
𝐴 ⊨  𝐵
𝐵 is a logical consequence of 𝐴; 
i.e., the truth of 𝐴 guarantees 
the truth of 𝐵 based on logical 
structure and meaning.
The ground is wet.
Yes
Jake hit snooze 4 times and 
his class starts in 10 minutes.
(There is a possible interpretation 
where 𝐴 is true but 𝐵 is false: Jake 
lives next door and can make it in 2 
minutes.
Jake will be late to class.
No
Sarah received an A on every assignment 
and every quiz/exam in the course.
Sarah will receive an A in the course.
Yes
All 
interpretations
𝑩 is true
𝑨 is 
true

Propositional Logic

Propositions
Definition. A proposition is a phrase that is either True or False (but not 
both). 
I have an orange cat.
2 + 2 = 4
Go directly to jail.
It is not true that 3 is an even integer or 7 is a prime number.
Knock before entering!
Examples. State whether each phrase is a proposition: yes / no.
Yes
Yes
No
Yes
No

Propositional Formula
Definition. The following strings are valid (well-formed) propositional sentences:
Symbols (atomic sentences)
• A variable name: often a capitalized letter.
Unary Operators
• Negation: ~𝜙 where 𝜙 is a (valid) propositional sentence.
Binary Operators
For 𝜙 and 𝜓 being (valid) propositional sentences:
• Conjunction: 𝜙 ∧ 𝜓
• Disjunction: 𝜙 ∨  𝜓
• Implication: 𝜙 ⇒  𝜓
• Biconditional: 𝜙 ⇔  𝜓
Other books/sources may 
indicate negation as ¬𝜙 or 𝜙′.
For example, P, Q, R.
And
Or
How we formally state an assumption (𝜙) and statement to prove (𝜓). 
𝜙: \phi 𝜓: \psi
Constants
• true, false
How we formally state equivalence. 

Propositional Sentence Examples
Suppose:
• 𝑃: “it is cold”
• 𝑄: “it is raining”
“If it is cold or it is raining, then I will wear a jacket” 𝑃 ∨ 𝑄 ⇒ 𝑅
“I will not wear a jacket.” ~𝑅
• 𝑅: “I will wear a jacket”
• 𝑆: “It is hot”
“If it is raining, then it is cold.” 𝑄 ⇒ 𝑃
“If it is cold, then it is raining.” 𝑃 ⇒ 𝑄
“I will wear a jacket if and only if it is cold and not hot.” 𝑅 ⇔ 𝑃 ∧ ~𝑆

Precedence
𝑃 ∧ Q ∨ 𝑆 ⇒ 𝑅In propositional logic, operator precedence matters. In 
decreasing order of precedence (i.e, we evaluate in this 
order):
• Negation (~)
• Conjunction (∧)
• Disjunction (∨)
• Biconditional (⇔) and Conditional (⇒)
⇒
𝑅
𝑄
∨
𝑃
∧ 𝑆
𝑃 ⇒ Q ⇔ 𝑆 ∧ ~𝑅
𝑃 ⇒ Q ⇒ 𝑆
⇒
𝑄
𝑃 ⇒
𝑆
⇒ and ⇔ are right-associative:
 𝑃 ⇒ Q ⇒ 𝑆 is interpreted as 𝑃 ⇒ Q ⇒ 𝑆
∧
𝑅
~𝑆
⇒
𝑄
𝑃 ⇔Use parentheses to 
guarantee well-formedness.

Propositional Logic Semantics

Semantics
All of the previous work helped us establish the syntax of propositional sentences for 
our language.
Every variable stands for a primitive proposition that may be either true or false.
Primitive Propositions
𝑃 : “It is raining.”
We construct compound sentences 
containing more than one primitive 
proposition:
𝑄 : “My umbrella is open.”
𝑅 : “I am singing.”
𝑆 : “I am dancing.”
𝑃 ∧ ~𝑄 ∧ (𝑅 ∨ 𝑆)
This sentence evaluates to true if:
It is raining and my umbrella is not open and
furthermore I am singing or dancing (or both).
Definition. The semantics are the compositional rules that define the meaning of 
logical connectives and how to evaluate the truth of formulas.

Models
We call each possible configuration of true and 
false values for a formula a model.
Let 𝑃 ∧ 𝑄 be a compound propositional sentence.
Consider configurations of true / false values for 
primitives 𝑃 and 𝑄.
𝑃 𝑄 𝑃 ∧ 𝑄
T T T
T F F
F T F
F F F
Definition. Let 𝑆 be a set of variable names. A model 𝑀 is a function that assigns a truth 
value to every variable name in 𝑆. That is, 𝑀 ∶ 𝑆 → 𝑇𝑟𝑢𝑒, 𝐹𝑎𝑙𝑠𝑒
There are 4 possible models for 𝑃 ∧ 𝑄.
Definition. A model 𝑀 satisfies sentence 𝛼 if 𝛼 is true under the assignment of truth values 
given by 𝑀.
A sentence 𝛼 is satisfiable if there exists at least one model that satisfies 𝛼 (makes the 
sentence true).

Example
𝑃 : “It is raining.”
𝑄 : “My umbrella is open.”
𝑅 : “I am singing.”
𝑆 : “I am dancing.”
𝑃 ∧  ~𝑞  ∧  (𝑅 ∨ 𝑆)
∧
∧ ∨
𝑅𝑃 ~
𝑄
𝑆
𝑀𝑃=𝑡𝑟𝑢𝑒
𝑀𝑄=𝑓𝑎𝑙𝑠𝑒
𝑀𝑅=𝑡𝑟𝑢𝑒
𝑀𝑆=𝑓𝑎𝑙𝑠𝑒
It is raining and my umbrella is not 
open and furthermore I am singing 
or dancing (or both).
∧
∧ ∨
𝑡𝑟𝑢𝑒 𝑡𝑟𝑢𝑒 𝑓𝑎𝑙𝑠𝑒𝑡𝑟𝑢𝑒
∧
𝑡𝑟𝑢𝑒 𝑡𝑟𝑢𝑒
𝑡𝑟𝑢𝑒
We can say that is sentence is satisfiable. (It 
may evaluate to true for other models.)

Example: Exclusive Or
Exercise. For propositions 𝐴 and 𝐵, the exclusive or operation, denoted as 𝐴 ⊕ 𝐵, yields true if and only 
if exactly one of the operands 𝐴 or 𝐵 is true. Define an equivalent logical expression for 𝐴 ⊕ 𝐵. 
Demonstrate the equivalence with a truth table.
𝐴 ∧ ~𝐵 ~𝐴 ∧ 𝐵
F F
T F
F T
F F
Solution.
𝐴 ∧ ~𝐵 ∨ ~𝐴 ∧ 𝐵
F
T
T
F
𝐴 𝐵
T T
T F
F T
F F

Associativity I
Exercise. For propositions 𝐴, 𝐵 and 𝐶, are the operators ∨ and/or ∧ associative operators?
𝐴 ∨ B ∨ 𝐶 ⇔ 𝐴 ∨ B ∨ 𝐶 𝐴 ∧ B ∧ 𝐶 ⇔ 𝐴 ∧ B ∧ 𝐶
Solution.
𝑨 𝑩 𝑪
T T T
T T F
T F T
T F F
F T T
F T F
F F T
F F F
𝑨 ∨ 𝑩 ∨ 𝑪 𝑨 ∨ 𝑩 ∨ 𝑪
T T
T T
T T
T T
T T
T T
T T
F F
𝑨 ∧ 𝑩 ∧ 𝑪 𝑨 ∧ 𝑩 ∧ 𝑪
T T
F F
F F
F F
F F
F F
F F
F F Clearly, yes. ∧ 
and ∨ are 
associative.

Associativity II
Exercise. Is ⇒ an associative operator?
𝑨 𝑩 𝑨 ⇒ 𝑩 𝑪
T T T T
T T T F
T F F T
T F F F
F T T T
F T T F
F F T T
F F T F
Solution.
𝑨 ⇒ 𝑩 ⇒ 𝑪
T
F
T
T
T
T
T
T
𝑨 ⇒ 𝑩 ⇒ 𝑪
T
F
T
T
T
F
T
F
𝑩 ⇒ 𝑪
T
F
T
T
T
F
T
T
⇒ is not associative.

Implication 𝜙 𝜓 𝜙 ⇒ 𝜓 ~𝝓 ∨  𝝍
T T T T
T F F F
F T T T
F F T T
𝜙 ⇒ 𝜓 would be 
false only if 𝜙 is 
true and 𝜓 is false. 
A helpful interpretation 𝜙 ⇒ 𝜓 is “𝜓 is a logical consequence of 𝜙”.
Example.
In each scenario do I keep my promise?
1. I am healthy, and I do go to class.
3. I am not healthy, and I do go to class.
2. I am healthy, and I do not go to class.
4. I am not healthy, and I do not go to class.
We often view implication as if 𝜙, then 𝜓.
𝑡𝑟𝑢𝑒 ⇒ 𝑡𝑟𝑢𝑒  
Did I keep my promise?
Yes.
𝑡𝑟𝑢𝑒 ⇒ 𝑓𝑎𝑙𝑠𝑒  
Suppose I make a promise that, “If I am healthy, I will go to class.”
No.
𝑓𝑎𝑙𝑠𝑒 ⇒ 𝑡𝑟𝑢𝑒  Yes.
Yes.𝑓𝑎𝑙𝑠𝑒 ⇒ 𝑓𝑎𝑙𝑠𝑒  
𝜙: \phi
𝜓: \psi

Inference

Knowledge Bases
How can an AI agent store, organize, and reason with everything it knows about the 
world?
Definition. A knowledge base 𝐾𝐵 is a set of sentences
𝐾𝐵 = 𝐴1, 𝐴2, … , A𝑛
These sentences are typically (conceptually) connected by logical conjunctions:
𝐾𝐵 = 𝐴1 ∧ 𝐴2 ∧ ⋯ ∧ A𝑛.
Each sentence 𝐴𝑖 represents a fact or assertion about the world, expressed in a 
formal logic language.

Ultimately, our goal is to infer (discover) new sentences that logically follow from a 
knowledge base.
Knowledge Base Entailment and Inference
Definition. In propositional logic, a sentence 𝑆 is entailed by a knowledge base 𝐾𝐵, 
written as
𝐾𝐵 ⊨ 𝑆
if and only if S is true in every model where all sentences in 𝐾𝐵 are true.
Entailment tells us what must be true given the facts and rules in the 𝐾𝐵; it is the foundation 
for logical reasoning in AI systems.
But, what else can we conclude from our 𝐾𝐵?

Knowledge Base Operations
Add new knowledge TELL(𝐾𝐵, sentence)
Retrieve entailed information ASK(𝐾𝐵, query)

Knowledge Base Operations: Example I
Suppose 𝐾𝐵 = { P: Alex is a student,
Q: Alex is enrolled in CSC-343
S: Alex needs a textbook
}
In propositional logic notation, we have 𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑆
TELL(𝐾𝐵, If Alex is enrolled in CSC-343, then Alex needs a textbook)
𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑆 ∧ 𝑄 ⇒ 𝑆results in

Knowledge Base Operations: Example II
ASK(𝐾𝐵, 𝑆)
Assume: 𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑄 ⇒ 𝑆
= true
𝐾𝐵 ⊨ 𝑆
𝑷 𝑸
T T
T T
T F
T F
F T
F T
F F
F F
𝑷 ∧ 𝑸 ∧ 𝑸 ⇒ 𝑺
T
F
F
F
F
F
F
F
𝑺
T
F
T
F
T
F
T
F
𝑸 ⇒ 𝑺
T
F
T
T
T
F
T
T
𝑺
T
F
T
F
T
F
T
F
Since 𝑆 is true in every model where 𝐾𝐵 
is true (just this one model), we conclude:

Knowledge Base Operations: Example III
ASK(𝐾𝐵, 𝑄 ⇒ 𝑆)
Assume: 𝐾𝐵 = 𝑃 ∧ 𝑄
= false
𝐾𝐵 ⊭ 𝑄 ⇒ 𝑆
𝑷 𝑸
T T
T T
T F
T F
F T
F T
F F
F F
𝑲𝑩 = 𝑷 ∧ 𝑸
T
T
F
F
F
F
F
F
𝑺
T
F
T
F
T
F
T
F
𝑸 ⇒ 𝑺
T
F
T
T
T
F
T
T
𝑄 ⇒ 𝑆  is not true in every model where 
𝐾𝐵 is true, we conclude:

Knowledge Base Operations: Example IV
ASK(𝐾𝐵, 𝑄 ⇒ 𝑆)
Assume: 𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑆
= true
𝐾𝐵 ⊨ 𝑄 ⇒ 𝑆
𝑷 𝑸
T T
T T
T F
T F
F T
F T
F F
F F
𝑲𝑩 = 𝑷 ∧ 𝑸 ∧ 𝑺
T
F
F
F
F
F
F
F
𝑺
T
F
T
F
T
F
T
F
𝑸 ⇒ 𝑺
T
F
T
T
T
F
T
T
𝑄 ⇒ 𝑆  is true in the only model where 
𝐾𝐵 is true, we conclude:
Caution: Implication (⇒) does not capture causation. While 
𝐾𝐵 technically entails 𝑄 ⇒ 𝑆 (because 𝑆 is already true), this 
does not mean 𝑄 is the reason for 𝑆. Propositional logic 
cannot distinguish correlation from causation.
We cannot conclude enrollment 
causes the textbook need. Maybe 
Alex needs it for another course!

From Logic to Learning
Extracting patterns from instances is a task that propositional logic was not 
designed for.
Given only facts in a knowledge base, searching for rules that relate them is 
computationally expensive and yields only correlations, not meaningful 
knowledge.
This motivates machine learning: given ground truth data, can we automatically 
induce the rules? 
Neural networks and other ML methods address exactly this challenge: learning 
patterns from examples rather than being told the rules explicitly.
Approach Input Output Direction
Logic / Knowledge Bases Rules + Facts New Facts Deduction
Machine Learning Instances / Data Patterns / Rules Induction
The Bridge
The Limitation

Inference
Inference is the process of deriving new sentences that are entailed by a 𝐾𝐵. Fundamentally, it 
allows us to answer queries, make decisions, and automate reasoning.
Definition. Inference is the process of deriving a sentence 𝑆 from a knowledge base 𝐾𝐵, written 
as
𝐾𝐵 ⊢ 𝑆
if and only if there exists a way for S to be derived from 𝐾𝐵 using a sound inference procedure*.
Given a knowledge base (KB), we want to derive new sentences that logically follow 
without checking every possible truth assignment (aka brute-force model checking).
From our prior example with 𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑄 ⇒ 𝑆 , we can say 𝐾𝐵 ⊢ 𝑆.
*we will talk about this

Methods of Inference: Enumeration
Enumeration is an inference procedure that checks whether a sentence is entailed by a knowledge base 
by evaluating all possible truth assignments to the propositional symbols.
Suppose 𝐾𝐵 = 𝑃 ∧ 𝑄 ∧ 𝑃 ⇒ 𝑆  and ASK(𝐾𝐵, 𝑆).
𝑷 𝑸 𝑺
T T T
T T F
T F T
T F F
F T T
F T F
F F T
F F F
𝐾𝐵 ⊨ 𝑆  ?
Yes.
Recall 𝐾𝐵 ⊨ 𝑆 if and only if 
in every model where 𝐾𝐵 is 
true, 𝑆 is also true.
𝐾𝐵 ⊢ 𝑆  ?
Yes.
There exists a way to derive 
𝑆 from 𝐾𝐵.
𝑲𝑩 = 𝑷 ∧ 𝑸 ∧ 𝑷 ⇒ 𝑺
T
F
F
F
F
F
F
F
𝑷 ⇒ 𝑺
T
F
T
F
T
T
T
T
Enumeration is an 
intractable procedure. Why? 2𝑛 models for 𝑛 variables.

Methods of Inference: Syntactic Manipulation
Inference rules provide precise, efficient steps for deriving conclusions: offering clarity and control 
(explainability) compared to broader procedures like enumeration or resolution, which are more 
exhaustive but less intuitive.
Modus Ponens
𝐴 ⇒ 𝐵, 𝐴 ⊢ 𝐵
Premise 1:
Premise 2:
Conclusion: 
𝐴 ⇒ 𝐵
𝐴
𝐵
And-Elimination
𝐴 ∧ 𝐵 ⊢ 𝐴, 𝐵
Premise 1:
Conclusion 1:
Conclusion 2: 
𝐴 ∧ 𝐵
𝐴
𝐵
DeMorgan’s Laws
~ 𝐴 ∧ 𝐵 ≡ ~ 𝐴 ∨ ~ 𝐵
There are many others.
~ 𝐴 ∨ 𝐵 ≡ ~ 𝐴 ∧ ~ 𝐵

Logical Inference Example
Example.
Premises: ~ 𝑃 ∨ 𝑄
~𝑃 ⇒ 𝑅
𝑅 ⇒ 𝑆
~ 𝑃 ∨ 𝑄 ≡ ~𝑃 ∧ ~𝑄 DeMorgan’s
⇒ ~𝑃 ∧ ~𝑄
⇒ ~𝑃
And-Elimination
⇒ ~𝑄
~𝑃 ∧ ~𝑄
⇒ 𝑅
Modus Ponens~𝑃, ~𝑃 ⇒ 𝑅
⇒ 𝑆
Modus Ponens𝑅, 𝑅 ⇒ 𝑆


Other Rules of Logical Inference
Rule Equivalence
Commutativity of ∧ 𝛼 ∧ 𝛽 ≡ 𝛽 ∧ 𝛼
Commutativity of ∨ 𝛼 ∨ 𝛽 ≡ 𝛽 ∨ 𝛼
Associativity of ∧ 𝛼 ∧ 𝛽 ∧ 𝛾 ≡ 𝛼 ∧ 𝛽 ∧ 𝛾
Associativity of ∨ 𝛼 ∨ 𝛽 ∨ 𝛾 ≡ 𝛼 ∨ 𝛽 ∨ 𝛾
Double-Negation Elimination ~ ~𝛼 ≡ 𝛼
Contraposition 𝛼 ⇒ 𝛽 ≡ ~𝛽 ⇒ 𝛼
Implication Elimination 𝛼 ⇒ 𝛽 ≡ ~𝛼 ∨ 𝛽
Biconditional Elimination 𝛼 ⇔ 𝛽 ≡ 𝛼 ⇒ 𝛽 ∧ 𝛽 ⇒ 𝛼
DeMorgan ~ 𝛼 ∧ 𝛽 ≡ ~𝛼 ∨ ~𝛽
DeMorgan ~ 𝛼 ∨ 𝛽 ≡ ~𝛼 ∧ ~𝛽
Distributivity of ∧ over ∨ 𝛼 ∧ 𝛽 ∨ 𝛾 ≡ 𝛼 ∧ 𝛽 ∨ 𝛼 ∧ 𝛾
Distributivity of ∨ over ∧ 𝛼 ∨ 𝛽 ∧ 𝛾 ≡ 𝛼 ∨ 𝛽 ∧ 𝛼 ∨ 𝛾
Absorption 𝛼 ∧ 𝛼 ∨ 𝛽 ≡ 𝛼 ≡ 𝛼 ∨ 𝛼 ∧ 𝛽

Methods of Inference: Chaining
A rule-based system has the following components:
• Facts: A database of true statements (known information).
• Rules: “If-then” statements that encode domain knowledge.
• Inference Engine: Algorithms to apply rules to facts to derive new knowledge.
There are two main approaches 
in rule-based systems:
• Data-driven reasoning with Forward Chaining.
• Goal-driven reasoning with Backward Chaining.

Forward Chaining
FORWARD_CHAINING(KB, query):
    facts = initial_facts
    if query in facts: return True
   new_facts = True
   while new_facts:
        new_facts = False
        for each rule in KB:
            if not rule.conditions_satisfied_by(facts):
               continue
            if rule.conclusion in facts:
               continue
            add rule.conclusion to facts
           new_facts = True
           if rule.conclusion == query: return True
   return False
Find rules whose conditions 
match current facts
A new fact has been derived 
when all ‘conditions’ are 
satisfied by database facts.
(Data-driven reasoning.)
Iterate exhaustively while 
new facts are inferred.

Forward Chaining: Example
R1: 𝐴 ∧ 𝐵 ⇒ 𝐷
R2: 𝐶 ⇒ 𝐸
R3: 𝐷 ∧ 𝐸 ⇒ 𝐹
R4: 𝐴 ∧ 𝐶 ⇒ 𝐺
R5: 𝐺 ⇒ 𝐻
R6: 𝐹 ∧ 𝐻 ⇒ 𝐼
R7: 𝐷 ⇒ 𝐽
R8: 𝐸 ∧ 𝐽 ⇒ 𝐾
Rules
𝐴, 𝐵, 𝐶Facts 𝐴, 𝐵, 𝐶
𝐴 ∧ 𝐵 ⇒ 𝐷
𝐶 ⇒ 𝐸
𝐷
𝐸
𝐴 ∧ 𝐶 ⇒ 𝐺 𝐺
𝐴, 𝐵, 𝐶, 𝐷, 𝐸, 𝐺
𝐷 ∧ 𝐸 ⇒ 𝐹 𝐹
𝐺 ⇒ 𝐻 𝐻
𝐷 ⇒ 𝐽 𝐽
𝐴, 𝐵, 𝐶, 𝐷, 𝐸, 𝐹, 𝐺, 𝐻, 𝐽
𝐸 ∧ 𝐽 ⇒ 𝐾 𝐾
𝐹 ∧ 𝐻 ⇒ 𝐼 𝐼
∅
𝐴, 𝐵, 𝐶, 𝐷, 𝐸, 𝐹, 
𝐺, 𝐻, 𝐼, 𝐽, 𝐾
Observe that the forward chaining algorithm as defined, is inefficient. We could easily optimize it using a 
‘marking’ algorithm which tracks ‘used’ rules. Thus, we would not need to iterate over those same rules 
repeatedly.

Forward Chaining: Try It
R1: 𝐴 ∧ 𝐵 ⇒ 𝐷
R2: 𝐵 ∧ 𝐶 ⇒ 𝐸
R3: 𝐴 ⇒ 𝐹
R4: 𝐷 ∧ 𝐹 ⇒ 𝐺
R5: 𝐸 ⇒ 𝐻
R6: 𝐶 ∧ 𝐷 ⇒ 𝐼
R7: 𝐺 ∧ 𝐻 ∧ 𝐼 ⇒ 𝐽
R8: 𝐹 ∧ 𝐽 ⇒ 𝐾
R9: 𝐷 ∧ 𝐿 ⇒ 𝑀
Rules
𝐴, 𝐵, 𝐶Facts

Backward Chaining
BACKWARD_CHAINING(KB, goal):
    if goal in facts: return True
    for each rule in KB:
        if rule.conclusion == goal:
            if PROVE_PREMISES(rule.conditions):
                return True
   return False
PROVE_PREMISES(premises):
    for each premise in premises:
       if not BACKWARD_CHAINING(KB, premise):
           return False
   return True
Think of the goal as being the root of a tree. Backward chaining is an inference technique that starts with a goal and 
builds that tree downward using the rules set. Ultimately, if the leaves of that tree are all in the known set of facts, 
we have deduced our goal from the knowledge base.  
Does a rule’s 
conclusion, match 
our current goal?
Must satisfy all premises for 
a rule to infer its conclusion.
Base case: goal is known.
Check all premises 
of matching rule.

Backward Chaining: Example
R1: 𝐴 ∧ 𝐵 ⇒ 𝐷
R2: 𝐶 ⇒ 𝐸
R3: 𝐷 ∧ 𝐸 ⇒ 𝐹
R4: 𝐴 ∧ 𝐶 ⇒ 𝐺
R5: 𝐺 ⇒ 𝐻
R6: 𝐹 ∧ 𝐻 ⇒ 𝐼
R7: 𝐷 ⇒ 𝐽
R8: 𝐸 ∧ 𝐽 ⇒ 𝐾
Rules
𝐴, 𝐵, 𝐶Facts
𝐴 ∧ 𝐵 ⇒ 𝐷
𝐶 ⇒ 𝐸
𝐷
𝐸
𝐷 ⇒ 𝐽 𝐽
𝐸 ∧ 𝐽 ⇒ 𝐾 𝐾
Backward chaining algorithm seems more efficient than forward training since it avoids unnecessary 
inference focusing on what is needed to prove the goal. However, it requires a starting point.
𝐶
𝐴
𝐵
𝐾Goal

Backward Chaining: Try It
R1: 𝐴 ∧ 𝐵 ⇒ 𝐷
R2: 𝐵 ∧ 𝐶 ⇒ 𝐸
R3: 𝐴 ⇒ 𝐹
R4: 𝐷 ∧ 𝐹 ⇒ 𝐺
R5: 𝐸 ⇒ 𝐻
R6: 𝐶 ∧ 𝐷 ⇒ 𝐼
R7: 𝐺 ∧ 𝐻 ∧ 𝐼 ⇒ 𝐽
R8: 𝐹 ∧ 𝐽 ⇒ 𝐾
R9: 𝐷 ∧ 𝐿 ⇒ 𝑀
Rules
𝐴, 𝐵, 𝐶Facts 𝐾Goal

Backward Chaining: Try It II
R1: 𝐴 ∧ 𝐵 ⇒ 𝐷
R2: B ∧ 𝐶 ⇒ 𝐷
R3: 𝐸 ∧ 𝐹 ⇒ 𝐷
R4: 𝐷 ∧ 𝐺 ⇒ 𝐻
R5: 𝐻 ⇒ 𝐾
Rules
𝐶, 𝐺Facts 𝐻Goal

Chaining Analogies
Forward Chaining Backward Chaining
• Start from known facts as the root of a tree.
• Apply rules to derive all possible conclusions.
• Explores every branch of a tree en route to 
inferring any / all facts (leaves in the tree).
• Goal: discovering everything that can be 
inferred.
• Start from a leaf (goal or query).
• Backward hypergraph search: Work 
backward tracing a path from the goal 
leaf back to the root.
• Goal: inferring a specific fact.
Copilot 
generated 
images! Ug.


Resolution

A Motivating Example
Problem. Prove that there are infinitely many prime numbers.
Can we prove this statement directly?
Doing so would require that we list or 
characterize all prime numbers (e.g., 𝑝 
is of the form 2𝑛 + 1 for 𝑛 > 1).
Instead…consider a short and elegant proof.
Proof by contradiction.
Suppose there are a finite number of prime numbers, enumerated as 𝑝1, 𝑝2, … 𝑝𝑛. Now, construct 
a value 𝑁 = 𝑝1 ⋅ 𝑝2 ⋅ … ⋅ 𝑝𝑛 + 1. Clearly, 𝑁 is not divisible by any prime 𝑝𝑖 (as 𝑁 % 𝑝𝑖 = 1 for all 
𝑖). 
∎
So we can conclude that either (1) 𝑁 is prime itself or (2) it is divisible by a prime number not in 
the list. In either case, we have a contradiction since all primes were in our enumerated list 
𝑝1, 𝑝2, … 𝑝𝑛.

Methods of Inference: Resolution 
Resolution, as an inference procedure, uses the idea of proof by contradiction.
Recall with proof by contraction, when proving 𝑝 ⇒ 𝑞, 
we are instead attempting to prove: 𝑝 ∧ ~𝑞 ⇒ 𝑓𝑎𝑙𝑠𝑒
𝒑 𝒒 𝒑 ⇒ 𝒒 𝒑 ∧ ~𝒒
T T T F
T F F T
F T T F
F F T F
Instead of juggling multiple inference rules, resolution uses one uniform rule to derive contradictions.
(The term refutation is often used in logic programming because 
the method focuses on refuting the negation of the goal.)
𝐾𝐵 ⊨ 𝑃 𝐾𝐵 ∧ ~𝑃 ⊨ 𝑓𝑎𝑙𝑠𝑒Direct inference
Resolution via Refutation
⇔

Conjunctive Normal Form (CNF)
A clause is a disjunction of literals (where a literal is an atomic proposition or its 
negation) whereas a sentence in CNF is a conjunction of one or more clauses.
~𝐴 ∨ 𝐵 ∨ 𝐶 ∧ ~𝐵 ∨ 𝐴 ∧ 𝐴 ∨ ~𝐶
clause clause clause
CNF

Converting to CNF
A clause is a disjunction of literals.
A sentence in CNF is a conjunction of one or more clauses.
Input: A sentence 𝑆.
Output: A sentence in CNF.
1. Eliminate implications:  ⇒ and ⇔.
2. Move negation (~) inward.
3. Apply distributive laws: ∨ over ∧.
4. Remove duplicate literals in a clause.
5. Remove tautologies.  
Distributivity of ∨ over ∧
𝛼 ∨ 𝛽 ∧ 𝛾 ≡ 𝛼 ∨ 𝛽 ∧ 𝛼 ∨ 𝛾

Try It
~ 𝑃 ⇒ 𝑄 ∧ 𝑅 ⇒ 𝑆
𝑃 ∨ 𝑅 ∧ 𝑃 ∨ ~𝑆 ∧ ~𝑄 ∨ 𝑅 ∧ ~𝑄 ∨ ~𝑆
Distributivity of ∨ over ∧
𝛼 ∨ 𝛽 ∧ 𝛾 ≡ 𝛼 ∨ 𝛽 ∧ 𝛼 ∨ 𝛾

Example: Converting to CNF I
~ 𝑃 ⇒ 𝑄 ⇔ 𝑅 ∨ 𝑆
~ 𝑃 ⇒ 𝑄 ⇒ 𝑅 ∧ 𝑅 ⇒ 𝑄 ∨ 𝑆
~ ~𝑃 ∨ ~𝑄 ∨ 𝑅 ∧ ~𝑅 ∨ 𝑄 ∨ 𝑆
𝑃 ∧ ~ ~𝑄 ∨ 𝑅 ∧ ~𝑅 ∨ 𝑄 ∨ 𝑆
Eliminate ⇔
Eliminate ⇒
Move negation (~) inward
𝑃 ∧ ~ ~𝑄 ∨ 𝑅 ∨ ~ ~𝑅 ∨ 𝑄 ∨ 𝑆
Move negation (~) inward
𝑃 ∧ 𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑄 ∨ 𝑆
Move negation (~) inward
𝑃 ∨ 𝑆 ∧ 𝑋 ∨ 𝑆
Apply distributive laws: ∨ over ∧
Let 𝑋 be 𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑄
𝑃 ∧ 𝑋 ∨ 𝑆
⇔
⇔
⇔
⇔
⇔
⇔
⇔
Remember to 
link expressions
Distributivity of ∨ over ∧
𝛼 ∨ 𝛽 ∧ 𝛾 ≡ 𝛼 ∨ 𝛽 ∧ 𝛼 ∨ 𝛾

Example: Converting to CNF II
𝑃 ∨ 𝑆 ∧ 𝑋 ∨ 𝑆
Handle 𝑋:
𝑋 ≡ 𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑄
Apply distributive laws: ∨ over ∧
𝑄 ∨ 𝑅 ∧ ~𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑄
𝑄 ∨ 𝑅 ∧ 𝑄 ∨ ~𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑅 ∨ ~𝑄
Apply distributive laws: ∨ over ∧
𝑄 ∨ 𝑅 ∧ 𝑄 ∨ ~𝑄 ∧ ~𝑅 ∨ 𝑅 ∧ ~𝑅 ∨ ~𝑄
Associativity of ∧
𝑄 ∨ 𝑅 ∧ ~𝑅 ∨ ~𝑄
Remove Tautologies
𝑃 ∨ 𝑆 ∧ 𝑄 ∨ 𝑅 ∧ ~𝑅 ∨ ~𝑄 ∨ 𝑆
𝑃 ∨ 𝑆 ∧ 𝑄 ∨ 𝑅 ∨ 𝑆 ∧ ~𝑅 ∨ ~𝑄 ∨ 𝑆
Apply distributive laws: ∨ over ∧
𝑃 ∨ 𝑆 ∧ 𝑄 ∨ 𝑅 ∨ 𝑆 ∧ ~𝑅 ∨ ~𝑄 ∨ 𝑆
Associativity of ∧
⇔
⇔
⇔
⇔
⇔
⇔
⇔
Distributivity of ∨ over ∧
𝛼 ∨ 𝛽 ∧ 𝛾 ≡ 𝛼 ∨ 𝛽 ∧ 𝛼 ∨ 𝛾

The Resolution Rule
𝐴 ∨ 𝐿 ∧ ~𝐿 ∨ 𝐵
𝐴 ∨ 𝐵 resolvent
parent clauses
Suppose we have clauses 𝐴, 𝐿, and 𝐵.
From a truth table:
𝑨 𝑳 𝑩
T T T
T T F
T F T
T F F
F T T
F T F
F F T
F F F
~𝑳 ∨ 𝑩
T
F
T
T
T
F
T
T
𝐀 ∨ 𝑳
T
T
T
T
T
T
F
F
𝑨 ∨ 𝑩
T
T
T
T
T
F
T
F
Whenever the parent clauses are 
both true, the resolvent is also true.
This is proof that the Resolution rule 
is sound: the resolvent is a logical 
consequence of its parent clauses.

Resolution Procedure
1) Combine 𝐾𝐵 ∧ ~𝑄.
2) Rename variables to avoid clashes. 
3) Convert 𝐾𝐵 ∧ ~𝑄 to CNF. 
Input:
• Knowledge base: 𝐾𝐵
• Query sentence: 𝑄
𝐴 ∨ 𝐿 ∧ ~𝐿 ∨ 𝐵
𝐴 ∨ 𝐵
5) Repeat (4) until either:
• Empty clause (⊥) is derived →
• Contradiction: 𝐾𝐵 ∧ ~𝑄 is unsatisfiable
• 𝐾𝐵 ⊨ 𝑄.
• No new clauses can be generated →
• 𝐾𝐵 ⊭ 𝑄 (Goal cannot be derived from 𝐾𝐵.)
4) Apply the Resolution rule.
Iterating: You are 
basically trying to 
prove the system 
breaks: if it does, your 
original idea was right.
Iterating: It’s like solving a 
puzzle: keep combining pieces 
until you either finish it or 
realize some pieces are missing.

Resolution Procedure Example
Input:
• Knowledge base: 𝑃 ∨ 𝑄, ~𝑃 ∨ 𝑅, ~𝑄 ∨ 𝑅
• Query sentence: 𝑅
1. Combine 𝐾𝐵 ∧ ~𝑄.
2. Rename variables to avoid clashes. 
3. Convert 𝐾𝐵 ∧ ~𝑄 to CNF. 
4. Apply the Resolution rule.
5. Repeat until (⊥) or exhaustion
The clauses are in CNF, so we have 𝐾𝐵 ∧ ~𝑅 ≡
𝑃 ∨ Q ∧ ~𝑃 ∨ 𝑅 ∧ ~𝑄 ∨ 𝑅 ∧ ~𝑅
Repeatedly apply the Resolution Rule to the existing 𝐾𝐵:
𝑃 ∨ Q ∧ ~𝑃 ∨ 𝑅
𝑄 ∨ 𝑅
~𝑄 ∨ 𝑅 ∧ ~𝑅
~𝑄
𝑃 ∨ Q ∧ ~𝑄 ∨ 𝑅
𝑃 ∨ 𝑅
Using the computed clauses:
𝑃 ∨ 𝑄 ∧ ~𝑄
𝑃
𝑄 ∨ 𝑅 ∧ ~𝑅
𝑄
We observe that we 
derived Q ∧ ~𝑄 ⊢⊥.
We conclude 𝐾𝐵 ⊨ 𝑅.
𝐴 = 𝐴 ∨ 𝑓𝑎𝑙𝑠𝑒

Resolution Example II
Input:
• Knowledge base: 𝐴 ∨ 𝐵 ∨ 𝐶, ~𝐴 ∨ 𝐷, ~𝐵 ∨ 𝐷, ~𝐶 ∨ ~𝐷
• Query sentence: 𝐷
1. Combine 𝐾𝐵 ∧ ~𝑄.
2. Rename variables to avoid clashes. 
3. Convert 𝐾𝐵 ∧ ~𝑄 to CNF. 
4. Apply the Resolution rule.
5. Repeat until (⊥) or exhaustion
The clauses are in CNF, so we have 𝐾𝐵 ∧ ~𝐷 ≡
𝐴 ∨ 𝐵 ∨ 𝐶 ∧ ~𝐴 ∨ 𝐷 ∧ ~𝐵 ∨ 𝐷 ∧ ~𝐶 ∨ ~𝐷 ∧ ~𝐷
Repeatedly apply the Resolution Rule to the existing 𝐾𝐵:
~𝐵 ∨ 𝐷 ∧ ~𝐷
~𝐵
~𝐴 ∨ 𝐷 ∧ ~𝐷
~𝐴
𝐴 ∨ 𝐵 ∨ C ∧ ~𝐴
𝐵 ∨ 𝐶
𝐵 ∨ 𝐶 ∧ ~𝐵
𝐶
~𝐶 ∨ ~𝐷 ∧ 𝐶
~𝐷
We have exhausted the 
useful resolutions.
We conclude 𝐾𝐵 ⊭ 𝐷.

Soundness and Completeness

Summary
Soundness 𝐾𝐵 ⊢ 𝜙 ⇒ 𝐾𝐵 ⊨ 𝜙“Don't derive false conclusions.”
Completeness 𝐾𝐵 ⊨ 𝜙 ⇒ 𝐾𝐵 ⊢ 𝜙“Can derive all true conclusions .”

Goal
Why?
A Sound and Complete Inference System
Syntactic derivation ⇔ Semantic validity
Syntactic (𝐾𝐵 ⊢ 𝜙): Rule application, 
symbol manipulation Semantic (𝐾𝐵 ⊨ 𝜙): Truth-based reasoning 
about logical relationships
In a sound and complete system, both approaches 
always give the same answer.

Soundness (of Propositional Logic)
Definition. An argument is sound if it 
is valid and all premises are actually true.Our general definition:
Definition. An inference system is sound if and only if for all knowledge bases 𝐾𝐵 and all sentences 
𝜙,
𝐾𝐵 ⊢ 𝜙 ⇒ 𝐾𝐵 ⊨ 𝜙
(If 𝜙 is derivable from 𝐾𝐵 using the inference rules, then 𝜙 is semantically entailed by 𝐾𝐵.)
Soundness is a guarantee that our inference system never leads us astray: every derivable conclusion is logically 
valid.
Without a sound inference system, we cannot trust our proofs since we might derive 𝜙 from ~𝜙.

Example: Not Sound
Suppose we accidentally design a system 
that includes an invalid rule: From 𝑃 ∨ 𝑄 we can derive 𝑃. 𝑃 ∨ 𝑄
𝑃
Consider a knowledge base 𝐾𝐵 = 𝑅, 𝑅 ⇒ 𝑆 ∨ 𝑇 .
Using modus ponens, 𝐾𝐵 = 𝑅, 𝑅 ⇒ 𝑆 ∨ 𝑇 , we can derive 𝑆 ∨ 𝑇.
𝑅, 𝑅 ⇒ 𝑆 ∨ 𝑇
𝑆 ∨ 𝑇
Using our invalid rule, we derive 𝑆. That is, 𝐾𝐵 ⊢ 𝑆. But to verify soundness, we need to show 𝐾𝐵 ⊨ 𝑆.
Suppose 𝑅 = 𝑡𝑟𝑢𝑒, 𝑆 = 𝑓𝑎𝑙𝑠𝑒, and 𝑇 = 𝑡𝑟𝑢𝑒. Then,
𝑅 = 𝑡𝑟𝑢𝑒
Recall, sound systems require that every inference rule preserves truth in all models. 
𝑅 ⇒ 𝑆 ∨ 𝑇
 𝑡𝑟𝑢𝑒 ⇒ 𝑓𝑎𝑙𝑠𝑒 ∨ 𝑡𝑟𝑢𝑒
 𝑡𝑟𝑢𝑒 ⇒ 𝑡𝑟𝑢𝑒⇔ 𝑡𝑟𝑢𝑒⇔
𝑆 ∨ 𝑇 𝑓𝑎𝑙𝑠𝑒 ∨ 𝑡𝑟𝑢𝑒
 𝑡𝑟𝑢𝑒⇔
𝑆 = 𝑓𝑎𝑙𝑠𝑒
𝑆 is not semantically entailed: 𝐾𝐵 ⊭ 𝑆.

Completeness (of Propositional Logic)
Definition. An inference system is complete if and only if for all knowledge bases 𝐾𝐵 and all 
sentences 𝜙,
𝐾𝐵 ⊨ 𝜙 ⇒ 𝐾𝐵 ⊢ 𝜙
(If 𝜙 is semantically entailed by 𝐾𝐵, then 𝜙 is derivable from 𝐾𝐵 using the inference rules.)
Completeness is a guarantee that our inference system can find all valid conclusions (i.e., no 
‘missing’ logical consequences).
Without a complete inference system, some valid conclusions might be unprovable (since we would 
miss important logical consequences).

Example: Not Complete
Suppose we have an inference system that only 
includes one inference rule: modus ponens.
From 𝑃 ⇒ 𝑄 and 𝑃, 
we can derive 𝑄.
𝑃 ⇒ 𝑄 ∧ 𝑃
𝑄
Consider a knowledge base 𝐾𝐵 = 𝑅 ∨ 𝑆, ~𝑅  with goal 𝑆.
We first perform a semantic check: 𝐾𝐵 ⊨ 𝑆.
𝑅 = 𝑡𝑟𝑢𝑒. Then, this is a  contradiction as 𝐾𝐵 ⊨ ~𝑅; 𝐾𝐵 cannot also entail 𝑅. 
𝑅 = 𝑓𝑎𝑙𝑠𝑒. Then, from 𝑅 ∨ 𝑆, we know 𝑆 must be true.
Definition [semantic entailment].
𝐾𝐵 ⊨ 𝑄 means “In every model 
where 𝐾𝐵 is true, 𝑄 is also true.”
Thus, 𝐾𝐵 ⊨ 𝑆.
Now, can we derive 𝑆? 𝐾𝐵 ⊢ 𝑆? Modus ponens requires a conditional format: 𝑃 ⇒ 𝑄. Our 
knowledge base does not have any clauses of this form.
Therefore, 𝐾𝐵 ⊬ 𝑆.
Thus, this inference system is not complete.

Theorem. Resolution for propositional logic is both sound and complete.

Theorem. If 𝐾𝐵 ∧ ~𝜙 ⊢⊥ by Resolution, then 𝐾𝐵 ⊨ 𝜙.
Proof. Suppose Resolution derives ⊥ from 𝐾𝐵 ∧ ~𝜙. 
Define two clauses 𝐶1 = 𝐿 ∨ 𝐴  and 𝐶2 = ~𝐿 ∨ 𝐵  that are both satisfiable and also let 𝑅 = 𝐴 ∨ 𝐵  be 
their resolvent.
Let 𝑀 be a model that satisfies both 𝐶1 and 𝐶2. Then 𝑀 must assign some truth value to 𝐿.
If 𝑀 𝐿 = 𝑓𝑎𝑙𝑠𝑒, then since 𝑀 satisfies 𝐶1 = 𝐿 ∨ 𝐴  , we must have 
𝑀 𝐴 =  𝑡𝑟𝑢𝑒, which again makes 𝑀 𝑅 = 𝑀 𝐴 ∨ 𝐵 = 𝑡𝑟𝑢𝑒.
First, we establish that the resolution rule is truth-preserving.
Therefore, 𝑅 is satisfiable whenever both parent clauses are satisfiable.
Since resolution preserves satisfiability, any clause derived through resolution can only be satisfiable if the 
original clauses are satisfiable. Therefore, if we derive ⊥ (the empty clause, which is always unsatisfiable), from 
𝐾𝐵 ∧ ~𝜙, this means 𝐾𝐵 ∧ ~𝜙 must be unsatisfiable.
That is, there is no model that makes both 𝐾𝐵  and ~𝜙 simultaneously true. Thus, in every model where 𝐾𝐵 is 
true, ~𝜙 must be false. Hence, 𝜙 must be true. It follows 𝐾𝐵 ⊨ 𝜙. ∎
Sound
If 𝑀 𝐿 =  𝑡𝑟𝑢𝑒, then since 𝑀 satisfies 𝐶2 = ~𝐿 ∨ 𝐵 , we must 
have 𝑀 𝐵 =  𝑡𝑟𝑢𝑒, which makes 𝑀 𝑅 = 𝑀 𝐴 ∨ 𝐵 = 𝑡𝑟𝑢𝑒.

Theorem. If 𝐾𝐵 ⊨ 𝜙, then Resolution derives ⊥ from  𝐾𝐵 ∧ ~𝜙.
Proof. Suppose 𝐾𝐵 ⊨ 𝜙. Then 𝐾𝐵 ∧ ~𝜙 is unsatisfiable.
Observe that for propositional logic there are finitely many distinct clauses. Thus, we know that 
Resolution terminates with a finite clause set 𝑆.
Therefore, Resolution must derive ⊥.∎
Since Resolution did not derive ⊥, the final clause set 𝑆 must be satisfiable. We therefore can construct 
a truth assignment that satisfies all clauses in 𝑆:
• For each propositional variable 𝑃, if there exists a unit clause 𝑃 in 𝑆, assign 𝑃 = 𝑡𝑟𝑢𝑒;
• If there exists a unit clause ~𝑃 in 𝑆, assign 𝑃 = 𝑓𝑎𝑙𝑠𝑒;
• Otherwise, assign 𝑃 arbitrarily.
Recall the Resolution procedure begins with 𝐾𝐵 ∧ ~𝜙. Since 𝑆 contains all clauses from the CNF 
conversion of 𝐾𝐵 ∧ ~𝜙 (as well as possibly other derived clauses), the truth assignment we 
constructed also satisfies 𝐾𝐵 ∧ ~𝜙. This is a contradiction.
Complete
Now, assume for the sake of contradiction that Resolution does not derive ⊥  from 𝐾𝐵 ∧ ~𝜙.

Summary (Again)
Soundness 𝐾𝐵 ⊢ 𝜙 ⇒ 𝐾𝐵 ⊨ 𝜙“Don't derive false conclusions.”
Completeness 𝐾𝐵 ⊨ 𝜙 ⇒ 𝐾𝐵 ⊢ 𝜙“Can derive all true conclusions .”
In practice:
Real-World Example:
No false negatives – the system will not miss valid conclusions.
Our Goal: Sound and Complete systems.
They ensure our AI is both trustworthy (no false conclusions) and comprehensive (no missed inferences).
If a patient actually has cancer (and this entailed by the 
symptoms), we want our system to identify it.
No false positives – the inference system will not “hallucinate” false conclusions.
If a medical diagnosis system says “a patient has cancer,” we 
want to be confident it is correct.
In practice:
Real-World Example:
```

## Uninformed Search

*Extracted from PDF: `2 Uninformed Search.pdf`*

```
Uniformed Search
Poppy is into it.

A Motivating Example
https://xkcd.com/1134/


Search Example: Jugs
5 2State Representation: 𝑓, 𝑡 = (#gallons in 5-gal, #gallons in 3-gal)
Given: 5-gallon jug and 2-gallon jug
Initial State: 5,0
Transitions:
𝑓, 𝑡 → 0, 𝑡Empty the 5-gallon jug
𝑓, 𝑡 → 𝑓, 0Empty the 2-gallon jug
𝑓, 2 → 𝑓 + 2,0 , where 𝑓 ≤ 3Pour 2-gallon jug into 5-gallon jug
𝑓, 0 → 𝑓 − 2,2  , where 𝑓 ≥ 2Pour 5-gallon jug into 2-gallon jug
1,0 → 0,1  Pour 1 gallon from 5-gallon jug into 2-gallon jug
Goal: Acquire 1 gallon Goal States: ∗, 1  or 1,∗ , where ∗ refers to any amount in the jug.
(These transitions imply you cannot measure or pour a specific amount of water from a jug.)

BFS Search of Jugs
5,0
0,0 5,0 3,2
T1
T2
T3
T4
T5 T1 T5
Redundant 
State
No water!
𝑓 = 5 ≰ 3
T2
T3 T4
0,2 3,0
T1 T2
5,0
Redundant 
State
T3
0,0
T2
2,0
T3
No water!
+ 
Redundant
Oscillation: 
Redundant 
States
0,0
T1
1,2
T4
No water!
+ 
Redundant
Does not apply

Search is Almost Everywhere in AI
Core Search Problems—These are 
fundamentally about exploring 
sequences of actions/choices to 
reach a goal state.
• Game Playing: How should I 
move my chess piece?
• Robotics: How should a robot 
navigate a room?
• Planning: How should I schedule 
tasks?
• Resource Allocation: How 
should I assign tasks to 
processors?
• Automated Theorem Proving: 
How do I prove this 
mathematical statement?
Hybrid/Search-Optional 
Problems—These can be solved 
with search or non-search 
methods. Modern approaches 
often blend techniques: search 
for exploration plus learning for 
evaluation.
• Computer Vision: How should 
I recognize objects in this 
image?
• Web Search: How should I 
rank these millions of pages?
• Recommendation Systems: 
What movie should I suggest 
next?
• Drug Discovery: Which 
molecular structure will treat 
this disease?
Search-Assisted Problems—
These primarily use other 
techniques (neural nets, 
statistical learning) but may 
incorporate search as a 
component.
• Natural Language: How 
should I parse this 
sentence? (May use a 
beam search.)
• Machine Learning: How 
should I find optimal 
parameters? (Gradient 
descent in ML.)

Formal Definition of Search
For:
𝑆: State space (set of all possible states) 𝑠0 ∈ 𝑆: Initial State
Actions 𝑠 : Set of legal actions in a state 𝑠
𝛿 𝑠, 𝑎 → 𝑠′ ∈ 𝑆: Transition function 𝛿 that applies action 𝑎 to state 𝑠 resulting in a state 𝑠′.
Goals ⊆ 𝑆: Set of goal states
𝑐 𝑠, 𝑎, 𝑠′ : an action cost function; cost of 𝛿 𝑠, 𝑎 → 𝑠′
𝑔 𝑛 = ෍
𝑖=1
depth 𝑛
𝑐 𝑠𝑖−1, 𝑎𝑖, 𝑠𝑖 for the path 𝑠0 → 𝑠1 → ⋯ → 𝑠𝑛
𝑎1 𝑎2 𝑎𝑛
A search algorithm finds a sequence of actions:
𝑎1, 𝑎2, … , 𝑎𝑛  such that 𝛿 … 𝛿 𝛿 𝑠0, 𝑎1 , 𝑎2 … , 𝑎𝑛 ∈ Goals
With a cost of:

Formal Search Compared to DFAs
Similarities
• Graph structure: Both work with states and 
transitions
• Path concepts: Finding paths through state space
• Goal-oriented:
• DFAs check acceptance,
• Search finds solutions
• State-action pairs:
• DFA transitions 𝛿 𝑞, 𝑎 → 𝑞′,
• Search transitions 𝑠, 𝑎 → 𝑠′
Key Differences
• Input vs. Choice:
• DFA reads string,
• Search chooses actions
• Determinism:
• DFA usually deterministic,
• Search often has multiple options
• Costs:
• DFA has no costs,
• Search often optimizes path cost
• Purpose:
• DFA recognizes ("Is string in language?"),
• Search constructs ("Find path to goal")
Search problems are like “interactive DFAs” where instead of passively 
consuming input, we actively choose actions to reach our goal states.

State Space (𝑆): 
Search Example: GPS Navigation
All possible locations
Some location (e.g., home)
A Mexican Restaurant
TurnLeft, TurnRight, GoStraight
Given a location, 𝑠, follow a 
direction to end up at 𝑠′
Travel time, distance, gas cost, 
environmental impact, etc.
Sequence of directionsSolution:
Initial State (𝛿):
Goal Set (Goals):
Actions(𝑠):
Transition function: 𝛿 𝑠, 𝑎 → 𝑠′
Path Cost:

State Space Graph
For a problem, a state space graph represents all 
possible states as nodes, with edges as legal 
actions between states.
Each edge has cost 𝑐 𝑠, 𝑎, 𝑠′ , and multiple paths 
may connect states. This graph captures the 
complete space search algorithms explore.
An optimal solution is the path from initial state 
to goal with minimum total cost—not 
necessarily the fewest actions. Some search 
algorithms guarantee finding optimal solutions; 
others do not.
The goal of search algorithms is to navigate the 
state space graph efficiently to find optimal (or 
acceptable) solution paths.
S A
G
B C
D
E
7
3
5
2
3
2
4
2
1
Paths to Goal:
S → A → G 5 + 3 = 8
Cost:
S → B → C  → G 2 + 2 + 7 = 11
S → A → C  → G 5 + 1 + 7 = 13
S → B → D  → E → C → G 2 + 4 + 3 + 2 + 7 = 18
Optimal means minimum 
cost, not fewest actions.

Search Trees
Each node represents a state
Each edge represents an action
Each path represents a sequence of actions
𝑠0
𝑠2𝑠1 … 𝑠𝑛𝑠3
𝑎1
𝑎2 𝑎3
𝑎𝑛
𝑎𝑖
𝑠𝑦𝑠𝑥 …
𝑎11
𝑎12
𝑎1𝑗
Given that the state space graph shows multiple paths to each state with different costs, search 
algorithms use a tree representation where each node tracks the complete path taken to reach that state.

Search by Environment Properties refers to what we know about the problem:
• Observability: Can we see the current state completely?
• Determinism: Do actions have predictable outcomes?
Types of Search Problems I: Environment Properties 
Types:
Single-State Problems (Fully observable, deterministic):
• 8-puzzle: See all tiles, moves are predictable
• Route planning: Know current location, roads are fixed
Multiple-State Problems (Partially observable, deterministic):
• Robot localization: Limited sensors, do not know exact position
• Sensorless planning: Robot vacuum with no position sensors
Contingency Problems (Observable, nondeterministic):
• Medical diagnosis: Can observe symptoms, treatment outcomes uncertain
• Game against opponent: See game state, opponent's moves unpredictable
Exploration Problems (Unknown state space):
• Mars rover navigation: Don't know terrain beforehand
• Web crawling: Discover links as you go

Types of Search Problems II: Objective
Search By Objective refers to what type of 
solution we want:
• Any valid solution vs. the best solution
• One answer vs. exploring all possibilities
• Final answer vs. improving answers over 
time
Types:
Finding Any Solution:
• Maze solving: Any path to exit
• Satisfiability (SAT): Any assignment that satisfies clauses
• Scheduling: Any valid assignment of tasks to resources
Finding Optimal Solution:
• Shortest path: GPS navigation finding fastest route
• Traveling salesman: Minimum-cost tour visiting all cities
• Resource allocation: Minimum cost assignment
State-Space Search vs. Path-Cost Search:
• Some problems care about reaching goal states (puzzles)
• Others care about path taken (navigation, planning 
sequences)
Single Solution vs. All Solutions:
• Chess: Find one good move
• Constraint satisfaction: Sometimes need all valid 
solutions
• Game tree analysis: Explore all possible outcomes

Uninformed Search (Blind Search)
• No problem-specific knowledge 
beyond definition
• Only knows actions, goal test, and 
action costs
Search Strategies
BFS: Explore level by level
DFS: Go deep first, backtrack when stuck
Uniform Cost Search: Always expand lowest-cost path
A*: Combines actual cost + estimated remaining cost
Greedy Best-First: Always move toward seemingly 
closest goal
Hill Climbing: Always take the best local step
Informed Search (Heuristic Search)
• Uses problem-specific knowledge 
(heuristic function)
• Estimates “goodness” of states
Some search algorithms are like exploring a new city without a map (systematic but blind), while
others are like having a compass pointing toward your destination (guided exploration).

Tree Search:
• Generates nodes without checking for duplicates
• Can visit same state multiple times
• Simpler implementation
Tree Search vs. Graph Search
Graph Search:
• Maintains explored set to avoid repeated states
• More efficient for state spaces with many paths to 
same state
• Higher memory requirements
A
B C
D A DF B
TS: Duplicate visits possible. GS: visit each state once
Which approach would you use?
Infinite state space?
(Like a forgetful housekeeper who cleans 
the same room multiple times.) (Like checking off rooms on a list as you clean them.)
Graph Search - prevents revisiting same locations
Graph Search - avoids revisiting solved positions
Depends - Graph search if cycles exist, Tree search if linear paths
Tree Search - unknown if cycles exist, save memory
8-puzzle (many paths to same state)?
Exploring unknown territory?
Robot navigation in known environment?

The Frontier in Search
Definition. The frontier (sometimes called fringe) is the 
set of all nodes that have been identified but not yet 
expanded in a search algorithm: leaf nodes in a search 
tree.
(It represents a “boundary” between explored 
and unexplored parts of the search tree.)
frontier

The General Search Algorithm
# Generic search algorithm
frontier = [initial_state]
explored = set()
while frontier:
    node = frontier.pop()     # Central component to Search
    if goal_test(node.state): return node   
    explored.add(node.state)
   for action in actions(node.state):
       child = child_node(node, action)
        if child.state not in explored and child not in frontier:
            frontier.add(child)
Data structure determines the search strategy

BFS
Goal
BFS: Expand the shallowest node first
• Examine states one step away from the initial states
• Examine states two steps away from the initial states
• … rippling outward
BFS: Frontier = FIFO queue
# Generic search algorithm
frontier = [initial_state]
explored = set()
while frontier:
    node = frontier.pop() # Central component to Search
    if goal_test(node.state): return node   
    explored.add(node.state)
   for action in actions(node.state):
       child = child_node(node, action)
        if child.state not in explored and child not in frontier:
            frontier.add(child) We need back pointers to 
recover the solution path.

Performance
Completeness: Does the algorithm guarantee finding a solution if one exists? 
(Not necessarily finding all solutions.)
Four measures of search algorithms:
Optimality: Does it find the best solution?
Time complexity: How runtime scales with problem size.
Space complexity: How much memory is required.

BFS Performance
• Back pointers for generated nodes: 𝑂 𝑏𝑑
• Queue / fringe: smaller, but still 𝑂 𝑏𝑑
Completeness: Does the algorithm guarantee finding a solution if one exists?
Optimality: Does it find the best solution?
Time complexity Space complexity
Yes.
Yes, if edges are positive and monotonically increasing in 
depth: 
𝑐𝑜𝑠𝑡(𝑝𝑎𝑡ℎ 𝑡𝑜 𝑑𝑒𝑝𝑡ℎ 𝑑)  ≤  𝑐𝑜𝑠𝑡(𝑝𝑎𝑡ℎ 𝑡𝑜 𝑑𝑒𝑝𝑡ℎ 𝑑 + 1).
Otherwise, no.
Worst case: goal is the last node at radius (depth) 𝑑.
• Explore all nodes up to and at radius 𝑑:
1 + 𝑏 + 𝑏2 + 𝑏3 + ⋯ + 𝑏𝑑 = 1 1 − 𝑏𝑑+1
1 − 𝑏 ∈ 𝑂 𝑏𝑑 (bad)
where 𝑏 is the branching factor.

# Generic search algorithm
frontier = [initial_state]
explored = set()
while frontier:
    node = frontier.pop() # Central component to Search
    if goal_test(node.state): return node   
    explored.add(node.state)
   for action in actions(node.state):
       child = child_node(node, action)
        if child.state not in explored and child not in frontier:
            frontier.add(child)
DFS
BFS: Expand the deepest node first
• Select a direction. Go deep until the end.
• Slightly change the end.
• Slightly change the end some more… fanning outward
DFS: Frontier = LIFO stack
Goal

DFS Fringe
Goal
BFS space + time: 𝑂 𝑏𝑑
Let 𝑚 be the maximum depth of the graph from Start.
Space complexity 𝑚 ⋅ 𝑏 − 1 ∈ 𝑂 𝑚𝑏
• The current path (up to depth 𝑚)
• The siblings of nodes along that path (up to 𝑏 
per level)
• With backtracking using the system stack, we 
do not explicitly use back-pointers.
Time complexity For a finite tree, we 
may visit all nodes: 𝑂 𝑏𝑚

The Problem with DFS
Finite tree:
Goal
Goal
Complete
Optimal
Yes.
No. Stops when the first goal is 
reached which is not 
guaranteed to be the best.
Infinite tree:
Complete
Optimal
No. May explore infinitely without 
backtracking toward solution.
No.
BFS

Questions
You need to search a randomly generated state space graph 
with one goal, uniform edge costs, depth of goal 𝑑 = 2, and 
maximum graph depth 𝑚 = 100. Considering worst-case 
performance, would you choose BFS or DFS for your search?
DFS could waste enormous time 
exploring deep, irrelevant paths: the 
goal is very shallow (𝑑 = 2) compared 
to maximum depth (𝑚 = 100).
You need to search a randomly generated state space graph 
with one goal, uniform edge costs, goal depth 𝑑 = 95, and 
maximum graph depth 𝑚 = 100. The branching factor is 
very large (𝑏 = 1000). Considering worst-case behavior, 
would you choose BFS or DFS for your search?
BFS is computationally infeasible:
Space complexity: 𝑂 100095
Time complexity: 𝑂 100095
BFS
DFS

Uniform-Cost Search (UCS)
• Expand the least-cost node first
• Use a priority queue to take the least-cost item This sounds familiar.
Suppose we have a graph in which each node has a path cost (i.e., sum of edge costs along the path) from the start 
node. We want to find a least-cost path to a goal.
UCS and Dijkstra Similarities:
• Explore nodes in order of 
lowest cumulative cost.
• Use priority queues for 
minimum-cost selection
• Guarantee optimal paths
Differences
Dijkstra's Algorithm Uniform Cost Search
Implementation Pre-load all vertices 
in priority queue
Lazy insertion - add nodes 
dynamically
Memory Usage Stores entire graph 
upfront
Memory-efficient, on-
demand generation
UCS is ideal for AI search problems with large or dynamically 
generated state spaces that cannot be fully stored in memory.

Example
Start: S
Goal: G 
2
S
G
5
A
D
CB
4
E
7
2 8 4 5
Consider successor nodes from 
left to right when there is a tie.
PQ
S A E B D C G S B G
S, 0
A, 2 B, 5 C, 7
D, 6 E, 4 G, 10
G, 9
Removed
S
A
E
B
D
C
G
Nodes visited: Path:

Uniform-Cost Search
Let:
• 𝐶∗ be the cost of the least-cost goal node.
• 𝜖 be the minimum edge cost in the graph: 𝑒𝑑𝑔𝑒-𝑐𝑜𝑠𝑡𝑠 ≥ 𝜖 >  0
Space complexityTime complexity 𝑂 𝑏 Τ𝐶∗ 𝜖
Complete?
Optimal?
Yes.
Yes.
𝑂 𝑏 Τ𝐶∗ 𝜖
In the worst-case, UCS may need to explore paths that use many small-cost 
edges. That is, to accumulate cost 𝐶∗ using only a minimum-cost number of 
edges 𝜖, we need 
𝐶∗
𝜖  edges:
𝐶∗ = 𝜖 ⋅ 𝑛𝑢𝑚(𝑒𝑑𝑔𝑒𝑠) 𝑛𝑢𝑚(𝑒𝑑𝑔𝑒𝑠) = 𝐶∗
𝜖 ⇔ 
UCS expands nodes by 
cost, not depth, and may 
follow deep low-cost paths 
before reaching a shorter 
but costlier goal path.
1
1
S G
4
A
B C
D
1
1
1
UCS may explore all nodes up to depth Τ𝐶∗
𝜖:
1 + 𝑏 + 𝑏2 + 𝑏3 + ⋯ + 𝑏 Τ𝐶∗ 𝜖 ∈ 𝑂 𝑏 Τ𝐶∗ 𝜖

Performance Measures for Search
Complexity
• 𝑏: Branching factor (maximum actions per state)
• 𝑑: Depth of shallowest goal node
• 𝑚: Maximum path length in state space
Most algorithms have 
exponential complexity.
Algorithm Time Space Optimal? Complete?
BFS O 𝑏𝑑 O 𝑏𝑑 Yes* Yes
DFS O 𝑏𝑚 O 𝑏𝑚 No No
UCS O 𝑏𝐶/𝜖 O 𝑏𝐶/𝜖 Yes Yes, assuming 𝜖 > 0
Since no search algorithm excels in all measures of time, space, and optimality, choose based on problem-specific 
constraints and priorities.
Completeness Does it always find a solution if one exists?
Optimality Does it find a least-cost solution?
Time Complexity Number of nodes generated/expanded
Space Complexity Maximum memory needed
* Positive, monotonically 
increasing edge weights.

Why can we not always do brute-force exhaustive search?
Questions to Consider
Efficient search needs heuristics estimating goal distance, domain knowledge, cost estimates, and 
constraint information - motivating informed search algorithms like A*.
Problems become exponentially harder with high branching factors, deep solutions, massive state 
spaces (like chess), and absence of good heuristics to guide search.
What makes some search problems exponentially harder?
Exhaustive search fails due to exponential growth 𝑂 𝑏𝑑 , memory constraints, prohibitive time 
requirements, and the fact that finding any good solution often suffices.
When might DFS be preferred over BFS?
Balancing quality versus resources involves choosing appropriate algorithms, setting time/memory 
limits, applying heuristics, and accepting suboptimal solutions when necessary.
How do we balance solution quality vs. computational resources?
What information would help guide our search efficiently?
DFS is preferred when memory is limited (𝑂 𝑏𝑚  vs. 𝑂 𝑏𝑑 ), solutions are likely deep, any solution 
suffices, or cycles are unlikely in tree-structured problems.

Depth-Limited Search (DLS)
What is the problem with DFS?
Infinite state spaces
Solution? Define a depth limit (ℓ) in which 
nodes beyond depth ℓ are not expanded.
What is the problem with depth-limited DFS?
Incomplete if 𝑑𝑒𝑝𝑡ℎ(𝑔𝑜𝑎𝑙) > ℓ.
Space complexity
Time complexity
𝑂 𝑏ℓ
𝑂 𝑏ℓ
Observe, DLS ≡ DFS when ℓ = ∞.
What if we iterate by increasing the value of ℓ? 
S
G
ℓ
1
𝑑𝑒𝑝𝑡ℎ = 0
2
…

Iterative Deepening
What if we had the best of DFS and BFS?
Memory Efficiency of DFS: stores only 
current path in memory thus linear 
space complexity 𝑂 𝑏𝑑 .
Completeness guarantee of BFS: 
systematically explores all depths and will 
not get stuck in infinite paths.
Problem? What about all the redundancy in which we revisit nodes?

IDS: Mathematically Reasonable Redundancy
Iterative deepening performs depth-limited searches with limits 0, 1, 2, … , 𝑑.
A node at depth 𝑗 will be visited each iteration from 𝑗 to 𝑑: exactly 𝑑 −  𝑗 +  1 times.
Therefore, the total number of node visits for IDS is given by:
𝑁 𝐼𝐷𝑆 = 𝑏0 ⋅ 𝑑 + 1 + 𝑏1 ⋅ 𝑑 + 𝑏2 ⋅ 𝑑 − 1 + ⋯ + 𝑏𝑑
𝑁 𝑛𝑜𝑑𝑒𝑠 𝑢𝑝 𝑡𝑜 𝑑𝑒𝑝𝑡ℎ 𝑑 = 𝑏0 + 𝑏1 + ⋯ + 𝑏𝑑−2 + 𝑏𝑑−1 =
𝑏𝑑−1
𝑏−1 ∈ 𝑂 𝑏𝑑
With exponential expansion, the deepest level dominates the computation:Intuition.
∈ 𝑂 𝑏𝑑
Asymptotically, the redundant work at shallow levels becomes 
insignificant compared to the work done at the target depth. So IDS is 𝑂 𝑏𝑑 ; same as BFS.
Iterative deepening is the preferred uninformed search method when the search state 
space is larger than can fit in memory and the depth of the solution is not known.
Suppose 𝑑 = 5.
A node at depth 𝑗 = 2 
appears in searches with 
limits 2, 3, 4, 5 → 4 times.

Example: Nodes Expanded by Search
Start: S
Goal: G 
2
S
G
5
A
D
CB
4
E
7
2 8 4 5
(UCS is the only uninformed 
search that worries about costs.)
Consider successor nodes from 
left to right when there is a tie.
Search Nodes Visited Solution Found
BFS S A B C D E G S A G
DFS S A D E G S A G
IDS S S A B C S A D E G S A G
UCS S A E B D C G S B G
What nodes are visited and what solutions are found by the search technique?
```

## Informed Search

*Extracted from PDF: `3 Informed Search.pdf`*

```
Informed Search

Uniformed Search vs. Informed Search
goal
𝒈 𝒏
start 𝑛
𝒉 𝒏
What we know with uninformed search:
• 𝒈 𝒏 : path cost from start to state 𝑛.
• Successor states
With Informed search, we know:
• All properties from uninformed search
• 𝒉 𝒏 : a heuristic path cost from 𝑛 to the goal.
What if we had some guidance 
about which direction to search?

Using the Heuristic
goal
𝒈 𝒏
start 𝑛
𝒉 𝒏′
Recall with uniform-cost search:
• We store potential next states with a priority queue
• Expand the state with the smallest “first-half-cost”: 𝒈 𝒏 𝒉 𝒏  is a “second-half-cost”
How can we use 𝒉 𝒏 ?
𝑛′′
𝑛′
𝒉 𝒏′′
𝒄𝒐𝒔𝒕 𝒏, 𝒏′′
Goal: speed up search using 
domain knowledge.

How does UCS proceed?
Problem: Visit too many nodes, some clearly out of the question.
Visualizing UCS vs. A*
A Classic Example
Straight-line Distances to Bucharest
Recall, it minimizes 𝒈 𝒏 .

Straight-line Distances to Bucharest
Approach: Choose smallest ℎ 𝑛
Arad → Sibiu → Rimnicu Vilcea → Pitesti
Attempt: Greedy Best-First


Greedy Best-First
Explore the grid expanding node 
with shortest distance to goal.Complete?
Optimal?
Start
 Goal
Optimal path
*assuming no cycles
Issue: Greedy Best-First ignores path 
gets lured by promising ℎ 𝑛  heuristic 
values and does not account for cost 
to reach those nodes: 𝑔 𝑛 .

Approach: Expand smallest 𝑔 𝑛 + ℎ 𝑛
A* Search By Example
Straight-line Distances to Bucharest
140 + 253 = 393
75 + 374 = 449
118 + 329 = 447
239 + 176 = 415
220 + 193 = 413
366 + 160 = 526
317 + 100 = 417
418 + 0 = 418
455 + 160 = 615
450 + 0 = 450

Node ℎ(𝑥)
S 7
A 3
B 4
C 8
D 4
E 3
F 2
G 0
Quick Example
𝑆
A B C
For A* choose minimal 𝑓(𝑛) = 𝑔 𝑛 + ℎ 𝑛
4 + 3 = 7 3 + 4 = 7 7 + 8 = 15
G
8 + 0 = 8
C D
5 + 8 = 13 4 + 4 = 8
E
6 + 3 = 9


Heuristic Properties: A Roadmap
Admissibility → Ensures A* finds optimal solutions 
Without this, A* may return suboptimal paths
A* is only as good as its heuristic. But what makes a “good” heuristic?
Goal: Design / select heuristics that make A* both optimal and efficient.
We consider three key properties of heuristics:
Dominance → Helps us choose between multiple admissible heuristics 
Given several valid heuristics, which one performs best?
Consistency → Enables more efficient search 
Allows A* to avoid redundant work

Admissible (Global) Heuristics
Under what conditions is A* guaranteed to find optimal solutions?
Interpretation: ℎ 𝑛  is admissible if it never overestimates the cost to reach the destination node.
Definition. Heuristic ℎ 𝑛  is admissible if:
0 ≤ ℎ 𝑛 ≤ ℎ∗ 𝑛 for all 𝑛 where ℎ∗ 𝑛  is the true cost from 𝑛 to goal.
Examples:
Straight-line distance for route finding
Manhattan distance for grid worlds
Number of misplaced tiles for 8-puzzle
Minimum Spanning Tree in the Traveling Salesperson problem.
Number of attacking pairs: in the 8-Queens problem.
Max(horizontal distance, vertical distance)
Random numbers
Actual driving time (overestimates driving 
distance)
Examples?


A* Proof of Optimality
Theorem. A*, with admissible heuristic, will find an optimal solution.
Proof by Contradiction.
Then some first node 𝑛 on the optimal path remains unexpanded with 𝑓(𝑛) ≥ 𝑪 > 𝐶∗ (otherwise A* 
would have expanded 𝑛 before the suboptimal goal.
Suppose the optimal path has cost 𝐶∗, but A* returns a suboptimal 
path with cost 𝑪 > 𝐶∗.
Recall, 𝑓 𝑛  is the path cost through 𝑛 to 
a goal (and how A* decides which node to expand next).
𝑓 𝑛 = 𝑔 𝑛 + ℎ 𝑛
= 𝑔∗ 𝑛 + ℎ 𝑛 Since 𝑛 is on an optimal path
≤ 𝑔∗ 𝑛 + ℎ∗ 𝑛 Admissability: ℎ 𝑛 ≤ ℎ∗ 𝑛  
= 𝐶∗ By definition, 𝐶∗ = 𝑔∗ 𝑛 + ℎ∗ 𝑛
However, our assumption was 𝑓 𝑛 > 𝐶∗. 
Contradiction.
Let 𝑔∗ 𝑛  be the cost of the optimal path from start to 𝑛 and ℎ∗ 𝑛  be the cost of the optimal path 
from 𝑛 to the goal.
𝒈∗ 𝒏
𝑆 𝑛
𝒉∗ 𝒏
… 𝐺…
Optimal path: 𝐶∗ = 𝑔∗ 𝑛 + ℎ∗ 𝑛
Suboptimal path: 𝑪 > 𝐶∗
𝑝
…

Put the start state 𝑆 on the priority queue called OPEN.
Repeat until OPEN is empty,
 Remove from OPEN and add to CLOSED a node 𝑛 for which 𝑓 𝑛 = 𝑔 𝑛 + ℎ 𝑛 is minimum.
 If 𝑛 is a goal node
  Exit (recover path by tracing back pointers from 𝑛 to 𝑆)
 Expand 𝑛, generating all successors and attach to pointers back to 𝑛.
 For each successor 𝑛′ of 𝑛:
 If 𝑛′ is not already on OPEN or CLOSED:  # New node found
ℎ 𝑛′ = 𝑐𝑜𝑚𝑝𝑢𝑡𝑒 𝑛′, 𝑔𝑜𝑎𝑙
𝑔 𝑛′ = 𝑔 𝑛 + 𝑐 𝑛, 𝑛′
𝑓 𝑛′ = 𝑔 𝑛′ + ℎ 𝑛′
 Place 𝑛′ on OPEN.
 Else If 𝑛′ is already on OPEN or CLOSED:
If 𝑔(𝑛′) is lower for the new version of 𝑛′.
Redirect pointers backward from 𝑛′ along path yielding lower 𝑔(𝑛′).
If (𝑛′ is already on OPEN) then update 𝑛′ on OPEN;
else add 𝑛′ to OPEN
Exit with failure
States already expanded
Full A* Algorithm

Heuristic Dominance
We have considered how different algorithms trade off optimality, completeness, and efficiency. But 
how can we evaluate the effectiveness of our heuristic?
That is, if we are using A*, how do we choose between different admissible heuristics?
Definition. Heuristic ℎ2 is said to dominate heuristic ℎ1 if both ℎ1 and ℎ2 are admissible 
and for all nodes 𝑛:
ℎ1 𝑛 ≤ ℎ2 𝑛
Recall, admissible heuristics are always optimistic 
(underestimate true cost):
ℎ1 𝑛 ≤ ℎ2 𝑛 ≤ ℎ3 𝑛 ≤ ⋯ ≤ ℎ∗ 𝑛
where ℎ∗ 𝑛  is the true optimal cost to goal.
Having dominant heuristics is important!
More accurate estimates → better guidance → fewer wrong paths explored
→ a dominating heuristic gives us estimates closer 
to the real costs (that are still admissible).

Heuristic Dominance: Example
8-puzzle: may only slide tiles into the 
empty space (no jumping or diagonal 
moves).
Example State: 𝑛
1 2 3
4 5 6
7 8
Goal State
Challenge: Find the minimum sequence 
of moves to reach the goal state from 
any given starting configuration.
3 1 2
7 5 6
8 4
ℎ1: (Misplaced tiles): Count tiles not in goal 
position
ℎ2: (Manhattan distance): Sum of distances each 
tile must move
ℎ3: (Manhattan + Linear Conflict):
Manhattan distance + 2 ⋅ number of linear conflicts
Two tiles are 
in linear 
conflict if:
• They are in the correct row/column.
• A pairwise comparison indicates they are not in 
correct relative order.
• Each conflict adds 2 to the heuristic indicating the 
minimum moves needed to resolve the conflict.
ℎ1 𝑛 = 1 + 1 + 1 + 1 + 0 + 0 + 1 + 1 = 6
ℎ2 𝑛 = 1 + 1 + 2 + 1 + 0 + 0 + 1 + 2 = 8
ℎ3 𝑛 = 8 + 2 ⋅ 𝑟𝑜𝑤1 + 𝑟𝑜𝑤2 + 𝑟𝑜𝑤3 + 𝑐𝑜𝑙1 + 𝑐𝑜𝑙2 + 𝑐𝑜𝑙3
= 8 + 2 ⋅ 1 + 1 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0 + 0
= 12 (Observe no column conflicts here: multiple tiles in 
each column are in the goal column but out of order.)
ℎ3 provides the tightest estimate (6 ≤
9 ≤ 12), meaning A* with ℎ3 would 
expand fewer nodes and reach the goal 
more efficiently than with ℎ2 or ℎ1.

From Admissible to Consistent
Admissibility
Consistency
A global promise about the goal
Never overestimate the cost to reach the goal.
But this says nothing about the journey along the way...
What if we made a promise about every single step?

A graph-search (without reopening) generates an optimal 
solution if ℎ(𝑛) is a consistent:
▪ ℎ(𝑛) is consistent (or monotonic) if for every node 𝑛 
and for every successor node 𝑛′ of 𝑛:
𝑛
𝑛’
𝑑
ℎ(𝑛)
𝑐(𝑛, 𝑛’) ℎ(𝑛’)
ℎ(𝑛) is consistent → ℎ(𝑛) is admissible
Consistency (Local Optimism)
(This is a form of triangle inequality.)
Example. Euclidean distance heuristic.
It represents the shortest possible path between two points, so the direct distance to the goal is always less than 
or equal to any indirect route through neighboring nodes.
With a consistent heuristic, the first time we reach a state, it will be on the optimal path. So we never have to re-
add a state to the frontier (or check the CLOSED list).
(An inconsistent heuristic may end up with multiple paths reaching the same state.)
ℎ(𝑛) ≤ 𝑐(𝑛, 𝑛’) + ℎ(𝑛’)

Inconsistent Example
Now imagine you are at Furman main entrance with 12 miles using surface roads to your 
destination: Cook Out.
You drive 2 miles to reach Timmons gate. From the Timmons gate, GPS discovered a more 
direct highway access that significantly shortens the remaining distance to Cook Out (only 
8 miles left).
ℎ(𝑛) ≤ 𝑐(𝑛, 𝑛’) + ℎ(𝑛’)
Consider a situation where your GPS estimates distance to destination based on old road information.
𝑀 𝐶𝑂
𝑇
𝟏𝟐
𝟖𝟐
Do we have consistency? 12 ≤ 2 + 8
?
No.

A* Optimality
Tree-search has no CLOSED list, allowing the same state to be expanded multiple times via different paths. 
Inefficient, but guarantees finding the optimal solution with any admissible heuristic.
Graph-search with reopening maintains CLOSED but checks it for cheaper paths. If found, it updates costs and re-
opens the node. This safety net means admissibility alone suffices.
Graph-search without reopening skips CLOSED nodes entirely, assuming the first path found is optimal. This is only 
true with a consistent heuristic, which ensures 𝑓-values never decrease along any path.
A* Version Requirement for Optimality Notes
Tree-search Admissible heuristic No CLOSED list—can re-expand 
states.
Graph-search with reopening Admissible heuristic Checks CLOSED nodes for 
cheaper paths.
Graph-search without reopening Consistent heuristic Skips CLOSED nodes entirely.
Bottom line: Consistency enables efficiency; no reopening is needed when you are guaranteed 
the first path is best.

A* Avoids the Best-First Trap
Start
 Goal

Brief A* Analysis
Time complexity:
Space complexity:
𝑂 𝑏𝑑 where:
• 𝑏 is the branching factor and
• 𝑑 the depth of the optimal solution.
However, with a good heuristic, A* can, in practice, be 𝑂 𝑏𝜖⋅𝑑  
where 0 < 𝜖 < 1 represents how much the heuristic can reduce 
the search space.
𝑂 𝑏𝑑
A* consumes lots of memory: 𝑂 #𝑠𝑡𝑎𝑡𝑒𝑠  (OPEN, CLOSED, back-pointers). Thus, 
may run out on large problems.
If the heuristic can be consistent, we earn space efficiency by not re-adding nodes 
to the open list (by re-opening CLOSED nodes).

IDA*
IDA*: incrementally increasing the maximum 𝑓-value 𝑓 𝑛 = 𝑔 𝑛 + ℎ 𝑛
We have encountered the problem of running out of memory before. Our solution to meld 
BFS and DFS was iterative deepening.
Time complexity:
Space complexity:
𝑂 𝑏𝑑 where:
• 𝑏 is the branching factor and
• 𝑑 the depth of the optimal solution.
𝑂 𝑏𝑑
Complete?
Optimal?
with an admissible heuristic.
(Just as A*)
stores path like DFS, but re-explores.

Beam Search
A* is optimal but uses exponential memory. IDA* is memory efficient but may re-explore nodes. What 
if we need something in between?
Complete?
Optimal?
Motivation: Reduce memory usage by limiting frontier size while allowing our heuristic to guide us.
Local Beam Search
• The frontier is a priority queue with fixed size beam width 𝑘.
• Expand all 𝑘 nodes simultaneously
• Keep best 𝑘 successors for next iteration
Stochastic Beam Search
• Beam width 𝑘
• Selection of 𝑘 successors is 
probabilistic.
• All successors are assigned 
probabilities based on 
‘goodness’.
• 𝑘 are then selected according 
to that distribution.
• Helps avoid getting trapped in local 
minima by introducing randomness 
into node selection
Can discard (optimal) paths by 
keeping only locally promising nodes
Space?
Time?
𝑂 𝑘
𝑂 𝑘 ⋅ 𝑑

Beyond Optimal Search: Weighted A*
What if optimality is not worth the computational cost? Sometimes “good enough” solutions found 
quickly are better than optimal solutions found slowly.
Weight 𝑤 is a tunable parameter that can emphasize the heuristic more heavily:
• 𝑤 = 1 : balanced between actual cost 𝑔 𝑛  and heuristic ℎ 𝑛
• 𝑤 → ∞: making search more "optimistic" about reaching the goal by emphasizing ℎ 𝑛
Weighted A*: 𝑓 𝑛 = 𝑔 𝑛 + 𝑤 ⋅ ℎ 𝑛 where 𝑤 > 1
Standard A*
Greedy Best-First
Complete?
Optimal?
Best-First and A* are complete; we are still using an admissible heuristic.
Space?
Time?
𝑂 𝑏𝑑
𝑂 𝑏𝑑
Solution cost is guaranteed to be ≤ 𝑤 ⋅ 𝐶∗where C* is optimal cost
Often faster than A* in practice.
Used in real-time systems, video games, robotics.
Often expands significantly fewer nodes in practice as 𝑤 increases.

Beyond Optimal Search: Anytime Algorithms
What if we do not know how much time we have to search?
Games, online planning, real-time decision making
Idea:
• Start with a quick, possibly suboptimal solution
• Improve solution quality over time if more time is available
• Stop anytime and return current best solution
• Graceful degradation: longer time → better solutions
Common in game environments due to issues with frame rate.
Goal: Always have 
some answer ready.
Properties
• Interruptible: Can stop and return solution at any time
• Monotonic improvement: Solution quality never decreases
• Diminishing returns: Biggest improvements happen early
Anytime A* Approaches
• With Weighted A*, start with high 𝑤, gradually reduce
• Iterative deepening with increasing time/space limits
• For beam search, increase beam width over time

Practical Consideration: When To Use?
Algorithm When to Use
Greedy Best-First
• Quick approximate solutions
• Good heuristic available
• Optimality not important
A*
• Need optimal solution
• Have good admissible heuristic
• Memory is available
IDA*
• Need optimal solution
• Memory is limited
• Heuristic is good (low branching factor)
Beam Search
• Large search spaces
• Optimal solution not required
• Time/memory constraints
Anytime Algorithms
• Uncertain time constraints
• Need solution quickly, improve if time allows
• Real-time systems (games, robotics)
```

## First-Order Logic

*Extracted from PDF: `4 First-Order Logic.pdf`*

```
First-Order Logic

Going Beyond Propositional Logic I
We explored Propositional Logic (PL). It allowed us to represent and reason about facts that 
are either true or false. It is powerful for modeling simple boolean scenarios (e.g., whether a 
light is on or off or whether a person is present or absent), but what if we want to express 
more nuanced ideas:
• If a person is a student, then 
they have an advisor.
• Some professors teach 
multiple courses.
• Every student in the class 
submitted the assignment.
PL cannot handle variables or object properties. We would need 
a rule like Student(x) ⇒ HasAdvisor(x).
PL cannot represent relationships between objects (e.g., 
professors and courses). We need a predicate like 
Teaches(ProfX, CourseY).
PL lacks quantifiers: ‘every’. We would need a separate 
proposition for each student (e.g., Submitted_Alice, 
Submitted_Bob). This does not scale or generalize.

First-Order Logic
First-Order Logic (FOL) is a formal system for representing knowledge and reasoning about 
objects, their properties, and relationships between them.
Properties
• More expressive than 
propositional logic
• Uses variables, predicates, and 
quantifiers
Capabilities
• Foundation for knowledge 
representation in AI
• Enables reasoning about infinite 
domains
First-Order Logic is sometimes refered to as Predicate Logic or Predicate Calculus.

Syntax: Terms
Definition. A term represents an object in the domain.
Functions: computed objects (map 
objects to objects)
Variables: placeholders for objects
Constants: specific objects
The father of John
The result of 2 + 3
The left leg of 𝑥
𝑥, 𝑦, 𝑝𝑒𝑟𝑠𝑜𝑛, 𝑛𝑢𝑚𝑏𝑒𝑟
John, 42, Alice, 2, Madison, Green
Types Examples
Father(John)
Plus(2,3)
LeftLeg(𝑥)
Definition. A ground term is a term with no variables.

Terms vs Sentences
Terms
Refer to objects in the domain:
Terms are not true or false, they 
just name objects
John
42
Father(John)
𝑥
a specific person
a specific number
John’s father (a person)
any object (placeholder)
Sentences
Sentences make claims that can be 
evaluated as true / false.
Sentences are true / false: they 
make assertions.
Student(Alice)
Tall(John)
Loves(Jesse, Jordan)
Is Alice a student?
Is John tall?
Does Jesse love Jordan?
Does every 
student have 
a laptop?
∀𝑥 Student(𝑥) ⇒ HasLaptop(𝑥)
Father(John) Tall(Father(John))refers to someone. claims something.

Distinguishing Functions from Predicates
Note, functions appear inside predicates:
In FOL, predicates and functions use the same syntax (Symbol(arg₁, arg₂, ...)), creating 
potential ambiguity: Father(John) might be a function (term) or predicate (sentence) depending on 
how Father is defined, whereas IsFather(John) is clearly a predicate.
Context and declaration are needed to disambiguate.
PredicateFunction
Father(John) Returns John's father.
Tall(Father(John)) Is the father of John tall? IsFather(John) Is John a father?
IsFather(John) ∧ Doctor(John)
Compound claim: Is John a 
father and is John a doctor?
Tall(Father(John))
No. Father(John) is not a sentence.Is Father(John) ∧ Doctor(John) 
a valid compound sentence?
You might write: ∃𝑥 (𝑥 = Father(John) ∧ Doctor(𝑥))

Syntax: Atomic Sentences
Intuitive Definition. An atomic sentence is the simplest sentence in FOL:
𝑃 𝑡1, 𝑡2 , … , 𝑡n
𝑃 is a predicate symbol and each 𝑡ᵢ is a term.
Arity refers to the number of arguments a predicate takes.
Unary Tall(John) Property of an object
Binary Loves(Alice, Bob) - Relation between two objects
Ternary Between(Madison, Chicago, Milwaukee) Relation among three objects
𝒏-ary Grade(Alice, CSC-343, Fall, 2026, A, …) In general, predicates can take any 
number of arguments
Atomic sentences make a single assertion without logical connectives (∧, ∨, ¬, ⇒) or quantifiers (∀, ∃), 
and can be evaluated as true or false.  
Why can 𝑃 not be a function?

Syntax: Complex Sentences (Quantifiers)
Logical Connectives (same interpretation as with propositional logic)
Quantified Statements
Not: ~𝜙
And: 𝜙 ∧ 𝜓
Or: 𝜙 ∨  𝜓
Implies: 𝜙 ⇒ 𝜓
Iff: 𝜙 ⇔ 𝜓
Universal (∀): Statement holds for all objects Existential (∃): Statement holds for at least one object
∀𝑥 Student 𝑥 ⇒ HasLaptop 𝑥
All students have a laptop.
∃𝑥 Student 𝑥 ∧ GPA 𝑥, 4.0
Some student has a 4.0 GPA
All CS majors must take CSC-223.
∃𝑥 Student 𝑥 ∧ Equals GPA 𝑥 , 4.0
Some student has a 4.0 GPA
∀𝑥 CS_Major 𝑥 ⇒ Take 𝑥, 𝐶𝑆𝐶_223
∃𝑥 Student John, 𝑥 ∧ Doctor 𝑥
John is a student of someone who is a doctor.

Syntax: Mixed Quantifiers
∀𝑥 ∃𝑦 Enrolled 𝑥, 𝑦
Order matters!
For all students…
For each 𝑥, we can choose a different 𝑦
Every student is enrolled in some course.
(Each student can be in a different course.)
∃𝑦 ∀𝑥 Enrolled 𝑥, 𝑦
There exists a course…
This same 𝑦 must work for all 𝑥
There's a course that every student is 
enrolled in.
(One specific course contains all students.)
We assume a domain where 𝑥 ranges over students, 𝑦 ranges over courses.

∀𝑥 ∃𝑦 𝐿𝑜𝑣𝑒𝑠(𝑥, 𝑦)
Syntax: Mixed Quantifiers II
(Each person loves at least one 
person; could be different people.) (There is one specific person that everyone loves.)
“Everyone loves someone” “Someone is loved by everyone”
∃𝑦 ∀𝑥 𝐿𝑜𝑣𝑒𝑠(𝑥, 𝑦)
Read mixed quantifiers left to right, thinking about dependency: 
∀𝑥 ∃𝑦 
The 𝑦 must be the same for all 𝑥. The 𝑦 can be different for each 𝑥.
“for each 𝑥, find a 𝑦”
(𝑦 depends on 𝑥)
∃𝑦 ∀𝑥 “find one 𝑦 that works for all 𝑥”

Question
Translate each FOL sentence to natural English; Domain: People.
∀𝑥 ∃𝑦 𝐿𝑖𝑘𝑒𝑠(𝑥, 𝑦)
∃𝑦 ∀𝑥 𝐿𝑖𝑘𝑒𝑠(𝑥, 𝑦)
∀𝑥 ∃𝑦 𝐾𝑛𝑜𝑤𝑠(𝑦, 𝑥)
∃𝑥 ∀𝑦 𝐾𝑛𝑜𝑤𝑠(𝑥, 𝑦)
∀𝑥 ∀𝑦 𝐿𝑖𝑘𝑒𝑠(𝑥, 𝑦)
∃𝑥 ∃𝑦 𝐿𝑖𝑘𝑒𝑠(𝑥, 𝑦)
Everyone likes someone
There′s someone everyone likes 
Everyone is known by someone
There′s someone who knows everyone
Everyone likes everyone
Someone likes someone
Each person likes at least one person, 
possibly different people
One specific person is liked by everyone
Each person has at least one person who 
knows them
One person knows all people
All people like all people
At least one person likes at least one 
person
Assume we read left to right:
𝐿𝑖𝑘𝑒𝑠(𝑥, 𝑦) means “𝑥 likes y”
English Description Interpretation

Question
Consider the following domain:
• People: {Alice, Bob, Carol}
• 𝐾𝑛𝑜𝑤𝑠 𝐴𝑙𝑖𝑐𝑒, 𝐵𝑜𝑏 = 𝑡𝑟𝑢𝑒
• 𝐾𝑛𝑜𝑤𝑠(𝐵𝑜𝑏, 𝐶𝑎𝑟𝑜𝑙)  =  𝑡𝑟𝑢𝑒
• 𝐾𝑛𝑜𝑤𝑠(𝐶𝑎𝑟𝑜𝑙, 𝐴𝑙𝑖𝑐𝑒)  =  𝑡𝑟𝑢𝑒
• (All other 𝐾𝑛𝑜𝑤𝑠 relationships are false.)
Evaluate each statement as true or false.
∀𝑥 ∃𝑦 𝐾𝑛𝑜𝑤𝑠(𝑥, 𝑦) 
Every person knows at least one other person.
True
∃𝑦 ∀𝑥 𝐾𝑛𝑜𝑤𝑠(𝑥, 𝑦)
There is a single person that everyone knows.
False
∀𝑥 ∃𝑦 𝐾𝑛𝑜𝑤𝑠(𝑦, 𝑥)
Everyone is known by someone.
True
∃𝑥 ∀𝑦 𝐾𝑛𝑜𝑤𝑠(𝑥, 𝑦)
There is a person who knows everyone.
False
Assume we read left to right:
𝐾𝑛𝑜𝑤𝑠(𝑥, 𝑦) means “𝑥 knows y”

Question
Every student has an advisor 
who advises them.
Each sentence below has an error in the FOL translation. Identify and fix it:
∃𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥) ⇒ ∃𝑦 𝐴𝑑𝑣𝑖𝑠𝑜𝑟(𝑦) ∧  𝐴𝑑𝑣𝑖𝑠𝑒𝑠(𝑦, 𝑥)
Uses ∃𝑥 instead of ∀𝑥.
Every professor teaches at 
least one course.
∀𝑥 ∃𝑦 𝑃𝑟𝑜𝑓𝑒𝑠𝑠𝑜𝑟(𝑥) ∧  𝐶𝑜𝑢𝑟𝑠𝑒(𝑦) ⇒ 𝑇𝑒𝑎𝑐ℎ𝑒𝑠(𝑥, 𝑦)
Correct Form:
∀𝑥 𝑃𝑟𝑜𝑓𝑒𝑠𝑠𝑜𝑟(𝑥) ⇒ ∃𝑦 𝐶𝑜𝑢𝑟𝑠𝑒(𝑦)  ∧  𝑇𝑒𝑎𝑐ℎ𝑒𝑠(𝑥, 𝑦)
This says, “For all 𝑥, there exists 𝑦 such that:
 if (𝑥 is a professor AND 𝑦 is a course), then 𝑥 teaches 𝑦.”
Implications are of the form
If [condition], then [consequence]

Question
A. Truth tables do not work for FOL because the domain can be infinite, and 
we need to consider all possible interpretations of predicates and functions, 
not just variable assignments.
How many entries does a truth table have for a FOL sentence with 𝑘 variables where 
each variable can take on 𝑛 values?
A. Truth tables are not applicable to FOL
B. 2𝑘
C. 𝑛𝑘
D. It depends

Quantifiers: Important Patterns
Universal (∀) typically uses implication (⇒)
∀𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥) ∧  𝑆𝑚𝑎𝑟𝑡(𝑥)∀𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥)  ⇒  𝑆𝑚𝑎𝑟𝑡(𝑥)
“All students are smart” “Everything is both a student and smart”
Existential (∃) typically uses conjunction (∧)
∃𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥)  ⇒  𝑆𝑚𝑎𝑟𝑡(𝑥)∃𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥)  ∧  𝑆𝑚𝑎𝑟𝑡(𝑥)
“Some student is smart” True if anything is not a student!
≡ ∃𝑥 ~𝑆𝑡𝑢𝑑𝑒𝑛𝑡 𝑥 ∨ 𝑆𝑚𝑎𝑟𝑡(𝑥)

1. “All birds can fly”
2. “Some students have laptops”
3. “No one is perfect”
4. “Everyone likes ice cream or cake”
5. “If someone is a teacher, then they 
have students”
Question
Translate to FOL.
1. ∀𝑥 𝐵𝑖𝑟𝑑(𝑥)  ⇒  𝐶𝑎𝑛𝐹𝑙𝑦(𝑥)
2. ∃𝑥 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥)  ∧  𝐻𝑎𝑠𝐿𝑎𝑝𝑡𝑜𝑝(𝑥)
3. ¬∃𝑥 𝑃𝑒𝑟𝑓𝑒𝑐𝑡(𝑥) 𝑜𝑟 ∀𝑥 ¬𝑃𝑒𝑟𝑓𝑒𝑐𝑡(𝑥)
4. ∀𝑥 𝐿𝑖𝑘𝑒𝑠(𝑥, 𝐼𝑐𝑒𝐶𝑟𝑒𝑎𝑚) ∨  𝐿𝑖𝑘𝑒𝑠(𝑥, 𝐶𝑎𝑘𝑒)
5. ∀𝑥 𝑇𝑒𝑎𝑐ℎ𝑒𝑟(𝑥)  ⇒  ∃𝑦 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑦)  ∧
 𝑇𝑒𝑎𝑐ℎ𝑒𝑠(𝑥, 𝑦)

Symmetry and Transitivity
“If 𝑥 is a sibling of 𝑦, then 𝑦 is a sibling of 𝑥”
This states that the sibling relation is symmetric.
“If 𝑥 is an ancestor of 𝑦, and 𝑦 is an ancestor of 𝑧, then 𝑥 is an ancestor of 𝑧”
This states that the ancestor relation is transitive.
∀𝑥 ∀𝑦 𝑆𝑖𝑏𝑙𝑖𝑛𝑔(𝑥, 𝑦)  ⇒  𝑆𝑖𝑏𝑙𝑖𝑛𝑔(𝑦, 𝑥)
∀𝑥 ∀𝑦 ∀𝑧 (𝐴𝑛𝑐𝑒𝑠𝑡𝑜𝑟(𝑥, 𝑦) ∧  𝐴𝑛𝑐𝑒𝑠𝑡𝑜𝑟(𝑦, 𝑧))  ⇒  𝐴𝑛𝑐𝑒𝑠𝑡𝑜𝑟(𝑥, 𝑧)

Unification


Unification: Matching Rules to Facts
We have facts in our knowledge base:
We have general rules:
Student(𝐴𝑙𝑖𝑐𝑒)
Takes(𝐴𝑙𝑖𝑐𝑒, 𝐶𝑆𝐶343)
∀𝑥 (Student(𝑥)  ∧ Takes(𝑥, 𝐶𝑆C343)) ⇒ Smart(𝑥)
Can we conclude Smart(𝐴𝑙𝑖𝑐𝑒)?

Unification: Matching Rules to Facts II
The challenge is that variables in rules can match any term
Which of these could 
match 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥)?
We need a systematic way to:
1. Find what value(s) make expressions match
2. Apply those values consistently throughout reasoning
3. Handle complex nested terms
Unification to the rescue!
• 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝐴𝑙𝑖𝑐𝑒)
• 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝐵𝑜𝑏)
• 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝐹𝑎𝑡ℎ𝑒𝑟𝑂𝑓(𝐶ℎ𝑎𝑟𝑙𝑖𝑒))
• 𝑇𝑒𝑎𝑐ℎ𝑒𝑟(𝐴𝑙𝑖𝑐𝑒)
• 𝑆𝑡𝑢𝑑𝑒𝑛𝑡(𝑥, CSC_343)
Different predicate
Different arity


Unification: The Main Idea
Unification finds substitutions that make expressions identical.
𝐿𝑖𝑘𝑒𝑠(𝐴𝑙𝑖𝑐𝑒, 𝑥)
What should 𝑥 be?
𝐿𝑖𝑘𝑒𝑠(𝐴𝑙𝑖𝑐𝑒, 𝑃𝑖𝑧𝑧𝑎)
Rules
Facts
𝑥 = 𝑃𝑖𝑧𝑧𝑎
Goal: Make two expressions match by finding substitutions for variables.
Unification enables automated reasoning by systematically matching facts 
with rules so we can apply inference in FOL and power systems like Prolog.
Once we can unify, we can automate logical reasoning!

Unification Examples
Example: Multiple variables
Sibling(x, y)
Sibling(John, Mary)
Example: Variables on both sides
Parent(x, Bob)
Parent(Alice, y)
Unifier: { x/John, y/Mary } Unifier: {x/Alice, y/Bob}
Example: Nested Terms
Ancestor(FatherOf(x), y)
Ancestor(FatherOf(John), Mary)
Unifier: { x/John, y/Mary }
Example: Functions Unifying with Variables
Age(x)
Age(MotherOf(Alice))
Unifier: { x/ MotherOf(Alice)) }

When Unification Fails
Example: Different Constants
Student(Alice)
Student(Bob)
Example:
Student(x)
Teacher(x)
Cannot Unify: Alice ≠ Bob Cannot Unify: Different Predicates
Example: Occurs Check
x
f(x)
Cannot unify! x appears inside f(x).
The occurs check prevents infinite substitutions.
If we unify x with  f(x) to acquire the substitution 
{ x / f(x)} (that is, x <- f(x)), then whenever we 
need to use the value of x, we replace it with f(x).
x <- f(x)
x <- f(f(x))
x <- f(f(f(x)))

Unification Algorithm
function UNIFY(exp1, exp2, Θ):
    if Θ = FAIL then return FAIL
    if exp1 = exp2 then return Θ
    if exp1 is a variable then
        return UNIFY-VAR(exp1, exp2, Θ)
    else if exp2 is a variable then
        return UNIFY-VAR(exp2, exp1, Θ)
    if exp1 and exp2 are functions/predicates then
        if they have same name and arity then
            UNIFY-ARGS(args(exp1), args(exp2), θ)
        else return FAIL
    return FAIL
# If already failed, propagate failure
# Identical expressions need no substitutions
# Handle either expression being variables
# Unify all arguments pairwise
# Different functions or arity
# Handle compound expressions
# Θ is a list of substitutions
# Cannot unify: no other cases match
{x/Alice, y/Bob}
Likes(x, y) = Likes(x, y)
x , Father(Bob)
Knows(x, y) and Knows(Alice, Bob)
{x/Alice, y/Bob}
Father(Bob) , x
x , Alice
Alice , x

UNIFY-VAR
function UNIFY-VAR(var, x, Θ):
    # If var already has a binding, unify its value with x
   if Θ(var) = val then
        return UNIFY(val, x, Θ)
    # If x is a variable with a binding, unify var with x's value 
    else if x is a variable and Θ(x) = val then
        return UNIFY(var, val, Θ)
   # Prevent binding var to a term containing var (prevent
    # infinite structures)
    else if OCCURS-CHECK(var, x) then return FAIL
    # No conflicts: add the new binding Θ(var) = x
    else return Θ ∪ var / x
Goal: Given a variable and an 
expression, find a substitution that 
makes them identical, following 
any existing bindings and 
preventing circular references.
var: z
x : Alice
Θ: {z/Bob}
UNIFY(Bob, Alice, Θ)
var: z
x: w
Θ = {w/Alice}
UNIFY(z, Alice, Θ)
FAIL
{w/Alice, z/Alice}
var: z
x: f(z)
Θ = {}
FAIL
var: z
x: Alice
Θ = {}
Θ = {z/Alice}

UNIFY-VAR Examples 
UNIFY-VAR(x, Alice, {}) {x/Alice}→
UNIFY-VAR(y, x, {x/Alice}) {x/Alice, y/Alice}→
UNIFY-VAR(x, Bob, {x/Alice}) FAIL→
Simple variable binding
Following existing 
bindings
Variable already bound
UNIFY-VAR(x, Parent(y, x), {y/Alice}) FAIL→Occurs check violation
UNIFY-VAR(z, MotherOf(Alice), {}) {z/MotherOf(Alice)}→Binding to a complex 
term
UNIFY-VAR(z, y, {x/Alice, y/x}) {x/Alice, y/x, z/Alice}→Chain of variable 
bindings

UNIFY-ARGSfunction UNIFY-ARGS(args1, args2, Θ):
    # Base case: no more arguments to unify
   if args1 and args2 are both empty then return Θ
    # Different number of arguments - should never 
    # happen; checked in UNIFY
    if args1 = ∅ and args2 ≠ ∅ then return FAIL
    if args1 ≠ ∅ and args2 = ∅ then return FAIL
    # Unify the first pair of arguments from the 
    # ‘parallel’ lists
    Θ’ = UNIFY(head(args1), head(args2), Θ)
    # If that failed, propagate failure
   if Θ′ = FAIL then return FAIL
    # Recursively unify remaining arguments with 
    # updated substitution
    return UNIFY-ARGS(tail(args1), tail(args2), Θ’)
𝐿 = head | tail
     ≡ 𝐿[0] + L[1: ]
Goal: Given two parallel lists, 
unify arguments one at a time 
(left to right), threading the 
substitution through each step.

UNIFY-ARGS Examples I 
UNIFY-ARGS([Alice, x], [y, Bob], {})
{y/Alice, x/Bob}→
UNIFY-ARGS([x, x], [Alice, y], {})
{x/Alice, y/Alice}→
UNIFY(Alice, y, {}) → {y/Alice}
UNIFY-ARGS([x], [Bob], {y/Alice})
UNIFY(x, Bob, {y/Alice})
UNIFY(x, Alice, {}) → {x/Alice}
UNIFY-ARGS([x], [y], {x/Alice})
UNIFY(x, y, {x/Alice})

UNIFY-ARGS Examples II
UNIFY-ARGS([x, MotherOf(y)],
           [Alice, MotherOf(Bob)], {})
{y/Alice, x/Bob}→
UNIFY(x, Alice, {}) → {x/Alice}
UNIFY-ARGS([MotherOf(y)], [MotherOf(Bob)], {x/Alice})
UNIFY(MotherOf(y), MotherOf(Bob), {x/Alice})
UNIFY-ARGS([y], [Bob], {x/Alice})
UNIFY(y, Bob, {x/Alice})
UNIFY-ARGS([Alice, x], [Bob, y], {})
UNIFY(Alice, Bob, {}) FAIL→

UNIFY Example
UNIFY(Parent(John, MotherOf(x)),
      Parent(y, MotherOf(Bob)), {})
UNIFY-ARGS([John, MotherOf(x)],
           [y, MotherOf(Bob)], {})
{y/John, x/Bob}→
Same predicate and arity
UNIFY(John, y, {}) → {y/John}
UNIFY(MotherOf(x), MotherOf(Bob), {y/John})
UNIFY-ARGS([x], [Bob], {y/John})
UNIFY(x, Bob, {y/John})

Inference in First-Order Logic

Toward Inference
What Has Been Built:
• Syntax: How to write statements in FOL.
• Unification: How to make expressions match.
Why does matching matter?
What is missing?
Goal: Automated Reasoning
Input: Facts and rules in a knowledge base Output: Answers to queries (true / false or variable bindings)
Process:
1. Find a rule that might apply to the query.
2. Use unification to match the rule's premises with known facts.
3. Apply the same substitution to the rule's conclusion. 
4. Derive new knowledge and repeat as needed.
→ Because rules are general but facts are specific!
→ How to derive new knowledge!
Knowledge Base:
Student(Alice)
∀x Student(x) ⇒ TakesCourses(x)
∀x TakesCourses(x) ⇒ NeedsCoffee(x)
Query: NeedsCoffee(Alice)? Yes.
We need formal rules for deriving new knowledge, using quantifiers, and making valid substitutions.

Inference Rules: Universal Instantiation
Rule: If something is true for all 𝑥, then it is true for any specific instance.
Formally:
Given:
Infer:
∀𝑥 𝑃(𝑥)
𝑃(𝑐) where 𝑐 is any term
KB:
Student(Alice)
Student(Bob)
Student(FatherOf(Charlie))
∀x Student(x) ⇒ Person(x)
Using universal instantiation, we can infer:
Student(Alice) ⇒ Person(Alice)
Student(Bob) ⇒ Person(Bob)
Student(FatherOf(Charlie)) ⇒ Person(FatherOf(Charlie))

Inference Rules: Existential Instantiation
Rule: If we know something with property 𝑃 exists, we can introduce a new 
constant to refer to it.
Given:
Infer:
∃𝑥 𝑃(𝑥)
𝑃(𝑘) where 𝑘 is a new constant (called Skolem 
constant): a unique new symbol introduced to 
represent the specific object whose existence is 
claimed
KB:
∃x Student(x) ∧ Smart(x)
Using existential instantiation, we can infer:
Student(S1) ∧ Smart(S1)
“There exists a student who is smart” “Let S1 be a Skolem constant that 
names the smart student.”
We don't know which student is smart, only that at least one exists so we 
need to use a new symbol not used elsewhere in the KB. 
Formally

Generalized Modus Ponens (GMP)
Universal Instantiation + Unification + Modus Ponens = Generalized Modus Ponens
Knowledge Base: 
Facts: 𝑓1, 𝑓2, … , 𝑓n
Rule(s): ∀𝑥 𝑟1, 𝑟2, … , 𝑟𝑛 ⇒ 𝑠
And we have a substitution Θ where 
for all 𝑖:
Suppose we have:
If we can unify facts with the premises of a rule, we can infer the conclusion with 
that same substitution. 
We can infer:
𝑓𝑖 = Θ 𝑟𝑖
Θ 𝑠 Since 𝑠 is a sentence that 
may contain variables that 
got bound during 
unification, we infer Θ 𝑠 .

Example of Generalized Modus Ponens
KB:
Teaches(Alvin, CSC343, Spring2026)
Enrolled(Alice, CSC343, Spring2026)
Rule(s):
∀prof ∀student ∀course ∀semester (Teaches(prof, course, semester) ∧ Enrolled(student, course, semester))
⇒ InClass(student, prof, course)
Θ(Teaches(prof, course, semester) ) = Teaches(Alvin, CSC343, Spring2026)
where  Θ(prof) = Alvin, Θ(course) = CSC343, and Θ(semester) = Spring2026
Match premises with facts using Θ:
Θ(Enrolled(student, course, semester)) = Enrolled(Alice, CSC343, Spring2026)) 
where  Θ(student) = Alice, Θ(course) = CSC343, and Θ(semester) = Spring2026
Θ(InClass(student, prof, course)) = InClass(Alice, Alvin, CSC343)
So by generalized Modus Ponens, we have:

Forward Chaining in FOL
1. Start with initial facts in KB
2. Find a rule whose premises match facts (using unification)
3. Apply GMP to derive the conclusion
4. Add the new fact to KB
5. Repeat until goal is derived or no new facts can be added
Properties
This is the same algorithm as in 
propositional logic, except here 
we use unification and GMP to 
derive new facts in FOL.
Sound: Everything derived is entailed by the KB
• Forward chaining only derives logical consequences
• No false conclusions from true premises
Complete for definite clauses: Find all entailed 
atomic facts
• Definite clause: 𝑝1 ∧ 𝑝2 ∧ ⋯ ∧ 𝑝n ⇒ q
(single positive conclusion)
• If entailed, forward chaining will eventually derive it
Exhaustive: Derives all entailed facts
• Continues until no new inferences
• Guarantees nothing is missed
May derive irrelevant facts: the “Shotgun 
approach”
• Produces facts unrelated to your query
• Inefficient for large KBs

Backward Chaining in FOL
1. Check if goal is already a fact in KB
2. Find rules whose conclusions could match the goal
3. Use UNIFY to match the rule's conclusion with the goal
4. If unification succeeds, apply θ to the rule's premises to get specific subgoals
5. Recursively apply backward chaining to prove each subgoal
6. If all subgoals are proven, return success; otherwise try next rule
7. If no rule succeeds, return failure
Properties
Same algorithm as in 
propositional logic, except 
here we use unification to 
work backwards from 
goals to facts in FOL.
Sound: Proves only entailed goals
• No false conclusions
• Every step is logically valid
Complete for definite clauses: Finds a proof if 
one exists
• Definite clause: 𝑝1 ∧ 𝑝2 ∧ ⋯ ∧ 𝑝n ⇒ q
• If entailed, backward chaining will prove it
Goal-Directed: More efficient than forward chaining
• Explores only facts relevant to the query
• Avoids irrelevant derivations
Prolog-based:
• Prolog uses backward chaining with 
depth-first search
• Ideal for answering queries

Example: Backward Chaining in FOL
KB:
1. Student(Alice)
2. Takes(Alice, CSC343)
3. ∀x (Student(x) ∧ Takes(x, CSC343)) ⇒ Smart(x)
Smart(Alice)
Θ = UNIFY Smart 𝑥 , Smart Alice = { 𝑥/Alice }
∀x (Student(x) ∧ Takes(x, CSC343)) ⇒ Smart(x)
Find matching rule: conclusion 
could match the goal
UNIFY goal with rule conclusion:
Apply Θ to premises to get subgoals.
Student Alice ∧ Takes Alice, CSC343
Prove subgoals
Student Alice Takes Alice, CSC343
In KB.
 In KB.
Query: Smart(Alice)

Inference in Prolog

Backtracking
If we reach a point where a goal cannot be matched, or the body of a rule cannot be matched, 
we backtrack to the last (most recent) spot where a choice of matching a particular fact or rule 
was made. 
We then try to match a different fact or rule. If this cannot be done, we go back to the next 
previous place where a choice was made and try a different match there.
We try alternatives until we are able to solve all the goals in our query or until all possible 
choices have been tried and found to fail.
If this happens, we answer “no” the query can’t be solved.
As we try to match facts and rules we try them in their order of definition.
Depth-first search.

Backtracking Example
grandMotherOf(X,GM) :- motherOf(X,M), motherOf(M,GM).
grandMotherOf(X,GM) :- fatherOf(X,F), motherOf(F,GM).
fatherOf(tom,dick).
fatherOf(dick,harry).
fatherOf(jane,harry).
motherOf(tom,judy).
motherOf(dick,mary).
motherOf(jane,mary).
Our database:
?- grandMotherOf(tom, GM).
Query:
We try the first grandMotherOf rule first.
This forces M = judy.
motherOf(judy,GM)
We have to solve:
motherOf(tom,M), motherOf(M,GM).
None of the motherOf rules 
match this goal, so we backtrack.
No other motherOf rule can 
solve motherOf(tom,M).
This forces X = tom.

Lists in Prolog
"_" (underscore) can be used as a wildcard or "don’t care" symbol in matches. 
The notation [H | T] represents a list with H matching the head of the list and T 
matching the rest of the list.
[1, 2, 3] = [1 | [2,3]] = [1, 2 | [3]] = [1, 2, 3 | [] ]


List Operations
List operations are defined using rules and facts.
The definitions are similar to those used in Scheme or ML, but they are non-procedural. That is, you do 
not give an execution order.
Instead, you state recursive rules and non-recursive "base cases" that characterize the operation you are 
defining.
append([], L, L).
append([H | T1], L2, [H | T3]) :- append(T1, L2, T3).
An empty list (argument 1) appended 
to any list L (argument 2) gives L 
(argument 3) as its answer.
% Base Case
% Recursion
The rest of the resulting list, T3, is the result of 
appending T1 (the rest of the first list) with L2 
(the second input list).
input output
input output
If we take a list that begins with H and has T1 as 
the rest of the list and append it to a list L2 then 
the resulting appended list will begin with H.

Example: append
append([], L, L).
append([H | T1], L2, [H | T3]) :- append(T1, L2, T3).
append([1], [2,3], T)
append([H | T1], L2, [H | T3]) :- append(T1, L2, T3).
Unify([], [1]) FAILS 
append([], L, L)
Unify([], T1=[]) SUCCESS 
append([], L, L)
Unify(L, L2=[2,3]) SUCCESS 
Unify(L=[2,3], T3) SUCCESS 
T3=[2,3]
T = [1,2,3]
Unify(H, 1) SUCCESS 
Unify(T1, []) SUCCESS 
Unify(L2, [2,3]) SUCCESS 
Unify(T, [1 | T3]) SUCCESS 
SUCCESS 
SUCCESS 
SUCCESS 
SUCCESS 

Ancestral Backtracking Example (continued)
grandMotherOf(X,GM) :- motherOf(X,M), motherOf(M,GM).
grandMotherOf(X,GM) :- fatherOf(X,F), motherOf(F,GM).
fatherOf(tom,dick).
fatherOf(dick,harry).
fatherOf(jane,harry).
motherOf(tom,judy).
motherOf(dick,mary).
motherOf(jane,mary).
?- grandMotherOf(tom, GM).Query:
We try the second grandMotherOf rule.
This forces F = dick.
motherOf(dick,GM)
We have to solve:
fatherOf(tom,F), motherOf(F,GM).
None of the fatherOf rules 
match this goal, so we backtrack.
No other motherOf rule can 
solve motherOf(dick, GM).
This forces X = tom.
We can match:
fatherOf(tom,dick).
We can match:
motherOf(dick, mary).
We have matched all our goals, so we 
know the query is true, with GM = mary.

Query Overview
grandMotherOf(X, GM)
motherOf(X, M), motherOf(M, GM) fatherOf(X, F), motherOf(F, GM)
motherOf(tom, judy)
motherOf(dick, mary)
motherOf(jane, mary)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
fatherOf(tom, dick)
fatherOf(dick, harry)
fatherOf(jane,harry)
X=   ,
M=
X=   ,
GM= 
X=   ,
GM= 
X=   ,
M=   ,
GM= 
X=   ,
F=
X=   ,
F=

Visualizing Prolog Query Search I
grandMotherOf(X, GM)
motherOf(X, M), motherOf(M, GM)
motherOf(tom, judy) motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
X=tom,
M=judy
X=?,
GM=?
X=tom,
M=judy,
GM=?


Visualizing Prolog Query Search II
grandMotherOf(X, GM)
motherOf(X, M), motherOf(M, GM)
motherOf(dick, mary)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
X=dick,
M=mary
X=   ,
GM= 
X=dick,
M=mary,
GM=?


Visualizing Prolog Query Search III
grandMotherOf(X, GM)
motherOf(X, M), motherOf(M, GM)
motherOf(jane, mary)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
X=jane,
M=mary
X=   ,
GM= 
X=jane,
M=mary,
GM= 


Visualizing Prolog Query Search IV: New Rule 
grandMotherOf(X, GM)
motherOf(X, M), motherOf(M, GM) fatherOf(X, F), motherOf(F, GM)
motherOf(tom, judy)
motherOf(dick, mary)
motherOf(jane, mary)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
fatherOf(tom, dick)
fatherOf(dick, harry)
fatherOf(jane,harry)
X=   ,
M= 
X=   ,
GM= 
X=   ,
GM= 
X=   ,
M=   ,
GM= 
X=   ,
F= 
X=   ,
F=   ,
GM= 

Visualizing Prolog Query Search V
grandMotherOf(X, GM)
fatherOf(X, F), motherOf(F, GM)
motherOf(dick, mary)
motherOf(tom,judy)
fatherOf(tom, dick)
X=?,
GM=?
X=tom,
F=dick
X=tom,
F=dick,
GM=maryGM=?
X=tom,
GM=mary


Visualizing Prolog Query Search VI
grandMotherOf(X, GM)
fatherOf(X, F), motherOf(F, GM)
fatherOf(tom, dick)
X=?,
GM=?
X=tom,
F=dick
X=tom,
F=dick,
GM=?
motherOf(jane, mary)


Visualizing Prolog Query Search VII
grandMotherOf(X, GM)
fatherOf(X, F), motherOf(F, GM)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
fatherOf(dick, harry)
X=   ,
GM= 
X=dick,
F=harry    
X=dick,
F=harry
GM=?


Visualizing Prolog Query Search VIII
grandMotherOf(X, GM)
fatherOf(X, F), motherOf(F, GM)
motherOf(jane, mary)
motherOf(dick, mary)
motherOf(tom,judy)
X=   ,
GM= 
X=jane,
F=harry    
X=jane,
F=harry
GM=?
fatherOf(jane,harry)
```

## Advanced Search (Optimization)

*Extracted from PDF: `5 Advanced Search (Optimization).pdf`*

```
Advanced Search 
(Optimization)

Search vs. Optimization
New setting: Optimization
• States 𝑠 have values 𝒇(𝑠)
Before, the goal was simply to find a path from the start state to the goal state using 
search strategies such as uninformed methods or informed approaches like A*.
Challenge: Too many states for uninformed and informed approaches
• Cannot enumerate all paths
• Function may not be differentiable (cannot use gradient descent)
Goal: Find 𝑠 with optimal value 𝒇(𝑠)
• Sometimes we maximize 𝒇(𝑠)(e.g., satisfaction, profit)
• Sometimes we minimize 𝒇(𝑠)(e.g., cost, distance)


𝑛-Queens
Classic puzzle: Place 𝑛 queens on an 𝑛 × 𝑛 chessboard so that no two 
queens attack each other (same row, column, or diagonal)
State: Configuration of the board (position of all queens)
Objective function 𝒇(𝑠): Number of non-attacking queen pairs
Goal: Maximize 𝒇(𝑠). Ideally, with all combinations: 𝒇 𝑠 =
𝑛 𝑛−1
2 .
nano banana
For large 𝑛 (e.g., 𝑛 = 1000), the search space becomes 
intractable; optimization methods will scale much better 
This problem can be solved using traditional search methods. 
However, consider when 𝑛, the number of queens and 
number of sides on the chessboard, becomes large.
Ug!
Why optimization instead of search?

Traveling Salesperson Problem (TSP)
Problem: Given a complete, weighted graph 𝐺 = (𝑉, 𝐸), find a 
Hamiltonian cycle that minimizes total distance
State: A particular cyclic path (ordered list of nodes, e.g., A-B-C-D-E-A)
Objective function 𝒇(𝑠): Total weight of the path (e.g., total miles)
Goal: Minimize 𝒇(𝑠)
Ug!
Number of possible paths in a complete weighted graph where every 
permutation of cities gives a valid tour : 
𝑛−1 !
2  .
Why optimization instead of search?
• Visits each node exactly once
• Returns to the initial node
• Minimizes total distance
For 𝑛 = 10 cities, there are ~181,000 tours; 𝑛 = 20 → ~60 quintillion.
• Even with good heuristics (e.g., MST), A* does not scale 
due to exponential state space and memory requirements
• We only need the best tour, not the path to find it

Boolean Satisfiability
Problem: Given a Boolean formula in CNF, find a satisfying assignment
State: Assignment to variables (e.g., A=T, B=F, C=T, D=T, E=T)
Objective function 𝒇(𝑠): Number of satisfied clauses
Goal: Maximize 𝒇(𝑠) (MAX-SAT: satisfy the maximum number of clauses)
2𝑛 possible assignments of true / false.
For hard or unsatisfiable instances, search may fail to 
quickly find a solution, but optimization techniques can 
still produce good assignments by maximizing satisfied 
clauses even when a perfect solution does not exist.
Why optimization instead of search?
Example
(A ∨ ¬B ∨ C) ∧
(¬A ∨ C ∨ D) ∧
(B ∨ D ∨ ¬E) ∧
(¬C ∨ ¬D ∨ ¬E) ∧
(¬A ∨ ¬C ∨ E)

Hill Climbing
Basic algorithm:
• Start at one state,
• Move to a neighbor with a better 𝒇(𝑠) value,
• Repeat until no neighbors have better 𝒇(𝑠) value.
Critical Question: How do we define neighbor?
• Neighbors refer to states reachable by a single action from current state
• In optimization, we have more freedom in defining actions than in path-finding
• Path-finding: actions often dictated by problem structure (roads, legal moves)
• Optimization: we choose what counts as an action (which queen to move? how to modify 
tour?)
• This design choice significantly impacts algorithm performance
• Requires careful consideration of tradeoffs

Defining Neighbors: 𝑛-Queens
Approach: Small changes to current state
• Look at the most-conflicting column (if a tie, choose the rightmost column)
• Move queen in that column vertically to a different location
Result: Neighborhood contains 𝑛 − 1 states 
(one for each possible vertical position)
… Neighborhood of 𝑠
Objective function 𝒇(𝑠): 
Number of non-attacking 
queen pairs
𝒇 𝑠 = 6 
𝒇 𝑠 = 6 
𝒇 𝑠 = 5 

Defining Neighbors: Traveling Salesperson Problem
Approach: 2-change operation
• Select two edges to remove
• Flipping the edges between the removed edges
• Reconnect the tour to the flipped edges
Original tour: A-B-C-D-E-F-G-H-A
A
B
C
D
E
F
G
H(B,C) and (E,F)
C-D-E → E-D-C
Our new tour.
Select two edges to remove:
Reverse the edges in-between:
Reconnect the tour with the reversed elements:
A-B    C-D-E    F-G-H-A
A-B    E-D-C F-G-H-A
A-B-E-D-C-F-G-H-A
𝒇(𝑠): Total weight of the path

Defining Neighbors: SAT
Approach: Flip one variable assignment
Example
(A ∨ ¬B ∨ C) ∧
(¬A ∨ C ∨ D) ∧
(B ∨ D ∨ ¬E) ∧
(¬C ∨ ¬D ∨ ¬E) ∧
(¬A ∨ ¬C ∨ E)Example:
Starting state (A=T, B=F, C=T, D=T, E=T)
Resulting Neighborhood:
(A=F, B=F, C=T, D=T, E=T)
(A=T, B=T, C=T, D=T, E=T)
(A=T, B=F, C=F, D=T, E=T)
(A=T, B=F, C=T, D=F, E=T)
(A=T, B=F, C=T, D=T, E=F)
𝒇(𝑠): Number of satisfied clauses
𝒇 𝑠 = 4
𝒇 𝑠 = 4
𝒇 𝑠 = 4
𝒇 𝑠 = 5
𝒇 𝑠 = 4
𝒇 𝑠 = 4

Hill Climbing: Tradeoffs
What is a neighbor?
Neighborhood too small?
Algorithm gets stuck in local optima
Vaguely: for a given problem structure, neighbors are states that
can be produced by a small change.
How to pick next state?
 Greedy: Choose best neighbor
Neighborhood too large?
Algorithm is inefficient (too many neighbors to evaluate)
When to terminate?
When no neighbor has better value than current state
The Tradeoff!

Hill Climbing Algorithm
Pick initial state 𝑠
Loop:
 Pick 𝑡 ∈ neighbors(𝑠) with the best 𝑓(𝑡)
 If 𝑓(𝑡) is not better than 𝑓(𝑠) THEN break
 𝑠 ← 𝑡
return 𝑠
What could have happened?
We may have found a “local 
optimum,” not a “global optimum”
Local optima!
The algorithm stops when no neighbor is better

Hill Climbing: The Local Optima Problem
Our space is a complex landscape 
with multiple optima.
Our goal is to find the global optimum.
But we can only see locally: fog 
obscures everything except 
immediate neighbors
The result is that we climb to a local 
optimum and stop, even though a global 
optimum exists elsewhere.
What is actually going onWhat we see
𝑓 𝑠
Global optimum: 
what we want to find
𝑠
𝑓 𝑠
𝑠

Hill Climbing: Escaping Local Optima
𝑓 𝑠
𝑠
𝑓 𝑠
𝑠
Done?
Where do I go?
Strategy 1: Random Restarts
• When stuck, pick a random new starting point
• Run hill climbing again
• Repeat 𝑘 times, return best result
Strategy 2: Stochastic Hill Climbing
• Transform 𝑓 𝑠  into a probability distribution 
over neighbors, with higher 𝑓 𝑠  values 
receiving higher probability
• Does not always pick the best neighbor
How do we escape Local optima?

Questions
A hill climbing algorithm is solving a scheduling problem. After 50 iterations, it finds a solution with 𝑓(𝑠) = 87. 
After 500 more iterations, we still have 𝑓(𝑠)  =  87. What is the BEST next step?
You are using hill climbing to solve a problem. The algorithm stops at a state where 𝑓(𝑠) = 15, and all 
neighbors have 𝑓(𝑡) ≤ 15. Which of the following is TRUE?
A. You have definitely found the global optimum
B. You have definitely found a local optimum, but it might also be the global optimum
C. The algorithm failed because it didn't improve the solution 
D. You need to restart with a different objective function
E. All neighbors must have 𝑓(𝑡) = 15 (no variation)
A. Declare the problem unsolvable and try a different algorithm
B. Continue running hill climbing longer—it just needs more time
C. Use random restart: pick a new random initial state and run hill climbing again
D. Reduce the neighborhood size to find smaller improvements
E. Increase the neighborhood size to explore more options 


Simulated Annealing
Inspiration: Annealing strengthens metal by heating it and cooling it 
slowly, relieving internal stresses and creating a uniform crystal structure.
𝑠 := choose initial state
best := 𝑠       # track best observed solution
T := 1     # temperature; this could be larger
K := 1     # iterations
for k = 0 through K:
    T := T ⋅ 0.99            # cool down
    𝑡 := neighbor(𝑠)       # pick a random neighbor 
    if 𝑓 𝑡 > 𝑓(𝑠), then
       𝑠 := 𝑡
        if 𝑓 𝑡 > 𝑓(𝑠), then best := 𝑡
    else with probability 𝑒− 𝑓 𝑠 −𝑓 𝑡
𝑇  do 𝑠 := 𝑡 
return best
wikihow.com
Algorithmic analog: Allow “bad” moves early (high temperature) then 
cool by becoming increasingly selective over time; eventually behaving 
like hill climbing (low temperature).
The Probability Formula:
• Borrowed from physics (Boltzmann 
distribution in thermodynamics)
• Gives desired properties: gradual 
transition from exploration to 
exploitation
• The exponential decay naturally 
handles the temperature cooling
# worse, 
but choose 
anyway

Simulated Annealing: Temperature Cooling Schedule
How fast to decrease 𝑻?
Too fast:
 Becomes hill climbing
 Gets stuck in local optima
Too slow:
 Takes too long to converge
 Wasteful exploration
Common approach:
  Geometric decay or something similar
  Commonly: 𝑇𝑡+1 = 0.99 ⋅ 𝑇𝑡
Phase Temperature Acceptance of 
Worse Moves 
Goal 
Early High Frequent Exploration
Middle Moderate Occasional Refinement
Late Low Rare Convergence
Evolution 
over time

Question
Which of the following is likely to give the best cooling schedule for simulated annealing?
A. 𝑇𝑡+1 = 𝑇𝑡 ⋅ 1.25
B. 𝑇𝑡+1 = 𝑇𝑡
C. 𝑇𝑡+1 = 𝑇𝑡 ⋅ 0.8
D. 𝑇𝑡+1 = 𝑇𝑡 ⋅ 0.001
Temperate is increasing
Temperate is constant
Cools way too fast; basically, hill-climbing


Questions
Which of the following would be better to solve 
with hill climbing rather than A* search?
i. Finding the smallest set of vertices such 
that every edge in the graph has at least 
one endpoint in the set
ii. Finding the fastest way to schedule jobs 
with varying runtimes on machines with 
varying processing power
iii. Finding the fastest way through a maze
Distinction
• Use A* when: small branching 
factor, want the path, good 
heuristic exists
• Use hill climbing when: huge 
state space, only care about 
final solution, can define 
neighbors easily
A*: Small branching factor, good heuristic (distance), 
need the path itself
Hill climbing: 2𝑛 state space (𝑛 vertices), no path 
structure, unclear heuristic for A*;
Start with valid set, remove vertices to improve
Hill climbing: Large state space. 
only care about final schedule
Start random, swap 
jobs/machines to improve
For 𝑛 jobs and 𝑚 machines,
𝑛! ⋅  𝑚𝑛 state space
𝑛! : ordering of jobs on machines 
affects completion time
𝑚𝑛 : each job assigned to one of 
𝑚 machines

Genetic Algorithms

Genetic Algorithms
Inspiration: Biological Evolution Algorithmic Analog
• Organisms encode genetic information in DNA
• Beneficial traits help survival and reproduction
• Population evolves toward better fitness over 
generations
• Encode solutions as “chromosomes”
• Better solutions have higher “fitness”
• Apply selection, crossover, and mutation 
operations


Genetic Algorithms: Biology 
  Computer Science
Biology CS Analog
DNA/Chromosome String or array (state representation) 
Gene Single element in array (e.g., position i) 
Population Collection of candidate solutions
Fitness Function Objective function value 𝒇(𝑠) 
Generation Iteration of the algorithm: replace some or all of the old 
population with new offspring
Evolution Iterative improvement over generations 
Operations
Natural Selection Probabilistic selection based on 𝒇(𝑠): better fitness have 
higher probability of reproducing
Crossover/Recombination Swap/merge portions of two arrays 
Mutation Randomly modify array element(s)

Genetic Algorithm Pseudocode
1. Let s₁, ..., sN be the current population
2. Let pᵢ = f(sᵢ) / Σⱼf(sⱼ) be the reproduction probability
3. for k = 1; k < N; k += 2:
      parent1 = randomly pick according to pᵢ
      parent2 = randomly pick another
      Randomly select crossover point, swap substrings of
         parents 1, 2 to generate children t[k], t[k+1]
4. for k = 1; k ≤ N; k++:
     Randomly mutate each position in t[k] with small
       probability (mutation rate)
5. New generation replaces old: {s} ← {t}. Repeat.
# Probability 
Distribution based on 
fitness of individuals;
Higher fitness → 
higher chance of 
being selected.
# Crossover to create 
a pair of children
# Mutate: Possibly modify 
each gene (position) of each 
individual in the population 
# Repeat the process with 
the next generation 

Example
Problem: Schedule 5 courses (A, B, C, D, E) into 3 time 
slots (Mon/Wed, Tue/Thu, Fri/Sat)
• Each course is assigned to exactly one time slot; 
multiple courses can share a slot
• Students can only attend one course per time 
slot
Goal: Maximize the number of students who 
can enroll in all their desired courses
Student 
Request
# Students
A, B, C 2
A, B, D 7
A, D, E 3
B, C, D 4
B, D, E 10
C, D, E 5
2 students want to take 
courses A, B, and C
Individual/Chromosome/State: Assignment of courses to time slots
Encoding: 5-character string (one character per course)
Character values: M (Mon/Wed), T (Tue/Thu), F (Fri/Sat)
Character positions: A = 1, B = 2, C = 3, D = 4, E = 5
Example chromosome: MMFTM
Population: Collection of chromosomes
• A → Mon/Wed
• B → Mon/Wed
• C → Fri/Sat
• D → Tue/Thu
• E → Mon/Wed
e.g. : { MMFTM, TTFMM, FMTTF, MTTTF }

Example: Fitness Calculation
What are we trying to optimize?
Maximize the number of students who can take all their desired courses.
What defines a valid solution for each student?
Their requested courses must be scheduled in different time slots (no conflicts).
How do we quantify solution quality?
Count satisfied constraints (students who can enroll without conflicts).
𝑓(𝑐ℎ𝑟𝑜𝑚𝑜𝑠𝑜𝑚𝑒) = # students who can enroll without conflicts

Example: Fitness Calculation
Time Slots
M, M, F 
M, M, T 
M, T, M 
M, F, T 
M, T, M 
F, T, M
𝑓(𝑐ℎ𝑟𝑜𝑚𝑜𝑠𝑜𝑚𝑒) = students who can enroll without conflicts
𝑓 MMFTM = 4 + 5 = 9
𝐴𝐵𝐶𝐷𝐸
Constraint
(Student Request)
# Students
A, B, C 2
A, B, D 7
A, D, E 3
B, C, D 4
B, D, E 10
C, D, E 5
Satisfied?
No
No
No
Yes
No
Yes
Time Slots
M, T, F 
M, T, M 
M, M, F 
T, F, M
T, M, F
F, M, F
Constraint
(Student Request)
# Students
A, B, C 2
A, B, D 7
A, D, E 3
B, C, D 4
B, D, E 10
C, D, E 5
Satisfied?
Yes
No
No
Yes
Yes
No
𝑓 MTFMF = 2 + 4 + 10 = 16

Population and Parent Selection
For an initial population, we can randomly 
generate strings and calculate their fitness:
Individual: 𝑠 𝑓(𝑠)
MMFTM 9
TTFMM 4
FMTTF 19
MTTTF 3
෍ 𝑓 𝑠 = 35
~%
26
11
54
9
Just like Stochastic Hill Climbing, we:
• Transform 𝑓 𝑠  into a probability distribution over 
individuals, with higher 𝑓 𝑠  values receiving higher 
probability
• Does not always pick the best individual
FMTTF is most likely to be selected 
as a parent but is not guaranteed.
Selecting Parents
A parent is an individual from the current population that is 
selected to contribute genetic material to create offspring 
for the next generation.

Crossover
Parents MMFTM FMTTF
Crossover is the operation of combining 
genetic material from two parents to 
create two children.
This is the way for the genetic algorithm 
to mix traits from different solutions to 
explore new combinations.
MMTTF FMFTMOffspring
Crossover Point: Index 2

Mutation
Original MMFTM FMTTF
Mutation is is the operation of 
randomly modifying individual genes 
(elements) of a chromosome.
This is a way for a genetic algorithm 
to introduce new genetic variation 
and explore solutions beyond the 
current population.
MFFTM FMFMMMutated
The mutation rate controls how often mutations 
occur (in each position of an individual).
Mutation Rate (𝜇) Behavior
0.001 (too low) Rare 
mutations 
0.05 (good) Occasional 
mutations 
0.5 (too high) Frequent 
mutations 
Result
Population lacks diversity, 
converges too quickly 
Maintains diversity, steady 
improvement 
Good solutions disrupted, 
poor convergence 
Convergence: When individuals in the population become highly 
similar to each other and fitness values stabilize across generations.

The Next Generation
Individual: 𝑠 𝑓(𝑠)
MMFTM 9
TTFMM 4
FMTTF 19
MTTTF 3
~%
26
11
54
9
The Original Population
Individual: 𝑠 𝑓(𝑠)
FMFTT 11
MMTTF 13
MMTFF 4
FTTTF 0
~%
39
46
14
0
selection, crossover, mutation
෍ 𝑓 𝑠 = 28
We want to improve with each generation, 
but our next generation is worse!
Average fitness dropped: 8.75 → 7
Best fitness dropped: 19 → 13
Total fitness dropped: 35 → 28
One solution: Elitism! Always keep the best individual(s) from the previous generation; 
we can modify the algorithm as:
5. New generation replaces old: {s} ← {t}, except:
       Keep the best k individuals from {s} in {t} (elitism)
The Next Generation
෍ 𝑓 𝑠 = 35

Genetic Algorithms: Key Parameters and Variations
Parameter / 
Choice
Options Recommendation
Population size 20-200 Larger for complex 
problems
Mutation Rate 0.01-0.1 Start with 1/n (n = 
chromosome length)
Generations 100-10000 Run until fitness 
plateaus
Selection Proportional / 
Rank / 
Tournament
Rank-based reduces 
extreme fitness 
effects
Crossover Single-point / 
Multi-point / 
Uniform 
Single-point is 
standard, simple
Elitism Yes / No always keep best 
solution(s)
Variation Description Benefit
Elitism Keep best k 
individuals from 
previous generation
Never lose best solution 
found
Rank-based 
selection
Order raw fitness 
values and assign a 
rank (1, 2, 3, …)
Reduces influence of 
extreme fitness values
Multi-point 
crossover
Split at multiple 
positions instead of 
one
Increases genetic mixing
Adaptive 
mutation rate
Change μ over time 
(high → low)
More exploration early, 
exploitation later
Tournament 
selection
Pick best from 
random subset
Simpler than probability 
calculation 
Choosing Variations
Elitism (Recommended): ensures best solution is never lost
Rank-based selection: Useful when fitness values vary widely
Adaptive parameters: requires tuning and experimentation
• Could also train a neural network to recommend parameters

Genetic Algorithms: Challenges
Challenge Problem Solution Approaches
Encoding design How to represent solutions 
as chromosomes?
Design so crossover is meaningful;
Ensure mutations maintain validity
Premature 
convergence
All individuals become 
identical early
Higher mutation rate;
Use niching techniques (methods to maintain diversity by 
encouraging different subpopulations to explore different 
regions of the search space.
Parameter 
selection
Choosing N, μ, crossover 
rate (whether to apply 
crossover), etc.
Use rules of thumb (μ = 1/n);
Experiment;
Adaptive parameters
Computational cost Large populations × many 
generations 
GPU parallelization;
Adaptive stopping criteria:
• No improvement stopping
• Convergence threshold
• Fitness target reached
• Rate of improvement is too slow

In Summary

Comparing the Three Approaches
Approach Local Optima? Population? Randomness? Parameters Best For
Hill Climbing Vulnerable Single state Deterministic Neighborhood 
definition
Simple problems, 
try first
Simulated 
Annealing
Better escape Single state Probabilistic Temperature, 
cooling rate
When HC gets 
stuck
Genetic 
Algorithms
Best escape Multiple states Probabilistic N, μ, selection, 
crossover
Hard, multimodal 
(many local 
optima) problems
Trade-offs
Hill climbing: Simplest, fastest per iteration, but gets stuck
Simulated annealing: More robust, requires tuning temperature
Genetic algorithms: Most complex, good for hard problems, many parameters

What We Saw
1. Optimization problems require different techniques than path-finding
2. Local search is efficient but can get trapped in local optima
3. Randomness helps escape local optima
4. Nature-inspired algorithms (annealing, evolution) provide powerful metaphors
Some Advice
• Start simple (hill climbing) 
• Add sophistication as needed (simulated annealing, genetic algorithms)
• Experiment with parameters
• Consider problem structure when designing state encoding and neighborhoods
```
