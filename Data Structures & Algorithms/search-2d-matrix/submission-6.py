class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix) - 1
        while row_l <= row_r:
            mid = (row_l + row_r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[0]) - 1
                while l <= r:
                    row_mid = (l + r)//2
                    if matrix[mid][row_mid] == target:
                        return True
                    elif matrix[mid][row_mid] < target:
                        l = row_mid + 1
                    elif matrix[mid][row_mid] > target:
                        r = row_mid - 1
                return False
            elif target < matrix[mid][0]:
                row_r = mid - 1
            elif target > matrix[mid][-1]:
                row_l = mid + 1
        
        return False