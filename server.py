a = "This is server"
def b(a):
    print(a)

b(a)
from time import sleep as s, perf_counter as time
dt = 0.0
t1 = time()
while True:
    print(f"\rtime = {dt:.3f} time_now = {time() - t1:.3f} (diff: {time() - t1 - dt:.3f})", end="")
    dt += 0.1
    s(0.1)
