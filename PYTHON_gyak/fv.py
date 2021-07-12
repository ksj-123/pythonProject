def foo():
    print('Hello')


x = 0
foo()


#####

def foo():
    print('Hello')
    print('alma')
    print('korte')


for i in range(5):
    foo()

::
Hello
alma
korte
Hello
alma
korte
Hello
alma
korte
Hello
alma
korte
Hello
alma
korte


#######
def foo(x):
    print('Hello')
    print(x)


for i in range(5):
    foo(i)

::
Hello
0
Hello
1
Hello
2
Hello
3
Hello
4


####

def foo_bar(x, y, z):
    print('Hello')
    print(x)


for i in range(5):
    foo_bar(i)

:::
0
1
2
DONE
10
9
8
7
6
5


####

def foo_bar(x):
    print('Hello', 1, 2)
    print(x)
    return

for i in range(5):
    foo_bar(i)

:::
Hello 1 2
0
Hello 1 2
1
Hello 1 2
2
Hello 1 2
3
Hello 1 2
4


####

def foo_bar(val_to_print):
    print(val_to_print)


for i in range(5):
    foo_bar(i)

:::
0
1
2
3
4



####
def addition(in_var, in_var_other):
    return in_var + in_var_other

x = addition(3, 5)
print(x)

:::
8


####
def addition(in_var, in_var_other):
    return in_var + in_var_other

my_x, my_y = 1, 12
x = addition(my_x, my_y)
print(x)

:::
13

#### fv láthatósága - legyen az alma a fv része, ne legyen kívül belőle
def addition(in_var, in_var_other, alma):
    return (in_var + in_var_other) * alma

my_alma = 12
my_x, my_y = 1, 12
x = addition(my_x, my_y, my_alma)
print(x)

:::
156


