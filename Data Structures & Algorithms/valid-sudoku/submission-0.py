class Solution:
    # @param i: valid index for a row
    def is_valid_row(self, board, i: int) -> bool:
        # loop through all elements at a row until we find a duplicate (store in map). 
        # If duplicate found -> return false
        # otherwise, return true
        map = {}
        for j in range(9):
            if (board[i][j] == "."):
                continue
            if (map.get(board[i][j])):
                return False
            # otherwise, add element to the map
            map[board[i][j]] = 1
        return True
            
    # @param i: valid index for a column
    def is_valid_column(self, board, j: int) -> bool:
        map = {}
        for i in range(9):
            if (board[i][j] == "."):
                continue
            if (map.get(board[i][j])):
                return False
            # otherwise, add element to the map
            map[board[i][j]] = 1
        return True
    # checks if a box is valid given indecies of top left corner 
    def is_valid_box(self, board, i, j):
        map = {}
        for a in range(i, i+3): # row
            for b in range(j, j+3): # column
                if (board[a][b] == "."):
                    continue
                if (map.get(board[a][b])):
                    return False
                map[board[a][b]] = 1
        return True
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        # checking all rows
        for row in range(9):
            if self.is_valid_row(board, row) == False:
                ans = False
        if ans == True:
            # checking columns only if answer is still true
            for col in range(9):
                if self.is_valid_column(board, col) == False:
                    ans = False
        if ans == True:
            # checking each box
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    if self.is_valid_box(board, i, j) == False:
                        ans = False
        return ans