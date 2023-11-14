class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_mapping.values():
                stack.append(char)
            elif char in bracket_mapping.keys():
                if not stack or bracket_mapping[char] != stack.pop():
                    return False
            else:
                return False

        return not stack