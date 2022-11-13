import multiprocessing
import time


def custom_worker(args):
    result = args[0]
    for x in range(10000):
        for y in range(10000):
            result += x*y
    return result


if __name__ == '__main__':
    processes_count = int(input('input processes count = '))
    timer = time.time()
    pool = multiprocessing.Pool(processes=processes_count)
    results = pool.map(custom_worker, [(0, )])
    print(time.time() - timer)
    pool.close()

