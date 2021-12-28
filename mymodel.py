import numpy as np
def linear_model(x,y):
    # print("X is", x)
    print("Y is", y[1:5])
    pass


import pandas as pd
data = pd.read_csv('LinearRegressionData.csv')

#define response variable
y = data[['GPA']]
y = np.array(y)

#define explanatory variable
x = data[['SAT']]
x = np.array(x)

# multiplication = np.multiply(x.T, x)
res = np.outer(x.T, x) #np.dot(x.T,x)

inverse = np.linalg.pinv(res)
# print(inverse)
res2 = np.outer(x.T, y)

final_result = np.outer(res,res2)

# print(x)
# print(len(x))
# print(x.T)
# print(len(x.T))
# # print(y.T)
# print(res)
# print(len(res))
# print(len(res[0]))
# # for row in res:
# #     print(row)
# print(inverse)
# print(res2)

print(final_result)
print(len(final_result))

# x = np.array([1,2,3,4])
# print(x)
# # linear_model(x,x)
# # y = np.transpose(x)
# print(x.T)

# a = np.array([5,4])[np.newaxis]
# print(a)
# print(a.T)