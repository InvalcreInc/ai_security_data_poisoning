# Data Poisoning: Simple Attack

In this section, we will demonstrate a **data poisoning attack** on a spam classifier model. We have already created a high-performing model and introduced the concept of data poisoning. Now, let's experiment by flipping the labels (`labels` and `label_num`) in a sample of the dataset and retrain the model with this poisoned data.

## 1. Data Loading

Before we begin, we need to ensure our environment is set up for data loading. We'll import necessary libraries and load the dataset using custom scripts. The `os` module is essential here since we will be working with local scripts for data handling and cleaning.

## 2. Data Processing

Next, we'll take a small sample (5-10%) of the dataset and process it. We will visualize the distribution of labels in this sample by creating a histogram that shows the proportions of 'ham' and 'spam' messages.

## 3. Staging the Attack

Once we have our sample, we'll perform the actual poisoning attack: flipping the labels (`label` and `label_num`). After flipping the labels, we'll generate a new histogram to observe the change in the distribution. The histogram for the poisoned dataset should show the opposite of the original distribution.

## 4. Saving the Poisoned Dataset

Now that we have successfully poisoned our dataset, we’ll concatenate the poisoned data with the original dataset and save it as `spam_ham_poisoned.csv`. This poisoned dataset will be loaded using the `load_dataset` function for training our model on the contaminated data.

## 5. Expected Results

After training the model on the poisoned dataset, we should expect a **decrease in accuracy**. The accuracy will likely vary depending on the proportion of poisoned data used. A higher proportion of flipped labels will have a greater negative impact on the model's performance.

# Russian

# Отравление данных: Простая атака

В этом разделе мы продемонстрируем **атаку на отравление данных** на модели классификатора спама. Мы уже создали высокоэффективную модель и рассмотрели концепцию отравления данных. Теперь давайте проведем эксперимент, перевернув метки (`labels` и `label_num`) в выборке из нашего набора данных и повторно обучим модель на отравленных данных.

## 1. Загрузка данных

Перед тем как начать, необходимо убедиться, что наша среда готова для загрузки данных. Мы импортируем необходимые библиотеки и загрузим набор данных с помощью пользовательских скриптов. Модуль `os` будет полезен, так как мы будем работать с локальными скриптами для обработки и очистки данных.

## 2. Обработка данных

Далее, мы возьмем небольшую выборку (5-10%) из набора данных и обработаем ее. Мы создадим гистограмму, чтобы визуализировать распределение меток в этой выборке и показать соотношение "ham" и "spam".

## 3. Реализация атаки

Когда выборка будет готова, мы приступим к самому процессу отравления данных: перевернем метки (`label` и `label_num`). После того как метки будут перевернуты, мы снова создадим гистограмму, чтобы увидеть изменения в распределении. Гистограмма для отравленных данных должна быть противоположной предыдущей.

## 4. Сохранение отравленных данных

Теперь, когда мы успешно отравили наш набор данных, мы объединим отравленные данные с исходными и сохраним их в файл `spam_ham_poisoned.csv`. Этот отравленный набор данных мы загрузим с помощью функции `load_dataset`, чтобы обучить модель на загрязненных данных.

## 5. Ожидаемые результаты

После обучения модели на отравленных данных мы должны ожидать **снижение точности**. Точность будет зависеть от пропорции отравленных данных. Чем больше данных с перевернутыми метками, тем сильнее будет негативное влияние на производительность модели.
