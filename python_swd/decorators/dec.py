def track(func):
    func.cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in func.cache:
            print(f'{args}{kwargs} found in cache')
            return func.cache[key]
        result = func(*args, **kwargs)
        func.cache[key] = result
        fib.count += 1
        return result

    return wrapper

def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('./log.txt', 'a') as logfile:
            logfile.write(f'{func.__name__}({args}, {kwargs}) = {result}\n')
        return result

    return wrapper

@track
@log
def fib(n):
   return n if n in (0,1) else fib(n-1) + fib(n-2)

fib.count = 0
result = fib(10)

print(f"{result} calls = {fib.count}")