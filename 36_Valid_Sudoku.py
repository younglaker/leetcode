

def isValidSudoku(self, board):
    """
    :type bo withard: List[List[str]]
    :rtype: bool
    """
    # count = 0
    n=[[0]*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                print('i=%d j=%d' %(i,j))
                print(n[(i//3)*3:(i//3)*3+2][(j//3)*3:(j//3)*3+2])
                print(board[i][j])
                if board[i][j] in n[i][:]:
                    return False
                if board[i][j] in n[:][j]:
                    return False
                if board[i][j] in n[(i//3)*3:(i//3)*3+2][(j//3)*3:(j//3)*3+2]:
                    return False
            n[i][j]=board[i][j]
    return True

a= isValidSudoku(0, [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
print(a)
