
def bubble_sort(l):

    bubble = True

    while bubble:

        bubble = False

        for i in range(len(l)-1):

            print(l)

            if (l[i]>l[i+1]):

                bubble = True

                l[i],l[i+1] = l[i+1], l[i]
    
    return l

unordened_list = [6, 5, 12, 10, 9, 1]
print(bubble_sort(unordened_list))
