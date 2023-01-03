# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:49:15 2022

@author: Aroma
"""

#Importing all the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#To read a comma separated values i.e csv file into a dataframe.
data_array = pd.read_csv("inputdata3.csv", header=0, sep=",")

#To assign the columns to variables x and y
x = data_array["Rainfall"]
y = data_array["Productivity"]

#To calculate a linear regression line for x and y.
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"Slope of the regression line = {slope} \nIntercept of the regression line = {intercept}")
print("Pearson correlation coefficient = ", r)
print("p-value = ", p)
print("Standard error=",std_err)

def slope_intercept(X):
    '''
    The above function is to define a function named slope_intercept which takes an 
    argument and returns the equation of the straight line.
    X: It is an independent variable in the equation of the straight line
    ''' 
    return slope *X + intercept

#The map() function applies the slope_intercept function to each item of the above variable x.
model = list(map(slope_intercept, x))
print(model)

#To compute the coefficient of variation
CV = stats.variation(model)
print("Co-efficient value of the model is", CV)

#To compute the R square value of the linear regression model.
r_square= r**2
print("R Square value is", r_square)

#To calculate the relationship between the 2 columns in the dataset.
correlation= data_array.corr().loc["Rainfall","Productivity"]
print("Correlation of x and y is", correlation)

#The value of rainfall with which the productivity coefficient needs to be predicted.
x_pred = 350

#Using the slope and intercept to compute the prediction.
y_pred = slope_intercept(x_pred)
print(f"Predicted value of 350 is {y_pred}")

#To plot the the linear regression graph.
'''
plt.figure is to create a new figure with figsize and dpi,
where figsize is the width and height of the figure in inches and dpi is dots per inch 
i.e to set the resolution of the image
'''
plt.figure(figsize=(10,10), dpi= 144)
#To plot the scatter graph.
plt.scatter(x, y, c='blue', label='Rainfall Vs productivity')
#To plot the linear regession line.
plt.plot(x, model, color='black', label='Regression Line')
#To plot the prediction point on the regression line.
plt.scatter (x_pred, y_pred, c='red', label='Predicted point')
#To add the predicted point value to the axes in the respective data-coordinates.
plt.text(x_pred, y_pred, "[0.14424]", va = 'top', fontsize = 15)
plt.xlabel("Amount of precipitations (mm per year)")  #To label the x-axis 
plt.ylabel("Productivity coefficient")  #To label the y-axis
plt.title("Graph representing the rainfall per year and field productivity")  #To mention the title for the graph.
plt.legend()  #To place a legend on the graph.
plt.savefig('Scatter plot.png') #Saving the image of the graph.
plt.show()  #To display all the figures on the graph.

