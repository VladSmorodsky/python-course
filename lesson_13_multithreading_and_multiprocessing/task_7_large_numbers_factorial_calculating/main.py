import multiprocessing

from factorial_functions import calculate_parallel_factorial

if __name__ == '__main__':
    number = 1000
    processes_count = multiprocessing.cpu_count()
    print(f"Calculating factorial of {number} with {processes_count} processes...")
    factorial_result = calculate_parallel_factorial(number, processes_count)
    print(f"Factorial of {number}:", factorial_result)
