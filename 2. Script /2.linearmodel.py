
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

#Reading csv file. 
dataset = pd.read_csv('benchmark.csv')
colm = list(dataset.columns)
colm = colm[2:]
rem = ['instructions','cycles']
for r in rem:
  colm.remove(r) 

#separating dependent variable (y) and independent variable(X)

cpi = dataset['cpi']
cpi

df = dataset[colm[:-1]]
df.head()
df_new = df
df_new.columns = colm[:-1]
df_new.head()

X = df_new
y = cpi

#dividing data into train and test data

from sklearn.model_selection import train_test_split
import statsmodels.api as sm
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
X2_test=sm.add_constant(X_test)
X.head()

#linear model using OLS and getting summary of model(Quality Parameters)
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
X2=sm.add_constant(X_train)
r1=sm.OLS(y_train,X2)
r2=r1.fit()
print(r2.summary())

#prediction 
y_pred = r2.predict(X2_test) #test

#calculation of rmse
from sklearn.metrics import mean_squared_error
from math import sqrt
rmse = sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:- ",rmse)


#cpi calculation for different event  
coef_value=r2.params

index = coef_value.index
a = list(index)
a.remove('const')

#Calculating the mean CPI

mean_cpi = dataset['cpi'].values.mean()
print(mean_cpi)                                               #Actual mean CPI

print("base cpi:",coef_value[0])      

#Contribution of diiferent miss events in CPI
meanW1=df_new[a[0]].values.mean()
cpi1=coef_value[1]*(meanW1)
print(a[0],cpi1)

meanW2=df_new[a[1]].values.mean()
cpi2=coef_value[2]*(meanW2)
print(a[1],cpi2)

meanW3=df_new[a[2]].values.mean()
cpi3=coef_value[3]*(meanW3)
print(a[2],cpi3)

meanW4=df_new[a[3]].values.mean()
cpi4=coef_value[4]*(meanW4)
print(a[3],cpi4)

meanW5=df_new[a[4]].values.mean()
cpi5=coef_value[5]*(meanW5)
print(a[4],cpi5)

meanW6=df_new[a[5]].values.mean()
cpi6=coef_value[6]*(meanW6)
print(a[5],cpi6)

meanW7=df_new[a[6]].values.mean()
cpi7=coef_value[7]*(meanW7)
print(a[6],cpi7)

meanW8=df_new[a[7]].values.mean()
cpi8=coef_value[8]*(meanW8)
print(a[7],cpi8)

print(cpi1+cpi2+cpi3+cpi4+cpi5+cpi6+cpi7+cpi8+base)          #Predicted CPI

#ploting prediction and actual value
import matplotlib.pyplot as plt 
plt.scatter(y_test, y_pred) 
plt.show()

#plotting Residuals
residuals = y_test-y_pred
plt.plot(X_test,residuals,'o',color='darkblue')
plt.title("Residual Plot")
plt.xlabel("Independent Variable")
plt.ylabel("Residual")
