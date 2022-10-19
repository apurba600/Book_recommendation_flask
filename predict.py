import tensorflow as tf
import numpy as np
import json

model = tf.keras.models.load_model('book_recommendation.h5')
books = list()

with open('wikibooks.json', 'r') as f:

    books = json.load(f)


# Creates a dict of the book title with its index pos as value
book_index = {book[0]: i for i, book in enumerate(books)}
index_book = {i: book[0] for i, book in enumerate(books)}


b_layer = model.get_layer("book_embedding")  # assigns the layer
b_weights = b_layer.get_weights()[0]

# Normalizes all the vectors in the array
b_weights = b_weights / np.linalg.norm(b_weights, axis=1).reshape((-1, 1))

# you can see the magnitude of the vectors is 1
np.sum(np.square(b_weights[0]))


def similar_books(name, weights, n=5, least_similar=False):
    index = book_index
    r_index = index_book

    # tries to see if the query book name is amonst the books in our list, if not returns not found

    try:
        # takes cosine similarities between vectors
        co_sim = np.dot(weights, weights[index[name]])

    except KeyError:
        print(f'{name} Not Found.')
        return list()

    # Sorts the correlation (-1 to 1) in ascending order
    sorted_idx = np.argsort(co_sim)
    # Sorts the correlation (-1 to 1) in descending order
    r_sorted_idx = sorted_idx[::-1]

    recommended_books = list()

    if least_similar:  # if True

        # print(f"The least similar books compared to {name} are:")
        # print("\n")

        for i in range(n):
            recommended_books.append(f'{r_index[sorted_idx[i]]:70}'.strip())
            # print(
            #     f"{r_index[sorted_idx[i]]:70} Similarity: {co_sim[sorted_idx[i]]}")

    else:
        # print(f"The Most similar books compared to {name} are:")
        # print("\n")

        for i in range(n):
            recommended_books.append(f'{r_index[r_sorted_idx[i]]:70}'.strip())
            # print(
            #     f"{r_index[r_sorted_idx[i]]:70} Similarity: {co_sim[r_sorted_idx[i]]}")
    return recommended_books

# print(similar_books("Freud: His Life and His Mind", b_weights))
