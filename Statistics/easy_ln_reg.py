import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('https://raw.githubusercontent.com/codebasics/py/master/ML/2_linear_reg_multivariate/homeprices.csv')
reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

reg.coef_ # for every one change in area, bedrooms and age, changes by this much 

reg.predict([[3000,3,40]]) # pass in things to predict on 
