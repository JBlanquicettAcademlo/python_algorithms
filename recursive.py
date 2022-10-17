# 1. Debe haber por lo menos un caso base.
# 2. Debe de llamarse a si mismo.
# 3. El algoritmo debe de cambiar de estado y moverse hacia el caso base.

# def i_am_recursive(n:int):

#     if n==0:
#         return 1

#     return n * i_am_recursive(n-1)

# print(i_am_recursive(5))

# n = 5; return 5 * ? = ?
# n = 4; return 4 * ? = ?
# n = 3; return 3 * ? = ?
# n = 2; return 2 * ? = ?
# n = 1; return 1 * ? = ?
# n = 0; return 1

# n = 0; return 1
# n = 1; return 1 * 1 = 1
# n = 2; return 2 * 1 = 2
# n = 3; return 3 * 2 = 6
# n = 4; return 4 * 6 = 24
# n = 5; return 5 * 24 = 120

# array1 = [1,2,3,4,5] #15
# array2 = [1,2,3,4,5,6] #21
# array3 = [1,2,3,4,5,6,7] #28
# array4 = [1,2,3,4,5,6,7,-8] #20

# def sum_list(items:list):

#     print(items)
    
#     if items == []:
#         return 0
#     else:
#         return items[0] + sum_list(items[1:])

# print(sum_list(array1))
# print(sum_list(array2))
# print(sum_list(array3))
# print(sum_list(array4))

# array[0] = 1 + ? [2,3,4,5] no esta vacio
# array[0] = 2 + ? [3,4,5] no esta vacio
# array[0] = 3 + ? [4,5] no esta vacio
# array[0] = 4 + ? [5] no esta vacio
# array[0] = 5 + ? [] no esta vacio

# 5 + 0 = 5
# 4 + 5 = 9
# 3 + 9 = 12
# 2 + 12 = 14
# 1 + 14 = 15

# reverse a list using recursion method


# def reverse_list(arr:list) -> list:
    
#     if arr == []:
#        return []
#     return reverse_list(arr[1:])+[arr[0]]

# ? + [1] : [2,3,4,5]
# ? + [2] : [3,4,5]
# ? + [3] : [4,5]
# ? + [4] : [5]
# ? + [5] : []

# []+[5] = [5]
# [5]+[4] = [5, 4]
# [5, 4] + [3] = [5, 4, 3]
# [5, 4, 3] + [2] = [5, 4, 3, 2]
# [5, 4, 3, 2] + [1] = [5, 4, 3, 2, 1]

# print(array1, reverse_list(array1))
# print(array2, reverse_list(array2))
# print(array3, reverse_list(array3))

