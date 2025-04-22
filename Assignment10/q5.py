import numpy as np


arr = np.array(["hello", "world", "numpy", "array", "padding"])


length = 15


centered = np.char.center(arr, length, fillchar='_')
left_justified = np.char.ljust(arr, length, fillchar='_')
right_justified = np.char.rjust(arr, length, fillchar='_')


print("Centered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)