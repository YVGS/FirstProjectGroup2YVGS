import numpy  as np

A = np.array([[2, 1, 1], [1, 3, 2], [3, 1, 2]])
print(A)
B = np.array([[10], [18], [17]])
print(np.linalg.det(A))
print(np.linalg.inv(A))

print('Eigenvalues of A:', np.linalg.eigvals(A))
print('Eigenvectors of A:', np.linalg.eig(A)[1])
X = np.linalg.solve(A, B)
print('x y z:', X)

R = A @ X - B
print('Residual:', R)

print("Euclidean norm of residual:", np.linalg.norm(R, ord=2))
