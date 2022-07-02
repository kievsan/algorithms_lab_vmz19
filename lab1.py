# Алгоритмы и структуры данных.
# 5 семестр ВМЗ-19
# Задание 1 Алгоритмы сортировки

from pprint import pprint
import numpy
import time


def algorithm_OddEvenSort(size):
    randoms = numpy.random.randint(100000, size=size)
    len_arr = len(randoms)
    hasSorted = 1
    start_time = time.time()
    while hasSorted:
        hasSorted = 0
        for odd_even in range(2):
            for n in range(odd_even, len_arr - 1, 2):
                if randoms[n] > randoms[n + 1]:
                    randoms[n], randoms[n + 1] = randoms[n + 1], randoms[n]
                    hasSorted = 1
    return time.time() - start_time


def algorithm_maxHeapSort(size):
    randoms = numpy.random.randint(100000, size=size)
    len_arr = len(randoms)
    start_time = time.time()
    # Build maxHeap:
    for n in range(len_arr, -1, -1):
        heapify_maxHeapSort(randoms, len_arr, n)
    # SWAP elements:
    for n in range(len_arr - 1, 0, -1):
        randoms[0], randoms[n] = randoms[n], randoms[0]
        heapify_maxHeapSort(randoms, n, 0)
    return time.time() - start_time


def heapify_maxHeapSort(arr, n, i):
    left_child = 2 * i + 1
    right_child = left_child + 1
    if left_child < n and arr[left_child] > arr[i]:
        max_ = left_child
    else:
        max_ = i
    if right_child < n and arr[right_child] > arr[max_]:
        max_ = right_child
    if max_ != i:
        arr[i], arr[max_] = arr[max_], arr[i]
        heapify_maxHeapSort(arr, n, max_)
