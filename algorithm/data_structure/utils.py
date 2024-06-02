import numpy as np

w = 32

def new_array(n, dtype=np.object_):
    return np.empty(n, dtype)

def _new_array(n):
    return [None]*n

def new_zero_array(n):
    return np.zeros(n)

def new_boolean_matrix(n, m):
    return np.zeros([n, m], np.bool_)

def new_boolean_array(n):
    return np.zeros(n, np.bool_)

def new_int_array(n, init=0):
    a = np.empty(n, np.int32)
    a.fill(init)
    return a

def binfmt(n):
    return "{0:012b}".format(n)