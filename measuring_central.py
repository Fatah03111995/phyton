import numpy as np
from scipy import stats

expl = np.array([1,2,5,5,5,6,7])

def show() :
    print(expl.mean())
    print(np.median(expl))
    print(stats.mode(expl)[1])