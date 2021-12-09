import sys
from datetime import datetime


def my_write(string_text):
    string_text = string_text.rstrip()
    if len(string_text) == 0:
        return
    else:
        original_write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]: {string_text}\n')


def timed_output(function):
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write

        def my_write(string_text):
            string_text = string_text.rstrip()
            if len(string_text) == 0:
                return
            else:
                original_write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]: {string_text}\n')

        sys.stdout.write = my_write
        function(*args, **kwargs)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


def redirect_output(filepath):
    def decorator(function):
        def wrapper(*args, **kwargs):
            original_output = sys.stdout
            sys.stdout = open(filepath, 'w')
            function(*args, **kwargs)
            sys.stdout.close()
            sys.stdout = original_output

        return wrapper

    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write

    print_greeting("Nikita")

    calculate()
