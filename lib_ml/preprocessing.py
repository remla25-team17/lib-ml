import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')

# Define the preprocessing function
def preprocess_reviews(dataset):
    """
    Preprocesses text data from a dataset.

    Args:
        dataset (pd.DataFrame): The dataset containing reviews.

    Returns:
        corpus: A list of preprocessed reviews.
    """
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    if 'not' in all_stopwords:
        all_stopwords.remove('not')

    corpus = []
    max_index = len(dataset) 

    for i in range(0, max_index):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower().split()
        review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    return corpus
