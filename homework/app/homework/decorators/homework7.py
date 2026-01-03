import datetime
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        duration = (end - start).total_seconds()
        print(f"{func.__name__} took {duration} seconds to run")
        return result
    return wrapper

@timer
def test_timer():
    time.sleep(3)

test_timer()