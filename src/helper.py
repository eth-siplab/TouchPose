import numpy as np

def flatten_arr(arr):
    return arr.reshape(arr.shape[0],arr.shape[1]*arr.shape[2])
