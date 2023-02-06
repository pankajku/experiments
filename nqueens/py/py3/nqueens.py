import sys
import helpers

def nqueen_solution_count(n):
    board = [[False for j in range(n)] for i in range(n)]
    used_rows = []
    solution_count = 0

    def place_queen(col):
        nonlocal solution_count, used_rows
        if col == n:
            solution_count += 1
            return
        for row in range(n):
            if row in used_rows:
                continue
            valid_cell = True
            for c in range(len(used_rows)):
                r = used_rows[c]
                if abs(r-row) == abs(c-col):
                    valid_cell = False
                    break
            if not valid_cell:
                continue
            board[row][col] = True
            used_rows.append(row)
            place_queen(col+1)
            used_rows.pop()
            board[row][col] = False

    place_queen(0)
    return solution_count

if len(sys.argv) < 2:
    print('Usage:: python nqueens.py <n>')
    sys.exit(0)

n = int(sys.argv[1])
if n <= 0:
    print('<n> must be a positive integer')
    sys.exit(1)

num_solutions = nqueen_solution_count(n)
print('n: {}'.format(n))
print('solution count: {}'.format(num_solutions))
