import numpy as np
import pandas as pd

# a = np.arange(15).reshape(3, 5)

# print(a)

# b = np.array([1, 2, 3])
# c = np.array([1.0, 2.5, 3.75])

# print(b.dtype)
# print(c.dtype)

a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
a3D = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]]])

print(a1D)
print(a2D)
print(a3D)

print(np.arange(10))
print(np.arange(1, 10, dtype=float))
print(np.arange(1, 10, 0.1))
print(np.linspace(1, 10, 5))

s = pd.Series([1, 2, 3, np.nan, 5])
print(s)

dates = pd.date_range("20260222", periods=5)
print(dates)