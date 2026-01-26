class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = (sorted(Counter(nums).values(), reverse=True))
        return True if counts[0] > 1 else False