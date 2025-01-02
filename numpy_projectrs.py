# ###############    matrix operations   ########################
# import numpy as np

# class matrix:
#     def __init__(self, m1=None, m2=None):
#         self.matrix_1 = m1
#         self.marix_2 = m2

#     def add(self):
#         return self.matrix_1 + self.marix_2
    
#     def sub(self):
#         return self.matrix_1 - self.marix_2
    
#     def multi(self):
#         return np.dot(self.matrix_1, self.marix_2)

#     def divi(self):
#         return self.matrix_1 / self.marix_2
    
#     def inverse(self, matrix):
#         return np.linalg.inv(matrix)
    
#     def eig(self, matrix):
#         return np.linalg.eig(matrix)


# while True:
#     print("#######  Enter your choice in this ########")
#     print("Add two matrices - Press 1")
#     print("Subtract two matrices - Press 2")
#     print("Multiply two matrices - Press 3")
#     print("Divide two matrices - Press 4")
#     print("Inverse of a matrix - Press 5")
#     print("Eigenvalues and eigenvectors - Press 6")
#     print("Exit - Press 0")
    
#     choice = int(input("Enter your choice: "))
    
#     if choice == 0:
#         print("Exiting the program. Goodbye!")
#         break

#     rows = int(input("Enter the number of rows for the matrices: "))
#     cols = int(input("Enter the number of columns for the matrices: "))

#     if choice==1:
#         print("Matrix 1 input:")
#         marix1 = []
#         for i in range(rows):
#             row = []
#             for j in range(cols):
#                 val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                 row.append(val)
#             marix1.append(row)

#         print("Matrix 2 input:")
#         marix2 = []
#         for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                    val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                    row.append(val)
#                 marix2.append(row)
        
#         a = matrix(np.array(marix1), np.array(marix2))
#         print("Addition of the two matrices is:\n", a.add())
        
    
#     elif choice == 2:
#             print("Matrix 1 input:")
#             marix1 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                   val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                   row.append(val)
#                 marix1.append(row)

#             print("Matrix 2 input:")
#             marix2 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                   val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                   row.append(val)
#                 marix2.append(row)
        
#             a = matrix(np.array(marix1), np.array(marix2))
#             print("Subtraction of the two matrices is:\n", a.sub())


#     elif choice == 3:
#             print("Matrix 1 input:")
#             marix1 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                    val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                    row.append(val)
#                 marix1.append(row)

#             print("Matrix 2 input:")
#             marix2 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                   val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                   row.append(val)
#                 marix2.append(row)
        
#             a = matrix(np.array(marix1), np.array(marix2))
#             print("Multiplication of the two matrices is:\n", a.multi())

#     elif choice == 4:
#             print("Matrix 1 input:")
#             marix1 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                    val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                    row.append(val)
#                 marix1.append(row)

#             print("Matrix 2 input:")
#             marix2 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                    val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                    row.append(val)
#                 marix2.append(row)
        
#             a = matrix(np.array(marix1), np.array(marix2))
#             print("Division of the two matrices is:\n", a.divi())

#     elif choice == 5:
#             print("Matrix 1 input:")
#             marix1 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                     val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                     row.append(val)
#                 marix1.append(row)
#             a = matrix()
#             print("Inverse of the matrices is:\n", a.inverse(np.array(marix1))) 

#     elif choice == 6:
#             print("Matrix 1 input:")
#             marix1 = []
#             for i in range(rows):
#                 row = []
#                 for j in range(cols):
#                     val = int(input(f"Enter element for row {i + 1}, column {j + 1}: "))
#                     row.append(val)
#                 marix1.append(row)
#             a = matrix()
#             b= a.eig(np.array(marix1))
#             print("Eigen_value of the matrices is:\n",b[0])    
#             print("Eigen_vector of the matrices is:\n",b[1])             
#             print("Eigen_value of the matrices is:\n",a.eig(np.array(marix1))) 

# import numpy as np
# from sklearn.datasets import load_iris

# # Load the Iris dataset
# iris = load_iris()
# data = iris.data  # Only the features (sepal length, sepal width, petal length, petal width)

# def min_max_scaling(data):
#     Xmin = np.min(data)
#     Xmax = np.max(data)
#     Xscaled = (data-Xmin)/(Xmax-Xmin)
#     return Xscaled

# def Z_score(data):
#     mean = np.mean(data)
#     std = np.std(data)
#     Xnormalization = (data-mean)/std
#     return Xnormalization
# arr1 = min_max_scaling(data)
# arr2 = Z_score(data)
# print(arr1[:5])
# print()
# print(arr2[:5])

# import numpy as np
# def cosine(A,B):
#     dot_product = np.dot(A,B)
#     norm_A = np.linalg.norm(A)
#     norm_B = np.linalg.norm(B)
#     cosine = dot_product/(norm_A*norm_B)
#     return cosine

# A = np.random.randint(0,400,size=(3,4))
# B = np.random.randint(0,300,size=(4,3))
# cost= cosine(A,B)
# print(cost)
# print()

# import numpy as np
# import matplotlib.pyplot as plt

# # Set random seed for reproducibility
# np.random.seed(42)

# # Generate random features (100 data points, 2 features per data point)
# X_class = np.random.randn(100, 2)

# # Create labels: Class 0 for points below a certain threshold, Class 1 above
# y_class = (X_class[:, 0] + X_class[:, 1] > 0).astype(int)  # Linear boundary

# # Add random noise to labels (flip some labels)
# noise_indices = np.random.choice(100, 20, replace=False)  # Randomly flip 20 labels
# y_class[noise_indices] = 1 - y_class[noise_indices]  # Flip the labels

# # Plot the classification data
# plt.scatter(X_class[:, 0], X_class[:, 1], c=y_class, cmap='coolwarm')
# plt.title("Synthetic Classification Data (with noise)")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.show()

