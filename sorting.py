import time
import numpy as np

def randomize(size):
    return np.random.randint(0, 200000, size)

def search(size):
    ran = np.random.randint(0, 200000)
    arr = randomize(size)
    found = False
    for num in arr:
        if num == ran:
            found = True
    return found

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        for i in range(n, 0, -1):
            if arr[i - 1] > arr[n]:
                temp = arr[i - 1]
                arr[i - 1] = arr[n]
                arr[n] = temp
    return arr

def insertion_sort(arr):
    for n in range(1, len(arr)):
        key = arr[n]
        j = n - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selection_sort(arr):
    for n in range(len(arr)):
        min_index = n
        for i in range(n + 1, len(arr), 1):
            if arr[i] < arr[min_index]:
                min_index = i

        temp = arr[min_index]
        arr[min_index] = arr[n]
        arr[n] = temp
    return arr

def run(size):
    print("size: ", size)

    tic = time.time()
    c1 = randomize(size)
    toc = time.time()
    print("randomize: ", (toc - tic) * 1000)

    c2 = c1.copy()
    c3 = c1.copy()

    tic = time.time()
    search(size)
    toc = time.time()
    print("search: ", (toc - tic) * 1000)

    tic = time.time()
    bubble_sort(c1)
    toc = time.time()
    print("bubble sort: ", (toc - tic) * 1000)

    tic = time.time()
    insertion_sort(c2)
    toc = time.time()
    print("insertion sort: ", (toc - tic) * 1000)

    tic = time.time()
    selection_sort(c3)
    toc = time.time()
    print("selection sort: ", (toc - tic) * 1000)

    print("------------------")

# print(randomize(20))
run(10)
run(100)
run(1000)
run(10000)
run(100000)
run(1000000) # 1 mil
run(10000000)