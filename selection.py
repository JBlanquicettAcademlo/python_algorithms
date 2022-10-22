def selection_sort(array):
    
    size = len(array) # constante
    for i in range(size): # lineal
        print(array) # constante
        min_index = i # constante
        for j in range(i+1, size): # lineal * lineal
            if array[j] < array[min_index]: # constante
                min_index = j # constante
        (array[i], array[min_index]) = (array[min_index], array[i]) # constante
    
    return array #constante

print(selection_sort([29, 72, 98, 13, 87, 66, 52, 51, 36]))
# Cuadratica