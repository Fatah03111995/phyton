import numpy as np
import pandas as pd

example = np.array([1,2,3,4,2,1,2,3,1])
example_series = pd.Series(example)
def show():
    print(example_series.var()) #VARIAN