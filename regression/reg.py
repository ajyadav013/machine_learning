# import pandas as pd
# import quandl
# import math

# #import sys
# #print(sys.path)
# #sys.path.append('/home/arjunsingh/practice/machine_learning/')


# #from core import local

# #quandl.ApiConfig.api_key = local.quandl_api_key
# data = quandl.get('WIKI/GOOGL')


# data = data[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# data['HL_PCT'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100
# data['PCT_change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100


# data = data[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# forecast_col = 'Adj. Close'

# data.fillna(-99999, inplace=True)

# forecast_out = int(math.ceil(0.01*len(data)))

# data['label'] = data[forecast_col].shift(-forecast_out)

# data.dropna(inplace=True)

# print(data.tail())


from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([1,2,3,4,5,6], dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m = ((mean(xs)*mean(ys) - mean(xs*ys)) / (mean(xs)**2 - mean(xs**2)))
    b = (mean(ys)-(m*mean(xs)))
    return m, b


m, b = best_fit_slope_and_intercept(xs, ys)

reg_line = [(m*x+b) for x in xs]
plt.scatter(xs, ys)
plt.plot(xs, reg_line)
plt.show()
