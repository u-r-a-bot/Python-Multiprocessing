from concurrent import futures
import time

def some_function(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return "This is returned"


if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(some_function , 1)
        f2 = executor.submit(some_function, 1)
        f3 = executor.submit(some_function, 2)
        print(f1.result())
        print(f2.result())
        print(f3.result())
    