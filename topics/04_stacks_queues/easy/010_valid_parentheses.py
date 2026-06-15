"""
Problem: Valid Parentheses
Difficulty: Easy
Companies: Amazon, Microsoft, Meta, Google

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

# OPTIMAL (Stack)
# Time: O(n), Space: O(n)
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
            
    return True if not stack else False

if __name__ == "__main__":
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    print("✅ All tests passed!")
