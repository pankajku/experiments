import sys

def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a

def nqueen_solution_count(n):
    num_solutions = 0
    for solution in queens(n, 0, [], [], []):
        num_solutions += 1
    return num_solutions

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