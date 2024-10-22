#1
def start(x):
    def increment(y):
        return x + y
    return increment

#2
def my_start(func):
    def wrapper(x, y):
        return func(x, y)
    return wrapper

@my_start
def my_increment(x, y):
    return x + y

first_inc = start(0)
second_inc = start(8)

print(first_inc(3))
print(second_inc(3))

print(my_increment(0, 3))
print(my_increment(8,3))
