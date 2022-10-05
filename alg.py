def bubble_sort(l):

    bubble = True #Constant O(1)

    while bubble: #lineal O(n) 

        bubble =False #Constant O(1)
        for i in range(len(l)-1): #lineal O(n) -1 = O(n) 

            if (l[i]>l[i+1]): #Constant O(1)

                bubble=True #Constant O(1)

                l[i], l[i+1] = l[i+1], l[i] #Constant O(1)
    return l
# O(n^2) Cuadratic time complexity

ordened_list = bubble_sort([4,6,7,8,45,2,4,4,1,4,5,68,89,2,433,21,4,3,2,13,45,3,1])
##4 > 6 .. F
##6 > 7 .. F
##7 > 8 .. F
##8 > 45 .. F 
##45 > 2 .. V 

# 4,6,7,8,45,2
# 4,6,7,8,2,45

print(ordened_list)
print(ordened_list[::-1])