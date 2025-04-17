import numpy as np
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

## Use sys.argv to pass in an integer value for the number
## of consecutive integers to operate on
length = int(sys.argv[1])

def task(n):
    time.sleep(1)
    return n * n #square of number passed in

if __name__ == '__main__':

    numbers = range(0, length) #takes integer value passed in
    ## create a pool of workers
    ## max_workers determines the number of parallel process to run
    with ProcessPoolExecutor(max_workers=4) as executor:
        ## Submit all the jobs to the executor
        results = [executor.submit(task, num) for num in numbers] #send tasks to CPU worker pool 

        ## As jobs finish, pull the results and print them
        for future in as_completed(results): #taking list and detecting when job is finished
        	#detects completion when worker pools finish their 'tasks'
                print(f"Result: {future.result()}")