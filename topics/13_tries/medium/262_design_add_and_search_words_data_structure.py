"""
Problem: Design Add and Search Words Data Structure
Difficulty: Medium
Topic: 13_tries
Companies: Meta, Amazon, Google, Microsoft, Apple

Problem Statement:
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the `WordDictionary` class:
- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

Complexity Proof:
- Time Complexity: `addWord` is O(M) where M is the length of the word. `search` is O(M) for words without dots. For words with dots, in the worst case it is O(26^M) since a dot branches out to all 26 possible children at each step.
- Space Complexity: O(N * M) where N is the number of words added and M is the maximum length of a word, as we create a new node for each character.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Time: O(M)
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    # Time: O(M) without dots, O(26^M) worst case with dots
    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # Try all possible children
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.is_word

        return dfs(0, self.root)


if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    assert wordDictionary.search("pad") == False
    assert wordDictionary.search("bad") == True
    assert wordDictionary.search(".ad") == True
    assert wordDictionary.search("b..") == True
    print("All tests passed successfully!")
