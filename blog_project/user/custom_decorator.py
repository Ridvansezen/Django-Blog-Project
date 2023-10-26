import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\n{func.__name__} çalışma süresi: {elapsed_time} saniye\n")
        return result
    return wrapper