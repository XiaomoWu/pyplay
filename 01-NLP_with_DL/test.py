# import modules
import os
import time
from itertools import product
from multiprocessing import Process, Pool, Queue

import numpy as np
import pandas as pd
import sklearn
from joblib import dump, load

#%%---------------------
def draw(n):
    x = np.random.randint(1, n+1)
    return x

def get_k(n):
    xs = set()
    k = 0
    while len(xs) < n:
        k += 1
        x = draw(n)
        xs.add(x)
    #print(f"k is {k}")
    return k

# time increase
def get_tp(m, n):
    ts = time.time()
    ks = []
    for i in range(m):
        ks.append(get_k(n))
    tp = time.time() - ts
    return {'m': m, 'n': n, 'tp': tp}

#%% ------------------------
if __name__ == '__main__':
    np.random.seed(42)
    m_range = [400, 1500, 2700, 3800, 5000]
    n_range = range(1, 22001, 2000)
    params = product(m_range, n_range)    

    with Pool(8) as pool:
        results = pool.starmap(get_tp, params)
    dump(results, 'q2.joblib')

#a = load('q2.joblib')
#print(a)

