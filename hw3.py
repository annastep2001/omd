class CountVectorizer():
    def __init__(self):
        self.count_matrix = []
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
        self.count_matrix = count_matrix
        return count_matrix

    def get_feature_names(self):
        return self.feature_names


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(count_matrix)
