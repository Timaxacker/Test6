from time import sleep as s, perf_counter as time
dt = 0
t1 = time()
while True:
    print(f"time = {dt} (diff: {time()-t1 - dt})")
    dt += 1
    s(1)