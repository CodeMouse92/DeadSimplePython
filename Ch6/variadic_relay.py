def call_something_else(func, *args, **kwargs):
    return func(*args, **kwargs)


def say_hi(name):
    print(f"Hello, {name}!")


call_something_else(say_hi, name="Bob")
