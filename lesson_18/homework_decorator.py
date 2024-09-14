import logging


logging.basicConfig(filename='function_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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

@log_arguments_and_results
@handle_exceptions
def sample_function(x, y):
    return x / y

if __name__ == "__main__":
    sample_function(10, 2)
    sample_function(10, 0)