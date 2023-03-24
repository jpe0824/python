import numpy as np

A = np.matrix('0, -7, 5; 0, 4, 7; 4, -3, 7')
b = np.matrix('50; -30; -40')
x = np.linalg.solve(A,b)
# print(x)
"""
[[-15.18115942]
 [ -7.24637681]
 [ -0.14492754]]
"""

result = np.matmul(A,x)

# print(result)
"""
[[ 50.]
 [-30.]
 [-40.]]
"""

A = np.array([[0, -3, 7], [1, 2, -1], [5, -2, 0]])
aDet = np.linalg.det(A)
print(aDet)
"""
-68.99999999999996
"""
