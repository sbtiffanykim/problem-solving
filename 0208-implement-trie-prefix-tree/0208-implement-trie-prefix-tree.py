class Trie:

    def __init__(self):
        self.prefix_table = defaultdict(set)  # {length: {prefix}}
        self.word_table = defaultdict(list)  # {starting alphabet: [word]}

    def insert(self, word: str) -> None:
        self.word_table[word[0]].append(word)
        for i in range(1, len(word)+1):
            self.prefix_table[i].add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.word_table[word[0]]

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_table[len(prefix)]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)