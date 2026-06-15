#!/usr/bin/env python3
"""
Master script to rename and fill all remaining template files with real MAANG problems.
Each template file will be replaced with a specific, curated problem.
"""

import os

# Maps old template path -> (new_filename, full_content)
PROBLEMS = {
    # ===================== 01 ARRAYS EASY =====================
    "topics/01_arrays/easy/006_template_problem.py": (
        "006_contains_duplicate.py",
        '''"""
Problem: Contains Duplicate
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Google, Microsoft, Apple, Meta

Problem Statement:
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Complexity Proof:
- Time Complexity: O(N) to iterate through the array once, adding each element to the hash set.
- Space Complexity: O(N) for the hash set in the worst case (all elements are unique).
"""
import pytest
from typing import List

def solve_brute(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def solve_optimal(nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
    "topics/01_arrays/easy/009_template_problem.py": (
        "009_move_zeroes.py",
        '''"""
Problem: Move Zeroes
Difficulty: Easy
Topic: 01_arrays
Companies: Meta, Amazon, Bloomberg, Microsoft, Apple

Problem Statement:
Given an integer array `nums`, move all 0s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

Complexity Proof:
- Time Complexity: O(N) — one pass to collect non-zeros and fill.
- Space Complexity: O(1) — in-place.
"""
import pytest
from typing import List

def solve_brute(nums: List[int]) -> None:
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    nums[:] = non_zeros + zeros

def solve_optimal(nums: List[int]) -> None:
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

@pytest.mark.parametrize("nums, expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([1], [1]),
])
def test_solve_optimal(nums, expected):
    solve_optimal(nums)
    assert nums == expected

@pytest.mark.parametrize("nums, expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
])
def test_solve_brute(nums, expected):
    solve_brute(nums)
    assert nums == expected
''',
    ),
    "topics/01_arrays/easy/012_template_problem.py": (
        "012_find_pivot_index.py",
        '''"""
Problem: Find Pivot Index
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Google, Microsoft

Problem Statement:
Given an array of integers `nums`, calculate the pivot index. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right.

Complexity Proof:
- Time Complexity: O(N) — prefix sum scan.
- Space Complexity: O(1) — only scalar variables.
"""
import pytest
from typing import List

def solve_brute(nums: List[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

def solve_optimal(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0
    for i, n in enumerate(nums):
        if left_sum == total - left_sum - n:
            return i
        left_sum += n
    return -1

@pytest.mark.parametrize("nums, expected", [
    ([1,7,3,6,5,6], 3),
    ([1,2,3], -1),
    ([2,1,-1], 0),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([1,7,3,6,5,6], 3),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
    "topics/01_arrays/easy/015_template_problem.py": (
        "015_single_number.py",
        '''"""
Problem: Single Number
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Microsoft, Apple, Google

Problem Statement:
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
You must implement a solution with O(n) runtime complexity and O(1) extra space.

Complexity Proof:
- Time Complexity: O(N) — one pass through the array.
- Space Complexity: O(1) — XOR trick uses no extra space.
"""
import pytest
from typing import List
from collections import Counter

def solve_brute(nums: List[int]) -> int:
    count = Counter(nums)
    for k, v in count.items():
        if v == 1:
            return k

def solve_optimal(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res

@pytest.mark.parametrize("nums, expected", [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([2,2,1], 1),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
    "topics/01_arrays/easy/018_template_problem.py": (
        "018_running_sum_of_1d_array.py",
        '''"""
Problem: Running Sum of 1D Array
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Google, Microsoft

Problem Statement:
Given an array `nums`, return the running sum of nums. Running sum = nums[0..i] for each i.

Complexity Proof:
- Time Complexity: O(N).
- Space Complexity: O(N) for the output, O(1) in-place.
"""
import pytest
from typing import List
import itertools

def solve_brute(nums: List[int]) -> List[int]:
    return [sum(nums[:i+1]) for i in range(len(nums))]

def solve_optimal(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4], [1,3,6,10]),
    ([1,1,1,1,1], [1,2,3,4,5]),
    ([3,1,2,10,1], [3,4,6,16,17]),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums[:]) == expected

@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,4], [1,3,6,10]),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
    "topics/01_arrays/easy/021_template_problem.py": (
        "021_missing_number.py",
        '''"""
Problem: Missing Number
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Microsoft, Apple, Bloomberg

Problem Statement:
Given an array `nums` containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Complexity Proof:
- Time Complexity: O(N) — Gauss sum trick.
- Space Complexity: O(1).
"""
import pytest
from typing import List

def solve_brute(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i

def solve_optimal(nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

@pytest.mark.parametrize("nums, expected", [
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([3,0,1], 2),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
    "topics/01_arrays/easy/024_template_problem.py": (
        "024_majority_element.py",
        '''"""
Problem: Majority Element
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon, Apple, Yahoo, Google

Problem Statement:
Given an array `nums` of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times.

Complexity Proof:
- Time Complexity: O(N) — Boyer–Moore Voting Algorithm.
- Space Complexity: O(1).
"""
import pytest
from typing import List
from collections import Counter

def solve_brute(nums: List[int]) -> int:
    count = Counter(nums)
    return max(count, key=count.get)

def solve_optimal(nums: List[int]) -> int:
    count = 0
    candidate = 0
    for n in nums:
        if count == 0:
            candidate = n
        count += (1 if n == candidate else -1)
    return candidate

@pytest.mark.parametrize("nums, expected", [
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
])
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([3,2,3], 3),
])
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
''',
    ),
}

# Generate remaining problems for all template files
REMAINING = {}


# Helper to generate content
def make_problem(
    title,
    difficulty,
    topic,
    companies,
    statement,
    brute_code,
    optimal_code,
    test_cases_brute,
    test_cases_optimal,
    imports="",
):
    return f'''"""
Problem: {title}
Difficulty: {difficulty}
Topic: {topic}
Companies: {companies}

Problem Statement:
{statement}
"""
import pytest
{imports}

def solve_brute({brute_code["sig"]}):
{brute_code["body"]}

def solve_optimal({optimal_code["sig"]}):
{optimal_code["body"]}

{test_cases_optimal}

{test_cases_brute}
'''


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.join(base, "..")

    count = 0
    for old_rel, (new_name, content) in PROBLEMS.items():
        old_path = os.path.join(repo, old_rel)
        if not os.path.exists(old_path):
            print(f"SKIP (not found): {old_rel}")
            continue

        new_path = os.path.join(os.path.dirname(old_path), new_name)
        os.rename(old_path, new_path)

        with open(new_path, "w") as f:
            f.write(content)

        print(f"✅ {new_name}")
        count += 1

    print(f"\nDone: {count} files processed.")
