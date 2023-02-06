
def print_board(board, n):
    print('-'*(2*n+1))
    for i in range(n):
        line = '|'
        for j in range(n):
            line += str('*' if board[i][j] else ' ')
            line += '|'
        print(line)
    print('-'*(2*n+1))
    return

def rows_valid(board, n):
    # ensure each row has exactly one queen
    for i in range(n):
        count = 0
        for j in range(n):
            if board[i][j]: count += 1
        if count != 1: return False
    return True

def cols_valid(board, n):
    # ensure each column has exactly one queen
    for j in range(n):
        count = 0
        for i in range(n):
            if board[i][j]: count += 1
        if count != 1: return False
    return True

def tl2br_diagonals_valid(board, n):
    # ensure each top-left to bottom-right diagonal has exactly one queen
    for i in range(n):
        count = 0
        for j in range(n-i):
            if board[i+j][j]: count += 1
        if count > 1: return False

    for j in range(1, n):
        count = 0
        for i in range(n-j):
            if board[i][i+j]: count += 1
        if count > 1: return False
    return True

def tr2bl_diagonals_valid(board, n):
    # ensure each top-right to bottom-left diagonal has exactly one queen
    for j in range(n):
        count = 0
        for i in range(j+1):
            if board[i][j-i]: count += 1
        if count > 1: return False

    for i in range(1, n):
        count = 0
        for j in range(n-i):
            if board[i+j][n-1-j]: count += 1
        if count > 1: return False
    return True

def is_solution(board, n):
    if not rows_valid(board, n): return False
    if not cols_valid(board, n): return False
    if not tl2br_diagonals_valid(board, n): return False
    if not tr2bl_diagonals_valid(board, n): return False

    return True

if __name__ == "__main__":
    import copy
    n = 4
    empty_board = [[False for j in range(n)] for i in range(n)]
    vboard1 = copy.deepcopy(empty_board)
    vboard1[0][1] = vboard1[1][3] = vboard1[2][0]  = vboard1[3][2] = True

    print_board(vboard1, 4)
    if is_solution(vboard1, 4): print("a solution")

    iboard1 = copy.deepcopy(empty_board)
    iboard1[0][0] = iboard1[1][1] = iboard1[2][2]  = iboard1[3][3] = True
    print_board(iboard1, 4)
    if not is_solution(iboard1, 4): print("not a solution")

    n = 8
    empty_board = [[False for j in range(n)] for i in range(n)]
    vboard1 = copy.deepcopy(empty_board)
    vboard1[0][3] = vboard1[1][6] = vboard1[2][2] = vboard1[3][7] = True
    vboard1[4][1] = vboard1[5][4] = vboard1[6][0] = vboard1[7][5] = True
    print_board(vboard1, 8)
    if is_solution(vboard1, 8): print("a solution")