import pandas as pd
import quandl

import sys
print(sys.path)


print(sys.path)
from core import local

quandl.ApiConfig.api_key = quandl_api_key
data = quandl.get_table('WIKI/PRICES')
print('data', data)
