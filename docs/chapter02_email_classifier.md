# Coursework: AI Security - Data Poisoning Attacks in ML Models

## Coursework description

### Project Structure

├── data/
│ ├── [spam_ham_dataset_poisoned.csv](data/spam_ham_dataset_poisoned.csv)
│ ├── [spam_ham_dataset_targeted.csv](../data/spam_ham_dataset_targeted.csv)
│ └── [spam_ham_dataset.csv](../data/spam_ham_dataset.csv)
├── docs(en)
│ ├── chapter01_intro.md
│ ├── chapter02_model.md
│ ├── chapter03_simple_attack.md
│ ├── chapter04_targeted_attack.md
│ └── chapter04_defense_strategies.md
├── env/
├── modules/
│ ├── clean_text.py
│ └── load_dataset.py

# Spam Classifier and Data Poisoning

## Overview

In this project, we build a spam classifier and explore the concept of **data poisoning**. Data poisoning is a malicious technique where an attacker manipulates the training data to degrade the model's performance or to introduce specific vulnerabilities. We demonstrate how this type of attack can be executed, the impact it has on the model, and how we can mitigate such risks. The process starts with creating a working spam classifier model and then proceeds to apply data poisoning and defense strategies.

---

# Spam Classifier

Before we can apply data poisoning techniques, it's crucial to first build a working model. This section explains how we construct that model, which will serve as the basis for experimenting with data poisoning.

While the initial dataset used in this example is `spam_ham_dataset.csv`, this approach is flexible. You can create poisoned datasets, retrain the model, and test its vulnerability by simply changing the filename to point to the newly created dataset. This makes it possible to test the model’s performance under different conditions, including attacks like label flipping or targeted poisoning.

Let’s get started!

---

## 1. Data Loading

In the first step, we prepare the environment for data loading. This includes importing the necessary libraries and ensuring that our dataset is correctly loaded from the specified file.

The `os` module is essential here, as we will be working with local scripts for handling and cleaning the data. The dataset filenames are set as variables, and we load the dataset based on the filename selected.

To load the dataset, simply uncomment the line corresponding to the desired dataset:

- `spam_ham_dataset.csv` for the original dataset
- `spam_ham_dataset_targeted.csv` for a targeted poisoned dataset
- `spam_ham_dataset_poisoned.csv` for a dataset with a generic poisoning attack

The dataset will then be loaded, cleaned, and preprocessed for model training.

---

## 2. Data Analysis

Before we begin processing the data, we need to gain an understanding of its structure. A crucial part of this process is analyzing the distribution of labels—whether the dataset consists mostly of `spam` emails or `ham` (non-spam) emails.

In this step, we generate a pie chart to visualize the proportion of `spam` vs. `ham` emails. This visualization helps us understand if the data is imbalanced, which is important because imbalanced datasets can negatively affect the model’s ability to generalize well on unseen data.

For example, if the dataset contains significantly more `ham` emails than `spam`, we may need to consider techniques like resampling (oversampling the minority class or undersampling the majority class) to correct the imbalance.

---

## 3. Data Processing

Data processing is a critical step to prepare the dataset for training. It involves several tasks to ensure the data is clean and in a usable format for machine learning models.

### - Check for Missing Data

First, we check if there are any missing or null values in the dataset. Missing data can lead to incorrect predictions, so we must handle it appropriately. If any missing values are found, we either remove the corresponding rows or fill them with placeholder values (depending on the specific case).

### - Data Cleaning

Next, we clean the text data. For this purpose, a custom `CleanText` class has been created. This class performs the following operations on the text data:

- **Remove Stop Words**: Common words like "the", "and", "is", which don't provide useful information for classification tasks.
- **Remove Punctuation and Special Characters**: Text often contains unnecessary punctuation, which we remove to clean up the text data.
- **Remove Empty or Invalid Entries**: Any empty or irrelevant entries in the dataset are discarded.

However, we choose **not to remove URLs** from the emails, as they may contain critical information (e.g., phishing URLs or other spam indicators) that could help improve the model’s performance.

---

## 4. Feature Selection

Once the data has been cleaned and preprocessed, the next step is feature selection. Feature selection is the process of identifying the most relevant features (in our case, words or n-grams) that the model will use to make predictions.

For text data, the features are typically words or sequences of words that appear frequently in spam emails and non-spam emails. We aim to select a subset of the most informative features, which will improve the model’s performance and reduce computational complexity.

---

## 5. Vectorization

Machine learning models require numerical data to make predictions, but text data is inherently non-numeric. Therefore, we need to convert the text into a numerical format through **vectorization**.

In this step, we use the **TF-IDF (Term Frequency-Inverse Document Frequency)** technique for vectorization. This method transforms text data into numerical vectors by considering both the frequency of words within a document and how common those words are across the entire dataset.

The **TF-IDF** approach allows us to weigh words that are frequent within a document but rare across all documents as more important, helping the model focus on words that are likely to contribute to distinguishing spam from ham.

---

## 6. Model Training

Now that the data is cleaned, preprocessed, and vectorized, we can begin training the machine learning models. In this section, we will experiment with two different models: **Multinomial Naive Bayes (MultinomialNB)** and **Logistic Regression**.

### - MultinomialNB

**Multinomial Naive Bayes** is a widely used algorithm for text classification tasks, particularly when the features are word frequencies. It is based on Bayes' Theorem and assumes that the features (i.e., words) are conditionally independent given the class label. This makes it a simple yet effective choice for spam detection.

We start with MultinomialNB as our baseline model because it is fast and effective, especially when dealing with large text datasets.

### - Logistic Regression

**Logistic Regression** is another popular classification algorithm. While it is primarily known for its use in binary classification tasks, it works well for text classification as well. Logistic Regression models the probability of a class (spam or ham) using a linear relationship between the features and the target.

After training both models, we will compare their performance using common metrics like accuracy, precision, recall, and F1-score. This comparison helps us identify which model is more suitable for our spam classification task.

---

## 7. Saving the Model

Once the model is trained and evaluated, we save both the model and the vectorizer to disk for future use. Saving the trained model allows us to easily reload it without needing to retrain it each time.

To ensure that the models can be identified later, we use descriptive filenames based on the dataset and model type. This way, we can easily distinguish between different versions of the models when working with multiple datasets or conducting experiments with poisoned data.

By saving the model and vectorizer, we can quickly test it with new data, including poisoned datasets, without retraining. This will be essential when testing the impact of data poisoning attacks in later sections.

---

### Conclusion

At this point, we have successfully built a working spam classifier using a variety of preprocessing, vectorization, and modeling techniques. In the next sections, we will focus on data poisoning, where we introduce malicious data points to the dataset in order to test how well the model handles attacks. We will also explore different strategies for defending against these attacks to improve the model's robustness.
