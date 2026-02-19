**1. Logistic Regression**
A statistical model used for classification (not regression). It calculates the probability ($0$ to $1$) that a transaction belongs to a specific category, like "Fraud" or "Normal."

**2. Stratify**
A sampling method that ensures the proportion of classes (e.g., 0.1% fraud) stays exactly the same in both your training and testing datasets. It prevents "lopsided" data splits.

**3. Accuracy Score**
The ratio of correct predictions to total predictions. In fraud detection, it is often a misleading metric because a model can be "99% accurate" while still missing 100% of the actual fraud.

**4. SMOTE**
Synthetic Minority Over-sampling Technique. A tool that creates "fake" but mathematically realistic fraud examples to balance the dataset so the model has more cases to learn from.

