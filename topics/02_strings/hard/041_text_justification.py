"""
Problem: Text Justification
Difficulty: Hard
Topic: 02_strings  Companies: Google,Amazon,Uber,Airbnb
Problem Statement: Given words and max width, format text so each line has exactly maxWidth chars, fully justified.
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(words, maxWidth):
    return solve_optimal(words, maxWidth)


def solve_optimal(words, maxWidth):
    res = []
    i = 0
    while i < len(words):
        line_len = len(words[i])
        j = i + 1
        while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
            line_len += 1 + len(words[j])
            j += 1
        line_words = words[i:j]
        gaps = j - i - 1
        if j == len(words) or gaps == 0:
            line = " ".join(line_words)
            line += " " * (maxWidth - len(line))
        else:
            total_spaces = maxWidth - sum(len(w) for w in line_words)
            space, extra = divmod(total_spaces, gaps)
            line = ""
            for k, w in enumerate(line_words[:-1]):
                line += w + " " * (space + (1 if k < extra else 0))
            line += line_words[-1]
        res.append(line)
        i = j
    return res


@pytest.mark.parametrize(
    "words,mw,ex",
    [
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16,
            ["This    is    an", "example  of text", "justification.  "],
        )
    ],
)
def test_opt(words, mw, ex):
    assert solve_optimal(words, mw) == ex
