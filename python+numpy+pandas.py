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
import pandas as pd
import numpy as np
files = pd.read_csv("C:/Users/hp5cd/Downloads/train.csv")
file = files.loc[0:10, ['Age', 'Pclass', 'Survived']]
if file['Age'].isnull().any():
    file['Age'] = file['Age'].fillna(file['Age'].median())
corrraltion1 = file['Age'].cov(file['Pclass'])
corrraltion2 = file['Pclass'].cov(file['Survived'])
corrraltion3 = file['Survived'].cov(file['Age'])
print("corelation of the age and pclass",corrraltion1)
print("correlation of the pclass and survived",corrraltion2)
print("correlation of the  survived and age",corrraltion3)
print(file.columns)
files = files.loc[0:20,['Sex','Embarked']]
def applyy(num):
    if num == 'male':
        return 0
    else:
        return 1

def changed(val):
    if val == 'S':
        return 1
    elif(val=='Q'):
        return 2
    elif(val=='C'):
        return 3
    
files['Sex'] = files['Sex'].apply(applyy)
files['Embarked'] = files['Embarked'].apply(changed)
print(files['Embarked'],files['Sex'])
print(files)    