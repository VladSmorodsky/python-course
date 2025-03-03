import logging
import multiprocessing

from factorial_functions import calculate_parallel_factorial

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    number = 1000
    processes_count = multiprocessing.cpu_count()
    logging.info(f"Calculating factorial of {number} with {processes_count} processes...")
    factorial_result = calculate_parallel_factorial(number, processes_count)
    logging.info(f"Factorial of {number}: {factorial_result}")
