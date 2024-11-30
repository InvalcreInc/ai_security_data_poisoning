# Data Poisoning: Targeted Attack

In this section, we will explore **targeted data poisoning attacks**. Specifically, we will craft a `spam` email, label it as `ham`, and inject it into the dataset. The goal of this attack is not to allow the attacker to bypass detection for just the exact poisoned email, but to manipulate the model so that it is more likely to misclassify **similar** spam emails as `ham`. This type of attack is particularly effective in scenarios where the attacker wants to subtly manipulate the model’s behavior, allowing them to bypass detection for future spam emails that resemble the poisoned sample.

Targeted attacks are more sophisticated and dangerous compared to simple data poisoning, as they focus on **deliberately misdirecting the model** in a way that undermines its ability to detect certain types of spam (or other specific classes in classification problems like image recognition).

## 1. Data Loading

Before we begin, we need to ensure our environment is set up for loading the dataset. We'll import the necessary libraries and use custom scripts to load and clean the data. The `os` module is crucial here, as it will help us manage file paths when working with local scripts.

## 2. Email Crafting

Next, we'll craft a **spam** email. While the content of the email is not overly complex, it will contain some text and a link that could represent typical spam content. This crafted email will later be injected into the dataset.

## 3. Staging the Attack

The dataset contains over 5,000 data points, so injecting just one poisoned sample won't have a significant impact on its overall distribution. However, we can take a **small sample** (1-5%) of the dataset and **map** it to our crafted `targeted` email. This will increase the likelihood of the poisoned email influencing the model during training.

## 4. Save the Poisoned Dataset

Once the targeted email has been injected into the dataset, we’ll concatenate it with the rest of the data and save the modified dataset as `spam_ham_dataset_targeted.csv`. This poisoned dataset will be used to retrain the model and observe how the targeted attack affects its performance.

## 5. Testing the Model

Now, we’ll load the **vectorizer** and **model** and test the classifier using the retrained, poisoned dataset. We expect that the model will misclassify our **spam** email as **ham**, which is exactly what the targeted attack aims to achieve.

> **As seen**, the model classifies our `spam` email as `ham`, successfully misclassifying it. This demonstrates the effectiveness of the targeted data poisoning attack in causing the model to incorrectly classify similar spam emails in the future.

# Ru

# Отравление данных: Целевая атака

В этом разделе мы исследуем **целевая атака с отравлением данных**. Мы создадим `спам` письмо, пометим его как `хам`, и внедрим его в набор данных. Цель этой атаки — не просто позволить атакующему обходить детекцию для конкретного отравленного письма, а манипулировать моделью так, чтобы она с большей вероятностью ошибочно классифицировала **похожие** спам-письма как `хам`. Этот тип атаки особенно эффективен в ситуациях, когда атакующий хочет незаметно изменить поведение модели, позволяя ей обходить детекцию для будущих спам-писем, схожих с отравленным образцом.

Целевые атаки более сложны и опасны по сравнению с простым отравлением данных, так как они направлены на **умышленное перенаправление** поведения модели, чтобы она не могла правильно классифицировать определенные типы спама (или другие классы в задачах классификации, такие как распознавание изображений).

## 1. Загрузка данных

Перед тем как начать, необходимо убедиться, что наша среда настроена для загрузки данных. Мы импортируем необходимые библиотеки и используем пользовательские скрипты для загрузки и очистки данных. Модуль `os` будет важен, так как он поможет нам работать с локальными файлами и скриптами.

## 2. Создание письма

Теперь давайте создадим **спам** письмо. Контент письма будет простым, с текстом и ссылкой, что является типичным для спама. Это письмо позже будет внедрено в набор данных.

## 3. Подготовка атаки

Наш набор данных содержит более 5,000 данных, и внедрение одного отравленного примера вряд ли существенно повлияет на его распределение. Однако, мы можем взять **небольшую выборку** (1-5%) и **сопоставить** её с нашим созданным `цельным` письмом. Это увеличит вероятность того, что отравленное письмо окажет влияние на модель во время обучения.

## 4. Сохранение отравленных данных

После того как целевое письмо было внедрено в набор данных, мы объединим его с остальными данными и сохраним в файл `spam_ham_targeted.csv`. Этот отравленный набор данных будет использован для повторного обучения модели и наблюдения за тем, как целевая атака влияет на её производительность.

## 5. Тестирование модели

Теперь мы загрузим **векторизатор** и **модель**, чтобы протестировать классификатор с использованием обновленного набора данных с отравленными данными. Мы ожидаем, что модель ошибочно классифицирует наше **спам** письмо как **хам**, что и является целью целевой атаки.

> **Как видно**, модель классифицирует наше `спам` письмо как `хам`, успешно вводя её в заблуждение. Это демонстрирует эффективность целевой атаки с отравлением данных, заставляя модель неправильно классифицировать подобные спам-письма в будущем.
