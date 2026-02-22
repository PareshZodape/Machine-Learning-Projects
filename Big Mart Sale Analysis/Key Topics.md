# XGBoost (Extreme Gradient Boosting):
An optimized library designed to be highly efficient and flexible. It builds an ensemble of decision trees sequentially, where each new tree corrects the errors of the previous ones.

# CV (Cross-Validation):
A technique to evaluate how well the model generalizes to unseen data. It splits the data into "folds" (e.g., 5 folds), trains on 4, and tests on 1, rotating until every fold has been used as the test set.


# Keyword	
- **n_estimators:**
The number of trees to build. Too few leads to underfitting; too many can lead to overfitting (though XGBoost is robust).

- **learning_rate:**
Also called eta. It shrinks the contribution of each tree to prevent the model from overshooting the optimal solution. Smaller values make the model more robust.

- **max_depth:**
Limits how deep each tree can grow. Higher depth allows the model to learn complex patterns but significantly increases the risk of overfitting.

- **subsample:**
The fraction of training data randomly sampled for each tree. Setting this to 0.8 means each tree uses 80% of the data, which adds randomness and prevents overfitting.

- **colsample_bytree:**
The fraction of features (columns) used for each tree. Similar to subsampling, this helps prevent one dominant feature from over-influencing the model.

- **reg_alpha:**
L1 regularization (Lasso). It penalizes the weight of features, often forcing unimportant feature weights to zero, effectively performing feature selection.

- **reg_lambda:**
L2 regularization (Ridge). It penalizes the square of the weights, making the model more conservative and smoothing out the predictions.

- **random_state:**
A seed that ensures the results are reproducible. If you use the same number, you will get the exact same model every time you run the code.
