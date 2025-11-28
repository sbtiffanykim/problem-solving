class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            # Found the target
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                # If the target is between l and mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Right half is sorted
            else:
                # If the target is between mid and r
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1