import sys
import numpy as np

def factor(A, n, pivot):
    for k in range(n - 1):
        # Find the index of the pivot row
        i_max = np.argmax(np.abs(A[k:n, k])) + k

        if A[i_max, k] == 0:
            return -1

        # Swap rows to pivot
        if i_max != k:
            A[[i_max, k], k:n] = A[[k, i_max], k:n]
            pivot[k], pivot[i_max] = pivot[i_max], pivot[k]

        # Elimination
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:n] -= factor * A[k, k:n]
            A[i, k] = factor

    return 0

def solve(A, n, pivot, b, x):
    # Apply partial pivoting to b
    for k in range(n - 1):
        if pivot[k] != k:
            b[k], b[pivot[k]] = b[pivot[k]], b[k]

    # Forward substitution
    for k in range(n):
        x[k] = b[k] - np.dot(A[k, :k], x[:k])

    # Backward substitution
    for k in range(n - 1, -1, -1):
        x[k] = (x[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / A[k, k]

def main():
    # Process input files
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                # Read rank of system
                n = int(f.readline())

                # Read matrix A
                A = np.zeros((n, n))
                for i in range(n):
                    A[i] = list(map(float, f.readline().split()))

                # Read number of right-hand sides
                num_rhs = int(f.readline())

                print(f"File: {filename}:")
                print("L\\U =")
                for i in range(n):
                    print(" ".join(f"{A[i, j]:.2f}" for j in range(n)))

                # Process each right-hand side
                for j in range(num_rhs):
                    # Read right-hand side
                    b = np.array(list(map(float, f.readline().split())))
                    # Initialize pivot vector
                    pivot = np.arange(n)

                    # Factorize A
                    status = factor(A, n, pivot)
                    if status == -1:
                        print(f"Error: singular matrix in file {filename}")
                        break

                    # Solve for x
                    x = np.zeros(n)
                    solve(A, n, pivot, b, x)

                    # Print results

                    print(f"b = {' '.join(f'{val:.2f}' for val in b)}")
                    print(f"x = {' '.join(f'{val:.2f}' for val in x)}")

        except FileNotFoundError:
            print(f"Error: file {filename} not found")

if __name__ == '__main__':
    main()
