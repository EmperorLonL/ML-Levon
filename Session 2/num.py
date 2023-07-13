import numpy as np 

arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])


x = [1, 2, 3, 4, 5, 6]
y = [[1, 2, 3], [4, 5, 6]]


arr_math1 = np.array([1,2,3])
arr_math2 = np.array([4,5,6])


arr_r = np.array([1,2,3,4,5,6])
print("Reshape: ",  arr_r.reshape(2, 3))


arr_stat = np.array([1,2,3,4,5,6])
print("Mean: ", np.mean(arr_stat))
print("Max: ", np.max(arr_stat))
print("Sum: ", np.sum(arr_stat))
 
