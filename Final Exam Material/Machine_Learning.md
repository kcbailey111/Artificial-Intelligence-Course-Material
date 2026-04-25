# Machine Learning

This document was generated from text extracted from the **Final Exam Material** folder. Slide PDFs may have imperfect reading order; formulas and diagrams appear as plain text. Topics: supervised learning (linear models to neural networks), evaluation metrics, class imbalance (SMOTE), explainability (SHAP).

## Supervised Learning: Linear Models to Neural Networks

*Extracted from PDF: `9 Supervised Learning From Linear Models to Neural Networks.pdf`*

```
Supervised Learning: From 
Linear Models to Neural 
Networks

Machine Learning: The Big Picture
Reinforcement Learning: Learn from rewards and penalties
• Agent takes actions and receives feedback from environment
• Examples: game playing (chess, Go), robotics, autonomous driving
Unsupervised Learning: Find patterns in unlabeled data
• Data has inputs but no labeled outputs
• Examples: clustering customers, dimensionality reduction, anomaly detection
Supervised Learning: Learn from labeled examples
• Training data includes correct answers (labels)
• Examples: spam detection, image classification, price prediction
Machine Learning refers to algorithms that improve through experience by learning patterns 
from data rather than relying on explicit programming.
Our focus for 
the rest of 
the course.
Presented in 
272.
Already 
Introduced This!
Given
Data (examples, observations, interactions)
Goal
Learn patterns to make predictions or decisions

Supervised Learning: The Setup
Training Data
Learning 
Algorithm
Hypothesis: h
Inference
(Prediction)
𝑒1 =  𝑥11 , 𝑥21, … , 𝑥𝑛1  →  𝑦₁ 
𝑒2 =  𝑥12 , 𝑥22, … , 𝑥𝑛2  →  𝑦2
…
𝑒𝑚 = 𝑥1𝑚 , 𝑥2𝑚, … , 𝑥𝑛𝑚 →  𝑦𝑚
(input, output) pairs
Finds patterns
Learned Model 
hypothesis ℎ about the 
world; it approximates 
the true function.
ො𝑦 for new example 𝐱∗
feature−vector outputexample
Apply ℎ for inference 
on new inputs:
𝑒 = 𝐱, 𝑦  where 𝐱 ∈ ℝ𝑛 and 𝑦 ∈ ℝ
(describes 
regression, not 
classification)
Map feature vectors 
to predictions:
ො𝑦 = ℎ 𝐱∗
ℎ: ℝ𝑛 → ℝ
Find the best parameters 
𝜃 by minimizing error: min
𝜃
෍
𝑖=1
𝑚
ℎ 𝐱𝑖 − 𝑦𝑖 2
* Refers to a new example

Supervised Classification Example: Set
Task
 Classify whether 3 cards form a valid 
Set according to the rules of Set:
• “Same trait”: All three cards 
share the exact same version of a 
trait
• “All different”: Each of the three 
cards possesses a unique version 
of a trait, with no repeats
Features Color, Shape, Number, Shading


Supervised Classification Example: Set
Training
Data
[[red, oval, 1, solid], [red, diamond, 1, solid], [red, squiggle, 1, solid]]
[[red, oval, 1, solid], [green, oval, 2, striped], [purple, oval, 3, empty]]
[[red, oval, 1, solid], [red, oval, 2, striped], [green, diamond, 1, solid]]
Label 𝒚 ∈ 𝑺𝒆𝒕, 𝑵𝒐𝒕 𝑺𝒆𝒕
Learning Find ℎ that predicts whether a combination of 3 cards is a Set.
Inference Given 3 new cards* → predict 𝑺𝒆𝒕 or 𝑵𝒐𝒕 𝑺𝒆𝒕
Scenario 
Assume the 
machine does 
not know the 
rules of Set. 
That is, it must 
intuit the 
pattern from 
examples (i.e., 
no explicit 
programming of 
“all same or all 
different”).
𝑺𝒆𝒕
𝑵𝒐𝒕 𝑺𝒆𝒕
𝑺𝒆𝒕
... (many more labeled examples)
𝑺𝒆𝒕* indicates a new input vector
Machine Learning: We provide examples, algorithm learns ‘rules’.

(Two) Types of Supervised Learning
Regression
Predict continuous values
Classification
Predict discrete categories
The difference is the type of output we are predicting.
𝑦 ∈ ℝ 𝑦 ∈ {1,2, … , 𝑘} (class labels)Output
Predicts
Examples
Type
• house prices
• temperature
• stock prices
• blood pressure
• spam/not spam
• cat/dog
• disease/healthy
• Categorizing a product 
(electronics, clothing, 
etc.)
nano banana
How much? Which one?Core Question

Supervised Regression Example: Temperature
Task Predict temperature from time and weather conditions
Training
Data
e₁ = [6am, 20%, 80%] → 15°C
e₂ = [2pm, 10%, 40%] → 28°C
e₃ = [9pm, 60%, 70%] → 18°C
…
𝐱 = [hour, cloud_cover, humidity] ∈ ℝ3
𝑦 ∈ ℝ (in °C)
Learning Find ℎ that predicts temperature
Inference Given new conditions x* → predict temperature ŷ
Observe, we 
are visualizing 
the input 
points only.

start equation theta
min lower limit theta of , sum of open second paren y sub i. minus h open third paren y sub i. , , close third paren , close second paren , squared
start equation 
lambda
lambda to the asterisk operator equals argmin lower limit lambda of , v a. l i. d a. t i. o n sub e r r o r
Training Phase
Use training set to learn 
parameters 𝜃; minimize loss:
 min
𝜃
σ 𝑦𝑖 − ℎ 𝑦𝑖
2
Tuning/Validation Phase
Evaluate hyperparameter (𝜆) 
combinations on validation set.
Select the best model configuration 
(𝜆∗ = argmin
𝜆
𝑣𝑎𝑙𝑖𝑑𝑎𝑡𝑖𝑜𝑛_𝑒𝑟𝑟𝑜𝑟)
Testing Phase
Final evaluation on test set
Report generalization 
performance
Training, Tuning, and Testing Pipeline and Data
Learn model 
parameters (60-80%):
𝑒𝟏 = 𝐱𝟏, 𝑦1  , 
𝑒𝟐 = 𝐱𝟐, 𝑦2  ,
…,
𝑒𝐧 = 𝐱𝐧, 𝑦𝑛  
Each phase has a specific role and 
dataset because we want to prevent 
overfitting to our training data (where 
the model memorizes the training 
data and generalizes poorly).
Select hyperparameters (𝜆) 
(10-20%):
• Choose model 
complexity, 
regularization, etc.
• Never used for learning 
parameters
Final evaluation (10-20%):
• Never used during 
training or tuning
• Measures generalization 
to new data
60-80% 10-20% 10-20%

The Generalization Challenge
Overfitting
Model memorizes training data
Perfect on training set, poor on test set
Too complex for the amount of data
Underfitting
Model too simple
Poor on both training and test sets
Does not capture patterns in data
Goal
Balance complexity with generalization
Good training performance and good test performance
nano 
banana

Linear Regression

Univariate Linear Regression
𝒚 (output)
𝒙 (input feature)
𝒙, 𝒚
𝑦-intercept: 𝜽𝟎
Training data:
𝒙𝒊, 𝒚𝒊
Slope: 𝜽𝟏
Linear regression finds 
the line that best fits 
the training data.

Univariate Linear Regression: MSE
𝐞𝒊=𝒚𝒊−ෝ𝒚𝒊
We want predictions ෝ𝒚𝒊 
close to actual values 𝒚𝒊.
The error for example 𝑖:
𝐞𝒊 = ෝ𝒚𝒊 − 𝒚𝒊
The squared error for 
example 𝑖:
𝐞𝒊
2 = ෝ𝒚𝒊 − 𝒚𝒊 2
• Always positive
• Penalizes large 
errors more heavily
Mean Squared Error (MSE):
MSE = 1
𝑚min
𝜽𝟎,𝜽𝟏
෍
𝑖=1
𝑚
ෝ𝒚𝒊 − 𝒚𝒊 2
Our objective is to find 𝜽𝟎 
and 𝜽𝟏 that minimize MSE.
𝐞𝒊
2

Multivariate Linear Regression
𝐱 = 𝑥1, 𝑥2, … , 𝑥𝑛 ∈ ℝ𝑛 Input 𝑥1, 𝑥2, … , 𝑥𝑛: feature values (e.g., size, bedrooms, age)
𝛉 = 𝜃0, 𝜃1, 𝜃2, … , 𝜃𝑛 ∈ ℝ𝑛+1 Parameters
𝜃0: intercept
𝜃1, 𝜃2, … , 𝜃𝑛: weights for each feature
ො𝑦 = ℎ𝛉 𝐱 = 𝜃0 + 𝜃1𝑥1 + 𝜃2𝑥2 + ⋯ + 𝜃n𝑥n = 𝛉 ⋅ 𝐱Model (𝐱 is augmented 
with 𝑥₀ = 1)
1
𝑚min
𝛉
෍
𝑖=1
𝑚
ෝ𝒚𝒊 − 𝒚𝒊 2Find 𝛉 that minimizes MSE:Training
Inference: ℎ𝛉: ℝ𝑛+1 → ℝResult
(Same principle  as univariate)
Maps feature vectors to 
predictions using learned 𝛉


Example: Predicting House Prices
𝑥1: size (in 𝑓𝑡2) 𝑥2: number of bedroomsFeatures
Training 
Data
ො𝑦 = 50 + 0.1𝑥1 + 30𝑥2Model
• 𝜃0 = 50: Base price ($50K)
• 𝜃1 = 0.1: Each 𝑓𝑡2 adds $100
• 𝜃2 = 30: Each bedroom adds $30K
ො𝑦 = ℎ 1800, 3 = 50 + 0.1 ⋅ 1800 + 30 ⋅ 3 = 320K
Inference 
Example


Example: Email Spam Detection
𝑥1 = 𝑓𝑟𝑒𝑞("𝑓𝑟𝑒𝑒")Features
Training 
Data
Model
Inference 
Example
𝑥2 = 𝑓𝑟𝑒𝑞("𝑚𝑜𝑛𝑒𝑦")
ො𝑦 = 0.16 + 0.61𝑥1 + 0.54𝑥2
• 𝜃0 = 0.16: Base prediction
• 𝜃1 = 0.61: Weight for “free” frequency
• 𝜃2 = 0.54: Weight for “money” frequency
ො𝑦 = ℎ freq("free") = 0.70, freq("money") = 0.60 = 0.16 + 0.61 ⋅ 0.70 + 0.54 ⋅ 0.60 = 0.911
𝑥1 = 𝑓𝑟𝑒𝑞("𝑓𝑟𝑒𝑒") 𝑥2 = 𝑓𝑟𝑒𝑞("𝑚𝑜𝑛𝑒𝑦") ෝ𝒚
0.10 0.05 Not Spam 
0.80 0.70 Spam
0.05 0.10 Not Spam 
0.90 0.60 Spam
0.15 0.20 Not Spam 
0.65 0.85 Spam
• Real-valued output does not directly correspond to discrete classes
• Linear regression produces a real number (0.91);  we need Spam or Not SpamProblem
We need a better approach…
Logistic Regression
• Predictions are unbounded and can be < 0 or > 1
• We want to interpret the result as a probability: 𝑃(spam ∣ 𝐱), not 
an arbitrary number

Training Linear Regression
We will consider an iterative method called 
gradient descent.
ො𝑦 = ℎ𝛉 𝐱 = 𝜃0 + 𝜃1𝑥1 + 𝜃2𝑥2 + ⋯ + 𝜃n𝑥n = 𝛉 ⋅ 𝐱 Our goal for training is to find 
parameters 𝛉 that minimize 
prediction error.
Mean Squared Error as Loss function for Linear Regression
𝑀𝑆𝐸 𝛉 = 1
𝑚min
𝛉
෍
𝑖=1
𝑚
ℎ𝛉 𝐱𝑖 − 𝒚𝒊 2
A Loss Function measures prediction error.
• Training attempts to  minimize loss
• The lower the loss results in better 
predictions
How do we find the optimal parameters 𝛉∗ that 
minimizes 𝑀𝑆𝐸 𝛉 ?

What is a Gradient?
Recall, our model has 𝑛 + 1 parameters 𝛉 = 𝜃0, 𝜃1, 𝜃2, … , 𝜃𝑛 ∈ ℝ𝑛+1.
How do we decide how to increase or decrease each parameter? Again, our goal 
is to reduce the loss, 𝑀𝑆𝐸 𝛉 . 
For a function 𝑓, the gradient ∇𝑓 is a 
mathematical construct that helps us identify 
the direction and rate of the steepest increase.
Thus, we are interested in computing ∇𝑀𝑆𝐸 𝛉 .
In a multivariable setting,∇𝑓 is a vector of 
partial derivatives, where each component 
represents how sensitive the function is to 
changes in one variable
∇𝑀𝑆𝐸 𝛉 = 𝜕𝑀𝑆𝐸
𝜕𝜃0
, 𝜕𝑀𝑆𝐸
𝜕𝜃1
, 𝜕𝑀𝑆𝐸
𝜕𝜃2
, … , 𝜕𝑀𝑆𝐸
𝜕𝜃𝑛
In gradient descent, we move opposite the gradient (downhill) to minimize MSE.

The Optimization Problem
Suppose our training data is defined as 
𝐗𝑚×(𝑛+1) (examples × features) with 
corresponding true output vector 𝐘𝑚×1.
Each of the 𝑚 rows of 𝐗𝑚×(𝑛+1) is a 
training example: 1, 𝑥1, 𝑥2, … , 𝑥𝑛
𝛉 = 𝜃0, 𝜃1, 𝜃2, … , 𝜃𝑛 ∈ ℝ𝑛+1
The linear system
𝑀𝑆𝐸 𝛉 = 1
𝑚min
𝛉
෍
𝑖=1
𝑚
ℎ𝛉 𝐱𝑖 − 𝒚𝒊 2
𝐗 ⋅ 𝛉 = 𝐘.
Now that we understand gradients, we can use them to solve our optimization problem. Gradients 
point uphill, so gradient descent moves downhill toward a minimum of our loss (error) function.
Training 
Data
Parameters
Model
Loss Function

Gradient Descent (Iterative Optimization)
Idea: Start with random 𝛉, iteratively improve it.
Initialize 𝛉 randomly (or to zeros)
repeat until convergence:
• for all training examples 𝑖 = 1, … , 𝑚, 
compute predictions:
• for all training examples 𝑖 = 1, … , 𝑚, 
compute errors:
ෝ𝑦𝑖 = ℎ𝛉 𝐱𝑖 = 𝛉𝐓𝐱𝒊
𝐞𝒊 = ෝ𝒚𝒊 − 𝒚𝒊
∇𝑀𝑆𝐸 𝛉 = 1
𝑚min
𝛉
෍
𝑖=1
𝑚
𝐞𝒊𝐱𝑖
𝛉 := 𝛉 − 𝛼 ⋅ ∇𝑀𝑆𝐸 𝛉
• Compute the direction of steepest increase 
(gradient):
• Update all parameters simultaneously in the 
direct of the steepest decrease:
• If MSE is decreasing by less than 𝜖 per 
iteration, stop (as the algorithm converged)
return 𝛉∗
𝛼: learning rate that 
controls step size

Example: Single Gradient Descent Update I
Setup 𝐱 = 1,2 , true label 𝑦 = 1One training example:
Initial parameters: 𝛉 = 0.5,0.2  
Learning Rate: 𝛼 = 0.1
Step 1: Compute Prediction ො𝑦 = ℎ𝛉 𝐱𝑖 = 𝛉𝐓𝐱𝒊 = 0.5 ⋅ 1 + 0.2 ⋅ 2 = 0.9
Step 2: Compute Error 
Step 3: Compute Gradient
𝐞 = ො𝑦 − 𝒚 = 0.9 − 1 = −0.1
Step 4: Update Parameters 𝛉 := 𝛉 − 𝛼 ⋅ ∇𝑀𝑆𝐸 𝛉
∇𝑀𝑆𝐸 𝛉 = 𝐞 ⋅ 𝐱 = −0.1 ⋅ 1,2 = −0.1, −0.2
𝛉 := 0.5,0.2 − 0.1 ⋅ −0.1, −0.2
𝛉 = 0.51,0.22
New Prediction: ො𝑦2 = 0.51 ⋅ 1 + 0.22 ⋅ 2 = 0.95 ො𝑦3 = 0.515 ⋅ 1 + 0.23 ⋅ 2 = 0.975

Monitoring Training: Loss Curves
Learning Rate Loss Pattern Interpretation Action
𝛼 too small Very slow decrease Creeping toward minimum Increase 𝛼
𝛼 just right Smooth decrease, plateaus Converged successfully Continue or stop
𝛼 too large Oscillates or increases Overshooting the minimum Decrease 𝛼
Early Stopping: Stop training when MSE 
improvement stalls (change < small threshold 𝜖). 
𝛉 := 𝛉 − 𝛼 ⋅ ∇𝑀𝑆𝐸 𝛉


Gradient Descent Variants
Variant Data Used Updates 
Per Epoch
Speed Stability Best For
Batch All 𝑚 examples 1 Slow Accurate Small Datasets
Stochastic (SGD) 1 random sample 𝑚 Fast Noisy Not recommended 
for fixed datasets
Mini-Batch Small batch (e.g., 𝑏 =
32)
𝑚
32
Fast Stable Standard Practice
Trade-Offs
• More data per update → fewer updates per 
epoch, slower per-epoch progress
• Less data per update → more updates per 
epoch, but each update is noisier
• Mini-batch balances: ~30 updates per epoch 
and stable gradients
Epoch: One complete pass through all training data
Standard practice: Train for multiple epochs using 
mini-batch gradient descent. Each epoch: shuffle 
data, compute 
𝑚
32 mini-batch updates, evaluate on 
validation set.

Training Linear Regression: Summary
The problem: Find 𝛉 that minimizes
 𝑀𝑆𝐸 𝛉 =
1
𝑚 σ𝑖=1
𝑚 ℎ𝛉 𝐱𝑖 − 𝒚𝒊 2
Solution 1: Normal Equation Solution 2: Gradient Descent
𝛉∗ = 𝐗𝐓𝐗
−𝟏
𝐗𝐓𝐲
• Direct computation so there is no iteration.
• Impractical for large 𝑛
𝛉 := 𝛉 − 𝛼 ⋅ ∇𝑀𝑆𝐸 𝛉
• Scales to big data
• Requires tuning 𝛼
Gradient descent is the fundamental optimization 
algorithm in machine learning. It works for:
• Linear regression
• Logistic regression
• Deep Neural networks
where 𝐲 is the target vector (actual labels for all 
𝑚 examples).  

Logistic Regression

Logistic Regression
Problem: Linear regression outputs real numbers (e.g., 0.91). For classification, we need probabilities or discrete 
classes.
Solution: Use the sigmoid function to squash outputs to a range of 0, 1 : 𝜎(𝑧) = 1
1 + 𝑒−𝑧
 where 𝑧 = 𝛉𝐓𝐱.
Model definition:
Logistic Regression = Linear model + Sigmoid activation
1. Apply sigmoid: ො𝑦 = 𝜎 𝛉𝐓𝐱 ∈ 0,1
2. Output: Probability for binary classification: 
𝑃(𝑐𝑙𝑎𝑠𝑠 = 1 ∣ 𝐱)
Training: Same gradient descent as before, but with different 
loss function (cross-entropy instead of MSE)
ො𝑦 > 0.5
Predict Class 1
ො𝑦 ≤ 0.5
Predict Class 0

Sigmoid Properties
lim
𝑧→−∞
𝜎 𝑧 = 0
lim
𝑧→∞
𝜎 𝑧 = 1
Inflection point at z = 0
Bounded output interpretable for 
classification.
Efficient derivative: The derivative depends 
only on the output value, so it can be 
computed once during backpropagation.
𝜎′(𝑧) = 𝜎(𝑧) 1 − 𝜎(𝑧)
Monotonically Increasing: Unambiguous 
relationship: as 𝑧 increases, 𝜎(𝑧) increases. 
Non-linear S-Shape: Learns non-linear decision boundaries. Pure 
linearity would fail for overlapping or non-separable classes.
Flexible decision 
boundaries; can 
handle complex 
patterns
Clear cause-effect 
between inputs and 
predictions
Gives valid 
probabilities. 
Fast gradient 
computation during 
training
Why these matter 
for Classification

Loss Function for Probability Predictions
Why CE Works?
• Sigmoid outputs are probabilities.
• Cross-entropy is designed to measure “how likely was the true label?” This is a natural fit for classification.
True Label = 1
Prediction MSE Loss Cross-Entropy 
Loss
MSE 
Interpretation
Cross-Entropy 
Interpretation
0.01 (very wrong) 1 − 0.01 2 = 0.98 −log 0.01 ≈ 4.6 small error huge penalty
0.5 (also wrong) 1 − 0.5 2 = 0.25 −log 0.5 ≈ 0.69 smaller error moderate penalty
• Both predictions look like “small errors”.
• MSE has weak gradients when most 
wrong: learning signal gets dampened at 
extremes.
• Confident mistakes (0.01) are heavily 
penalized.
• Strong gradients when most wrong thus it 
learns fast from confident mistakes.
MSE CE

Logistic Regression is a Single-Layer NN
Neural networks are built by stacking these layers:
• More layers = deeper networks
• Different activation functions (𝑅𝑒𝐿𝑈, tanh)
• Same optimization principle: gradient 
descent with appropriate loss function
This is logistic regression. 
It is a neural network!
Now we can evaluate it: Precision, Recall, 
F1, AUC all apply to classifiers like this.
𝑧 = 𝛉𝐓𝐱 𝜎 𝑧 ∈ 0,1
Input Features
```

