import multiprocessing

ret = {'foo': False}


def worker(queue):
    ret = queue.get()
    ret['foo'] = True
    queue.put(ret)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    queue.put(ret)
    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()
    p.join()
    print(queue.get())  # Prints {"foo": True}
