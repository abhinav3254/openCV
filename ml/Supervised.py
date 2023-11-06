# imports
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# datasets
house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

# Reshapes the size data into a 2D array using NumPy.
# Reshaping is necessary to match the format required by the LinearRegression model.
size2 = np.array(size).reshape((-1, 1))


# Fitting into the model
regr = linear_model.LinearRegression()
regr.fit(size2, house_price)
print('Coefficients: \n', regr.coef_)
print('Intercept: \n', regr.intercept_)


# Function to plot the prediction line
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)

# Plotting the prediction line using the trained model
graph('regr.coef_ * x + regr.intercept_', range(1000, 2700))
print(regr.score(size2, house_price))


# this is for graph
plt.scatter(size, house_price, color='black')
plt.ylabel('House Price')
plt.xlabel('Size of House')
plt.show()

