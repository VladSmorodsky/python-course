import multiprocessing


def calculate_partial_factorial(startNumber: int, endNumber: int) -> int:
    """
    Calculate the partial factorial between start and end.
    :param startNumber:
    :param endNumber:
    :return:
    """
    result = 1
    for number in range(startNumber, endNumber + 1):
        result *= number
    return result


def calculate_parallel_factorial(number: int, processes_count: int) -> int:
    """
    Calculate large number factorial in parallel way
    :param number:
    :param processes_count:
    :return:
    """
    chunk_size = number // processes_count
    results = []

    with multiprocessing.Pool(processes_count) as pool:
        for process_index in range(processes_count):
            start = process_index * chunk_size + 1
            end = number if process_index == processes_count - 1 else (process_index + 1) * chunk_size
            results.append(pool.apply_async(calculate_partial_factorial, (start, end)))
        total = 1
        for result in results:
            print(result.get())
            total *= result.get()
    return total
