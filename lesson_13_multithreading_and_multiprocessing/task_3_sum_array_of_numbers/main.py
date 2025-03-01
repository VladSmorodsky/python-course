import multiprocessing
from typing import List


def calculate_sum(numbers, result, index):
    """
    Calculate the sum of numbers[index]
    :param numbers:
    :param result:
    :param index:
    :return:
    """
    total = sum(numbers)
    result[index] = total


def total_array_sum(large_array: List[int | float]) -> float:
    """
    Calculate the total sum of all numbers in the array
    :param large_array:
    :return:
    """
    num_processes = multiprocessing.cpu_count()  # Available processes count
    chunk_size = len(large_array) // num_processes

    processes = []
    results = multiprocessing.Array('l', num_processes)

    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = start_index + chunk_size if i < (num_processes - 1) else len(large_array)
        p = multiprocessing.Process(target=calculate_sum, args=(large_array[start_index:end_index], results, i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total_sum = sum(results)
    return total_sum


if __name__ == '__main__':
    huge_array = list(range(1000000))
    print(total_array_sum(huge_array))
