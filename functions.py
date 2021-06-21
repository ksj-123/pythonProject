
def my_func(a, b, c):  # position based parameter passing
    print(a, b, c)
    return a

def my_func(a,b,c=1): # default value
    print(a,b,c)

my_func(b=1, a=2)

l = [1,2,3]
t = (1,2,3)
# s = set(1,2,3)

d = {"key": "value", "key2": 2, "key3": 5}

my_func(*l) # python idiomatic code
my_func(*t) # python idiomatic code
# my_func(*s) # python idiomatic code
my_func(*d.values()) # python idiomatic code

def my_print(*args, **kwargs):
    print(args)
    print(*args)
    print(kwargs)
    print(*args, **kwargs)

my_print(1,23,3,3,3,end='-', sep='|')
print(1,23,3,3,3)
# print(1,2,3,4,54,5,656,7,8,89,9,9,9,98,9,9,9)