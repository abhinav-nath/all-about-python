import multiprocessing
import math
import time

iterations_count = round(1e7)


def f1():
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


def f2():
    [math.exp(i) * math.sinh(i) for i in [1] * iterations_count]


if __name__ == '__main__':

    start_time = time.time()

    p1 = multiprocessing.Pool(processes=5)
    a = p1.apply_async(f1)

    p2 = multiprocessing.Pool(processes=5)
    b = p2.apply_async(f2)

    a.wait()
    b.wait()

    p1.close()
    p2.close()

    print("\nexecution time :", round(time.time() - start_time, 2), "seconds")

