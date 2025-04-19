#1 linear regression
import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5, 6, 7]
y = [3, 6, 8, 7, 3, 1, 1]
plt.scatter(x,y,)
plt.title("Nuriia's study hours")
plt.xlabel("Days")
plt.ylabel("hours")
plt.show()

#2 linear regrassion 2
x = np.array([1, 2, 3, 4, 5, 6,7])
y = np.array([7, 8, 9, 10, 3, 4, 4])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Nuriias sleeping hours")
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 0, 3, 4, 0, 2, 2])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Nuriia's reading hours")
plt.show()

#3 regrassion table
import pandas as pd
import statsmodels.formula.api as smf
df = pd.DataFrame({
    'x': [1, 2, 3, 4,5],
    'y': [1, 2, 3, 4, 5]
})
model = smf.ols('y~x', data=df).fit()
print(model.summary())
 #regrassion table ~ the .summary() gives us everything: coefficient, R, t-status, p-values, confidence intervals
 #regression Coefficients ~ tells us how much y changes with each x
 #regrassion P-Value ~ helps test if x significantly affects y. if p < 0.05, the effect is significant
 #R-squared ~ measures how well the model explains the variation in y. Closer to 1= better