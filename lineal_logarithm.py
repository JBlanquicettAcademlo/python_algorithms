
def merge_sort(data):

    if len(data)<=1:
        return

    mid = len(data)//2

    left_data = data[:mid]
    right_data = data[mid:]

    print(left_data, right_data)

    merge_sort(left_data)
    merge_sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left_data) and right_index < len(right_data):

        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        
        else:
            data[data_index] = right_data[right_index]
            right_index +=1

        data_index +=1

    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    
    return data


if __name__ == "__main__":

    # [6, 5, 12, 10, 9, 1]
    # [6, 5, 12, 10, 9, 1, 99, 24, 9, 1, 4, 44, 2, 45, 8, 9]
    unordened_list = [6, 5, 12, 10, 9, 1]

    print(merge_sort(unordened_list))
