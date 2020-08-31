import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle 


# sk learn for statistical models (datat science, mathematical)
# deep learning (neural networks) keras and tesorflow

# tensoflow is built on keras

# user keras for neural networks 

# deep learning compute a loss function how accurate 

# matplotlib use it w sklearn 

data = pd.read_csv("heart.csv", sep=",")

print(data.head())

age = data["age"]
sex = data["sex"]
cp = data["cp"]
trestbps = data["trestbps"]
chol = data["chol"]
fbs = data["fbs"]
restecg = data["restecg"]
thalach = data["thalach"]
exang = data["exang"]
oldpeak = data["oldpeak"]
slope = data["slope"]
ca = data["ca"]
thal = data["thal"]
target = data["target"]


print(age.head())
print(sex.head())
print(cp.head())
print(trestbps.head())
print(chol.head())
print(fbs.head())
print(restecg.head())
print(thalach.head())
print(exang.head())
print(oldpeak.head())
print(slope.head())
print(ca.head())
print(thal.head())
print(target.head())
