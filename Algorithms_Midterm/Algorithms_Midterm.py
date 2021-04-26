
import random
import time
import matplotlib.pyplot as plt
import sys

N1 = 100
N2 = 1000
N3 = 10000

def random_array_creator(arr1, arr2, arr3):
    arr1.append(random.sample(range(1, N1 + 1), N1))
    arr2.append(random.sample(range(1, N2 + 1), N2))
    arr3.append(random.sample(range(1, N3 + 1), N3))
    
    return arr1[0], arr2[0], arr3[0]

def bubble_sort(arr):
    for i in range(len(arr) - 1):
         for j in range(len(arr) - 1 - i):
             if arr[j] > arr[j + 1]:
                 temp = arr[j]
                 arr[j] = arr[j + 1]
                 arr[j + 1] = temp
    return arr

def insertion_sort(arr):
    for i in range(len(arr) - 1):
        key = arr[i + 1]
        for j in range(i, -1, -1):
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            else: 
                break
    return arr

def merge_sort_merge(left_arr, right_arr):                  
    if not (len(left_arr) and len(right_arr)):     
        return left_arr or right_arr     
               
    temp = []                            
    i = 0
    j = 0                              

    while (len(temp) < len(left_arr) + len(right_arr) ):                                      
        if i == len(left_arr) or j == len(right_arr):                                          
            temp.extend(left_arr[i:] or right_arr[j:])                                         
        elif left_arr[i] < right_arr[j]:             
            temp.append(left_arr[i])             
            i += 1                             
        else:                                
            temp.append(right_arr[j])            
            j += 1                          

    return temp                          

def merge_sort_divide(arr):
    middle = len(arr) // 2
    right_arr = arr[:middle]
    left_arr = arr[middle:]       

    if len(arr) <= 1:                        
        return arr   

    return merge_sort_merge(merge_sort_divide(right_arr), merge_sort_divide(left_arr))     

def quicksort(a, start, end):
    if start < end: 
        pivot = a[start]
        count = start + 1
        for i in range(start, end):
            if pivot > a[i + 1]:
                if (end - start == 1):
                    count += 1
                    break               
                temp = a[count]
                a[count] = a[i + 1]
                a[i + 1] = temp
                count += 1

        a[start] = a[count - 1] 
        a[count - 1] = pivot 
        
        quicksort(a, start = start, end = count - 2)
        quicksort(a, start = count, end = end)
    return a

def find_max_min(arr):
    small = arr[0]
    big = arr[0]
    for i in range(1, len(arr)):
        if small > arr[i]:
            small = arr[i]
        if big < arr[i]:
            big = arr[i]
    return small, big

