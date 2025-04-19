import numpy
values = [70, 100, 20, 90, 80, 40, 10,30,50,60 ]
x = numpy.percentile(values, 50)
print(x)

import numpy
values = [10, 20, 30, 40, 50]
x = numpy.std(values)
print(x)

import numpy as np
z = [4, 7, 13, 16, 20]
var = np.var(z)
print(var)

import numpy as np
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
correlation = np.corrcoef(x, z)
print(correlation)

import pandas as pd
df = pd.DataFrame({
    'Math':[90, 95, 75,88],
    'Science':[65, 60, 50, 85],
})
print(df.corr())

x =[10, 20, 30, 40]
z = [2, 3, 4, 5]
print(np.corrcoef(x,z))