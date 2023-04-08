# ============
# time series plot with standard deviation in shading
#
# x1 (sd1) is the mean (standard deviation) for the 1st time series 
# x2 (sd2) is the mean (standard deviation) for the 2nd time series
# x3 (sd3) is the mean (standard deviation) for the 3rd time series

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colnames = ['mon','x1','sd1','x2','sd2','x3','sd3']

data_all = pd.read_csv('data.csv', sep='\s+', header=None, names=colnames)

mon = data_all['mon'].values

x1  = data_all['x1'].values
sd1 = data_all['sd1'].values

x2  = data_all['x2'].values
sd2 = data_all['sd2'].values

x3  = data_all['x3'].values
sd3 = data_all['sd3'].values


x1_low = x1 - sd1
x1_high = x1 + sd1

x2_low = x2 - sd2
x2_high = x2 + sd2

x3_low = x3 - sd3
x3_high = x3 + sd3

plt.xticks(list(range(1,max(mon)+1)),[str(i) for i in range(1,max(mon)+1)])
plt.xlabel('month')
plt.ylabel('X (unit)')

plt.plot(mon, x1, lw=2, label='X1', color = 'blue')
plt.plot(mon, x2, lw=2, label='X2', color = 'red')
plt.plot(mon, x3, lw=2, label='X3', color = 'green')

plt.legend(loc='upper left')

plt.fill_between(mon, x1_high, x1_low, alpha = 0.2, color = 'blue')
plt.fill_between(mon, x2_high, x2_low, alpha = 0.2, color = 'red')
plt.fill_between(mon, x3_high, x3_low, alpha = 0.2, color = 'green')

plt.title('Some Plot Showing Interannual Variability for Each Month')

plt.savefig('time_ser.png')

