# ============================================================
# NumPy – Mathematical Operations
# ============================================================
import numpy as np

a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
b = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

# --- Element-wise arithmetic ---
print("a + b:", a + b)
print("a * b:", a * b)
print("b / a:", b / a)
print("a ** 2:", a ** 2)

# --- Universal functions (ufuncs) ---
print("\nsqrt(a):", np.sqrt(a))
print("exp(a):", np.exp(a))
print("log(b):", np.log(b))
print("sin(pi/4):", np.sin(np.pi / 4))

# --- Aggregation ---
print("\nSum:", a.sum())
print("Mean:", a.mean())
print("Std:", a.std())
print("Min:", a.min(), "Max:", a.max())
print("Cumulative sum:", a.cumsum())

# --- Matrix operations ---
A = np.array([[1, 2], [3, 4]], dtype=float)
B = np.array([[5, 6], [7, 8]], dtype=float)

print("\nMatrix multiply A @ B:\n", A @ B)
print("Transpose of A:\n", A.T)
print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

# --- Eigenvalues ---
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# --- Solving a linear system  Ax = b ---
b_vec = np.array([5.0, 11.0])
x = np.linalg.solve(A, b_vec)
print("\nSolution to Ax = b:", x)

# --- Broadcasting ---
row = np.array([[1], [2], [3]])
col = np.array([10, 20, 30])
print("\nBroadcasting row + col:\n", row + col)
