import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

nltk.download('stopwords')

#Define the preprocessing function
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
        review = preprocess_text(dataset['Review'][i], all_stopwords, ps)
        corpus.append(review)

    return corpus


def embed_reviews(dataset):
    """
    Embeds text data from a dataset.
    """
    embeddings = []
    for i in range(len(dataset)):
        embeddings.append(model.encode(dataset['Review'][i]))

    return embeddings

def preprocess_text(text, all_stopwords=None, ps=None):
    """
    Preprocesses a single text review.

    Args:
        text (str): The review text.
        all_stopwords (list): List of stopwords to remove.
        ps (PorterStemmer): Instance of PorterStemmer for stemming.

    Returns:
        str: The preprocessed review.
    """

    if all_stopwords is None:
        all_stopwords = stopwords.words('english')
        if 'not' in all_stopwords:
            all_stopwords.remove('not')

    if ps is None:
        ps = PorterStemmer()

    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
    review = ' '.join(review)

    return review