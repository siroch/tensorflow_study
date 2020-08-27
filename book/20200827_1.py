import numpy as np

print("-----------------------------")

list1 = [1, 2, 3]
print(type(list1))
print("-----------------------------")

array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)
print("-----------------------------")

list2 = [1, 2, 'test']
array2 = np.array(list2)
print(array2, array2.dtype)
print("-----------------------------")

list3 = [1, 2, 3.0]
array3 = np.array(list3)
print(array3, array3.dtype)
print("-----------------------------")

arr_int = np.array([1, 2, 3])
arr_float = arr_int.astype('float64')
print(arr_float, arr_float.dtype)
print("-----------------------------")

arr_int1 = arr_float.astype('int32')
print(arr_int1, arr_int1.dtype)
print("-----------------------------")

arr_float1 = np.array([1.1, 2.1, 3.9])
arr_int2 = arr_float1.astype('int32')
print(arr_int2, arr_int2.dtype)
print("-----------------------------")

seq_arr = np.arange(10)
print(seq_arr)
print(seq_arr.dtype, seq_arr.shape)
print("-----------------------------")

zero_arr = np.zeros((3, 2), dtype='int32')
print(zero_arr)
print(zero_arr.dtype, zero_arr.shape)
print("-----------------------------")

one_arr = np.ones((3, 2))
print(one_arr)
print(one_arr.dtype, one_arr.shape)
print("-----------------------------")