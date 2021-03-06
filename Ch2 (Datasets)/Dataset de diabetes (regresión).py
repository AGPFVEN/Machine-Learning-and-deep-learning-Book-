from cProfile import label
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

"""
Loading data
"""
diabetes = load_diabetes()

X = diabetes.data
Y = diabetes.target

age = 0
sex = 1
mass_index = 2
blood_pressure = 3

#print(diabetes.DESCR) #Text information about this dataset

print(X.shape)         #Contains 442 samples (rows) of 10 features (columns)
print(Y.shape)         #Adequate for Regreession. The target are numbers

print(X[0:5, :])       #Print rows of data, starting from 0 to 4
print(Y[0:5])          #Print rows of target data, starting from 0 to 4

print(X[1, mass_index])#Print mass index (third column)
print(X[1:3, age])     #Print age of second and third samples (first column)

#print(diabetes.data.shape[0])

x = range(0, diabetes.data.shape[0], 1)

"""
Plot some features
"""
plt.figure(figsize=(30,8))
plt.plot(x, X[:, mass_index], "y-", label="Mass Index")

plt.show()