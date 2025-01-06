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
file = pd.read_csv("C:/Users/hp5cd/Downloads/train.csv")
file.dropna(axis=0,how='any')
print(file.columns)
print(file.loc[0:10,['Name', 'Sex', 'Age']])
print(file.iloc[0:10,[0,1,2,3,4]])
