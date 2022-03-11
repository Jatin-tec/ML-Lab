import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head())

X = dataset['Head Size(cm^3)'].values
Y = dataset['Brain Weight(grams)'].values

x_mean = np.mean(X)
y_mean = np.mean(Y)

n = len(X)

numerator = 0
denominator = 0

plot_X = []
plot_Y = []
for i in range(n):
    numerator += (X[i]*Y[i] - X[i]*y_mean)
    denominator += ((X[i]**2) - X[i]*x_mean) 
    b1 = numerator / denominator
    b0 = y_mean - (b1 * x_mean)

    plot_X.append(X[i])
    plot_Y.append(Y[i])

    #plotting values 
    x_max = np.max(X) + 100
    x_min = np.min(X) - 100

    #calculating line values of x and y
    x = np.linspace(x_min, x_max, 1000)
    y = b0 + b1 * x
    
    #plotting line 
    plt.plot(x, y, color='#00ff00', label=f'Linear Regression  slope={b1}')
    
    #plot the data point
    plt.scatter(plot_X, plot_Y, color='#ff0000', label=f'Data Point y-intercept={b0}')
    
    # x-axis label
    plt.xlabel('Head Size (cm^3)')
    
    #y-axis label
    plt.ylabel('Brain Weight (grams)')
    
    plt.legend()
    plt.show()