## Evaluation Metrics (deck 1)

*Extracted from PDF: `10 Evaluation Metrics.pdf`*

```
Evaluation Metrics

Accuracy
Definition. The accuracy of a classifier 𝑴 on a dataset of 𝑛 examples is given by: 
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦(𝑴)  = 𝑖 ∶ 𝑴 𝐱𝑖 = 𝑦𝑖
𝑛
where:
• 𝐱𝑖: input features for example 𝑖, 
• 𝑦𝑖 ∈ {1, 2, … , 𝑘}: example 𝑖 is one of k classes, and
• 𝑴 𝐱𝑖 ∈ {1, 2, … , 𝑘}: predicted label for example 𝑖.
= # correct predictions
𝑛
Example. Suppose we have an animal image classifier with 𝑘 = 3 
classes: 𝑐𝑎𝑡, 𝑏𝑖𝑟𝑑, 𝑑𝑜𝑔 .
Also suppose we have a dataset with 100 images 
and the following results.
Predicted 
Cat
Predicted 
Dog
Predicted 
Bird
Actual 
Cat
70 5 0
Actual 
Dog
8 12 0
Actual 
Bird
3 0 2
TOTAL
75
20
5
TOTAL 81 17 2 100
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 𝑴 = 70 + 12 + 2
100 = 0.84
What is the problem with using accuracy with this dataset?
A naive classifier always predicting “cat” gets 75% accuracy.
High overall accuracy masks poor performance on rare classes!

The Confusion Matrix
Definition. For a classifier with 𝑘 > 2 classes, the confusion matrix is a 𝑘 × 𝑘 table given by:
where 𝐶𝑖,𝑗 is the count: 𝑒𝑥𝑎𝑚𝑝𝑙𝑒𝑠 𝑤𝑖𝑡ℎ 𝑡𝑟𝑢𝑒 𝑐𝑙𝑎𝑠𝑠 𝑖, 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 𝑎𝑠 𝑐𝑙𝑎𝑠𝑠 𝑗 .
We observed the use of a matrix to present the results of a classifier in the last example. Let’s formalize this notion. 
ො𝑦 = 1 ො𝑦 = 2 … ො𝑦 = 𝑘
𝑦 = 1 𝐶1,1 𝐶1,2 … 𝐶1,𝑘
𝑦 = 2 𝐶2,1 𝐶2,2 … 𝐶2,𝑘
… … … … …
𝑦 = 𝑘 𝐶𝑘,1 𝐶𝑘,2 … 𝐶𝑘,𝑘
Actual
Predicted
The main diagonal gives us the counts of correct predictions; all others are mis-classifications.

The Confusion Matrix
Predicted Positive Predicted Negative
Actually Positive True Positive (𝑇𝑃) False Negative (𝑭𝑵)
Actually Negative False Positive (𝑭𝑷) True Negative (𝑇𝑁)
It is most common for us to consider 
confusion matrices for binary classifiers and 
refer to the labels as 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒, 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑒.
When 𝑘 > 2, per-class metrics are obtained by reducing 
to 𝑘 binary classification problems (one-vs-all).
In the 𝑐𝑎𝑡, 𝑏𝑖𝑟𝑑, 𝑑𝑜𝑔  example, we would treat cats 
as positive, {dog, bird} as negative, then repeat for 
each class taking on the positive moniker.
There are 4 possible outcomes we visualize 
as the binary confusion matrix. 

Evaluating Impact vs. Accuracy I
In many real-world scenarios, one type 
of error is much worse than another.
Consider a scenario where missing a 
disease diagnosis is dangerous.
Sick Healthy
Sick CORRECT DIAGNOSIS (𝑇𝑃)
Patient receives life-saving treatment.
Outcome: Survival
MISSED DIAGNOSIS (𝑭𝑵)
Patient is sent home while sick; disease 
progresses without care.
Outcome: Dangerous / Critical
Healthy FALSE ALARM (𝑭𝑷)
Patient undergoes unnecessary stress and extra 
testing.
Outcome: Inconvenience / Anxiety
CLEAN BILL OF HEALTH (𝑇𝑁)
Healthy patient is correctly reassured.
Outcome: Peace of Mind
Actual
Predicted

Evaluating Impact vs. Accuracy II
Consider a scenario where the justice system must decide if a defendant is guilty or innocent.
Guilty Not Guilty
Guilty JUSTICE SERVED (𝑇𝑃)
The perpetrator is held accountable for their 
actions.
Outcome: Justice
ACQUITTAL BY ERROR (𝑭𝑵)
A guilty person is released back into society.
Outcome: Public Risk
Not Guilty WRONGFUL CONVICTION (𝑭𝑷)
An innocent person is convicted and deprived of 
their liberty.
Outcome: Miscarriage of Justice
EXONERATION (𝑇𝑁)
The innocent person is correctly cleared of all 
charges.
Outcome: Freedom Preserved
Actual
Predicted

Questions
If you were designing an Airport Security Scanner, 
which box would you be most afraid of, and why?
Positive Negative
Positive True Positive (𝑇𝑃) False Negative (𝑭𝑵)
Negative False Positive (𝑭𝑷) True Negative (𝑇𝑁)
Actual
Predicted
False Negative (“Miss”): A threat (weapon/explosive) 
passes through undetected, risking catastrophic loss of life.
False Positive (“False Alarm”): A harmless item triggers an alarm, 
resulting only in a minor delay or manual search.
If you are an e-commerce giant building a “Fraud 
Detection” system to auto-block credit cards, why 
are you terrified of a False Positive?
A False Positive means you just blocked a loyal 
customer's legitimate purchase. The Consequence 
may be that the immediate sale is lost, we frustrate 
the customer, and likely drive them to a competitor.
(A False Negative occurs when a stolen credit card is used, but the 
model fails to flag it and allows the transaction to go through.)
When an automated sensor scans $1,000 smartphone 
screens for cracks, why is a mistake in either direction 
a disaster?
Both mistakes hit the “bottom line” equally hard.
• The False Negative is a cracked screen reaches a 
customer, leading to expensive returns and a 
damaged reputation.
• The False Positive is a perfect, expensive screen 
is thrown in the trash, directly wasting profit.

Precision
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a measurement that tells us: Of all the times the 
model predicted positive, how often was it actually right?
If your email spam filter 
identifies 100 emails as 
Junk, but 20 of them were 
actually important 
messages, is your filter 
doing a good job?
The Experience: The user stops trusting the filter. They feel forced to check the Junk 
folder every day anyway, just in case the filter made a mistake.
The Lesson: It is not enough to catch a lot of junk; you have to be accurate in your 
accusations. If you say something is Junk, you better be right, or you are just creating 
more work for the user.
Definition. The Precision of a binary 
classifier 𝑀 is the fraction of positive 
predictions that are correct:
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 = 𝑇𝑃
𝑇𝑃 + 𝑭𝑷 
We need a way to measure trust.
If you arrest everyone on the street, you 
will definitely catch the thief, but you just 
ruined the lives of thousands of innocent 
people.

Recall
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a measurement that tells us: Of all the actual positive 
cases that exist, how many did the model find?
If a massive earthquake is 
starting, but your system 
stays silent because it 
wasn’t “100% sure” it 
wasn't just a heavy truck 
driving by, what happens?
The Experience: You do not care if the alarm goes off once in a while for a false 
vibration (a False Alarm). You only care that when a real disaster happens, the 
alarm sounds every single time.
The Lesson: When lives are at stake, hesitation is the greatest risk. We prefer a 
system that is highly sensitive: one that triggers easily rather than one that waits 
for perfect certainty while the danger slips by.
Definition. The Recall of a binary 
classifier 𝑀 is the fraction of actual 
positives that are correctly identified:
𝑅𝑒𝑐𝑎𝑙𝑙 𝑀 = 𝑇𝑃
𝑇𝑃 + 𝑭𝑵 
We need a way to measure coverage.
Recall is finding every rock that falls; in 
safety, we maximize this metric to ensure a 
single miss does not become a catastrophe.

Precision & Recall 
  Soundness & Completeness
A reminder about what we learned from Logic. A proof system or reasoning system is:
Sound: Every conclusion is correct. Complete Every truth can be proven.
No false positives! No false negatives!
Logic Classification Metric
Sound (no false proofs) Few false positives 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛
Complete (proves all truths) Few false negatives 𝑅𝑒𝑐𝑎𝑙𝑙
Sound and Complete
(Both approaches always give the 
same answer.)
Perfect Positive Classification
{ Predicted positive } = { Actual positive }
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =  𝑅𝑒𝑐𝑎𝑙𝑙 =  1
In logic, there are many interesting systems that are either sound OR complete, not both. In Machine Learning, 
most classifiers must trade off 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 and 𝑅𝑒𝑐𝑎𝑙𝑙; achieving both equal to 1 is rare.
Important Note: This only guarantees correct handling of positives. (True negatives are not considered.)

The Precision-Recall Tradeoff
• Blue curve: Distribution of actual 
negatives across predicted 
probabilities.
• Orange curve: Distribution of actual 
positives across predicted probabilities
• Overlap region: Where the model is 
uncertain: where errors happen
• Move threshold left: Catch more positives (↑ Recall) but 
more false alarms (↓ Precision)
• Move threshold right: Fewer false alarms (↑ Precision) but 
miss more positives (↓ Recall)
There is no “correct” threshold — it 
depends on the cost of each type of 
error.
The Tradeoff


With a measurement, how can we 
balance 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 and 𝑅𝑒𝑐𝑎𝑙𝑙?


Harmonic Mean
Calculate the average speed a car travels on a round trip where outbound we travel 60 miles at 30 mph and on the 
return trip, we travel 60 miles at 60 mph.
Arithmetic Mean Geometric Mean Harmonic Mean
30 + 60
2  =  45 𝑚𝑝ℎ
Predicted
Total Time
Average
1
45  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 2.67 ℎ𝑜𝑢𝑟𝑠
We can informally compute the total time and then the average speed.
30 ⋅ 60 = 42.426 𝑚𝑝ℎ
1
42.426  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 2.828 ℎ𝑜𝑢𝑟𝑠
2
1
30 + 1
60
=  40.0 𝑚𝑝ℎ
1
40.0  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 3.0 ℎ𝑜𝑢𝑟𝑠
Speed is a rate
𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒
𝑡𝑖𝑚𝑒 . When averaging 
rates, we use the  harmonic mean.
𝐻 = 𝑛
1
𝑟1
+ 1
𝑟2
+ ⋯ 1
𝑟𝑛
𝐴𝑣𝑔 𝑠𝑝𝑒𝑒𝑑 = 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒
𝑡𝑖𝑚𝑒 = 120𝑚𝑖𝑙𝑒𝑠
3 ℎ𝑜𝑢𝑟𝑠 = 40𝑚𝑝ℎ𝑇𝑜𝑡𝑎𝑙 𝑡𝑖𝑚𝑒= 60𝑚𝑖𝑙𝑒𝑠
30𝑚𝑝ℎ + 60𝑚𝑖𝑙𝑒𝑠
60𝑚𝑝ℎ = 3ℎ𝑜𝑢𝑟𝑠
Let us try different averaging mechanisms.

𝐹1 Score
𝐻 = 2
1
𝑃 + 1
𝑅
= 2
𝑃 + 𝑅
𝑃𝑅
= 2𝑃𝑅
𝑃 + 𝑅
How can we average 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 (𝑃) and 𝑅𝑒𝑐𝑎𝑙𝑙 (𝑅)?
Note, each of these values are rates (with no units).
So, 
Definition. The 𝑭𝟏 score of a binary classifier 𝑀 is the harmonic mean of precision and recall:
𝐹1 𝑀 = 2 ⋅ 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 ⋅ 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 + 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀  
where 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 =
𝑇𝑃
𝑇𝑃+𝑭𝑷 and 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀 =
𝑇𝑃
𝑇𝑃+𝑭𝑵.
𝐹𝛽 𝑀 = 1 + 𝛽2 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 ⋅ 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀
𝛽2 ⋅ 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 + 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀  
We can also give weight to 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 or 𝑅𝑒𝑐𝑎𝑙𝑙 using the 
generalized 𝛽 version.
When 𝛽 = 1 each have equal weight as defined above.
𝛽 = 2 weights 𝑅𝑒𝑐𝑎𝑙𝑙 twice as much as 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 (since 
𝛽2 is in the denominator). 


Examples: 𝐹1 Score
Calculate 𝐹1 for each confusion matrix.
Spam Not
Spam 47 3
Not 47 3
Actual
Predicted
Spam Not
Spam 25 25
Not 1 49
Actual
Predicted
Spam Not
Spam 45 5
Not 5 45
Actual
Predicted
𝑷𝒓𝒆𝒄𝒊𝒔𝒊𝒐𝒏
𝑹𝒆𝒄𝒂𝒍𝒍
𝑭𝟏
47
47 + 47 = 0.5
47
47 + 3 = 0.94
2 ⋅ 0.5 ⋅ 0.94
0.5 + 0.94 = 0.6528
25
25 + 1 = 0.9615
25
25 + 25 = 0.5
2 ⋅ 0.9615 ⋅ 0.5
0.9615 + 0.5 = 0.6579
45
45 + 5 = 0.9
45
45 + 5 = 0.9
2 ⋅ 0.9 ⋅ 0.9
0.9 + 0.9 = 0.9
Too many false alarms. Misses too much spam. ‘Well’ balanced.

Remember: Cross Entropy as an Evaluation Metric
From our NLP discussion on entropy and 
information theory... Cross Entropy measures 
how well a model's predicted distribution 
matches the true distribution.
Definition. For two probability 
distributions 𝑻 (ground truth distribution) 
and 𝑴 (model distribution) over the same 
set of outcomes 𝑐₁, 𝑐₂, … , 𝑐𝐾 , the cross 
entropy of 𝑻 with respect to 𝑴 is given by
𝐶𝑟𝑜𝑠𝑠𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑻, 𝑴 = − ෍
𝑖=1
𝐾
𝑝𝑐𝑖 log2 𝑞𝑐𝑖
where 𝑝𝑐𝑖 is the true probability of outcome 
𝑐𝑖 and 𝑞𝑐𝑖 is the predicted probability of 
outcome 𝑐𝑖.
Recall: Cross entropy measures how “surprised” a model is by 
the actual outcomes.
• Low CE → The model expected what actually happened
• High CE → The model was surprised by reality
• We sample from 𝑻 (reality)
• We measure surprise using 𝑴's beliefs
• log2 𝑞𝑐𝑖 is the model's surprise when 
event 𝑐𝑖 occurs
• We weight by 𝑝𝑐𝑖 how often 𝑐𝑖 actually 
happens

Why Confidence Matters
Suppose two spam classifiers both achieve 80% accuracy. Are they equally good?
Accuracy tells you what the model got right; however, cross entropy tells you how well the 
model's probability estimates match reality.
In some cases, cross 
entropy reveals problems 
that accuracy hides.
Model A (Calibrated) Model B (Overconfident)
When correct “Probably spam” “Definitely spam”
When wrong “Not sure, maybe spam?” “Definitely spam”
Why the difference?
• Model B is confidently 
wrong with its mistakes.
• Cross entropy penalizes 
confident mistakes more 
heavily than hesitant ones.
• Medical diagnosis: “90% vs 55% chance of cancer” require different follow-
ups, even if both exceed a threshold
• Weather forecasting: “90% vs 60% chance of rain” affects whether you 
cancel the outdoor wedding.
• ER triage: Must prioritize patients by actual risk level, not just “at risk” vs 
“not at risk”
Cross Entropy Lower Higher

Cross Entropy vs. 
Accuracy/𝐹1/Precision/Recall
These metrics 
answer different 
questions.
These metrics are complementary, not 
competing: use accuracy/𝐹1/precision/recall 
to evaluate decisions, use cross entropy to 
evaluate confidence.
Accuracy / F1 / Precision / Recall Cross Entropy
Question "Did we decide correctly?" "Are our probabilities trustworthy?"
Operates on Hard predictions (class labels) Soft predictions (probabilities)
Evaluates Decision quality Probability quality
Throws away Probability information Nothing
Suppose we have predictions with probabilities
𝑝 = 0.51 and 𝑝 = 0.99.
These are identical to accuracy/𝐹1/precision/recall (both predict 
positive classification), but they are very different to cross entropy.
nano banana

Beyond 𝐹1: True Negatives
𝐹1 Score combines Precision and Recall, but ignores True Negatives.
This matters as many applications, correctly identifying negatives is just as important as identifying positives.
If you were designing an Airport Security Scanner, which box would you be most afraid of, and why?
Predicted Threat Predicted Safe
Actual Threat 40 60
Actual Safe 200 700
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= 40
240 = 0.167
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
Predicted Threat Predicted Safe
Actual Threat 35 65
Actual Safe 10 890
Classifier A Classifier B
• Classifier A flags 200 innocent passengers compared to 
10 for Classifier B
• 200 more false positives means 200 fewer true negatives. 
𝑅𝑒𝑐𝑎𝑙𝑙 = 40
100 = 0.4 𝐹1 = 0.235
The false positives are a critical operational 
difference; the 𝐹1 scores slightly reveal this 
cost.
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= 35
45 = 0.777 𝑅𝑒𝑐𝑎𝑙𝑙 = 35
100 = 0.35 𝐹1 = 0.4828

How We Got Here
Metric What It Tells Us What It Ignores Consequence
Accuracy
Overall correctness: percentage 
of all predictions that are 
correct
Class distribution
With imbalanced datasets, a naive 
"always predict majority class" 
classifier can achieve high accuracy
MCC
Overall correlation between 
predictions and reality across all 
four confusion matrix cells
Different error costs
Treats all errors equally; may not reflect 
scenarios where one error type is much 
more costly
Precision
Trust in positive predictions: 
when we predict positive, how 
often are we right?
False negatives
Can achieve perfect precision by being 
extremely conservative and missing 
most positives
Recall
Coverage of positives: of all 
actual positives, how many did 
we find?
False positives Can achieve perfect recall by predicting 
everything as positive
𝑭𝟏
Balance between precision and 
recall for the positive class True negatives
Does not account for the cost of 
false positives when they create 
operational burdens
𝑇𝑃 + 𝑇𝑁
𝑇𝑃 + 𝑇𝑁 + 𝑭𝑵 + 𝑭𝑷 

Toward Matthews Correlation Coefficient (MCC)
What would a truly balanced metric look like?
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a metric that:
• Considers all four confusion matrix cells (not just 𝑇𝑃, 𝑭𝑷, 𝑭𝑵)
• Measures overall agreement between predictions and reality
• Treats both classes symmetrically
Can we measure agreement? Disagreement?
𝑇𝑃 ⋅ 𝑇𝑁 𝑭𝑷 ⋅ 𝑭𝑵
[Multiplication enforces an ‘and’ 
(joint) condition with the 
components.]
We can thus compute the difference between how much we (dis)agree:
 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵 Then, we need to normalize.

Matthews Correlation Coefficient (MCC)
MCC is a balanced correlation between predictions and truth, giving equal weight to 
all four parts of the confusion matrix.
Value Meaning
+1 Perfect prediction
0 No better than random guessing
-1 Total disagreement (perfectly wrong)
𝑀𝐶𝐶 = 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵
(𝑇𝑃 + 𝑭𝑷)(𝑇𝑃 + 𝑭𝑵)(𝑇𝑁 + 𝑭𝑷)(𝑇𝑁 + 𝑭𝑵)
MCC applies the same correlation idea to binary outcomes.
Recall the correlation coefficient 𝑟 from statistics? That 
is the Pearson Correlation Coefficient (PCC): a measure 
of how two variables move together.
Agreement - Disagreement
: marginals
Predicted 
Positive
Actual 
Positives
Actual 
Negatives
Predicted 
Negatives


MCC Example
If you were designing an Airport Security Scanner, which box would you be most afraid of, and why?
Classifier A Classifier B
𝑀𝐶𝐶 = 40 ⋅ 700 − 𝟐𝟎𝟎 ⋅ 𝟔𝟎
(40 + 𝟐𝟎𝟎)(40 + 𝟔𝟎)(700 + 𝟐𝟎𝟎)(700 + 𝟔𝟎)
= 0.1249
𝑀𝐶𝐶 = 35 ⋅ 890 − 𝟏𝟎 ⋅ 𝟔𝟓
(35 + 𝟏𝟎)(35 + 𝟔𝟓)(890 + 𝟏𝟎)(890 + 𝟔𝟓)
= 0.4904
MCC clearly distinguishes the better classifier with greater granularity than 𝐹1 (0.235 vs 0.4828).
Predicted Threat Predicted Safe
Actual Threat 40 60
Actual Safe 200 700
Predicted Threat Predicted Safe
Actual Threat 35 65
Actual Safe 10 890

Suppose we have three spam filters, each with 50 spam and 50 legitimate emails:
Pred Spam Pred Not
Actual Spam 47 3
Actual Not 3 47
Actual Spam 25 25
Actual Not 1 49
Actual Spam 48 2
Actual Not 48 2
• Filters B and C have identical 
F1 scores but very different 
behavior.
• MCC correctly identifies both 
as equally mediocre.
MCC vs. 𝐹1: A Direct Comparison
Precision Recall F1 MCC
94% 94% 94% 0.88
96% 50% 66% 0.53
50% 96% 66% 0.53
Best practice is to report both metrics: 𝐹1 for alignment with the existing literature, 
and MCC to capture truly balanced performance.

With MCC, all four cells of the confusion matrix contribute equally to the 
result. This symmetry makes MCC particularly reliable for:
• Imbalanced datasets
• Cases where both classes matter equally
• Comparing classifiers with different precision/recall tradeoffs
MCC is Balanced
𝑀𝐶𝐶 = 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵
(𝑇𝑃 + 𝑭𝑷)(𝑇𝑃 + 𝑭𝑵)(𝑇𝑁 + 𝑭𝑷)(𝑇𝑁 + 𝑭𝑵)

Accuracy Precision Recall F1 MCC
Handles class 
imbalance?
No Partial Partial Partial Yes
Considers TN? Yes No No No Yes
Needs Companion 
Metrics?
Yes Yes Yes Yes No
Fully balanced? No No No Partial Yes
Best for… Balanced 
data
Trust Coverage Positive focus Overall 
balance
Choosing Your Metric
```

