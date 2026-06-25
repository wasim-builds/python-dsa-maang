"""
Problem: Minimize XOR
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Find minimum integer x with same number of set bits as target, minimizing x XOR num.
Complexity: Time O(log N), Space O(1)
"""


def solve_brute(num, target):
    return solve_optimal(num, target)


def solve_optimal(num, target):
    t_bits = bin(target).count("1")
    n_bits = bin(num).count("1")
    x = 0
    if t_bits <= n_bits:
        cnt = t_bits
        for i in range(31, -1, -1):
            if cnt > 0 and (num >> i) & 1:
                x |= 1 << i
                cnt -= 1
    else:
        x = num
        cnt = t_bits - n_bits
        for i in range(32):
            if cnt > 0 and not ((x >> i) & 1):
                x |= 1 << i
                cnt -= 1
    return x


if __name__ == "__main__":
    test_cases = [(3, 5, 3), (1, 12, 3)]

    for num, t, ex in test_cases:
        assert solve_optimal(num, t) == ex
    print("All tests passed successfully!")
