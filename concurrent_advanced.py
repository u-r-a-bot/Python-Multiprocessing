from concurrent import futures
import time

def some_function(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"This is returned with sec {seconds}"


if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as executor:  ### If want to use Thread just repalce ProcessPoolExecutor with ThreadPoolExecutor
        secs = [1, 2 , 5 , 2 ,4 ]
        results = executor.map(some_function, secs)
        
        for result in results:
            print(result)