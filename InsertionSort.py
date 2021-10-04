counter = 0

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0:
            global counter
            counter += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr

def get_num_of_comparison():
    '''return the number of comparisons in
    previous case and set counter at 0'''

    global counter
    this_counter = counter
    counter = 0
    return this_counter
