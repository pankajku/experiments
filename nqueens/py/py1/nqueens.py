import sys
import helpers

def nqueen_solution_count(n):
    board = [[False for j in range(n)] for i in range(n)]
    solution_count = 0
    is_solution_invocations = 0

    def place_queen(col):
        nonlocal solution_count, is_solution_invocations
        if col == n:
            if helpers.is_solution(board, n):
                solution_count += 1
                # helpers.print_board(board, n)
            is_solution_invocations += 1
            return
        for row in range(n):
            board[row][col] = True
            place_queen(col+1)
            board[row][col] = False

    place_queen(0)
    return (solution_count, is_solution_invocations)

if len(sys.argv) < 2:
    print('Usage:: python nqueens.py <n>')
    sys.exit(0)

n = int(sys.argv[1])
if n <= 0:
    print('<n> must be a positive integer')
    sys.exit(1)

num_solutions, is_solution_invocations = nqueen_solution_count(n)
print('n: {}'.format(n))
print('solution count: {}'.format(num_solutions))
print('is_solution_invocations: {}'.format(is_solution_invocations))