from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt

diabetes = load_diabetes()

X = diabetes.data
Y = diabetes.target

age = 0
sex = 1
blood_pressure = 3

print(diabetes.DESCR)