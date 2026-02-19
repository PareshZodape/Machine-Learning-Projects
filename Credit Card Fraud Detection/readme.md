# Overview
A machine learning project designed to identify fraudulent transactions within a highly imbalanced dataset using anomaly detection and privacy-preserving mathematical transformations.

# Objective
To build a robust classification system that can accurately distinguish rare fraudulent activities from millions of legitimate transactions without being misled by the overwhelming frequency of normal data.

# Technical Flow

- **Data Anonymization:** Utilizes PCA-transformed features ($V1$ through $V28$) to maintain user privacy while preserving statistical patterns.

- **Feature Engineering:** Scales the remaining raw features, specifically Time and Amount, to ensure they align with the normalized PCA variables.

- **Handling Imbalance:** Implements Under-sampling or SMOTE (Over-sampling) to prevent the model from developing a bias toward the majority class.

- **Anomaly Detection:** Deploys specialized algorithms like Isolation Forest (isolating outliers) and Local Outlier Factor (measuring local density) to flag suspicious points.

- **OutcomesMetric Shift:** Successfully moves the evaluation focus from misleading Accuracy to high-stakes Precision and Recall.

- **Fraud Identification:** Minimizes "False Negatives" (missed frauds) to protect financial assets.

  **Operational Efficiency:** Provides a clear confusion matrix that helps stakeholders understand the trade-off between catching fraud and annoying legitimate customers with false alarms.
