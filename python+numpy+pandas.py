# # Question 1 Basic Data Handling 
# import numpy as np
# import pandas as pd
# file = pd.read_csv("C:/Users/hp5cd/Downloads/used_car_dataset.csv")
# file=file.loc[0:10,['Brand', 'model','AskPrice']]
# file = pd.DataFrame(file)
# filter_BMW1 = file.where((file['Brand']=="BMW")|(file['Brand']=="Toyota")|(file['AskPrice']>='₹ 6,85,000'))
# filter_BMW1.dropna(axis=0,how='all',inplace=True)
# print(filter_BMW1)
# print()
# import pandas as pd
# import numpy as np
# files = pd.read_csv("C:/Users/hp5cd/Downloads/train.csv")
# file = files.loc[0:10, ['Age', 'Pclass', 'Survived']]
# if file['Age'].isnull().any():
#     file['Age'] = file['Age'].fillna(file['Age'].median())
# corrraltion1 = file['Age'].cov(file['Pclass'])
# corrraltion2 = file['Pclass'].cov(file['Survived'])
# corrraltion3 = file['Survived'].cov(file['Age'])
# print("corelation of the age and pclass",corrraltion1)
# print("correlation of the pclass and survived",corrraltion2)
# print("correlation of the  survived and age",corrraltion3)
# print(file.columns)
# files = files.loc[0:20,['Sex','Embarked']]
# def applyy(num):
#     if num == 'male':
#         return 0
#     else:
#         return 1

# def changed(val):
#     if val == 'S':
#         return 1
#     elif(val=='Q'):
#         return 2
#     elif(val=='C'):
#         return 3
    
# files['Sex'] = files['Sex'].apply(applyy)
# files['Embarked'] = files['Embarked'].apply(changed)
# print(files['Embarked'],files['Sex'])
# print(files)    
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as py
# file = pd.read_csv("C:/Users/hp5cd/Downloads/used_car_dataset.csv")
# # print(file)
# # print(file.describe())
# # print(file.tail())
# def ma(lis):
#     mean = lis.mean()
#     medium = lis.median()
#     mode = lis.mode().values[0]
#     return(mean,medium,mode)

# def fueltonum(val):
#     if(val=='Petrol'):
#         return 1
#     elif(val=='Diesel'):
#         return 2
#     else:
#         return 3
    
# (mean,median,mode) = ma(file['Year'])
# print(mean)
# print(median)
# print(mode)


# quar1 = file['Year'].quantile(q=0.25)
# quar3 = file['Year'].quantile(q=0.75)
# quar2 = quar3-quar1
# lower_boundry = quar1-(1.5*quar2)
# upper_boundery = quar3+(1.5*quar2)
# print(quar3)
# print(lower_boundry)
# print(upper_boundery)
# print(file[(file['Year']<lower_boundry) | (file['Year']>upper_boundery)])
# # print(file.loc[0:10,['FuelType']])
# file['FuelType'] = file['FuelType'].apply(fueltonum)
# print(file)
# py.hist(file['Year'])
# py.show()

# import numpy as np
# import pandas as pd
# arr1 = [5,7,12,16,20]
# arr2 = [40,102,180,210,240]
# df1 = pd.Series(arr1)
# df2 = pd.Series(arr2)
# mean1 = df1.sum()/df1.count()
# mean2 = df2.sum()/df2.count()
# c = sum()

# print(mean1)

# print(df1.cov(df2))
import pandas as pd

# Given series
arr1 = [5, 7, 12, 16, 20]
arr2 = [40, 102, 180, 210, 240]
df1 = pd.Series(arr1)
df2 = pd.Series(arr2)

# Calculate slope (m) and intercept (c)
n = len(df1)
sum_x = df1.sum()
sum_y = df2.sum()
sum_xy = (df1 * df2).sum()
sum_x2 = (df1 ** 2).sum()

# Slope (m)
slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

# Intercept (c)
intercept = (sum_y / n) - slope * (sum_x / n)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

