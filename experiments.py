import random
import time
import copy

import SelectionSort
import InsertionSort
import MergeSort
import ShellSort


def generate_arrays():
    arrays = []
    for i in range(7, 16):
        arrays.append([random.uniform(0, 1) for x in range(2**i)])
    return arrays


def generate_arrays_from_values(values):
    arrays = []
    for i in range(7, 16):
        arrays.append(random.choices(values, k=2**i))
    return arrays


def experiment1and4(arrays, sort_name, num_of_rep):
    '''Run the experiment num_of_rep times and
    calculates the average execution time and
    average number of comparisons'''

    for arr in arrays:
        this_arr = copy.deepcopy(arr)          #rewrite the current instance of the array to another variable
        execution_time = 0                     #so as not to distort the original data
        comp_num = 0

        for i in range(num_of_rep):
            start_time = time.time()
            eval(sort_name + '.' + sort_name + "(this_arr)")
            execution_time += (time.time() - start_time)
            comp_num += eval(sort_name + '.get_num_of_comparison()')

        average_ex_time = execution_time/num_of_rep
        average_comp_num = comp_num/num_of_rep

        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('Len: {}    Time: {:.10f}    Num of comparisons: {}\n'.format(
                len(this_arr), average_ex_time, average_comp_num))


def experiment2and3(arrays, sort_name):
    for arr in arrays:
        this_arr = copy.deepcopy(arr)
        execution_time = 0
        start_time = time.time()
        eval(sort_name + '.' + sort_name + "(this_arr)")
        execution_time = (time.time() - start_time)
        comp_num = eval(sort_name + '.get_num_of_comparison()')
        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('Len: {}    Time: {:.10f}    Num of comparisons: {}\n'.format(
                len(this_arr), execution_time, comp_num))


def main():
    list_of_algo = ["SelectionSort", "InsertionSort", "MergeSort", "ShellSort"]
    test_arrays = generate_arrays()

    with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('    Experiment 1: the average runtime of algorithms on randomly generated arrays\n  ')
    
    for sort in list_of_algo:
        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('-----' + sort + '-----\n')
        experiment1and4(test_arrays, sort, 5)
    
    
    with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('    Experiment 2: the values of the input array are sorted in ascending order\n  ')
    
    for i in range(len(test_arrays)):
        test_arrays[i] = sorted(test_arrays[i])
    
    for sort in list_of_algo:
        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('-----' + sort + '-----\n')
        experiment2and3(test_arrays, sort)
    
    with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('    Experiment 3: the values of the input array are sorted in reverse order\n  ')

    for i in range(len(test_arrays)):
        test_arrays[i] = sorted(test_arrays[i], reverse=True)
    
    for sort in list_of_algo:
        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('-----' + sort + '-----\n')
        experiment2and3(test_arrays, sort)

    with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('    Experiment 4: the array contains only elements from the set {1, 2, 3}\n  ')

    test_arrays = generate_arrays_from_values([1, 2, 3])
    for sort in list_of_algo:
        with open('result.txt', mode='a', encoding='utf-8') as file:
            file.write('-----' + sort + '-----\n')
        experiment1and4(test_arrays, sort, 3)


if __name__ == "__main__":
    main()
