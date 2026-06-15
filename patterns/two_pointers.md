# ✌️ Two Pointers Pattern

## 📖 Concept

The **Two Pointers** pattern involves using two variables (pointers) to iterate through an array or list, usually from different ends or at different speeds, to solve problems involving pairs, subarrays, or searching.

This pattern is highly effective for problems where you need to compare elements, find a specific sum, or manipulate a sorted array in place, often reducing an $O(N^2)$ brute-force solution to $O(N)$.

## ⚙️ How it Works

There are a few common variations of this pattern:

1.  **Opposite Ends (Meeting in the middle):**
    *   Initialize one pointer at the beginning (`left = 0`) and one at the end (`right = len(arr) - 1`).
    *   Move them towards each other based on a condition until they meet or cross.
    *   *Commonly used for:* Searching for pairs in a sorted array (e.g., Two Sum II), reversing an array, or trapping rain water.

2.  **Same Direction (Lagging pointer):**
    *   Initialize two pointers at the beginning (`slow = 0`, `fast = 0`).
    *   Move them in the same direction, but at different paces or conditionally.
    *   *Commonly used for:* Removing duplicates in place, or finding a subarray.

## 📝 Example Code Structure (Opposite Ends)

```python
def twoPointers(arr, target):
    # Usually requires the array to be sorted
    arr.sort() 
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            # We need a larger sum, so move the left pointer right
            left += 1
        else:
            # We need a smaller sum, so move the right pointer left
            right -= 1
            
    return []
```

## 🎯 Related Problems in Repo

- [001: Two Sum](../topics/01_arrays/easy/001_two_sum.py) (Hash Map is optimal, but sorting + Two Pointers is a valid alternative)
- *(More coming soon...)*
