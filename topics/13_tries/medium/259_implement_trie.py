"""
Problem: Implement Trie (Prefix Tree)
Difficulty: Medium
Topic: 13_tries
Companies: Amazon, Microsoft, Twitter, Google, Meta

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
Implement the Trie class:
- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

Complexity Proof:
- Time Complexity: O(M) for `insert`, `search`, and `startsWith`, where M is the length of the string/prefix. We do exactly M hash map lookups.
- Space Complexity: O(N * M) where N is the number of words inserted and M is the maximum word length, as we create a new node for every character.
"""

import pytest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True  # return True
    assert trie.search("app") == False  # return False
    assert trie.startsWith("app") == True  # return True
    trie.insert("app")
    assert trie.search("app") == True  # return True
