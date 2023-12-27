#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if they have fewer than 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Perform element-wise addition
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple

