#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = tuple_a if len(tuple_a) > len(tuple_b) else tuple_b
    tup2 = tuple_a if len(tuple_a) <= len(tuple_b) else tuple_b
    newtup = (tup1[0] + (0 if len(tup2) <= 0 else tup2[0]),)

    for t in range(1, len(tup1)):
        b = 0 if len(tup2) <= t else tup2[t]
        newtup += ((0 if len(tup2) <= t else tup2[t]) + tup1[t],)
    return (newtup)
