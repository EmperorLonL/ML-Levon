import numpy as np

arr = np.random.randint(0, 10, size = 10)
print("Array: ", arr)
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Sum: ", np.sum(arr))
print("Sorted array: ", np.sort(arr))
print("Shuffled array: ", np.random.permutation(arr))
print("Squared array: ", np.square(arr))
print("Square root: ", np.sqrt(arr))


