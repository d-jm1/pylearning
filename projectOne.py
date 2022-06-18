import matplotlib


from matplotlib import pyplot as plt
import pandas as pd
import tushare as ts
data = ts.get_hist_data("000001",start="2020-01-01",end="2022-01-01")
print(data)
