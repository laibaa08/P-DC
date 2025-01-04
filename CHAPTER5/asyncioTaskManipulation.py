import asyncio

# Define the factorial coroutine using async def
async def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        await asyncio.sleep(1)  # Use await instead of yield from
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))

# Define the fibonacci coroutine using async def
async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        await asyncio.sleep(1)  # Use await instead of yield from
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))

# Define the binomial_coefficient coroutine using async def
async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print("Asyncio.Task: Compute binomial_coefficient (%s)" % (i))
        await asyncio.sleep(1)  # Use await instead of yield from
    print("Asyncio.Task - binomial_coefficient(%s , %s) = %s" % (n, k, result))

# Main function to run the tasks concurrently
async def main():
    task_list = [
        asyncio.create_task(factorial(10)),  # Use asyncio.create_task
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]
    
    await asyncio.gather(*task_list)

# Now run the program
if __name__ == '__main__':
    asyncio.run(main())  # Call main() using asyncio.run