# 
def insertion_sort(arr):

    for i in range(1, len(arr)): #lineal
        key = arr[i] # constante
        j = i - 1 # constante
        print(arr) # constante
        while j >= 0 and key < arr[j]: # lineal * lineal
            arr[j+1] = arr[j] # constante
            j -=1 # constante
        arr[j+1] = key # constante
    
    return arr # constante

print(insertion_sort([9, 7, 6, 15, 17, 5, 10, 11]))
# Cuadratica