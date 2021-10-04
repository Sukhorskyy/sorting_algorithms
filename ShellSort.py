counter = 0

def ShellSort(arr):
    length = len(arr)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = arr[i]
            j = i
            while j >= gap:
                global counter
                counter += 1
                if arr[j-gap] > temp:
                    arr[j] = arr[j-gap]
                    j -= gap
                else:
                    break
            arr[j] = temp
        gap //= 2
    return arr

def get_num_of_comparison():
    '''return the number of comparisons in
    previous case and set counter at 0'''

    global counter
    this_counter = counter
    counter = 0
    return this_counter
