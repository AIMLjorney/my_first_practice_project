import random
import numpy as np
matrix = np.random.randint(low=10,high=50,size=(3,3))
print(matrix)
last_row = matrix[1,]
print(last_row)
last_columns = matrix[:,2]
print(last_columns)
# matrix = matrix.flatten()
matrix.resize(-1)
print()
print(matrix)
