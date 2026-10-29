class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        blocks = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue
                if char in rows[r]:
                    return False
                rows[r] = rows[r].union(char)
                if char in cols[c]:
                    return False
                cols[c] = cols[c].union(char)
                br, bc = r//3, c//3
                if char in blocks[br, bc]:
                    return False
                blocks[br, bc] = blocks[br, bc].union(char)
        
        return flag