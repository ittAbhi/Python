# NumPy — Important Concepts for Machine Learning

## 1. Reshaping Arrays

**Definition:** Reshaping changes the dimensions of an array without changing its elements.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Convert a 1D array into a 2D array with 2 rows and 3 columns.
reshaped = arr.reshape(2, 3)

# Automatically determine the number of rows using -1.
reshaped_auto = arr.reshape(-1, 2)

# Convert a multidimensional array into a 1D array.
flattened = reshaped.flatten()
```

**Important:** The total number of elements must remain the same when reshaping.

---

## 2. Broadcasting

**Definition:** Broadcasting allows NumPy to perform operations on arrays of compatible shapes without manually repeating elements.

```python
# Broadcasting with a scalar.
arr = np.array([1, 2, 3])
result = arr + 10  # Add 10 to every element.

# Broadcasting with a 2D array and a 1D array.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

row = np.array([10, 20, 30])

# Apply the row array to each row of the matrix.
result = matrix + row
```

**Rule:** Compare dimensions from right to left. Two dimensions are compatible if they are equal or one of them is `1`.

**ML use:** Normalization, feature scaling, and mathematical operations on datasets.

---

## 3. Transpose

**Definition:** Transpose swaps the rows and columns of a 2D array.

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Swap rows and columns.
transposed = matrix.T

# Alternatively, use np.transpose().
transposed_alt = np.transpose(matrix)
```

**ML use:** Changing matrix orientation and preparing data for linear algebra operations.

---

## 4. Copy vs. View

**Definition:**
- **View:** Provides access to the same underlying data.
- **Copy:** Creates an independent array with its own data.

```python
arr = np.array([10, 20, 30, 40])

# Create a view that shares the underlying data.
view_arr = arr.view()

# Create an independent copy.
copy_arr = arr.copy()

# Changes through the view can affect the original array.
view_arr[0] = 100

# Changes to the copy do not affect the original array.
copy_arr[1] = 200
```

**Important:** Some NumPy operations return views, while others return copies. Use `.copy()` when you need independent data.

---

## 5. Data Types (`dtype`)

**Definition:** `dtype` specifies the type of elements stored in a NumPy array.

```python
# Create an array with 64-bit floating-point values.
arr = np.array([1, 2, 3, 4], dtype=np.float64)

# Check the array's data type.
print(arr.dtype)

# Convert the array to 32-bit integers.
int_arr = arr.astype(np.int32)
```

### Common NumPy data types

| Data type | Description |
|---|---|
| `np.int32` | 32-bit integer |
| `np.int64` | 64-bit integer |
| `np.float32` | 32-bit floating-point number |
| `np.float64` | 64-bit floating-point number |
| `bool` | Boolean value (`True` or `False`) |

**ML use:** Managing memory and matching the data types expected by ML libraries.

---

## 6. Statistical and Indexing Functions

```python
arr = np.array([10, 20, 30, 40, 50])

# Find the median value.
median = np.median(arr)

# Calculate the standard deviation.
std_dev = np.std(arr)

# Find the index of the maximum value.
max_index = np.argmax(arr)

# Find the index of the minimum value.
min_index = np.argmin(arr)

# Get the sorted unique values.
unique_values = np.unique(arr)

# Restrict values to a specified range.
clipped = np.clip(arr, 20, 40)
```

### Important functions

| Function | Purpose |
|---|---|
| `np.median()` | Finds the middle value |
| `np.std()` | Calculates standard deviation |
| `np.var()` | Calculates variance |
| `np.argmax()` | Returns the index of the maximum value |
| `np.argmin()` | Returns the index of the minimum value |
| `np.unique()` | Returns unique values |
| `np.clip()` | Restricts values to a specified range |

**ML use:** Statistical analysis, identifying extreme values, and understanding feature distributions.

---

## 7. Handling Missing Values (`NaN`)

**Definition:** `NaN` means "Not a Number." It is commonly used to represent missing or undefined numerical data.

```python
arr = np.array([10.0, 20.0, np.nan, 40.0])

# Identify missing values.
missing_mask = np.isnan(arr)

# Calculate the mean while ignoring NaN values.
average = np.nanmean(arr)

# Replace NaN values with zero.
cleaned = np.nan_to_num(arr, nan=0.0)
```

**Important:** Do not automatically replace every missing value with zero. Choose a suitable strategy based on the dataset and the meaning of the missing data.

---

## 8. Random Number Generation

NumPy provides random-number tools for simulations, sampling, and ML experiments.

```python
# Create a random number generator with a fixed seed.
rng = np.random.default_rng(42)

# Generate random integers between 0 and 99.
random_ints = rng.integers(0, 100, size=5)

# Generate random floating-point values in [0, 1).
random_values = rng.random(5)

# Shuffle an array in place.
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)
```

**Important:** A fixed seed helps make experiments reproducible when the same generator setup and operations are repeated.

**ML use:** Random sampling, shuffling datasets, and reproducible experiments.

---

## 9. Matrix Multiplication and Linear Algebra

```python
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Element-wise multiplication.
element_product = A * B

# Matrix multiplication.
matrix_product = A @ B

# Calculate the determinant of a square matrix.
determinant = np.linalg.det(A)

# Calculate the inverse of an invertible square matrix.
inverse = np.linalg.inv(A)

# Solve the linear system A @ x = b.
b = np.array([5, 11])
solution = np.linalg.solve(A, b)
```

### Important distinction

- `A * B`: Multiplies corresponding elements.
- `A @ B`: Performs matrix multiplication.
- `np.linalg.det(A)`: Calculates the determinant.
- `np.linalg.inv(A)`: Calculates the inverse when it exists.
- `np.linalg.solve(A, b)`: Solves a system of linear equations.

**ML use:** Linear regression, neural networks, and mathematical model implementations.

**Best practice:** Prefer `np.linalg.solve()` over explicitly calculating a matrix inverse when solving a linear system.

---

## 10. Data Normalization and Standardization

**Definition:** Scaling transforms numerical features to make their ranges more suitable for analysis or machine learning.

```python
features = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

# Min-max scaling maps values to the range [0, 1].
normalized = (
    (features - np.min(features))
    / (np.max(features) - np.min(features))
)

# Standardization transforms values using the mean and standard deviation.
standardized = (
    (features - np.mean(features))
    / np.std(features)
)
```

### Difference

- **Min-max scaling:** Rescales values to a specified range, commonly `[0, 1]`.
- **Standardization:** Centers values around zero and scales them using their standard deviation.

**Important ML rule:** Fit scaling parameters on the training set only, then apply those same parameters to validation and test data. This helps prevent data leakage.

---

## 11. Additional Useful NumPy Functions

| Function | Purpose |
|---|---|
| `np.concatenate()` | Joins arrays along an existing axis |
| `np.split()` | Divides an array into sections |
| `np.expand_dims()` | Adds a dimension |
| `np.squeeze()` | Removes dimensions of size `1` |
| `np.any()` | Checks whether at least one condition is true |
| `np.all()` | Checks whether all conditions are true |
| `np.isnan()` | Identifies `NaN` values |
| `np.isinf()` | Identifies infinite values |
| `np.corrcoef()` | Calculates correlation coefficients |
| `np.meshgrid()` | Creates coordinate grids |
| `np.where()` | Finds matching indices or selects values conditionally |
| `np.random.permutation()` | Returns a randomly permuted array or sequence |

---

