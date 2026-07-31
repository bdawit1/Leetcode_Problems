class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        sqaures = [set() for _ in range(9)] #index (r//3) * 3 + (c//3)

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                
                s = (r//3) * 3 + (c//3)

                if v in rows[r] or v in cols[c] or v in sqaures[s]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                sqaures[s].add(v)
        return True
