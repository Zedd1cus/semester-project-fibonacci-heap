from src.fibonacci_heap import FibonacciHeap
import time

def fill_heap(heap, array):
    for key in array:
        heap.insert(key)
    return heap

def bench_insert(path:str):
    new_heap = FibonacciHeap()
    with open(path) as input_data:
        input_keys = [int(key) for key in input_data.readlines()]
        time_fst = time.time()
        new_heap = fill_heap(new_heap, input_keys)
        time_mcs = (time.time() - time_fst)*1000
    return time_mcs

def bench_union(path:str):
    new_heap = FibonacciHeap()
    with open(path) as input_data:
        input_keys = [key for key in input_data.readlines()]
        dever = input_keys.index('\n')
        input_keys1 = [int(key) for key in input_keys[:dever]]
        input_keys2 = [int(key) for key in input_keys[dever+1:]]
        heap1 = fill_heap(new_heap, input_keys1)
        heap2 = fill_heap(new_heap, input_keys2)
        time_fst = time.time()
        heap1.union(heap2)
        time_mcs = (time.time() - time_fst) * 1000
    return time_mcs

def bench_extract_min(path:str):
    new_heap = FibonacciHeap()
    with open(path) as input_data:
        input_keys = [int(key) for key in input_data.readlines()]
        new_heap = fill_heap(new_heap, input_keys[:len(input_keys)-2])
        minim = new_heap.get_min()
        time_fst = time.time()
        exctr_minim = new_heap.extract_min()
        time_mcs = (time.time() - time_fst) * 1000
        if minim != exctr_minim:
            raise RuntimeError('Что-то пошло не так')
    return time_mcs

if __name__ == '__main__':
    print(bench_union('C:/Users/ninza/Projects/semester-project-fibonacci-heap/dataset/100.txt'))