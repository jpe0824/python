import sys

def factor(A, n, pivot):
    for k in range(n - 1):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[p][k] == 0:
            return -1
        #swap rows to pivot
        if p != k:
            A[k], A[p] = A[p], A[k]
            pivot[k], pivot[p] = pivot[p], pivot[k]

        # elimination
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            A[i][k] = round(factor, 2)
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
                A[i][j] = round(A[i][j],2)
    #print l/u
    print("L/U = ", end='\t')
    for i in range(n):
        for j in range(n):
            print(f'{A[i][j]:.2f}', end = '\t')
        print('',end='\n\t')
    print()

def solve(A, n, pivot, b, x):
    # forward substitution
    for i in range(n):
        tot = sum(A[i][j] * x[j] for j in range(i))
        x[i] = b[pivot[i]] - tot
    # backward substitution
    for i in range(n - 1, -1, -1):
        tot = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (x[i] - tot) / A[i][i]

def main():
    if(len(sys.argv[1:]) < 1):
        print('Error:\n usage: lud.py lu1.dat lu2.dat')
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                # read input data
                n = int(f.readline())
                A = [list(map(float, f.readline().split())) for _ in range(n)]
                num_rhs = int(f.readline())
                b_arr = [list(map(float, f.readline().split())) for _ in range(num_rhs)]
                pivot = list(range(n))
                x = [0] * n

                # factorization
                print(f'File {filename}:')
                status = factor(A, n, pivot)
                if status == -1:
                    print(f"Error: {filename}, A matrix is singular")
                    continue

                #solving
                for b in b_arr:
                    solve(A, n, pivot, b, x)
                    print(f"b = {'  '.join(f'{val:.2f}' for val in b)}")
                    print(f"x = {'  '.join(f'{val:.2f}' for val in x)}")
                print('\n')
        except FileNotFoundError:
            print(f"Error: {filename} not found")

if __name__ == '__main__':
    main()