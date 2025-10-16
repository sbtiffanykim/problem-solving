class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^0-9a-z]', '', s.lower())  # remove all non-alphanumeric characters
        return s == s[::-1]