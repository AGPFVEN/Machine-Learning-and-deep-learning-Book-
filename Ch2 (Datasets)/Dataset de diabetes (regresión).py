from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

diabetes = load_diabetes()

X = diabetes.data
Y = diabetes.target

age = 0
sex = 1
blood_pressure = 3

#print(diabetes.DESCR) #Text information about this dataset

print(X.shape) #Contains 442 samples (rows) of 10 features (columns)
print(Y.shape) #Adequate for Regreession. The target are numbers

print(X[0:5, :]) #Print rows of data, starting from 0 to 4