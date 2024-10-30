import multiprocessing
import time

def some_function(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

if __name__ == '__main__':
    start = time.perf_counter()

    processes = []

    for _ in range(10):
        process = multiprocessing.Process(target=some_function, args=[2])
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    final = time.perf_counter()
    print(f"Time executed: {final - start} seconds")
