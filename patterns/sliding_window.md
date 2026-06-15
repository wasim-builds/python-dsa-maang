# 🪟 Sliding Window Pattern

## 📖 Concept

The **Sliding Window** pattern is used to perform operations on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s, or finding the longest substring with no repeating characters.

Instead of calculating a result for every possible subarray/substring (which usually takes $O(N^2)$ or $O(N^3)$ time), sliding window algorithms process the data in $O(N)$ time by maintaining a "window" that slides over the data.

## ⚙️ How it Works

1. You maintain two pointers, `left` and `right`, which define the bounds of the "window".
2. You expand the window by moving the `right` pointer and updating your current state (e.g., adding to a sum, or adding a character to a hash map).
3. If the window violates the problem's constraint (e.g., the sum becomes too large, or a duplicate character is found), you shrink the window by moving the `left` pointer until the condition is satisfied again.
4. Throughout this process, you keep track of the optimal result (maximum length, minimum length, etc.).

## 📝 Example Code Structure

```python
def slidingWindow(arr):
    left = 0
    max_len = 0
    state = {} # or a sum, or a count

    for right in range(len(arr)):
        # 1. Add arr[right] to state
        
        # 2. Check if state is invalid
        while invalid(state):
            # 3. Remove arr[left] from state
            left += 1
            
        # 4. Update max_len based on valid window
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

## 🎯 Related Problems in Repo

- [005: Longest Substring Without Repeating Characters](../topics/02_strings/medium/005_longest_substring_without_repeating_characters.py)
- *(More coming soon...)*
