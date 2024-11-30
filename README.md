# Results

This section presents the results of our experiments on the **Spam Classifier** model across three different scenarios: **Clean Classifier**, **Simple Poisoned Attack**, and **Targeted Poisoned Attack**. For each scenario, we evaluate model performance using key metrics such as accuracy, precision, recall, and F1-score for both classes (Ham and Spam). The following tables summarize the results for these three models.

---

## The distribution of labels: Spam vs Ham

### 1. Clean Classifier

![Distribution of Labels - Clean Model](reports/distribution_clean_model.png)

### 2. Simple Poisoned Attack

## ![Distribution of Labels - Poisoned Model](reports/distribution_poisoned_model.png)

---

## Model Performance Metrics

| **Model**                    | **Accuracy** | **Precision (Ham - Class 0)** | **Recall (Ham - Class 0)** | **F1-Score (Ham - Class 0)** | **Precision (Spam - Class 1)** | **Recall (Spam - Class 1)** | **F1-Score (Spam - Class 1)** |
| ---------------------------- | ------------ | ----------------------------- | -------------------------- | ---------------------------- | ------------------------------ | --------------------------- | ----------------------------- |
| **Clean Classifier**         | 96.23%       | 98.0%                         | 97.0%                      | 97.0%                        | 93.0%                          | 95.0%                       | 94.0%                         |
| **Simple Poisoned Attack**   | 86.12%       | 90.0%                         | 89.0%                      | 90.0%                        | 78.0%                          | 80.0%                       | 79.0%                         |
| **Targeted Poisoned Attack** | 96.65%       | 98.0%                         | 97.0%                      | 98.0%                        | 93.0%                          | 95.0%                       | 94.0%                         |

---

## Confusion Matrices

Below are the confusion matrices for each model. The confusion matrix shows how well the model performs in terms of classifying **Ham** (Class 0) and **Spam** (Class 1) emails.

### 1. Clean Classifier

![Confusion Matrix - Clean Model](reports/confusion_matrix_clean_model.png)

### 2. Simple Poisoned Attack

![Confusion Matrix - Poisoned Model](reports/confusion_matrix_simple_poisoned.png)

### 3. Targeted Poisoned Attack

![Confusion Matrix - Targeted Model](reports/confusion_matrix_targeted_poisoned.png)

---

## Accuracy Comparison

This table compares the accuracy of the models across different scenarios, demonstrating how data poisoning impacts model performance.

| **Model**                    | **Accuracy (%)** |
| ---------------------------- | ---------------- |
| **Clean Classifier**         | 96.23%           |
| **Simple Poisoned Attack**   | 86.12%           |
| **Targeted Poisoned Attack** | 96.65%           |

![Accuracy Comparison - Clean vs Poisoned](images/comparison_accuracy_poisoned.png)

---

## Classification Report: Clean Classifier

The classification report provides a breakdown of precision, recall, and F1-score for each class (Ham and Spam). The **Clean Classifier** shows strong performance with high values for both Ham and Spam classification.

---

## Conclusion

The results clearly show the detrimental impact of data poisoning attacks on the spam classifier model. The **Clean Model** performs significantly better, with high accuracy, precision, and recall across both classes. However, both the **Simple Poisoned Model** and **Targeted Poisoned Model** suffer a noticeable decline in performance.

The **Targeted Poisoned Attack** demonstrates how an attacker can manipulate the model to misclassify spam emails as ham, bypassing the spam detection mechanism. These results highlight the importance of defending against such attacks to maintain the integrity and reliability of machine learning models.

---
