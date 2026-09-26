class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for char in s:
            if char in pairs:  # открывающая
                stack.append(char)
            else:  # закрывающая
                if not stack or pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0