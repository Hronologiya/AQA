import logging


logging.basicConfig(filename='iterator_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_arguments_and_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f'Function {func.__name__} called with arguments {args} and {kwargs}. Result: {result}')
        return result
    return wrapper

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Exception in function {func.__name__}: {e}')
            return None
    return wrapper

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

@log_arguments_and_results
@handle_exceptions
def get_reversed_list(data):
    return list(ReverseIterator(data))

@log_arguments_and_results
@handle_exceptions
def get_even_numbers(n):
    return list(EvenIterator(n))

if __name__ == "__main__":
    print(get_reversed_list([1, 2, 3, 4, 5]))
    print(get_even_numbers(10))