## Evaluation Metrics (deck 2)

*Extracted from PDF: `11 Evaluation Metrics.pdf`*

```
Evaluation Metrics

Accuracy
Definition. The accuracy of a classifier 𝑴 on a dataset of 𝑛 examples is given by: 
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦(𝑴)  = 𝑖 ∶ 𝑴 𝐱𝑖 = 𝑦𝑖
𝑛
where:
• 𝐱𝑖: input features for example 𝑖, 
• 𝑦𝑖 ∈ {1, 2, … , 𝑘}: example 𝑖 is one of k classes, and
• 𝑴 𝐱𝑖 ∈ {1, 2, … , 𝑘}: predicted label for example 𝑖.
= # correct predictions
𝑛
Example. Suppose we have an animal image classifier with 𝑘 = 3 
classes: 𝑐𝑎𝑡, 𝑏𝑖𝑟𝑑, 𝑑𝑜𝑔 .
Also suppose we have a dataset with 100 images 
and the following results.
Predicted 
Cat
Predicted 
Dog
Predicted 
Bird
Actual 
Cat
70 5 0
Actual 
Dog
8 12 0
Actual 
Bird
3 0 2
TOTAL
75
20
5
TOTAL 81 17 2 100
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 𝑴 = 70 + 12 + 2
100 = 0.84
What is the problem with using accuracy with this dataset?
A naive classifier always predicting “cat” gets 75% accuracy.
High overall accuracy masks poor performance on rare classes!

The Confusion Matrix
Definition. For a classifier with 𝑘 > 2 classes, the confusion matrix is a 𝑘 × 𝑘 table given by:
where 𝐶𝑖,𝑗 is the count: 𝑒𝑥𝑎𝑚𝑝𝑙𝑒𝑠 𝑤𝑖𝑡ℎ 𝑡𝑟𝑢𝑒 𝑐𝑙𝑎𝑠𝑠 𝑖, 𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 𝑎𝑠 𝑐𝑙𝑎𝑠𝑠 𝑗 .
We observed the use of a matrix to present the results of a classifier in the last example. Let’s formalize this notion. 
ො𝑦 = 1 ො𝑦 = 2 … ො𝑦 = 𝑘
𝑦 = 1 𝐶1,1 𝐶1,2 … 𝐶1,𝑘
𝑦 = 2 𝐶2,1 𝐶2,2 … 𝐶2,𝑘
… … … … …
𝑦 = 𝑘 𝐶𝑘,1 𝐶𝑘,2 … 𝐶𝑘,𝑘
Actual
Predicted
The main diagonal gives us the counts of correct predictions; all others are mis-classifications.

The Confusion Matrix
Predicted Positive Predicted Negative
Actually Positive True Positive (𝑇𝑃) False Negative (𝑭𝑵)
Actually Negative False Positive (𝑭𝑷) True Negative (𝑇𝑁)
It is most common for us to consider 
confusion matrices for binary classifiers and 
refer to the labels as 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑒, 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑒.
When 𝑘 > 2, per-class metrics are obtained by reducing 
to 𝑘 binary classification problems (one-vs-all).
In the 𝑐𝑎𝑡, 𝑏𝑖𝑟𝑑, 𝑑𝑜𝑔  example, we would treat cats 
as positive, {dog, bird} as negative, then repeat for 
each class taking on the positive moniker.
There are 4 possible outcomes we visualize 
as the binary confusion matrix. 

Evaluating Impact vs. Accuracy I
In many real-world scenarios, one type 
of error is much worse than another.
Consider a scenario where missing a 
disease diagnosis is dangerous.
Sick Healthy
Sick CORRECT DIAGNOSIS (𝑇𝑃)
Patient receives life-saving treatment.
Outcome: Survival
MISSED DIAGNOSIS (𝑭𝑵)
Patient is sent home while sick; disease 
progresses without care.
Outcome: Dangerous / Critical
Healthy FALSE ALARM (𝑭𝑷)
Patient undergoes unnecessary stress and extra 
testing.
Outcome: Inconvenience / Anxiety
CLEAN BILL OF HEALTH (𝑇𝑁)
Healthy patient is correctly reassured.
Outcome: Peace of Mind
Actual
Predicted

Evaluating Impact vs. Accuracy II
Consider a scenario where the justice system must decide if a defendant is guilty or innocent.
Guilty Not Guilty
Guilty JUSTICE SERVED (𝑇𝑃)
The perpetrator is held accountable for their 
actions.
Outcome: Justice
ACQUITTAL BY ERROR (𝑭𝑵)
A guilty person is released back into society.
Outcome: Public Risk
Not Guilty WRONGFUL CONVICTION (𝑭𝑷)
An innocent person is convicted and deprived of 
their liberty.
Outcome: Miscarriage of Justice
EXONERATION (𝑇𝑁)
The innocent person is correctly cleared of all 
charges.
Outcome: Freedom Preserved
Actual
Predicted

Questions
If you were designing an Airport Security Scanner, 
which box would you be most afraid of, and why?
Positive Negative
Positive True Positive (𝑇𝑃) False Negative (𝑭𝑵)
Negative False Positive (𝑭𝑷) True Negative (𝑇𝑁)
Actual
Predicted
False Negative (“Miss”): A threat (weapon/explosive) 
passes through undetected, risking catastrophic loss of life.
False Positive (“False Alarm”): A harmless item triggers an alarm, 
resulting only in a minor delay or manual search.
If you are an e-commerce giant building a “Fraud 
Detection” system to auto-block credit cards, why 
are you terrified of a False Positive?
A False Positive means you just blocked a loyal 
customer's legitimate purchase. The Consequence 
may be that the immediate sale is lost, we frustrate 
the customer, and likely drive them to a competitor.
(A False Negative occurs when a stolen credit card is used, but the 
model fails to flag it and allows the transaction to go through.)
When an automated sensor scans $1,000 smartphone 
screens for cracks, why is a mistake in either direction 
a disaster?
Both mistakes hit the “bottom line” equally hard.
• The False Negative is a cracked screen reaches a 
customer, leading to expensive returns and a 
damaged reputation.
• The False Positive is a perfect, expensive screen 
is thrown in the trash, directly wasting profit.

Precision
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a measurement that tells us: Of all the times the 
model predicted positive, how often was it actually right?
If your email spam filter 
identifies 100 emails as 
Junk, but 20 of them were 
actually important 
messages, is your filter 
doing a good job?
The Experience: The user stops trusting the filter. They feel forced to check the Junk 
folder every day anyway, just in case the filter made a mistake.
The Lesson: It is not enough to catch a lot of junk; you have to be accurate in your 
accusations. If you say something is Junk, you better be right, or you are just creating 
more work for the user.
Definition. The Precision of a binary 
classifier 𝑀 is the fraction of positive 
predictions that are correct:
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 = 𝑇𝑃
𝑇𝑃 + 𝑭𝑷 
We need a way to measure trust.
If you arrest everyone on the street, you 
will definitely catch the thief, but you just 
ruined the lives of thousands of innocent 
people.

Recall
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a measurement that tells us: Of all the actual positive 
cases that exist, how many did the model find?
If a massive earthquake is 
starting, but your system 
stays silent because it 
wasn’t “100% sure” it 
wasn't just a heavy truck 
driving by, what happens?
The Experience: You do not care if the alarm goes off once in a while for a false 
vibration (a False Alarm). You only care that when a real disaster happens, the 
alarm sounds every single time.
The Lesson: When lives are at stake, hesitation is the greatest risk. We prefer a 
system that is highly sensitive: one that triggers easily rather than one that waits 
for perfect certainty while the danger slips by.
Definition. The Recall of a binary 
classifier 𝑀 is the fraction of actual 
positives that are correctly identified:
𝑅𝑒𝑐𝑎𝑙𝑙 𝑀 = 𝑇𝑃
𝑇𝑃 + 𝑭𝑵 
We need a way to measure coverage.
Recall is finding every rock that falls; in 
safety, we maximize this metric to ensure a 
single miss does not become a catastrophe.

Precision & Recall 
  Soundness & Completeness
A reminder about what we learned from Logic. A proof system or reasoning system is:
Sound: Every conclusion is correct. Complete Every truth can be proven.
No false positives! No false negatives!
Logic Classification Metric
Sound (no false proofs) Few false positives 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛
Complete (proves all truths) Few false negatives 𝑅𝑒𝑐𝑎𝑙𝑙
Sound and Complete
(Both approaches always give the 
same answer.)
Perfect Positive Classification
{ Predicted positive } = { Actual positive }
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =  𝑅𝑒𝑐𝑎𝑙𝑙 =  1
In logic, there are many interesting systems that are either sound OR complete, not both. In Machine Learning, 
most classifiers must trade off 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 and 𝑅𝑒𝑐𝑎𝑙𝑙; achieving both equal to 1 is rare.
Important Note: This only guarantees correct handling of positives. (True negatives are not considered.)

The Precision-Recall Tradeoff
• Blue curve: Distribution of actual 
negatives across predicted 
probabilities.
• Orange curve: Distribution of actual 
positives across predicted probabilities
• Overlap region: Where the model is 
uncertain: where errors happen
• Move threshold left: Catch more positives (↑ Recall) but 
more false alarms (↓ Precision)
• Move threshold right: Fewer false alarms (↑ Precision) but 
miss more positives (↓ Recall)
There is no “correct” threshold — it 
depends on the cost of each type of 
error.
The Tradeoff


With a measurement, how can we 
balance 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 and 𝑅𝑒𝑐𝑎𝑙𝑙?


Harmonic Mean
Calculate the average speed a car travels on a round trip where outbound we travel 60 miles at 30 mph and on the 
return trip, we travel 60 miles at 60 mph.
Arithmetic Mean Geometric Mean Harmonic Mean
30 + 60
2  =  45 𝑚𝑝ℎ
Predicted
Total Time
Average
1
45  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 2.67 ℎ𝑜𝑢𝑟𝑠
We can informally compute the total time and then the average speed.
30 ⋅ 60 = 42.426 𝑚𝑝ℎ
1
42.426  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 2.828 ℎ𝑜𝑢𝑟𝑠
2
1
30 + 1
60
=  40.0 𝑚𝑝ℎ
1
40.0  ℎ𝑝𝑚 ⋅ 120 𝑚𝑖𝑙𝑒𝑠
= 3.0 ℎ𝑜𝑢𝑟𝑠
Speed is a rate
𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒
𝑡𝑖𝑚𝑒 . When averaging 
rates, we use the  harmonic mean.
𝐻 = 𝑛
1
𝑟1
+ 1
𝑟2
+ ⋯ 1
𝑟𝑛
𝐴𝑣𝑔 𝑠𝑝𝑒𝑒𝑑 = 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒
𝑡𝑖𝑚𝑒 = 120𝑚𝑖𝑙𝑒𝑠
3 ℎ𝑜𝑢𝑟𝑠 = 40𝑚𝑝ℎ𝑇𝑜𝑡𝑎𝑙 𝑡𝑖𝑚𝑒= 60𝑚𝑖𝑙𝑒𝑠
30𝑚𝑝ℎ + 60𝑚𝑖𝑙𝑒𝑠
60𝑚𝑝ℎ = 3ℎ𝑜𝑢𝑟𝑠
Let us try different averaging mechanisms.

F1 Score
𝐻 = 2
1
𝑃 + 1
𝑅
= 2
𝑃 + 𝑅
𝑃𝑅
= 2𝑃𝑅
𝑃 + 𝑅
How can we average 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 (𝑃) and 𝑅𝑒𝑐𝑎𝑙𝑙 (𝑅)?
Note, each of these values are rates (with no units).
So, 
Definition. The 𝑭𝟏 score of a binary classifier 𝑀 is the harmonic mean of precision and recall:
𝐹1 𝑀 = 2 ⋅ 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 ⋅ 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 + 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀  
where 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 =
𝑇𝑃
𝑇𝑃+𝑭𝑷 and 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀 =
𝑇𝑃
𝑇𝑃+𝑭𝑵.
𝐹𝛽 𝑀 = 1 + 𝛽2 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 ⋅ 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀
𝛽2 ⋅ 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑀 + 𝑅𝑒𝑐𝑎𝑙𝑙 𝑀  
We can also give weight to 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 or 𝑅𝑒𝑐𝑎𝑙𝑙 using the 
generalized 𝛽 version.
When 𝛽 = 1 each have equal weight as defined above.
𝛽 = 2 weights 𝑅𝑒𝑐𝑎𝑙𝑙 twice as much as 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛. 


Examples: F1 Score
Calculate 𝐹1 for each confusion matrix.
Spam Not
Spam 47 3
Not 47 3
Actual
Predicted
Spam Not
Spam 25 25
Not 1 49
Actual
Predicted
Spam Not
Spam 45 5
Not 5 45
Actual
Predicted
𝑷𝒓𝒆𝒄𝒊𝒔𝒊𝒐𝒏
𝑹𝒆𝒄𝒂𝒍𝒍
𝑭𝟏
47
47 + 47 = 0.5
47
47 + 3 = 0.94
2 ⋅ 0.5 ⋅ 0.94
0.5 + 0.94 = 0.6528
25
25 + 1 = 0.9615
25
25 + 25 = 0.5
2 ⋅ 0.9615 ⋅ 0.5
0.9615 + 0.5 = 0.6579
45
45 + 5 = 0.9
45
45 + 5 = 0.9
2 ⋅ 0.9 ⋅ 0.9
0.9 + 0.9 = 0.9
Too many false alarms. Misses too much spam. ‘Well’ balanced.

Remember: Cross Entropy as an Evaluation Metric
From our NLP discussion on entropy and 
information theory... Cross Entropy measures 
how well a model's predicted distribution 
matches the true distribution.
Definition. For two probability 
distributions 𝑻 (ground true distribution) 
and 𝑴 (model distribution) over the same 
set of outcomes 𝑐₁, 𝑐₂, … , 𝑐𝐾 , the cross 
entropy of 𝑻 with respect to 𝑴 is given by
𝐶𝑟𝑜𝑠𝑠𝐸𝑛𝑡𝑟𝑜𝑝𝑦 𝑻, 𝑴 = − ෍
𝑖=1
𝐾
𝑝𝑐𝑖 log2 𝑞𝑐𝑖
where 𝑝𝑐𝑖 is the true probability of outcome 
𝑐𝑖 and 𝑞𝑐𝑖 is the predicted probability of 
outcome 𝑐𝑖.
Recall: Cross entropy measures how “surprised” a model is by 
the actual outcomes.
• Low CE → The model expected what actually happened
• High CE → The model was surprised by reality
• We sample from 𝑻 (reality)
• We measure surprise using 𝑴's beliefs
• log2 𝑞𝑐𝑖 is the model's surprise when 
event 𝑐𝑖 occurs
• We weight by 𝑝𝑐𝑖 how often 𝑐𝑖 actually 
happens

Why Confidence Matters
Suppose two spam classifiers both achieve 80% accuracy. Are they equally good?
Accuracy tells you what the model got right; however, cross entropy tells you how well the 
model's probability estimates match reality
In some cases, cross 
entropy reveals problems 
that accuracy hides.
Model A (Calibrated) Model B (Overconfident)
When correct “Probably spam” “Definitely spam”
When wrong “Not sure, maybe spam?” “Definitely spam”
Why the difference?
• Model B is confidently 
wrong with its mistakes.
• Cross entropy penalizes 
confident mistakes more 
heavily than hesitant ones.
• Medical diagnosis: “90% vs 55% chance of cancer” require different follow-
ups, even if both exceed a threshold
• Weather forecasting: “90% vs 60% chance of rain” affects whether you 
cancel the outdoor wedding.
• ER triage: Must prioritize patients by actual risk level, not just “at risk” vs 
“not at risk”
Cross Entropy Lower Higher

Cross Entropy vs. 
Accuracy/F1/Precision/Recall
These metrics 
answer different 
questions.
These metrics are complementary, not 
competing: use accuracy/F1/precision/recall 
to evaluate decisions, use cross entropy to 
evaluate confidence.
Accuracy / F1 / Precision / Recall Cross Entropy
Question "Did we decide correctly?" "Are our probabilities trustworthy?"
Operates on Hard predictions (class labels) Soft predictions (probabilities)
Evaluates Decision quality Probability quality
Throws away Probability information Nothing
Suppose we have predictions with probabilities
𝑝 = 0.51 and 𝑝 = 0.99.
These are identical to accuracy/F1/precision/recall (both predict 
positive classification), but they are very different to cross entropy.
nano banana

Beyond F1: True Negatives
F1 Score combines Precision and Recall, but ignores True Negatives.
This matters as many applications, correctly identifying negatives is just as important as identifying positives.
If you were designing an Airport Security Scanner, which box would you be most afraid of, and why?
Predicted Threat Predicted Safe
Actual Threat 40 60
Actual Safe 200 700
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= 40
240 = 0.167
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
Predicted Threat Predicted Safe
Actual Threat 35 65
Actual Safe 10 890
Classifier A Classifier B
• Classifier A flags 200 innocent passengers compared to 
10 for Classifier B
• 200 more false positives means 200 fewer true negatives. 
𝑅𝑒𝑐𝑎𝑙𝑙 = 40
100 = 0.4 𝐹1 = 0.235
The false positives are a critical operational 
difference; the F1 scores slightly reveal this 
cost.
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛= 35
45 = 0.777 𝑅𝑒𝑐𝑎𝑙𝑙 = 35
100 = 0.35 𝐹1 = 0.4828

How We Got Here
Metric What It Tells Us What It Ignores Consequence
Accuracy
Overall correctness: percentage 
of all predictions that are 
correct
Class distribution
With imbalanced datasets, a naive 
"always predict majority class" 
classifier can achieve high accuracy
MCC
Overall correlation between 
predictions and reality across all 
four confusion matrix cells
Different error costs
Treats all errors equally; may not reflect 
scenarios where one error type is much 
more costly
Precision
Trust in positive predictions: 
when we predict positive, how 
often are we right?
False negatives
Can achieve perfect precision by being 
extremely conservative and missing 
most positives
Recall
Coverage of positives: of all 
actual positives, how many did 
we find?
False positives Can achieve perfect recall by predicting 
everything as positive
F1 Balance between precision and 
recall for the positive class True negatives
Doesn't account for the cost of 
false positives when they create 
operational burdens
𝑇𝑃 + 𝑇𝑁
𝑇𝑃 + 𝑇𝑁 + 𝑭𝑵 + 𝑭𝑷 

Toward Matthews Correlation Coefficient (MCC)
What would a truly balanced metric look like?
Positive Negative
Positive 𝑇𝑃 𝑭𝑵
Negative 𝑭𝑷 𝑇𝑁
Actual
Predicted
We need a metric that:
• Considers all four confusion matrix cells (not just 𝑇𝑃, 𝑭𝑷, 𝑭𝑵)
• Measures overall agreement between predictions and reality
• Treats both classes symmetrically
Can we measure agreement? Disagreement?
𝑇𝑃 ⋅ 𝑇𝑁 𝑭𝑷 ⋅ 𝑭𝑵
[Multiplication enforces an ‘and’ 
(joint) condition with the 
components.]
We can thus compute the difference between how much we (dis)agree:
 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵 Then, we need to normalize.

Matthews Correlation Coefficient (MCC)
MCC is a balanced correlation between predictions and truth, giving equal weight to all four parts of the 
confusion matrix.
Value Meaning
+1 Perfect prediction
0 No better than random guessing
-1 Total disagreement (perfectly wrong)
𝑀𝐶𝐶 = 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵
(𝑇𝑃 + 𝑭𝑷)(𝑇𝑃 + 𝑭𝑵)(𝑇𝑁 + 𝑭𝑷)(𝑇𝑁 + 𝑭𝑵)
MCC applies the same correlation idea to binary outcomes.
Recall the correlation coefficient 𝑟 from statistics? That 
is the Pearson Correlation Coefficient (PCC): a measure 
of how two variables move together.
Agreement - Disagreement
: marginals
Predicted 
Positive
Actual 
Positives
Actual 
Negatives
Predicted 
Negatives

MCC Example
If you were designing an Airport Security Scanner, which box would you be most afraid of, and why?
Classifier A Classifier B
𝑀𝐶𝐶 = 40 ⋅ 700 − 𝟐𝟎𝟎 ⋅ 𝟔𝟎
(40 + 𝟐𝟎𝟎)(40 + 𝟔𝟎)(700 + 𝟐𝟎𝟎)(700 + 𝟔𝟎)
= 0.1249
𝑀𝐶𝐶 = 35 ⋅ 890 − 𝟏𝟎 ⋅ 𝟔𝟓
(35 + 𝟏𝟎)(35 + 𝟔𝟓)(890 + 𝟏𝟎)(890 + 𝟔𝟓)
= 0.4904
MCC clearly distinguishes the better classifier with greater granularity than F1 (0.235 vs 0.4828).
Predicted Threat Predicted Safe
Actual Threat 40 60
Actual Safe 200 700
Predicted Threat Predicted Safe
Actual Threat 35 65
Actual Safe 10 890

Suppose we have three spam filters, each with 50 spam and 50 legitimate emails:
Pred Spam Pred Not
Actual Spam 47 3
Actual Not 3 47
Actual Spam 25 25
Actual Not 1 49
Actual Spam 48 2
Actual Not 48 2
• Filters B and C have identical 
F1 scores but very different 
behavior.
• MCC correctly identifies both 
as equally mediocre.
MCC vs. F1: A Direct Comparison
Precision Recall F1 MCC
94% 94% 94% 0.88
96% 50% 66% 0.53
50% 96% 66% 0.53
Best practice is to report both metrics: F1 for alignment with the existing literature, 
and MCC to capture truly balanced performance.

With MCC, all four cells of the confusion matrix contribute equally to the 
result. This symmetry makes MCC particularly reliable for:
• Imbalanced datasets
• Cases where both classes matter equally
• Comparing classifiers with different precision/recall tradeoffs
MCC is Balanced
𝑀𝐶𝐶 = 𝑇𝑃 ⋅ 𝑇𝑁 − 𝑭𝑷 ⋅ 𝑭𝑵
(𝑇𝑃 + 𝑭𝑷)(𝑇𝑃 + 𝑭𝑵)(𝑇𝑁 + 𝑭𝑷)(𝑇𝑁 + 𝑭𝑵)

Accuracy Precision Recall F1 MCC
Handles class 
imbalance?
No Yes Yes Yes Yes
Considers TN? Yes No No No Yes
Needs Companion 
Metrics?
Yes No No Yes Yes
Fully balanced? No No No Partial Yes
Best for… Balanced 
data
Trust Coverage Positive focus Overall 
balance
Choosing Your Metric
```

