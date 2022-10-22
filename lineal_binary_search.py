import pandas as pd

def ask_for_number(arr:list):

    for i in arr:
        print(i)
    n = int(input("Select a number: "))
    if n in arr:
        return n
    else:
        raise Exception(f'n is not in arr')

def lineal_search(arr, n):
    iters = 0
    for i in range(len(arr)):
        iters+=1
        if arr[i]==n:
            return f'{arr[i]} in position {i}; iters={iters}'
    raise ValueError('Not found')


def binary_search(arr:list, value):
    
    n = len(arr)
    left = 0
    right = n - 1

    iters = 0

    while left <= right:

        iters+=1

        middle = (left+right) // 2

        print(left, middle, right)
       

        if value < arr[middle]:
            right = middle -1
        
        elif value > arr[middle]:
            left = middle +1
        
        else:
            return f'{arr[middle]} in position {middle}; iters={iters}'
    
    raise ValueError('Not found')

df = pd.read_csv('numbers.csv')
arr = df['numbers'].values.tolist()
# df['next_column'][0]
n = ask_for_number(arr)

lineal_result = lineal_search(arr, n)
binary_result = binary_search(arr, n)
# print(lineal_result)
print(binary_result)

# **700**
# left, middle, right
# 0, 502 ,1004
# 503, 753 ,1004
# 503, 627 ,752
# 628, 690 ,752
# 691, 721 ,752
# 691, 705 ,720
# 691, 697 ,704
# 698, 701 ,704
# 698, 699 ,700

# arr[699] = 700

# middle = (left+right) // 2

# if value < arr[middle]:
#   right = middle -1
        
# elif value > arr[middle]:
#   left = middle +1

# ** 200 **
# left, middle, right
# 0, 502 ,1004
# 0, 250 ,501
# 0, 124 ,249
# 125, 187 ,249
# 188, 218 ,249
# 188, 202 ,217
# 188, 194 ,201
# 195, 198 ,201
# 199, 200 ,201
# 199, 199, 199
# arr[199] = 200