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