## Handling Class Imbalance with SMOTE

*Extracted from PDF: `12 Handling Class Imbalance with SMOTE.pdf`*

```
Handling Class Imbalance 
with SMOTE


What is Class Imbalance?
A dataset where one class (the majority) vastly outnumbers another (the minority) is said to be class-
imbalanced. In many real-world classification problems, one class is far more common than another.
• Fraud detection: 0.1% of transactions are fraudulent
• Medical diagnosis: 1–5% of patients have a rare disease
• Spam filtering: Spam may be a small fraction of all email
• Network intrusion detection: Malicious traffic is a tiny fraction of all network packets.
• Defect detection in manufacturing: Most manufactured items are defect-free; defective cases may be 
<0.5%.
• Wildlife conservation / species detection: Camera traps show animals in only a small fraction of images; 
rare species appear in <1%.
• Earthquake early warning: True seismic events are extremely rare compared to non-events in continuous 
sensor data.
• Credit default prediction: Defaults occur in only a small % of loans.
• Coastal water quality monitoring: Hypoxic events (dissolved oxygen ≤2.0 mg/L) are rare relative to normal 
(normoxic) conditions, creating a highly imbalanced dataset for binary classification.

What does Class Imbalance Matter?
A classifier trained on imbalanced data is biased toward the majority class. Consider a dataset with 95% 
positive and 5% negative examples:
Strategy
Predict everything as positve
Actually learn the minority class
High accuracy can be misleading.
We saw this previously in Evaluation Metrics: A 
classifier that predicts only the majority class gets:
• High accuracy,
• Recall of the minority class is 0,
• Near-0 MCC.
Accuracy
95%
Harder, but more useful
Standard learning algorithms optimize overall error.
That is equivalent to maximizing accuracy! 
the metric we just agreed is broken under imbalance.
The minority class is often the most important one to get right.
That's exactly why Recall and F1 exist missing a rare but critical 
case can be far more costly than a false alarm.

Possible Solutions
Oversample the Minority Class: Duplicate minority 
class examples until classes are balanced
• Creates a balanced training set
• The risk is Overfitting: the model 
memorizes the same minority examples.
Two straightforward strategies address imbalance by 
changing the training set:
Both approaches are simple but come with real trade-offs. 
Can we do better?
Undersample the Majority Class: Remove majority 
class examples until classes are balanced
• Creates a balanced training set
• We risk losing potentially useful information 
from the majority class


Synthetic Oversampling with SMOTE
Instead of duplicating minority examples, what if we generated new, synthetic ones?
• New examples should be similar to real minority instances
• They should diversify the minority class, not just repeat it
Synthetic Minority Over-sampling TEchnique (SMOTE)
Chawla et al. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of Artificial Intelligence Research.
This addresses the overfitting risk of naive oversampling.


Interpolation: Motivation
Interpolation is a blending of two values.
Consider two points in the Euclidean Plane.
If we move from 1, 4  to 5, 7 , using a linear function we might have to compute the 
equation of the line using point-slope form:
y − 𝑦0 = 𝑦1 − 𝑦0
𝑥1 − 𝑥0
x − 𝑥0 .
For the two points, y − 7 =
4−7
1−5 x − 5
 y − 7 =
3
4 x − 5 .
5, 7
1, 4
We may then consider any 𝑥-value in the interval 1, 5 .
For example, we might compute the midpoint as:
𝑥𝑀, 𝑦𝑀 =
1+5
2 , 𝑓
1+5
2 = 3, 5.5
where 𝑓 is the equation of the line.
3, 5.5

Interpolation: Motivation II
To acquire a blending of points, we do not want to compute the function 𝑓 that passes through 
the two points, we want to compute individual points along that line.
5, 7
1, 4
Consider again computing the midpoint of the two points.
We are well-aware of a formula for doing so: 
𝑥𝑀, 𝑦𝑀 = 𝑥0 + 𝑥1
2 , 𝑦0 + 𝑦1
2 = 1 + 5
2 , 4 + 7
2 = 3, 5.5
This technique is very specific to a single point. We should work to generalize 
this notion to allow us to compute any point on the line segment between our 
given points.
𝑥𝑀, 𝑦𝑀 = 𝑥0 + 0. 5 ∗ 𝑥1 − 𝑥0 , 𝑦0 + 0. 5 ∗ 𝑦1 − 𝑦0
𝑥1 − 𝑥0
𝑦1−𝑦0
3, 5.5
For this example,
𝑥𝑀, 𝑦𝑀 = 1 + 0. 5 ∗ 5 − 1 , 4 + 0. 5 ∗ 7 − 4 = 3, 5.5

Interpolation: Motivation III
Given two points in the plane*, we can compute any point on the line defined by two points as:
𝑥𝑢, 𝑦𝑢 = 𝑥0, 𝑦0 + 𝑢 ∙ 𝑥1 − 𝑥0 , 𝑦1 − 𝑦0
where 𝑢 is a constant and 𝑥0, 𝑦0  is the origination point.
5, 7
1, 4
 𝑥1 − 𝑥0
𝑦1−𝑦0
2, 4.75
*This can easily be extended to 𝑛 dimensions.
Example. Compute the point that is one-fourth distance away from 1, 4  
toward 5, 7 .
Solution.
Here, 𝑢 = 0.25.
𝑥.25, 𝑦.25 = 1, 4 + 0.25 ∗ 5 − 1 , 0.25 ∗ 7 − 4 = 2, 4.75

Linear Interpolation and SMOTE
What may look more familiar is an equivalent expression to our formula.
𝑥𝑢, 𝑦𝑢 = 𝑥0, 𝑦0 + 𝑢 ∙ 𝑥1 − 𝑥0 , 𝑦1 − 𝑦0
 = 𝑥0, 𝑦0 + 𝑢 ∙ 𝑥1, 𝑦1 − 𝑢 ∙ 𝑥0, 𝑦0
 = 𝑢 ∙ 𝑥1, 𝑦1 + 1 − 𝑢 ∙ 𝑥0, 𝑦0
 = 𝑢 ∙ 𝑃1 + 1 − 𝑢 ∙ 𝑃0
where 𝑃0 and 𝑃1 are points in the plane and 𝑢 is a constant.
𝑃1
𝑃0
𝑥1 − 𝑥0
𝑦1−𝑦0
𝑥𝑢, 𝑦𝑢
• Take 2 (real) minority class examples: 𝑚1, 𝑚2.
• Draw randomly 𝜆 ∈ 0,1 .
• Create a synthetic example 𝑆 between 𝑚1 and 𝑚2, where 𝜆 controls its position along the segment.
• Repeat for many examples to grow the minority class to the desired size
The idea behind SMOTE:

SMOTE Algorithm
SMOTE generates synthetic minority examples by interpolating between existing ones.
Observe: due to interpolation, synthetic examples lie between 
real minority examples in feature space and not outside them.
Input: Minority example 𝑥
1. Find the 𝑘 nearest neighbors of 𝑥 among other minority examples (typically 𝑘 = 5)
2. Randomly select one neighbor 𝑥′
3. Generate a new synthetic example along the line segment between 𝑥 and x’:
𝑥𝑛𝑒𝑤 = 𝑥 + 𝜆 ⋅ (𝑥′ − 𝑥), 𝜆 ∈ [0,1]
4. Repeat until the desired class balance is reached
Borderline-SMOTE: focuses synthesis near the decision boundary

Questions
In SMOTE, what is the role of λ?
a) It determines how many neighbors to consider
b) It controls where the synthetic example lies between two minority examples
c) It sets the desired class ratio after oversampling
d) It measures the distance between two minority examples
SMOTE should be applied to:
a) The full dataset before any split
b) The test set only
c) Both training and test sets equally
d) The training set only
Which of the following is a known limitation of SMOTE?
a) It always undersamples the majority class
b) It can generate noisy synthetic examples in regions of 
class overlap
c) It can only be applied when the minority class has at 
least 100 examples
d) It only works when 𝜆 = 0.5
```

