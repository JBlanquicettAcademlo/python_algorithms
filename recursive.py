
# 1. Debe haber por lo menos un caso base
# 2. El algoritmo debe de cambiar de estado y moverse hacia el caso base
# 3. debe llamarse a si mismo (callback)


def bubble_sort(arr, cant):

    if cant>1:

        for i in range(0, cant-1):
            
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            
            bubble_sort(arr, cant -1)
    
    return arr

print(bubble_sort([3,1,2], len([3,1,2])))

# 8: arr=[3,1,2] cant=3, 9: if ok, 11: 0, 2, 13: if OK, 14: [1,3,2], 16: ([1,3,2], 2)
# 8: arr=[1,3,2] cant=2, 9: if ok, 11: 0, 1, 13: if NO, 16: ([1,3,2], 1)
# Se sale de la recursividad y i se incrementa en 1
# 11: arr=[1,3,2] range(0, 3-1=2) i=1, 13: if OK, 14: [1, 2, 3], 16: ([1,2,3], 2)
# 
