"""
Problem: Implement Magic Dictionary
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Design dictionary that searches with one character changed.
Complexity: Time O(N*L) build, O(26*L^2) search
"""


class MagicDictionary:
    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary):
        for w in dictionary:
            self.words.add(w)

    def search(self, searchWord):
        for i in range(len(searchWord)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == searchWord[i]:
                    continue
                nw = searchWord[:i] + c + searchWord[i + 1 :]
                if nw in self.words:
                    return True
        return False


if __name__ == "__main__":
    m = MagicDictionary()
    m.buildDict(["hello", "leetcode"])
    assert not m.search("hello")
    assert m.search("hhllo")
    assert not m.search("hell")
    assert m.search("leetcoded") == False
    print("All tests passed successfully!")
