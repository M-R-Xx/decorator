def cast(return_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return return_type(result)
            except:
                return TypeError(f"Could not cast {result} to {return_type}")
        return wrapper
    return decorator

@cast(str)
def get_int():
    return 10

print(get_int())

@cast(int)
def get_str():
    return 'hhh'

print(get_str())
