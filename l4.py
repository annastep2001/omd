from math import log


class CountVectorizer():
    def __init__(self):
        self.feature_names = []

    def fit_transform(self, raw_documents: list):
        feature_names = set()
        count_matrix = []
        for line in raw_documents:
            for word in line.lower().split():
                feature_names.add(word)

        self.feature_names = list(feature_names)
        dict_size = len(self.feature_names)
        word_dict = dict(zip(self.feature_names, range(dict_size)))

        for line in raw_documents:
            cur_line = [0] * dict_size
            for word in line.lower().split():
                ind = word_dict[word]
                cur_line[ind] += 1
            count_matrix.append(cur_line)
        return count_matrix

    def get_feature_names(self):
        return self.feature_names


class TfIdfTransformer:
    def tf_transform(self, count_matrix):
        tf_matrix = []

        for text in count_matrix:
            length = sum(text)
            tf_matrix_row = [round(i / length, 3) for i in text]
            tf_matrix.append(tf_matrix_row)

        return tf_matrix

    def idf_transform(self, count_matrix):
        # ln(всего док + 1 / док со словом + 1) + 1
        res = []
        docs_count = len(count_matrix)

        for i in range(len(count_matrix[0])):
            docs_with = 0
            for j in range(len(count_matrix)):
                if count_matrix[j][i] != 0:
                    docs_with += 1
            res.append(round(log((docs_count + 1) / (docs_with + 1)) + 1, 2))
        return res

    def fit_transform(self, matrix):
        tf = self.tf_transform(matrix)
        idf = self.idf_transform(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])

        return tf_idf


class TfIdfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    transformer = TfIdfTransformer()
    tf = transformer.tf_transform(count_matrix)
    idf = transformer.idf_transform(count_matrix)
    print(vectorizer.get_feature_names())
    print(count_matrix)
    print(tf)
    print(idf)

    tfidfvectorizer = TfIdfVectorizer()
    print(tfidfvectorizer.fit_transform(corpus))
