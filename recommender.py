from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

# loads the dataset and returns an object
def load_data(dataset_location):
    df = pd.read_csv(dataset_location)
    return df

# takes book name, dataset to refer to and prints a list of book to recommend
def recommender(bookname, difficulty):
    bookname =  bookname.lower()
    difficulty =  difficulty.lower()
    dataset = load_data("./Datasets/Recommender.csv")
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # vectorize the description of the books present in the dataset
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['Description'])

    # find the similarity score between user profile and books in dataset
    cosine_sim = linear_kernel(
        tfidf_matrix, tfidf_vectorizer.transform([bookname]))

    # sort the recommendations so that we get the most similar books to the topic
    book_indices = cosine_sim.T[0].argsort()[::-1]

    # filter books according to skill level
    output = []
    for index in book_indices:
        book = dataset.iloc[index]
        # filtering books
        if (f" {bookname} " in book['Description'].lower() or f" {bookname} " in book["Book_title"].lower()):
            if (book["skill_level"] == difficulty):
            # begin.append(index)
                output.append(book["Book_title"])
    return output[:5]
