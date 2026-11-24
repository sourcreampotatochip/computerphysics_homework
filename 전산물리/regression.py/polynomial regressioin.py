import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()

import numpy
from sklearn.metrics import r2_score

# fit a polynomial regression model (degree 3)
mymodel = numpy.poly1d(numpy.polyfit(x,y,3))

# generate line points for the polynomial cureve
myline = numpy.linspace(1,22,100)

# calculate R-squard score
r2 = r2_score(y, mymodel(x))

# plot scatter points and regression line
plt.scatter(x, y, color="blue", label="Data Points")
plt.plot(myline, mymodel(myline), color="red", label=f"Regression Line (R^2 = {r2:.2f})")

# add labels, title, and legend
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Polynomial Regression with R^2 score")
plt.legend()
plt.show()