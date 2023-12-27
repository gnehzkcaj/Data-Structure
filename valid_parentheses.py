
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parent_map={'}':'{',']':'[',')':'('}
        for _ in s:
            if _ not in parent_map:
                stack.append(_)
            elif not stack or parent_map[_]  != stack.pop():
                return -1
        return not stack
solution_instance = Solution()
s = "()" 
s2 = "(]"
print(solution_instance.isValid(s))
print(solution_instance.isValid(s2))           