import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


class CleanText:
    def __init__(self):
        # Preload the stopwords in the constructor to improve efficiency
        self.stop_words = set(stopwords.words('english'))

    def on_clean(self, text: str):
        # Convert text to lowercase
        text = text.lower()

        # Remove special characters (keeping punctuation like !, ?, etc.)
        text = re.sub(r'[^\w\s!?.,;]', '', text)

        # Remove extra whitespaces and strip leading/trailing spaces
        text = re.sub(r'\s+', ' ', text).strip()

        # Remove stopwords
        text = ' '.join([word for word in text.split()
                        if word not in self.stop_words])

        return text
