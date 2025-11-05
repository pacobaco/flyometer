from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_responses(keyword, responses):
    texts = [keyword] + list(responses.values())
    vectorizer = TfidfVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    keyword_vector = vectors[0]
    
    scores = {}
    for i, model in enumerate(responses):
        similarity = cosine_similarity([keyword_vector], [vectors[i+1]])[0][0]
        scores[model] = similarity
    return scores
