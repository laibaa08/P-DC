# Basic Python Codes

This repository contains Python scripts that demonstrate both fundamental programming concepts and advanced techniques such as parallel computing, threading, multiprocessing, and GPU computing. The goal is to provide beginner and intermediate programmers with practical examples to enhance their understanding of Python.

---

## 🗂️ **Contents**

1. **[`calculator.py`](calculator.py)**  
   A simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division).  
   - Input two numbers and choose an operation to perform.

2. **[`data_structures.py`](data_structures.py)**  
   Demonstrates the use of various Python data structures, including:  
   - Tuples  
   - Lists  
   - Dictionaries  

3. **[`functions.py`](functions.py)**  
   Explains how to define and use functions in Python.  
   - Defining functions  
   - Function parameters and return values  
   - Calling functions with examples  

4. **[`classes.py`](classes.py)**  
   Introduces object-oriented programming (OOP) in Python:  
   - Creating classes and objects  
   - Defining methods  
   - Using inheritance  

5. **[`mpi_example.py`](mpi_example.py)**  
   Demonstrates distributed computing using **MPI** (Message Passing Interface) with **mpi4py**:  
   - Sending and receiving data  
   - Handling process ranks and sizes  

6. **[`multiprocessing_vs_threading.py`](multiprocessing_vs_threading.py)**  
   Compares multiprocessing and threading for concurrent programming:  
   - `multiprocessing`: Spawns multiple processes for parallel tasks.  
   - `threading`: Spawns multiple threads for shared-memory tasks.  
   - Includes execution time comparison for both approaches.

7. **[`num_parallel_computing.py`](num_parallel_computing.py)**  
   Demonstrates vector addition using **NumPy** for data parallelism:  
   - Efficient computation with large vectors  
   - Measures execution time for optimized tasks.

8. **[`threadpool_executor.py`](threadpool_executor.py)**  
   Illustrates concurrent execution using **ThreadPoolExecutor**:  
   - Managing thread pools  
   - Running functions asynchronously.

9. **[`producer_consumer.py`](producer_consumer.py)**  
   Demonstrates the producer-consumer problem using **multiprocessing**:  
   - `Queue` for inter-process communication.  
   - Producer generates items; consumer processes them.

10. **[`semaphore_example.py`](semaphore_example.py)**  
    Demonstrates using **semaphores** to manage shared resource access with threading:  
    - Limits the number of concurrent threads accessing a resource.  

11. **[`fibonacci_threading.py`](fibonacci_threading.py)**  
    Calculates Fibonacci numbers concurrently using **threading**.

12. **[`threading_event_example.py`](threading_event_example.py)**  
    Explains **threading events** for thread synchronization:  
    - Producer creates random numbers, and consumer processes them with event-based signaling.

13. **[`lock_example.py`](lock_example.py)**  
    Demonstrates using **thread locks** for synchronization:  
    - Prevents race conditions when multiple threads access shared resources.

---

## 📦 **Requirements**

Ensure you have Python 3.x installed. Additionally, install the following libraries:  
- `mpi4py` for MPI examples  
- Standard Python libraries like `threading`, `multiprocessing`, and `concurrent.futures`  

To install `mpi4py`, run:  
```bash
pip install mpi4py
