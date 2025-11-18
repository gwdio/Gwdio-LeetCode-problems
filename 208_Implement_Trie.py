class Trie:

    def __init__(self):
        self._children = {}

    def insert(self, word: str) -> None:
        if not word:
            self._children[''] = None
            return
        if word[0] not in self._children:
            self._children[word[0]] = Trie()
        self._children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return "" in self._children
        if word[0] not in self._children:
            return False
        return self._children[word[0]].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        if prefix[0] not in self._children:
            return False
        return self._children[prefix[0]].startsWith(prefix[1:])