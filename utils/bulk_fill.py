#!/usr/bin/env python3
"""Bulk fill remaining template files with real MAANG problems."""

import os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STUB = '''"""
Problem: {title}
Difficulty: {diff}
Topic: {topic}
Companies: {companies}

Problem Statement:
{statement}

Complexity Proof:
- Time: {time_c}
- Space: {space_c}
"""
import pytest
{extra_imports}

{code}

{tests}
'''

PROBLEMS = [
    # (old_path, new_name, title, diff, topic, companies, statement, time_c, space_c, extra_imports, code, tests)
    (
        "topics/01_arrays/easy/006_template_problem.py",
        "006_contains_duplicate.py",
        "Contains Duplicate",
        "Easy",
        "01_arrays",
        "Amazon,Google,Meta",
        "Return true if any value appears at least twice.",
        "O(N)",
        "O(N)",
        "from typing import List",
        "def solve_brute(nums):\n    return len(nums) != len(set(nums))\n\ndef solve_optimal(nums):\n    seen = set()\n    for n in nums:\n        if n in seen: return True\n        seen.add(n)\n    return False",
        '@pytest.mark.parametrize("nums,expected",[([1,2,3,1],True),([1,2,3,4],False)])\ndef test_optimal(nums,expected): assert solve_optimal(nums)==expected\n@pytest.mark.parametrize("nums,expected",[([1,2,3,1],True)])\ndef test_brute(nums,expected): assert solve_brute(nums)==expected',
    ),
    (
        "topics/01_arrays/easy/009_template_problem.py",
        "009_move_zeroes.py",
        "Move Zeroes",
        "Easy",
        "01_arrays",
        "Meta,Amazon",
        "Move all 0s to end while maintaining relative order of non-zero elements.",
        "O(N)",
        "O(1)",
        "from typing import List",
        "def solve_brute(nums):\n    nz=[x for x in nums if x!=0]; nums[:]=nz+[0]*(len(nums)-len(nz))\n\ndef solve_optimal(nums):\n    p=0\n    for i in range(len(nums)):\n        if nums[i]!=0: nums[p],nums[i]=nums[i],nums[p]; p+=1",
        '@pytest.mark.parametrize("nums,expected",[([0,1,0,3,12],[1,3,12,0,0]),([0],[0])])\ndef test_optimal(nums,expected): solve_optimal(nums); assert nums==expected',
    ),
    (
        "topics/01_arrays/easy/012_template_problem.py",
        "012_find_pivot_index.py",
        "Find Pivot Index",
        "Easy",
        "01_arrays",
        "Amazon,Google",
        "Find index where sum of left equals sum of right.",
        "O(N)",
        "O(1)",
        "from typing import List",
        "def solve_brute(nums):\n    for i in range(len(nums)):\n        if sum(nums[:i])==sum(nums[i+1:]): return i\n    return -1\n\ndef solve_optimal(nums):\n    total=sum(nums); left=0\n    for i,n in enumerate(nums):\n        if left==total-left-n: return i\n        left+=n\n    return -1",
        '@pytest.mark.parametrize("nums,expected",[([1,7,3,6,5,6],3),([1,2,3],-1)])\ndef test_optimal(nums,expected): assert solve_optimal(nums)==expected',
    ),
    (
        "topics/01_arrays/easy/015_template_problem.py",
        "015_single_number.py",
        "Single Number",
        "Easy",
        "01_arrays",
        "Amazon,LeetCode",
        "Every element appears twice except one. Find the single one using O(1) space.",
        "O(N)",
        "O(1)",
        "from typing import List",
        "def solve_brute(nums):\n    from collections import Counter\n    c=Counter(nums)\n    return [k for k,v in c.items() if v==1][0]\n\ndef solve_optimal(nums):\n    r=0\n    for n in nums: r^=n\n    return r",
        '@pytest.mark.parametrize("nums,expected",[([2,2,1],1),([4,1,2,1,2],4)])\ndef test_optimal(nums,expected): assert solve_optimal(nums)==expected',
    ),
    (
        "topics/01_arrays/easy/018_template_problem.py",
        "018_running_sum.py",
        "Running Sum of 1D Array",
        "Easy",
        "01_arrays",
        "Amazon,Google",
        "Return running sum where result[i] = sum(nums[0..i]).",
        "O(N)",
        "O(N)",
        "from typing import List",
        "def solve_brute(nums):\n    return [sum(nums[:i+1]) for i in range(len(nums))]\n\ndef solve_optimal(nums):\n    for i in range(1,len(nums)): nums[i]+=nums[i-1]\n    return nums",
        '@pytest.mark.parametrize("nums,expected",[([1,2,3,4],[1,3,6,10]),([1,1,1],[1,2,3])])\ndef test_optimal(nums,expected): assert solve_optimal(nums[:])==expected',
    ),
    (
        "topics/01_arrays/easy/021_template_problem.py",
        "021_missing_number.py",
        "Missing Number",
        "Easy",
        "01_arrays",
        "Amazon,Microsoft",
        "Find the missing number in range [0,n].",
        "O(N)",
        "O(1)",
        "from typing import List",
        "def solve_brute(nums):\n    return [i for i in range(len(nums)+1) if i not in nums][0]\n\ndef solve_optimal(nums):\n    n=len(nums); return n*(n+1)//2-sum(nums)",
        '@pytest.mark.parametrize("nums,expected",[([3,0,1],2),([0,1],2),([9,6,4,2,3,5,7,0,1],8)])\ndef test_optimal(nums,expected): assert solve_optimal(nums)==expected',
    ),
    (
        "topics/01_arrays/easy/024_template_problem.py",
        "024_majority_element.py",
        "Majority Element",
        "Easy",
        "01_arrays",
        "Amazon,Apple",
        "Find the element appearing more than n/2 times. Use O(1) space (Boyer-Moore).",
        "O(N)",
        "O(1)",
        "from typing import List",
        "def solve_brute(nums):\n    from collections import Counter\n    return max(Counter(nums),key=Counter(nums).get)\n\ndef solve_optimal(nums):\n    count=0; cand=None\n    for n in nums:\n        if count==0: cand=n\n        count+=(1 if n==cand else -1)\n    return cand",
        '@pytest.mark.parametrize("nums,expected",[([3,2,3],3),([2,2,1,1,1,2,2],2)])\ndef test_optimal(nums,expected): assert solve_optimal(nums)==expected',
    ),
]


def process(
    old_rel,
    new_name,
    title,
    diff,
    topic,
    companies,
    statement,
    time_c,
    space_c,
    extra_imports,
    code,
    tests,
):
    old_path = os.path.join(REPO, old_rel)
    if not os.path.exists(old_path):
        print(f"SKIP: {old_rel}")
        return False
    new_path = os.path.join(os.path.dirname(old_path), new_name)
    content = STUB.format(
        title=title,
        diff=diff,
        topic=topic,
        companies=companies,
        statement=statement,
        time_c=time_c,
        space_c=space_c,
        extra_imports=extra_imports,
        code=code,
        tests=tests,
    )
    os.rename(old_path, new_path)
    with open(new_path, "w") as f:
        f.write(content)
    print(f"OK: {new_name}")
    return True


done = sum(1 for p in PROBLEMS if process(*p))
print(f"\nBatch done: {done}/{len(PROBLEMS)}")
