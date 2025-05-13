from gensim import corpora, models
from pprint import pprint

documents = [
    "I love natural language processing and machine learning.",
    "Topic modeling is an interesting technique in NLP.",
    "Python programming language is widely used for NLP tasks.",
    "Machine learning algorithms play a crucial role in NLP applications."
]


tokenised = [doc.lower().split() for doc in documents]

dictionary = corpora.Dictionary(tokenised)

# Create a bag-of-words representation of the documents
corpus = [dictionary.doc2bow(doc) for doc in tokenised]

# Build the TF-IDF model
tfidf_model = models.TfidfModel(corpus)

# Build the LSA model
lsa_model = models.LsiModel(tfidf_model[corpus], id2word=dictionary, num_topics=2)

pprint(lsa_model.print_topics())

# Transform the corpus using the LSA model
transformed_corpus = lsa_model[tfidf_model[corpus]]

# Print the transformed corpus
for doc in transformed_corpus:
    print(doc)
