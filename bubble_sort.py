def bubble_sort(l):

    bubble = True

    while bubble:

        bubble = False

        for i in range(len(l)-1):

            if(l[i]>l[i+1]):

                bubble = True

                l[i],l[i+1] = l[i+1], l[i]
    return l
