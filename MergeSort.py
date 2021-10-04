counter = 0

def MergeSort(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        left_sorted = MergeSort(arr[:n//2])
        right_sorted = MergeSort(arr[n//2:])
        
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged_arr = []
    while left and right:
        if left[0] <= right[0]:
            merged_arr.append(left.pop(0))
        else:
            merged_arr.append(right.pop(0))
        global counter
        counter += 1
    merged_arr = merged_arr + left + right
    return merged_arr

def get_num_of_comparison():
    '''return the number of comparisons in
    previous case and set counter at 0'''

    global counter
    this_counter = counter
    counter = 0
    return this_counter
