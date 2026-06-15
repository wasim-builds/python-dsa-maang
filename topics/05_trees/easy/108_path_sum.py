"""
Problem: Path Sum
Difficulty: Easy  Companies: Amazon,Microsoft,Google,Bloomberg
Problem Statement: Given root and targetSum, return true if tree has root-to-leaf path summing to targetSum.
Complexity: Time O(N), Space O(H)
"""

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../"))
from utils.data_structures import TreeNode, list_to_tree


def solve_brute(root, t):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == t
    return solve_brute(root.left, t - root.val) or solve_brute(root.right, t - root.val)


def solve_optimal(root, t):
    return solve_brute(root, t)


if __name__ == "__main__":
    test_cases = [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([], 0, False),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for arr, t, ex in test_cases:
        from utils.data_structures import list_to_tree

        assert solve_optimal(list_to_tree(arr), t) == ex
    print("All tests passed successfully!")
