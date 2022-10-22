def bubble_sort(l):
    
    bubble = True # Constante

    while bubble: # lineal

        bubble = False # constante

        for i in range(len(l)-1): # lineal * lineal

            print(l) # constante

            if l[i]>l[i+1]: # constante

                bubble = True # constante
                l[i], l[i+1] = l[i+1], l[i] #constante
        
    return l #constante

print(bubble_sort([5, 1, 4, 2, 8]))
# Cuadratica