# # Preview the first few data points and their labels
# print("First 5 data points (X, y):")
# print(np.hstack((X_class[:5], y_class[:5].reshape(-1, 1))))
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the image using Pillow
# image = Image.open("your_image.jpg")  # Replace with your image path

# # Convert the image to a NumPy array
# image_array = np.array(image)

# # Display the original image
# plt.imshow(image)
# plt.title("Original Image")
# plt.axis('off')
# plt.show()

# # 1. **Rotation**
# # Rotate the image by 45 degrees
# rotated_image = image.rotate(45)
# rotated_image_array = np.array(rotated_image)

# # Display the rotated image
# plt.imshow(rotated_image)
# plt.title("Rotated Image (45 degrees)")
# plt.axis('off')
# plt.show()

# # 2. **Cropping**
# # Crop the image (top-left corner starting from (100, 100) to (300, 300))
# cropped_image = image.crop((100, 100, 300, 300))
# cropped_image_array = np.array(cropped_image)

# # Display the cropped image
# plt.imshow(cropped_image)
# plt.title("Cropped Image")
# plt.axis('off')
# plt.show()

# # 3. **Resizing**
# # Resize the image to 200x200
# resized_image = image.resize((200, 200))
# resized_image_array = np.array(resized_image)

# # Display the resized image
# plt.imshow(resized_image)
# plt.title("Resized Image (200x200)")
# plt.axis('off')
# plt.show()

# # 4. **Color Inversion**
# # Invert the colors by subtracting the pixel values from 255
# inverted_image_array = 255 - image_array

# # Convert the inverted array back to an image
# inverted_image = Image.fromarray(inverted_image_array)

# # Display the color-inverted image
# plt.imshow(inverted_image)
# plt.title("Inverted Image")
# plt.axis('off')
# plt.show()
 # import pandas as pd
# import numpy as np
# def normalize(arr):
#     min = np.min(arr)
#     max = np.max(arr)
#     if ((max-min) != 0):
#         return ((arr-min)/(max-min))
#     else:
#         return "not possible because max - min equal to zero"  

# def dot(arr):
#     if normalize(arr) is not None:
#         return (np.dot(arr.flatten(),arr.flatten()))
#     else:
#         return "nothing product" 

# array_1d = np.random.randint(low=1,high=50,size=(1,20))
# array_2d = np.random.randint(low = 10,high=100,size=(3,3))
# array_22d = np.linspace(10,100,20)
# array_22d.resize((4,5))
# print(dot(array_22d))

# print("Rows of the Mean :- ")
# print(np.mean(array_22d[0][0:]))
# print(np.mean(array_22d[1]))
# print(np.mean(array_22d[2]))
# print(np.mean(array_22d[3]))

# print("columns of the Mean")
# print(np.mean(array_22d[:,:1]))
# print(np.mean(array_22d[:,1:2]))
# print(np.mean(array_22d[:,2:3]))
# print(np.mean(array_22d[:,3:4]))


# # print()
# # m = pd.DataFrame(array_22d)
# # print(m)
# # print()


# array_22d[np.where((array_22d[:,:1])<(np.mean(array_22d[:,:1])))] = 0
# array_22d[np.where((array_22d[:,1:2])<(np.mean(array_22d[:,1:2])))] = 0
# array_22d[np.where((array_22d[:,2:3])<(np.mean(array_22d[:,2:3])))] = 0
# array_22d[np.where((array_22d[:,3:4])<(np.mean(array_22d[:,3:4])))] = 0
# print(array_22d)

#############   pandas ###################
import pandas as pd
import numpy as np
# df = pd.Series([50,60,70,80,90])
# print(df)
# df = pd.Series({'Model A':90,'Model B':85,'Model C':78})
# print(df)
# print(df.shape)
# df  = pd.Series(np.random.randint(low=200,high=300,size=100),index=(np.linspace(100,200,100)))
# print(df)
# features = {
#     "Features1":[1,2,3],
#     "Featus2":[0.1,0.5,0.9],
# }
# df = pd.DataFrame(features)
# print(df)

# arr = np.random.randint(low=100,high=300,size=(5,3))
# df = pd.DataFrame(arr,columns=["A","B","C"])
# print(df)

# file = pd.read_csv("D:/lab_activity_5.csv")
# df = pd.DataFrame(file,index=[1,2,3,4,5,6])
# df.dropna(inplace=True)
# df.rename(columns={
#     'output':"Output",
#     "lower limit":"Lower_limit",
#     "upper limit":"Upper_limit",
#     "bonus":"Bonus",
#     "cumlatyive":"Cumulative_frequency",
#     "number of employees":"no.of.employee",
#     "bon*number":"Total_bonus",
#     "mid value":"Mid_values",
#     "xi*fi":"Total"
# },inplace=True)
# print(df)
# print(df.head(10))
# print(df.tail())
# print(df.info())
# print(df.describe())
# print()
# print()
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# if df.isnull == True:
#     print(df.fillna(np.mean(df['Lower_limit'])))
# else:
#     pass
# print(df) 
# print(df.iloc[0:2,:])
# print(df.loc[:,["Total","Total_bonus"]])
# print(df.loc[2:4,["Total"]])

# def compute(lis):
#     import pandas as pd
#     import numpy as np
#     coun = 0
#     cun = list()
#     for i in lis:
#         coun= cun.count(i)
#         cun.append(coun)
#     print(cun)    

# lis = [12,3,4,5,5,6,6,7,7,8,8,98,9,0]
# compute(lis)
import pandas as pd
import numpy as np
file = pd.read_csv("C:/Users/hp5cd/Downloads/used_car_dataset.csv")
print(file[0:20].s)


