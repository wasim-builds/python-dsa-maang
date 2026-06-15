"""
Problem: Number of Atoms
Difficulty: Hard  Companies: Google,Facebook
Problem Statement: Given formula of a chemical compound, return count of each atom.
Complexity: Time O(N^2), Space O(N)
"""

import pytest
from collections import defaultdict


def solve_brute(f):
    return solve_optimal(f)


def solve_optimal(formula):
    stack = [defaultdict(int)]
    i = 0
    n = len(formula)
    while i < n:
        if formula[i] == "(":
            stack.append(defaultdict(int))
            i += 1
        elif formula[i] == ")":
            i += 1
            j = i
            while i < n and formula[i].isdigit():
                i += 1
            mult = int(formula[j:i]) if j < i else 1
            top = stack.pop()
            for k, v in top.items():
                stack[-1][k] += v * mult
        elif formula[i].isupper():
            j = i + 1
            while j < n and formula[j].islower():
                j += 1
            atom = formula[i:j]
            i = j
            while i < n and formula[i].isdigit():
                j = i
                i += 1
            cnt = int(formula[j:i]) if formula[j:i] else 1
            stack[-1][atom] += cnt
    res = stack[0]
    return "".join(f"{k}{v if v>1 else ''}" for k, v in sorted(res.items()))


@pytest.mark.parametrize(
    "f,ex", [("H2O", "H2O"), ("Mg(OH)2", "H2MgO2"), ("K4(ON(SO3)2)2", "K4N2O14S4")]
)
def test_opt(f, ex):
    assert solve_optimal(f) == ex
