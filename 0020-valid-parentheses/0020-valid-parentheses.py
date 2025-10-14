class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {")":"(", "}":"{", "]":"["}  # closed:opened
        opened_p = ["(", "{", "["]
        stack = list()

        if s[0] not in opened_p:  # deal with the edge case
            return False

        for char in s:
            if char in opened_p:
                stack.append(char)
            elif stack and stack[-1] == p_map[char]:
                stack.pop()
        
        return True if not stack else False