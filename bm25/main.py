import numpy as np
from collections import Counter
import re

class BM25FromScratch:
    def __init__(self, b=0.75, k1=1.5):
        self.b = b
        self.k1 = k1
        self.doc_lengths = []
        self.avg_doc_len = 0
        self.corpus_size = 0
        self.vocab = {}
        self.idf = {}
        self.doc_term_freqs = []

    def _tokenize(self, text):
        return re.findall(r'\w+', text.lower())

    def fit(self, corpus):
        self.corpus_size = len(corpus)
        tokenized_corpus = [self._tokenize(doc) for doc in corpus]
        self.doc_lengths = np.array([len(doc) for doc in tokenized_corpus])
        self.avg_doc_len = np.mean(self.doc_lengths)
        
        # Build global vocabulary and document frequencies
        doc_counts = Counter()
        for doc in tokenized_corpus:
            unique_terms = set(doc)
            self.doc_term_freqs.append(Counter(doc))
            for term in unique_terms:
                doc_counts[term] += 1
                
        self.vocab = list(doc_counts.keys())
        
        # Compute IDF via standard Lucene BM25 formula
        for term, freq in doc_counts.items():
            self.idf[term] = np.log(1 + (self.corpus_size - freq + 0.5) / (freq + 0.5))

    def transform(self, query):
        query_terms = self.doc_term_freqs[0]._tokenize(query) if hasattr(self, '_tokenize') else re.findall(r'\w+', query.lower())
        scores = np.zeros(self.corpus_size)
        
        # Calculate standard BM25 vectors over documents
        for term in query_terms:
            if term not in self.idf:
                continue
            
            # Extract raw term frequencies across all docs using list comp converted to numpy
            tf = np.array([freqs[term] for freqs in self.doc_term_freqs])
            
            # The core BM25 formula denominator component: k1 * (1 - b + b * (doc_len / avg_len))
            denominator = tf + self.k1 * (1 - self.b + self.b * (self.doc_lengths / self.avg_doc_len))
            numerator = tf * (self.k1 + 1)
            
            # Add up inverse document frequency weighted matrix scores
            scores += self.idf[term] * (numerator / denominator)
            
        return scores

if __name__ == "__main__":
    # Test Data: Simple legal/cyber security snippet queries
    corpus = [
        "Deployable Knowledge uses hybrid index logic in local web execution structures.",
        "Cryptographic infrastructure and zero-trust systems require high mathematical defense.",
        "High-dimensional statistical matrix calculations scale poorly without structural optimization.",
        "BM25 lexical search scores relevance based on term frequency and document length scaling."
    ]
    
    search_engine = BM25FromScratch()
    search_engine.fit(corpus)
    
    query = "hybrid search logic execution"
    rankings = search_engine.transform(query)
    
    print(f"Query: '{query}'\n")
    for idx in np.argsort(rankings)[::-1]:
        print(f"[Score: {rankings[idx]:.4f}] -> {corpus[idx]}")
