import sys

def nqueen_solution_count(n):
    rows = [-1 for i in range(n)]
    solution_count = 0
    def can_place(row, col):
        for prev in range(col):
            if rows[prev] == row or abs(rows[prev] - row) == abs(prev - col):
                return False
        return True

    def place_queen(col):
        nonlocal solution_count
        if col == n:
            solution_count += 1
            return
        for row in range(n):
            if can_place(row, col):
                rows[col] = row
                place_queen(col+1)

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
print('solution count for n = {}: {}'.format(n, num_solutions))
