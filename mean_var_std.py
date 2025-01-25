import numpy as np

def calculate(array):
    if len(array) < 9:
        raise ValueError("List must contain nine numbers.")
        
    array = np.array(array).reshape((3, 3))

    def apply(func):
        return [list(func(array, axis=0)), list(func(array, axis=1)), func(array)]

    return {
        'mean': apply(np.mean),
        'variance': apply(np.var),
        'standard deviation': apply(np.std),
        'max': apply(np.max),
        'min': apply(np.min),
        'sum': apply(np.sum),
    }