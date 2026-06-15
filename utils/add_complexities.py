import os

BASE_DIR = "/home/wasim/Documents/github/python-dsa-maang/topics"

PROOFS = {
    "001_two_sum.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we iterate through the list at most once. Hash map lookups take O(1) time on average.\n- Space Complexity: O(N) because in the worst case, we might need to store N-1 elements in our hash map before finding a match.\n",
    "002_best_time_to_buy_and_sell_stock.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we only make a single pass through the prices array.\n- Space Complexity: O(1) because we only use two variables (`min_price` and `max_profit`) regardless of the array size.\n",
    "003_contains_duplicate.py": "\nComplexity Proof:\n- Time Complexity: O(N) because creating a set from an array of N elements requires iterating through every element once.\n- Space Complexity: O(N) because the set can grow up to the size of the array if all elements are distinct.\n",
    "004_valid_anagram.py": "\nComplexity Proof:\n- Time Complexity: O(N) where N is the length of the string. We iterate through the strings exactly twice.\n- Space Complexity: O(1) because the size of the hash map is bounded by the size of the alphabet (e.g., 26 lowercase English letters), which is a constant regardless of N.\n",
    "005_longest_substring_without_repeating_characters.py": "\nComplexity Proof:\n- Time Complexity: O(N) because both the left and right pointers only move forward, meaning each character is processed at most twice.\n- Space Complexity: O(min(N, M)) where M is the size of the charset (e.g. 26 or 128 or 256), since the hash map stores at most the unique characters.\n",
    "006_maximum_subarray.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we iterate through the array of numbers exactly once, performing O(1) operations at each step.\n- Space Complexity: O(1) because we only maintain two variables (`max_sum` and `curr_sum`).\n",
    "007_product_of_array_except_self.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we make two separate passes through the array (one for prefix, one for postfix).\n- Space Complexity: O(1) because the output array does not count towards extra space complexity according to the problem statement. We only use constant extra variables.\n",
    "008_reverse_linked_list.py": "\nComplexity Proof:\n- Time Complexity: O(N) where N is the number of nodes in the linked list. We visit each node exactly once.\n- Space Complexity: O(1) because we only use three pointers (`prev`, `curr`, `nxt`) to reverse the links in place.\n",
    "009_merge_two_sorted_lists.py": "\nComplexity Proof:\n- Time Complexity: O(N + M) where N and M are the lengths of the two lists. In the worst case, we iterate until we exhaust both lists.\n- Space Complexity: O(1) because we only allocate a dummy node and a few pointers. We reuse the existing nodes from the input lists.\n",
    "010_valid_parentheses.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we traverse the string once, and stack `push` and `pop` operations are O(1).\n- Space Complexity: O(N) because in the worst case (e.g., all open brackets), the stack will store all N characters.\n",
    "011_climbing_stairs.py": "\nComplexity Proof:\n- Time Complexity: O(N) because we have a single loop running N times to compute the Fibonacci sequence.\n- Space Complexity: O(1) because we only need to store the previous two values (`one` and `two`) rather than a full DP array of size N.\n",
    "012_binary_search.py": "\nComplexity Proof:\n- Time Complexity: O(log N) because we halve the search space at every step.\n- Space Complexity: O(1) because we only use two pointers (`l` and `r`) to define the search bounds.\n",
}


def add_proofs():
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file in PROOFS:
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read()

                # Check if proof already exists
                if "Complexity Proof:" not in content:
                    # Insert the proof before the closing docstring quotes
                    parts = content.split('"""')
                    if len(parts) >= 3:
                        # parts[1] is the docstring content
                        parts[1] = parts[1] + PROOFS[file]
                        content = '"""'.join(parts)
                        with open(filepath, "w") as f:
                            f.write(content)
                        count += 1
    print(f"Added proofs to {count} files.")


if __name__ == "__main__":
    add_proofs()
