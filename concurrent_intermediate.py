from concurrent import futures
import time

def some_function(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"This is returned with sec {seconds}"


if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as executor:
        secs = [1, 2 , 5 , 2 ,4 ]
        results = [executor.submit(some_function,sec) for sec in secs]
        
        for f in futures.as_completed(results):
            print(f.result())