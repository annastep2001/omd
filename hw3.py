from collections import Counter


class CountVectorizer():
    def __init__(self):
        self.feature_names = []

    def fit(self, raw_documents):
        feature_names = set()
        count_matrix = []
        for line in raw_documents:
            for word in line.lower().split():
                feature_names.add(word)

        self.feature_names = sorted(list(feature_names))

    def transform(self, raw_documents):
        count_matrix = []
        all_words = dict.fromkeys(self.feature_names, 0)
        for line in raw_documents:
            cur = Counter(line.lower().split())
            cur.update(all_words)
            cur = dict(sorted(cur.items(), key=lambda x: x[0]))
            count_matrix.append(list(cur.values()))
        return count_matrix

    def fit_transform(self, raw_documents: list):
        self.fit(raw_documents)
        return self.transform(raw_documents)

    def get_feature_names(self):
        return self.feature_names


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
