import numpy as np
import pandas as pd
def linear_model(df1_x,df1_y):

    x=df1_x.iloc[:,0]
    x=pd.to_numeric(x)

    y=df1_y.iloc[:,0]
    y = pd.to_numeric(y)

    df1_x_mean=np.mean(df1_x)
    df1_y_mean=np.mean(df1_y)

    deviation_x=[]
    for i in x:
        deviation_x.append(i-df1_x_mean)

    deviation_y=[]
    for i in y:
        deviation_y.append(i-df1_y_mean)

    product_deviation=np.array(deviation_x)*np.array(deviation_y) 

    Sum_product_deviation=np.sum(product_deviation) 

    Sq_x_deviation=np.array(deviation_x)**2 

    Sum_Sq_x_deviation=np.sum(Sq_x_deviation) 

    Regression_coefficient=Sum_product_deviation/Sum_Sq_x_deviation
    print(Regression_coefficient)
    intercept=float(df1_y_mean)-(Regression_coefficient*float(df1_x_mean)) 
    print(intercept)

    return [Regression_coefficient, intercept]
