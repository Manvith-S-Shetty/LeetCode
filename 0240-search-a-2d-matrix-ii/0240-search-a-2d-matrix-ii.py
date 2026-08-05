class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row=len(matrix)
        col=len(matrix[0])
        left=0
        right = col-1
        while left < row and right >= 0:
            if matrix[left][right]== target:
                return True
            elif matrix[left][right] < target:
                left += 1
            else:right -=1
        return False