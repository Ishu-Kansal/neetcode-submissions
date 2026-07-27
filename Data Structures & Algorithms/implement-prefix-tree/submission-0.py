class PrefixTree:
    # set of prefixes
    def __init__(self):
        self.root = set()
        self.finalWords = set()

    def insert(self, word: str) -> None:
        partial = ""
        for ch in word:
            partial += ch
            if(partial not in self.root):
                self.root.add(partial)
        self.finalWords.add(word)

    def search(self, word: str) -> bool:
        if word in self.finalWords:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.root:
            return True
        return False
        