## Explainable AI — SHAP

*Extracted from PDF: `13 Explainable AI -- SHAP.pdf`*

```
Explainable AI and SHAP: 
Understanding and Explaining 
Machine Learning Models

The Stakes of AI Decisions
AI systems now make high-stakes decisions.
Domain Decision Impact
Finance Loan approval, credit scoring Economic opportunity
Healthcare Diagnosis, treatment recommendations Patient outcomes
Criminal Justice Risk assessment, sentencing Liberty and fairness
Hiring Resume screening, interview scoring Employment opportunity
The question is not just:
“What did the model predict?”
Instead, we ask:
• “Why?”
• “Should we trust it?”

What is Explainable AI?
Explainable AI (XAI) refers to methods that make AI system outputs understandable to 
humans.
Goal Question
Transparency How does the model work?
What patterns did it learn?
Interpretability Why did it make this prediction?
Which features mattered?
Trustworthiness Is the reasoning sound?
Does it align with domain knowledge?
XAI bridges the gap between model performance and human understanding.

The XAI Landscape
Different stakeholders ask different questions and require different types of explanations.
Stakeholder Question Needs
End User “Why was I denied?” Simple, actionable reasoning
Data Scientist “Is this model learning 
spurious correlations?”
Debugging tools
Regulator “Is this system fair?” Auditable decision logic
Explanation methods differ in three main ways:
Dimension Options Why it Matters
Scope: What does it explain? Global (overall behavior) vs.
Local (single prediction)
Global: “Which features drive this model?”
Local: “Why was this applicant denied?”
Model Access: Does it need 
access to model internals?
Model-agnostic (any model) vs.
Model-specific
Agnostic works on any model; specific is faster but limited to certain 
architectures.
Timing: When is 
interpretability added?
Intrinsic (built-in) vs.
Post-hoc (after training)
Intrinsic models (e.g., linear regression) are simple to understand 
directly but may be less accurate.
Post-hoc methods let you use powerful models first, then explain 
them afterward.

The Problem with Simple Models
We could just use interpretable models...
Model How to Interpret Limitation
Linear regression Coefficients are feature weights Can't capture nonlinear relationships
Decision tree Follow the path from root to leaf Deep trees overfit; shallow trees underfit
Rule lists Read the if-then rules Struggles with continuous features
But we often need complex models (random forests, neural nets) for accuracy.
Can we get the accuracy of complex models and still explain their predictions?
(The post-hoc approach.)


What We Want from an Explanation
For a single prediction, we want to know:
Is there a principled way to do this, not just a heuristic?
• How much did each feature contribute?
• Did it push the prediction up or down?
• Do the contributions add up to the final prediction? (Nothing left unexplained.)
Across many predictions, we want:
• Which features matter most overall?
• Consistent methodology: if a feature has the 
same effect in two different predictions, it 
should receive the same credit in both.
Features


Revisiting Game Theory
The feature attribution problem looks like a fair 
division problem.
A prediction is like a team's total earnings.
Features are like team members.
We want to divide credit fairly.
Fair Division
How a shared outcome is split among 
contributors, so each gets credit 
proportional to what they actually added.
Shapley (1953) solved the fair division problem in economics; Lundberg 
& Lee (2017) applied it to machine learning.
SHAP = SHapley Additive exPlanations
A principled, theoretically grounded method for feature attribution.
Game Theory → SHAP
Players → Features
Payout → Prediction
Fair share → SHAP value

SHapley Additive exPlanations 
(SHAP)

An Analogy from Cooperative Game Theory
THE GAME
Three friends (Alice, Bob, Carol) collaborate and earn $100. How should they split it fairly?
SHAPLEY’S INSIGHT (1953):
Pay each player their average marginal contribution 
across all possible orderings of team formation.
If Alice joins first and earns $40, then Bob joins (+$30), then Carol (+$30)…
but what if Bob joined first? Average over all arrival orders.
Marginal is being used in the economics 
sense:
marginal ≡ “the incremental value of 
adding this player/feature to what is 
already there”


The SHAP Decomposition
𝑓(𝐱) = 𝜙0 + 𝜙1 + 𝜙2 + ⋯ + 𝜙𝑛
The model's average output over 
all training examples: baseline
Feature 𝑖’s SHAP value 
(𝜙𝑖) contribution
Final prediction SHAP value for a single instance 𝐱. This formula defines a local scope by 
explaining one prediction. 
Assume the average applicant in the training data 
had 50% approval. What about this applicant 
pushed them to 78%?
Income Credit 
Score
Debt 
Ratio
Model 
Prediction
85K 720 35% 78% 
Approval
𝜙𝑖 0.19 0.115 -0.025𝑓 𝐱 = 0.5 + 0.19 + 0.115 − 0.025 = 0.78
How much did this feature push the 
prediction up or down from the baseline?How do we compute 𝜙𝑖?

Why Not Just Measure Each Feature Independently?
This fails because features are rarely 
independent.
A 720 (out of 800) credit score has a different 
effect depending on income: a high credit 
score may add little to the approval when an 
applicant may already have a high income 
which adds significantly.
Measuring in isolation assumes no interaction 
among features, producing a main effect that 
ignores how features combine in actual 
predictions.
“Measure each feature's effect in isolation”: 
hold all other features at neutral values (e.g., 
their averages), vary only one feature, and 
see how the prediction changes.
Add features one at a time, tracking the changes.
Consider an ordering of features to add in sequence:
Credit → Income → Debt
Step Add Feature Prediction Marginal
0 (none) 0.50 —
1 Credit 0.65 +0.15
2 Income 0.72 +0.07
3 Debt 0.78 +0.06
The problem is that the order matters. Credit arrives 
first and absorbs all shared effects. Income and Debt only 
get attribution for what remains after Credit Score already 
claimed the correlated impact.
If we used a different ordering we would get different 
attributions. Which ordering of features is “right”?
Idea #1 Idea #2

The Shapley Insight: Average Over All Orderings
What if we tried every possible ordering and averaged?
Ordering Credit’s
marginal
Income’s
Marginal
Debt’s
marginal
C → I → D +0.15 +0.07 +0.06
C → D → I +0.15 +0.18 -0.05
I → C → D +0.14 +0.08 +0.06
I → D → C +0.26 +0.08 -0.06
D → C → I +0.18 +0.18 -0.08
D → I → C +0.26 +0.10 -0.08
With 3 features how many 
orderings do we have? 𝑛 features?
𝑃 3,3 = 3! = 6 𝑛! Average: 
Shapley 
Value (𝜙𝑖)
+0.19 +0.115 -0.025
IDEA: Average each column to get that feature's Shapley 
value thus no feature gets positional advantage: each 
features is measured fairly across all possible contexts.
𝚺
+0.28
+0.28
+0.28
+0.28
+0.28
+0.28

Toward the SHAPley Value Formula
Let 𝑁 enumerated as 1, 2, … , 𝑛  be a set of features.
How many possible orderings are there for 𝑁? 𝑁 !
Suppose 𝑆 is a subset of features that arrived before 
feature 𝑖. State the number of orderings of 𝑆. 𝑆 !
Give an expression for the number of features that arrived 
after feature 𝑖. State the number of corresponding 
orderings.
𝑁 − 𝑆 − 1 𝑁 − 𝑆 − 1 !
For a model 𝑓, express the marginal contribution of feature 
𝑖: how much 𝑖 contributes comparatively to the model’s 
prediction when considering 𝑆. 
𝑓(𝑆 ∪ {𝑖}) − 𝑓(𝑆)
What does the expression 𝑆 !⋅ 𝑁 − 𝑆 −1 !
𝑁  represent? The proportion of orderings where exactly 
the features in 𝑆 arrive before feature 𝑖. 
What does the expression 𝑆 ! ⋅ 𝑁 − 𝑆 − 1 ! represent?
The number of orderings where exactly 
the features in 𝑆 arrive before feature 𝑖.
𝑆 is sometimes 
called a coalition.

The SHAPley Value Formula
If we combine the expressions to obtain the 
expression on the right, we observe that it computes
𝑆 ! ⋅ 𝑁 − 𝑆 − 1 !
𝑁 ⋅ 𝑓(𝑆 ∪ {𝑖}) − 𝑓(𝑆) 
the marginal contribution of 𝒊 scaled by a fractional weight: 
the number of sets with the number of orderings where 
exactly the features in 𝑆 arrive before feature 𝑖. 
If we sum the result of allowing feature 𝑖 to sequentially arrive in each position in the ordering, 
we have the following definition.
Definition. Let 𝑁 be a set of features enumerated by 1, 2, … , 𝑛 . Then, the Shapley value 
for feature 𝒊, 𝜙𝑖, is defined as:
𝜙𝑖 = ෍
𝑆⊆𝑁\{𝑖}
|𝑆|! (|𝑁| − |𝑆| − 1)!
|𝑁|! ⋅ 𝑓(𝑆 ∪ {𝑖}) − 𝑓(𝑆)

Coalition 𝑆
(before 
Credit)
𝑺 Orderings Count Weight
𝑪𝒐𝒖𝒏𝒕
𝟔
Weights
Consider a case where we have 𝑁 = 3 features we will refer to as 𝑁 = 𝐶, 𝐼, 𝐷 .
This means 𝑃 3,3 = 3! = 6 orderings.
0 𝐶 → 𝐼 → 𝐷
𝐶 → 𝐷 → 𝐼
2 1
3
1 𝐼 → 𝐶 → 𝐷 1 1
6
1 𝐷 → 𝐶 → 𝐼 1 1
6
1 𝐼 → 𝐷 → 𝐶
𝐷 → 𝐼 → 𝐶
2 1
3
We will compute the weights for Credit score; Credit can arrive first, second or third. 
∅
𝐼
𝐷
𝐼, 𝐷
0! (3 − 0 − 1)!
3! = 1
3
1! (3 − 1 − 1)!
3! = 1
6
1! (3 − 1 − 1)!
3! = 1
6
2! (3 − 2 − 1)!
3! = 1
3
|𝑆|! (|𝑁| − |𝑆| − 1)!
|𝑁|!

Computing 𝜙𝐼
For SHAP , we have to retrain a model for each coalition. We then can compute a prediction score for a single 
record in our data. 
Coalition 𝑺 𝒇 𝑺
∅ 0.50
𝐼 0.58
𝐶 0.65
𝐷 0.42
𝐼, 𝐶 0.72
𝐼, 𝐷 0.52
𝐶, 𝐷 0.60
𝐼, 𝐶, 𝐷 0.78
Suppose we then have the following prediction 
scores for a single applicant:
Income = $85K, Credit = 720, Debt Ratio = 35%
For example, 𝑓 𝐶 =  0.65 means: “For this 
applicant, using only their Credit Score (720), the 
model predicts 0.65 approval probability.” 
Computing 𝜙𝐼
Coalition 𝑺 𝒇 𝑺 𝑺 ∪ 𝑰 𝒇 𝑺 ∪ 𝑰
∅ 0.50 𝐼 0.58
𝐶 0.65 𝐼, 𝐶 0.72
𝐷 0.42 𝐼, 𝐷 0.52
𝐶, 𝐷 0.60 𝐼, 𝐶, 𝐷 0.78
1
6 ⋅ 0.52 − 0.42 + 1
3 ⋅ 0.78 − 0.60 = 0.115
𝜙𝐼 = 1
3 ⋅ 0.58 − 0.5 + 1
6 ⋅ 0.72 − 0.65 +

Computing 𝜙𝐶
Coalition 𝑺 𝒇 𝑺
∅ 0.50
𝐼 0.58
𝐶 0.65
𝐷 0.42
𝐼, 𝐶 0.72
𝐼, 𝐷 0.52
𝐶, 𝐷 0.60
𝐼, 𝐶, 𝐷 0.78
Compute 𝜙𝐶 = 0.19 and 𝜙𝐷 = −0.025.
1
6 ⋅ 0.6 − 0.42 + 1
3 ⋅ 0.78 − 0.52 = 0.19
𝜙𝐶 = 1
3 ⋅ 0.65 − 0.5 + 1
6 ⋅ 0.72 − 0.58 +
1
6 ⋅ 0.6 − 0.65 + 1
3 ⋅ 0.78 − 0.72 = −0.025
𝜙𝐷 = 1
3 ⋅ 0.42 − 0.5 + 1
6 ⋅ 0.52 − 0.58 +
Altogether, (𝜙𝐶 = +0.19, 𝜙𝐼 = +0.115) move this applicant from the 
0.50 baseline to 0.78 approval probability. The poor Debt ratio did not 
help with approval (𝜙𝐷 = −0.025).
Observe in terms of overall explainability of this score for this applicant:
𝑓 𝐼, 𝐶, 𝐷 − 𝑓 ∅ = 0.78 − 0.50 = 0.28 = 𝜙𝐼 + 𝜙𝐶 + 𝜙𝐷

Properties of SHAP
Shapley values are the unique solution satisfying:
*Shapley (1953) proved 
a uniqueness theorem.
Axiom Property
Efficiency SHAP values sum to 𝑓 𝐱 − 𝑏𝑎𝑠𝑒. All credit distributed.
Symmetry Equal contributors receive equal values.
Dummy Non-contributing features receive zero.
Additivity For 𝑓 + 𝑔: 𝜙𝑖(𝑓 + 𝑔) = 𝜙𝑖(𝑓) + 𝜙𝑖(𝑔)
Shapley values are the unique attribution method satisfying all 
four properties. Any other method must violate at least one.*

The SHAP Process and Its Cost
To compute the SHAP value for one feature of 𝑁  features on one prediction:
• Enumerate all coalitions 𝑆 (subsets of other features)
• For each coalition, train or evaluate a model using only the features in 𝑆
• Compute 𝑓(𝑆) and 𝑓(𝑆 ∪ {𝑖}) for each coalition
• Calculate the marginal contribution: 𝑓(𝑆 ∪ {𝑖}) −  𝑓(𝑆)
• Weight each marginal by 
𝑆 ! 𝑁 − 𝑆 −1 !
𝑁 !
• Sum the weighted marginals: 𝜙𝑖
For 𝑁  features, the set of all coalitions is 
the powerset: 2 𝑁  subsets. Each requires 
either training a separate model or 
simulating absent features by marginalizing 
over their values.
Exact SHAP is exponential in the number of 
features. For real-world models, we need 
approximations — KernelSHAP, TreeSHAP, 
DeepSHAP — that estimate Shapley values 
without exhaustive enumeration.

From Local to Global: SHAP Across a Dataset
Locally we ask: “Why was this applicant denied?”
Globally we ask: “What drives approvals in general?”
Definition. Let 𝜙𝑖
𝑗 denote the SHAP value of feature 𝑖 for 
sample 𝑗 in a dataset of 𝑛 samples. The global importance of 
feature 𝑖 is defined as: 
𝐼𝑖 = 1
𝑛෍
𝑗=1
𝑛
𝜙𝑖
𝑗
Intuitively, 𝐼𝑖 measures how much a single feature matters across all samples.
Low 𝐼𝑖 → feature 𝑖 rarely influences predictions.
High 𝐼𝑖 → feature 𝑖 consistently moves predictions away from the baseline, regardless 
of direction, across the dataset.
Interested in SHAP magnitude: 
features pushing predictions away 
from baselines regardless of sign. 

Visualizing Global SHAP: Beeswarm Plot
image credit
𝑋-axis: SHAP value (impact on prediction)
𝑌-axis: Features (ranked by importance: 𝐼𝑖)
Adult income dataset (classification task to predict if people made 
over $50k in the 1990s).
Each dot represents one sample's SHAP value, 𝜙𝑖
𝑗 : 
how much feature 𝑖 contributed for sample 𝑗.
Color indicates whether that sample had a low (blue) 
or high (red) value for the feature. 
Age Red dots ≡ older individuals
Blue dots ≡ younger individuals
Age affects many samples moderately (spread of dots)
Capitol Gain affects few samples, but those 
few see a large effect (tight cluster + long tail)
Most people have little or no capital gain, so 
the feature does not affect their prediction. 
But for those who do have high capital gains, 
the impact is dramatic.
```
