class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 1. ignore any leading whitespace
        if not s:
            return 0

        i, n = 0, len(s)

        # 2. Handle Sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3. Conversion Loop
        ans = 0
        while i < n and s[i].isdigit():
            ans = (ans * 10) + int(s[i])
            i += 1
        ans *= sign  # get the number

        # 4. Rounding
        MAX_INT, MIN_INT = 2 ** 31 - 1, -2 ** 31
        return min(MAX_INT, max(MIN_INT, ans))