class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)

        for m in magazine:
            count[m] += 1
        
        for r in ransomNote:
            count[r] -= 1
            if count[r] < 0:
                return False
        return True