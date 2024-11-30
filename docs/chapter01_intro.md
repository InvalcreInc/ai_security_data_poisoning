# Coursework: AI Security - Data Poisoning Attacks in ML Models

## 1. Topic: Data Poisoning Attacks in Machine Learning Models

- **Objective**: This coursework aims to analyze and demonstrate the vulnerability of machine learning models to **data poisoning attacks**. These attacks involve injecting malicious data into the training set to degrade the performance of the model or mislead its predictions. Specifically, this work explores **data poisoning** as an attack vector for **spam classification models** and examines the impact on model performance.

## 2. Content

### 2.1. Introduction

- **Overview**:  
  Machine learning models are widely deployed in critical applications, including spam detection, financial forecasting, and medical diagnosis. As these models are trusted to make important decisions, they also become targets for adversarial attacks. **Data poisoning attacks** are among the most insidious forms of adversarial manipulation, where attackers inject corrupted data into the training set to manipulate the model’s behavior.

  In this coursework, we use the **Spambase dataset**, a common benchmark dataset for spam email classification, to simulate and assess **data poisoning attacks**. Specifically, we explore **label flipping** (where spam emails are mislabeled as non-spam) and **targeted attacks** (where attackers craft specific emails to bypass spam detection). The goal is to understand the impact of such attacks on machine learning models and explore effective defense strategies.

- **Research Question**:  
  How do data poisoning attacks impact the accuracy and generalization of machine learning models, and what defense mechanisms can be implemented to counteract these threats?

### 2.2. Relevance

#### 2.2.1. Architecture and Technologies

- **Architecture**:  
  The AI model in this coursework is built using **supervised learning** techniques. The primary task is to train a model to distinguish between spam and non-spam (ham) emails. Below is a brief breakdown of the architecture:

  - **Preprocessing**:

    - Data cleaning, handling missing values, encoding categorical variables, and feature engineering to prepare the data for modeling.

  - **Model Training**:

    - Basic machine learning models such as **Logistic Regression** and **Multinomial Naive Bayes (MultinomialNB)** are used as baselines for classification.

  - **Attack Simulation**:

    - **Data poisoning** attacks are simulated by manipulating the training data to either introduce noise or inject targeted spam emails to mislead the model.

  - **Defense Strategies**:
    - Several defense techniques, such as **outlier detection** and **adversarial training**, are implemented to mitigate the effects of data poisoning on model performance.

- **Technologies**:
  - **Python**: The programming language used for implementing the machine learning pipeline.
  - **Scikit-learn**: A Python library for training machine learning models, implementing algorithms for classification, and evaluation.
  - **Matplotlib** and **Seaborn**: Libraries used for data visualization and plotting confusion matrices, histograms, and model performance metrics.
  - **Jupyter Notebooks**: For an interactive environment that allows for step-by-step data exploration and model development.

#### 2.2.2. Relevant Attack Topics

- **Data Poisoning Attack**:  
  Data poisoning attacks can take several forms, but the core idea is to manipulate the training data to mislead the model. The two main types of attacks we focus on are:

  - **Label Flipping**:  
    This technique involves flipping the labels of a portion of the training data. For example, some **spam** emails are misclassified as **ham**, and vice versa. This confuses the model, leading it to misclassify emails during inference.

  - **Targeted Attack**:  
    In this more advanced form of poisoning, attackers specifically craft certain emails that appear as **ham** (non-spam) but are actually **spam**. Injecting these emails into the training dataset allows the attacker to bypass the spam detection model, making the model misclassify future spam emails as **ham**.

  - **Impact of Data Poisoning**:  
    The model becomes biased and may not generalize well to new, unseen data, as it has learned from corrupted training data. This leads to lower accuracy and poor classification performance, especially in critical applications like spam detection, fraud detection, and medical diagnosis.

### 2.3. System Design

#### 2.3.1. Implementation and Testing

- **Dataset**:  
  The **Spambase dataset** is used for binary classification. The dataset consists of a collection of emails labeled as either **spam** or **ham** (non-spam). The dataset includes various features, such as word frequencies and metadata, that help distinguish between spam and non-spam emails.
