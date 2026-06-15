# 🐢🐇 Fast & Slow Pointers Pattern

## 📖 Concept

The **Fast & Slow Pointers** pattern, also known as the **Hare & Tortoise algorithm**, is a pointer algorithm that uses two pointers which move through an array (or linked list) at different speeds. 

This approach is extremely useful for finding cyclic dependencies (loops) and finding the middle element of a sequence.

## ⚙️ How it Works

1. Initialize two pointers, usually called `slow` and `fast`. Both start at the beginning of the data structure (e.g., the head of a linked list).
2. The `slow` pointer moves one step at a time (`slow = slow.next`).
3. The `fast` pointer moves two steps at a time (`fast = fast.next.next`).
4. **Cycle Detection:** If there is a cycle, the `fast` pointer will eventually catch up to the `slow` pointer from behind. If there is no cycle, `fast` will reach the end.
5. **Finding the Middle:** By the time the `fast` pointer reaches the end of the list, the `slow` pointer will be exactly at the midpoint.

## 📝 Example Code Structure (Cycle Detection)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # Moves 1 step
        fast = fast.next.next     # Moves 2 steps
        
        if slow == fast:          # They meet! There is a cycle
            return True
            
    return False                  # Reached the end, no cycle
```

## 🎯 Related Problems in Repo

- *(Linked List Cycle - Coming soon...)*
- *(Middle of the Linked List - Coming soon...)*
