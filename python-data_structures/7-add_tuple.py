#!/usr/bin/python3
def add(t1, t2, i):
    a = (0 if len(t1) <= i else t1[i])
    b = (0 if len(t2) <= i else t2[i])
    return (a + b, )

def add_tuple(tuple_a=(), tuple_b=()):
    tup1, tup2 = (tuple_a, tuple_b) if len(tuple_a) < len(tuple_b) else (tuple_b, tuple_a)
    newtup = add(tup1, tup2, 0)
    leng = len(tup1) if len(tup1) > 1 else 2

    for t in range(1, leng):
        newtup += add(tup1, tup2, t)

    return (newtup)
