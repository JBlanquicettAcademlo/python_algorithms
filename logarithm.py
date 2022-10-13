# def log_1(data:list): 
    
#     for index in range(0, len(data), 4): #O(log n)

#         print(data, index)

# log_1([1, 2, 3, 4, 5, 6, 7])

#O(log n) logaritmica


def binary_search(data:list, value):
    
    n = len(data)
    left = 0
    right = n -1

    while left <= right:
        print(data)

        middle = (left+right) // 2
        
        if value < data[middle]:
            right = middle -1
        
        elif value > data[middle]:
            left = middle + 1
        
        else: 
            return middle, data[middle]
    
    raise ValueError('Not found')


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))


