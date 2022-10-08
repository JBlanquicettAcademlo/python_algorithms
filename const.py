y = 20 #O(1)
x = y #O(1)

def suma(x, y): #O(1) constant complexity

    r1 = x + y #O(1)
    r2 = r1*2 #O(1)
    return r2 #O(1)

print(suma(10,20)) #O(1)

def constant(items): #O(1)
    result = items[0] * items[0] #O(1)
    if items[0] > 20: #O(1)
        return 0 #O(1)
    return result #O(1)

lista = [1, 2, 4] #O(1)

print(constant(lista)) #O(1)