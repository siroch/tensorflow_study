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

arr1 = np.arange(10)
print('arr1:\n',arr1)
arr2 = arr1.reshape((2, 5))
print('arr2:\n',arr2)
arr3 = arr1.reshape((5, 2))
print('arr3:\n',arr3)
# print(arr1.reshape((4,3))) <-- 크기가 안맞아서 에러남
print("-----------------------------")

arr1 = np.arange(10)
print('arr1:\n',arr1)
arr2 = arr1.reshape((-1, 5))
print('arr2:\n',arr2, arr2.shape)
arr3 = arr1.reshape((5, -1))
print('arr3:\n',arr3, arr3.shape)
print("-----------------------------")


arr1 = np.arange(8)
arr3d = arr1.reshape((2, 2, 2))
print('arr3d:\n',arr3d.tolist())

arr2 = arr3d.reshape(-1, 1)
print('arr2:\n',arr2.tolist(),'\narr2 shape:\n',arr2.shape)

arr3 = arr1.reshape((-1, 1))
print('arr3:\n',arr3.tolist(),'\narr3 shape:\n',arr3.shape)
print("-----------------------------")


arr1 = np.arange(start=1, stop=10)
print('arr1:',arr1)
value = arr1[2]
print('value:',value)
print(type(value))
print("-----------------------------")

arr1d = np.arange(start=1, stop=10)
arr2d = arr1d.reshape(3, 3)
print(arr2d)

print('(row=0, col=0) index 가리키는 값:', arr2d[0, 0])
print('(row=0, col=1) index 가리키는 값:', arr2d[0, 1])
print('(row=1, col=0) index 가리키는 값:', arr2d[1, 0])
print('(row=2, col=2) index 가리키는 값:', arr2d[2, 2])
print("-----------------------------")

arr1 = np.arange(start=1, stop=10)
arr3 = arr1[arr1>5]
print(arr3)
print("-----------------------------")

arr1 = np.array([3, 2, 1, 9])
print(np.sort(arr1))
print(np.sort(arr1)[::-1])
print("-----------------------------")

print('행렬곱')
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

dot_product = np.dot(A, B)
print(dot_product)
print("-----------------------------")

A = np.array([[1, 2], [3, 4]])
T_m = np.transpose(A)
print(T_m)
print("-----------------------------")







