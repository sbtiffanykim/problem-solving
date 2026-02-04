class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        print(left, right, top, bottom)

        while left < right and top < bottom:
            # 1. Traverse from left to right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1  # Move the top boundary down

            # 2. Traverse from top to bottom
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1  # Move the right boundary left

            # Check if boundaries have crossed after the last move
            if not (left < right and top < bottom):
                break
            
            # 3. Traverse from right to left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1  # Move the bottom boundary up

            # 4. Traverse from bottom to top
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1  # Move the left boundary right
        
        return res