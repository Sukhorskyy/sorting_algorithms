counter = 0

def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            global counter
            counter = counter + 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def get_num_of_comparison():
    '''return the number of comparisons in
    previous case and set counter at 0'''

    global counter
    this_counter = counter
    counter = 0
    return this_counter
