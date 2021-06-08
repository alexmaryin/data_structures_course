import time


def measured_time(function):
    def wrapped(*args):
        start = time.perf_counter_ns()
        result = function(*args)
        stop = int((time.perf_counter_ns() - start) / 1000000)
        print(f'Time estimated is {stop} ms')
        return result
    return wrapped
