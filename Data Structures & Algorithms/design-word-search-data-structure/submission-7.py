class WordDictionary:

    def __init__(self):
        self.lvlMap = {} # stores map of letters to children

    def addWord(self, word: str) -> None:
        currLetter = word[0]
        word += '#'
        if(currLetter in self.lvlMap):
            currLevel = self.lvlMap[currLetter]
        else:
            self.lvlMap[currLetter] = {}
            currLevel = self.lvlMap[currLetter]

        for ch in word[1:]:
            if(ch in currLevel):
                currLevel = currLevel[ch]
            else:
                currLevel[ch] = {}
                currLevel = currLevel[ch]

    def search(self, word: str) -> bool:
        currLetter = word[0]
        toExplore = []
        currLevel = self.lvlMap
        if(word[-1] != '#'):
            word += '#'
        for i in range(len(word)):
            ch = word[i]
            if(ch != '.'):
                if(ch not in currLevel):
                    return False
                currLevel = currLevel[ch]
            else:
                exists = False
                for ltr in currLevel.keys():
                    currExp = word[:i] + ltr + word[i+1:]
                    exists = exists or self.search(currExp)
                    if(exists):
                        return True
                return exists

        return True

