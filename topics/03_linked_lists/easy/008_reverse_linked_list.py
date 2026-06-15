"""
Problem: Reverse Linked List
Difficulty: Easy
Companies: Amazon, Microsoft, Apple, Google

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
from utils.data_structures import ListNode, list_to_linked, linked_to_list

# OPTIMAL (Iterative)
# Time: O(n), Space: O(1)
def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5])
    rev_head = reverseList(head)
    assert linked_to_list(rev_head) == [5,4,3,2,1]
    print("✅ All tests passed!")
