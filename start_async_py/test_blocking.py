from timeit import default_timer as timer
import time

start = timer()

print("First Task. 1 Second")
time.sleep(1) # Wait for a 1 second

print("Second Task, 2 Seconds") 
time.sleep(2)# Wait for 2 seconds

print("Third Task, 3 Seconds") 
time.sleep(3) # Wait for 3 seconds

print(f"Time Elapsed: {timer()-start} seconds")