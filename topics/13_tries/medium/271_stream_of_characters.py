"""
Problem: Stream of Characters
Difficulty: Medium  Companies: Amazon,Google,Microsoft
Problem Statement: Query characters from stream. Return true if any word in words forms suffix of queried chars.
Complexity: Time O(N * L) build, O(L) query; Space O(N * L)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class StreamChecker:
    def __init__(self, words):
        self.root = TrieNode()
        self.stream = []
        self.max_len = max(len(w) for w in words)
        for w in words:
            node = self.root
            for c in reversed(w):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True

    def query(self, letter):
        self.stream.append(letter)
        node = self.root
        for c in reversed(self.stream[-self.max_len :]):
            if c not in node.children:
                return False
            node = node.children[c]
            if node.is_end:
                return True
        return False


if __name__ == "__main__":
    sc = StreamChecker(["cd", "f", "kl"])
    for c, ex in [
        ("a", False),
        ("b", False),
        ("c", False),
        ("d", True),
        ("e", False),
        ("f", True),
    ]:
        assert sc.query(c) == ex
    print("All tests passed successfully!")