def radix_sort(arr):
    big = find_max_min(arr)[1]
    decimal_count = 1
    stop = big 
    temp = arr

    while(1):
        if (stop < 10):
            break
        else:
            stop = stop // 10
            decimal_count += 1

    for count in range(0, decimal_count):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(arr)):
            index = (temp[i] // (10 ** count) ) % 10 
            bucket[index].append(temp[i])        
        temp = []
        for i in range(10):
            for j in range(len(bucket[i])):
                temp.append(bucket[i][j])
        # print("count",  count + 1, "\n", temp)        
    return temp
    
    
def bucket_sort(arr, bucket_number):
    small, big = find_max_min(arr)
    bucket_size = (big - small + 1) // bucket_number
    bucket = []
    temp = []

    for i in range(bucket_number):
        bucket.append([i])
    print(bucket)
    for i in range(len(arr)):
        if arr[i] % bucket_size == 0:
            index = (arr[i] // bucket_size) - 1
        else:
            index = (arr[i] // bucket_size)
        bucket[index].append(arr[i])

    for i in range(bucket_number):
        bucket[i] = bucket[i][1:]
        quicksort(bucket[i], 0, bucket_size - 1)

    for i in range(bucket_number):
        for j in range(bucket_size):
            temp.append(bucket[i][j])

    return temp


def check_execution_time(func_number, arr):
    if func_number == 1:
        start_time = time.time()
        arr = bubble_sort(arr)
        execution_time = time.time() - start_time
    elif func_number == 2:
        start_time = time.time()
        arr = insertion_sort(arr)
        execution_time = time.time() - start_time
    elif func_number == 3:
        start_time = time.time()
        arr = merge_sort_divide(arr)
        execution_time = time.time() - start_time
    elif func_number == 4:
        start_time = time.time()
        arr = radix_sort(arr)
        execution_time = time.time() - start_time
    elif func_number == 5:
        start_time = time.time()
        arr = quicksort(arr, 0, len(arr) - 1)
        execution_time = time.time() - start_time
    elif func_number == 6:
        bucket_num = 10
        if len(arr) == 1000:
            bucket_num = 20
        elif len(arr) == 10000:
            bucket_num = 50
        start_time = time.time()
        arr = bucket_sort(arr, bucket_num)
        execution_time = time.time() - start_time
    return execution_time


def plot_execution_times(time_bubble, time_insertion, time_merge, time_radix, time_quick, time_bucket):
    input_size = [N1, N2, N3]

    plt.figure(figsize = (10, 8))
    plt.title("execution times of sorting algorithms")

    plt.plot(input_size, time_bubble, '-', color = "blue", label = "bubble sort")
    plt.plot(input_size, time_insertion, '-', color = "red", label ="insertion sort")
    plt.plot(input_size, time_merge, '-', color = "green", label = "merge sort")
    plt.plot(input_size, time_radix, '-', color = "yellow", label = "radix sort")
    plt.plot(input_size, time_quick, '-', color = "purple", label = "quick sort")
    plt.plot(input_size, time_bucket, '-', color = "orange", label = "bucket sort")
    
    plt.xlabel("input size: 100, 1000, 10000")
    plt.ylabel("execution time")

    plt.legend(loc = 2)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def run():
    arr1 = []
    arr2 = []
    arr3 = []

    arr1, arr2, arr3 = random_array_creator(arr1, arr2, arr3)
    temp1, temp2, temp3 = arr1, arr2, arr3
    # bubble sort
    time_bubble = []
    time_bubble.append(check_execution_time(1, temp1))
    time_bubble.append(check_execution_time(1, temp2))
    time_bubble.append(check_execution_time(1, temp3))
    
    # insertion sort
    temp1, temp2, temp3 = arr1, arr2, arr3
    time_insertion = []
    time_insertion.append(check_execution_time(2, temp1))
    time_insertion.append(check_execution_time(2, temp2))
    time_insertion.append(check_execution_time(2, temp3))

    # merge sort
    temp1, temp2, temp3 = arr1, arr2, arr3
    time_merge = []
    time_merge.append(check_execution_time(3, temp1))
    time_merge.append(check_execution_time(3, temp2))
    time_merge.append(check_execution_time(3, temp3))

    # radix sort
    temp1, temp2, temp3 = arr1, arr2, arr3
    time_radix = []
    time_radix.append(check_execution_time(4, temp1))
    time_radix.append(check_execution_time(4, temp2))
    time_radix.append(check_execution_time(4, temp3))

    # quick sort
    temp1, temp2, temp3 = arr1, arr2, arr3
    time_quick = []
    time_quick.append(check_execution_time(5, temp1))
    time_quick.append(check_execution_time(5, temp2))
    # time_quick.append(check_execution_time(5, temp3))
    time_quick.append(1)

    # bucket sort
    temp1, temp2, temp3 = arr1, arr2, arr3
    time_bucket = []
    time_bucket.append(check_execution_time(6, temp1))
    time_bucket.append(check_execution_time(6, temp2))
    time_bucket.append(check_execution_time(6, temp3))

    plot_execution_times(time_bubble, time_insertion, time_merge, time_radix, time_quick, time_bucket)

sys.setrecursionlimit(4000)
run()