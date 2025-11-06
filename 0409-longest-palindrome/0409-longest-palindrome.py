class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_found = False
        length = 0

        for v in Counter(s).values():
            if v % 2 == 0:
                length += v  # Use all characters if count is even
            else:
                length += v - 1  # Use all but one character to keep it even
                odd_found = True
        
        if odd_found:
            length += 1  # One odd character can be placed in the center
        
        return length