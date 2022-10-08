def lineal_search(items, value):

    for i in items:
        print(items)
        if items[i] == value:
            return i, items[i]

print(lineal_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))