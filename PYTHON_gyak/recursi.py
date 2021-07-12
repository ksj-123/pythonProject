# rekursion
# Aki nem érti a rekurziót az nem érti a rekurziót
def fn(a):
    if a == 0: # base variant, alapeset
        return 0
    else:
        r = fn(a-1)
        print(r)
        return a
fn(10)