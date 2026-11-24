import matplotlib.pyplot as plt

x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
from scipy import stats

# smaple data
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

# Perform linear regression
slope, intercept, r, p, std_err = stats.linregress(x,y)

def myfunc(x):
    return slope*x+intercept

# Generate the regression funcion
mymodel = list(map(myfunc, x))

# mymodel = []
# for balue in x:
#     y_fit = myfunc(value)
#     mymodel.append(y_fit)

plt.scatter(x,y)
plt.plot(x, mymodel)
plt.show()

# Scatter plot of data potins
plt.scatter(x, y, color="blue", label="Data Points")

# Plot the regression line
plt.plot(x, mymodel, color="red", label=f"Regression Line (r={r:.2f}, ste_err={std_err:.2f})")

# Add legend
plt.legend()

# Display plot
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Plot")
plt.show()

prediction = myfunc(10)

print(prediction)