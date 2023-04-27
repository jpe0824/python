import numpy as np

def strassen(A, B):
    n = A.shape[0]

    # Base case: if matrices are 1x1, do regular multiplication
    if n == 1:
        return A * B

    # Split matrices into four submatrices
    A11, A12, A21, A22 = np.array_split(A, 4, axis=0)
    B11, B12, B21, B22 = np.array_split(B, 4, axis=1)

    # Compute seven matrix products recursively
    P1 = strassen(A11, B12 - B22)
    P2 = strassen(A11 + A12, B22)
    P3 = strassen(A21 + A22, B11)
    P4 = strassen(A22, B21 - B11)
    P5 = strassen(A11 + A22, B11 + B22)
    P6 = strassen(A12 - A22, B21 + B22)
    P7 = strassen(A11 - A21, B11 + B12)

    # Compute the output matrices recursively
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    # Combine the output matrices to form the output matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C
import numpy as np

# Define two matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11], [12, 13], [14, 15]])

# Pad matrices with zeros to make their shape a power of 2 along both axes
n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
m = 2**np.ceil(np.log2(n)).astype(int)
A_padded = np.zeros((m, m))
A_padded[:A.shape[0], :A.shape[1]] = A
B_padded = np.zeros((m, m))
B_padded[:B.shape[0], :B.shape[1]] = B

# Multiply matrices using the Strassen algorithm
C = strassen(A_padded, B_padded)

# Print the result
print(C[:A.shape[0], :B.shape[1]])
