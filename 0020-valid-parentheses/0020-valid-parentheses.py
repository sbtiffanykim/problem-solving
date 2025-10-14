class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {")":"(", "}":"{", "]":"["}  # closed:opened
        opened_p = ["(", "{", "["]
        stack = list()

        for char in s:
            if char in opened_p:
                stack.append(char)
            elif not stack or stack[-1] != p_map[char]:
                return False
            else:
                stack.pop()
        
        return True if not stack else False