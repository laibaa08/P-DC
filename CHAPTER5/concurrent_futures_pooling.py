import concurrent.futures
import time

number_list = list(range(1, 11))

def count(number):
    for i in range(0, 100000000):
        i += 1
    return i * number

def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    # Use time.perf_counter() instead of time.clock() for high precision timing
    start_time = time.perf_counter()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.perf_counter() - start_time))
    
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.perf_counter() - start_time))
    
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.perf_counter() - start_time))