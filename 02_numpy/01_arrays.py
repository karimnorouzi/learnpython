# ============================================================
# NumPy – Arrays
# ============================================================
import numpy as np

# --- Creating arrays ---
a = np.array([1, 2, 3, 4, 5])
print("1-D array:", a)
print("dtype:", a.dtype, "shape:", a.shape)

# --- 2-D array ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2-D array:\n", matrix)
print("Shape:", matrix.shape, "ndim:", matrix.ndim)

# --- Special arrays ---
print("\nzeros (2x3):\n", np.zeros((2, 3)))
print("ones (3x2):\n", np.ones((3, 2)))
print("identity (3x3):\n", np.eye(3))
print("arange 0-9:", np.arange(10))
print("linspace 0-1 (5 pts):", np.linspace(0, 1, 5))

# --- Indexing and slicing ---
print("\nElement [1,2]:", matrix[1, 2])
print("First row:", matrix[0, :])
print("Last column:", matrix[:, -1])
print("Sub-matrix (rows 0-1, cols 1-2):\n", matrix[:2, 1:])

# --- Reshaping ---
flat = np.arange(12)
reshaped = flat.reshape(3, 4)
print("\nReshaped 3x4:\n", reshaped)

# --- Boolean indexing ---
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print("\nValues > 25:", arr[mask])

# --- Random arrays ---
rng = np.random.default_rng(seed=42)
random_arr = rng.integers(0, 100, size=(2, 4))
print("\nRandom integer array:\n", random_arr)
