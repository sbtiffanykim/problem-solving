class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(index, path): 
            # base case: level == length
            if index == len(nums):
                results.append(path[:])
                return 
            
            path.append(nums[index])  # add number to a path
            backtrack(index + 1, path)
            path.pop() # backtracking step
                
            backtrack(index + 1, path)            
        
        backtrack(0, [])
        return results