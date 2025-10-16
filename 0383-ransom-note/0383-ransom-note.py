class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ransom = defaultdict(int)
        for r in ransomNote:
            map_ransom[r] += 1
        
        for m in magazine:
            if m in map_ransom and map_ransom[m] > 0:
                map_ransom[m] -= 1
        
        for val in map_ransom.values():
            if val > 0:
                return False
        return True