- **Model**:  
  Two baseline machine learning models are used to train the classifier:

  - **Logistic Regression**: A linear model that predicts the probability of an email being spam based on its features.
  - **Multinomial Naive Bayes (MultinomialNB)**: A probabilistic model that assumes feature independence and works well with text classification tasks.

- **Attack Implementation**:  
  The following steps are taken to simulate data poisoning:

  - **Label Flipping**: A random subset of the dataset is selected, and the labels are flipped. This introduces noise and confuses the model during training.
  - **Targeted Attack**: A crafted **spam** email is injected into the dataset and labeled as **ham** (non-spam). This attack allows the model to learn that certain spam emails should be classified as non-spam.

- **Defense Techniques**:  
  Several defense mechanisms are explored to mitigate the impact of data poisoning:

  - **Outlier Detection**: Using techniques like **Principal Component Analysis (PCA)** and **Isolation Forest** to identify and remove outliers (i.e., poisoned data points).

  - **Adversarial Training**: The model is trained on a mix of clean and poisoned data, making it more robust against attacks.

  - **Regularization**: **L2 regularization** is applied to prevent overfitting to the poisoned data, improving model generalization.

- **Testing**:  
  The performance of the model is tested using the following evaluation metrics:

  - **Accuracy**: Measures the percentage of correctly classified emails.
  - **Confusion Matrix**: Helps assess false positives, false negatives, precision, recall, and F1 score.
  - **F1-Score**: A balanced measure of precision and recall.

#### 2.3.2. Results Analysis

- **Performance Metrics**:
  The results show a significant drop in model performance when poisoned data is introduced. For example, **accuracy** and **F1 score** decrease, and the model becomes less reliable at detecting spam emails.

  - **Before Attack**: The model has a high accuracy in distinguishing between spam and ham emails.
  - **After Poisoning**: Accuracy drops, and the model misclassifies more emails. The confusion matrix shows an increase in false positives (non-spam emails labeled as spam) and false negatives (spam emails labeled as non-spam).

- **Defense Effectiveness**:
  - **Outlier Detection**: Removing the outliers (poisoned data) improves model accuracy and reduces the misclassification rate.
  - **Adversarial Training**: Training with both clean and poisoned data makes the model more resilient to future attacks.
  - **Regularization**: Regularization helps prevent the model from overfitting to the poisoned data, leading to better performance on unseen data.

### 2.4. Conclusion

- **Summary of Findings**:  
  Data poisoning attacks can significantly degrade the performance of machine learning models, especially in critical applications like spam detection. Label flipping and targeted attacks confuse the model, leading to misclassifications and poor generalization.

  However, by implementing effective defense mechanisms such as **outlier detection**, **adversarial training**, and **regularization**, the impact of these attacks can be minimized, and the model’s robustness can be improved.

- **Impact on AI Security**:  
  This experiment demonstrates the importance of securing machine learning pipelines, especially when these models are deployed in sensitive applications. As AI systems become more integrated into critical infrastructure, it is crucial to protect them from adversarial attacks that can compromise their integrity and functionality.

- **Future Work**:  
  Future research could focus on more advanced attacks, such as **backdoor attacks** (where specific triggers are embedded into the model) and **model integrity verification**. Additionally, more robust defense techniques could be explored, including **anomaly detection** and **model ensembling**.

---

## 3. References

1. Sotiropoulos, John. “Adversarial AI Attacks, Mitigations, and Defense Strategies.” _Excerpt From: Adversarial AI Attacks, Mitigations, and Defense Strategies_. https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0
2. "Adversarial Machine Learning" - URL https://www.springer.com/gp/book/9783030461377
3. "A Comprehensive Guide to Data Poisoning Attacks" - URL: https://arxiv.org/abs/2003.03056
4. Reinders, J., and McCool, M. L. "Parallel Programming: For Multicore and Cluster Systems". Addison-Wesley, 2013.

---
