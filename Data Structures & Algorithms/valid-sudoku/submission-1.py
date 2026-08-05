class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## defaultdict(set) because we are checking duplicates
        rows = defaultdict(set) # rows 
        columns = defaultdict(set) # columns 
        squares = defaultdict(set) # 3x3 (row/3 x column x 3)

        for r in range(9): ## if r is in the range 9
            for c in range(9): ## if c is in the range 9
                value = board[r][c] #the value is equal to the board[rows][cols]
                if value != ".": 
                #                # is this digit already seen in its row, column, or box?
                    if value in rows[r] or value in columns[c] or value in squares[(r//3, c//3)]:
                        #do // because we need to see if its a 3x3 so we don't need decimals
                        return False
                    #if not already seen add the values for rows,cols,and sqaures
                    rows[r].add(value)
                    columns[c].add(value)
                    squares[(r//3, c//3)].add(value)
        return True
                       

                    