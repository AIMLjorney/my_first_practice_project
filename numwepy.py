import numpy as np
############   temperature conversion (celsius to frhrenhit)
# temperature_celsiu = np.array([23,20,21,21,21,22,20,20,21,22])
# fahrenhit_temperature = (temperature_celsiu*1.8)+32
# print("temperature_celsiu",temperature_celsiu)
# print("fahrenhit_temperature",fahrenhit_temperature)
# print("Average of celsiu",np.average(temperature_celsiu))
# print("min of fahrenhit",np.min(fahrenhit_temperature))
# print("max of celsiu ",np.max(fahrenhit_temperature))


#################  Monthly Sales Analysis  ################
# monthly_sales = np.array([1564,3668,1860,1054,3835,782,643,1628,4518,4205,1114,4994,749,2527,2510,4059,2642,2931,3802,3157,3311,1640,2980,2818,3027,1214,3380,1798,4901])

# print("Total sales :-",np.sum(monthly_sales))
# print("Average Sales :-",np.average(monthly_sales))
# print("Higest_sales",np.max(monthly_sales))
# print("higest_sales",monthly_sales[np.argmax(monthly_sales)])
# print((monthly_sales-np.min(monthly_sales)/(np.max(monthly_sales)-np.min(monthly_sales))))

# sutents_scores = np.array([[99,90,89,87,80,40],[30,20,33,80,40,10],[20,30,60,80,40,75],[23,56,45,89,78,45]])
# weight = np.array([4.0,4.0,4.0,4.0,4.0,2.0])

# if(np.shape(sutents_scores)[1] == np.shape(weight)[0]):
#     multiplication = np.dot(sutents_scores,weight)
#     print(multiplication)

# weif = np.random.randint(15,35,7)
# print(weif)
# print("Mean:-",np.mean(weif))
# print("Varience:-",np.var(weif))
# print("Standard :- ",np.std(weif))
# for i in weif:
#     if (i>np.mean(weif)):
#         print("above value of the mean:-",i)
#         break
#     else:
#         pass

# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# # Step 1: Load the image
# image = Image.open("c:/Users/hp5cd/OneDrive/Pictures/3d-eagle-rendering-while-flying_23-2150724319.jpg")  # Replace with your image path
# plt.figure(figsize=(8, 4))

# # Original resized image
# plt.subplot(1, 2, 1)
# plt.imshow(image)
# plt.title("Resized Image")
# plt.axis("off")


# plt.show()

# # Step 2: Convert the image to a NumPy array
# image_array = np.array(image)
# print("Image Shape:", image_array.shape)  # Shows (Height, Width, Channels)

# # Step 3: Resize the image
# resized_image = image.resize((10000, 10000))  # Resize to 100x100 pixels
# resized_image_array = np.array(resized_image)

# # Step 4: Slice a specific region
# sliced_region = resized_image_array[:5000, :5000]  # Extract top-left 50x50 region

# # Step 5: Convert the region to grayscale
# grayscale_region = np.mean(sliced_region, axis=2, keepdims=True)
# grayscale_region = np.repeat(grayscale_region, 3, axis=2).astype(np.uint8)
# resized_image_array[:5000, :5000] = grayscale_region  # Replace the region

# # Step 6: Display the images
# plt.figure(figsize=(8, 4))

# # Original resized image
# plt.subplot(1, 2, 1)
# plt.imshow(resized_image)
# plt.title("Resized Image")
# plt.axis("off")

# # Modified image
# plt.subplot(1, 2, 2)
# plt.imshow(resized_image_array)
# plt.title("Manipulated Image")
# plt.axis("off")

# plt.show()

# import numpy as np
# data = np.random.randint(1,100,size=(10,5))

# mean = np.mean(data,axis=0)
# std = np.std(data,axis=0)
# normalization = (data-mean)/std
# print(normalization.flatten())

# zero_array1 = np.zeros((3,4),dtype=bool)
# zreo_array2 = np.zeros((3,4),dtype=bool)
# ones_array = np.ones((3,4),dtype=bool)
# digonal_array = np.eye(3,4)
# print(zero_array1+zreo_array2+ones_array+digonal_array)
# print(digonal_array)
import random
import numpy as np
# matrix = np.random.randint(low=10,high=50,size=(3,3))
# print(matrix)
# last_row = matrix[1,]
# print(last_row)
# last_columns = matrix[:,2]
# print(last_columns)
# # matrix = matrix.flatten()
# matrix=matrix.reshape(-1)
# print()
# print(matrix)
# np.random.seed(12)
# sales = np.random.randint(low=10,high=90,size=(3,3))
# print(sales)
# total_sales = np.sum(sales)
# average_sales = np.average(sales)
# minimum_sales = np.min(sales)
# maximum_sales = np.max(sales)
# for i in sales:
#     for j in i:
#         if (j>average_sales):
#             print("values :-",j)
#             break
#         else:
#             pass

# print(minimum_sales)
# print(maximum_sales)
# print(total_sales)
# print(average_sales)

# new_array = sales*10/100
# print(new_array)
# total_sales = np.sum(new_array)
# average_sales = np.average(new_array)
# minimum_sales = np.min(new_array)
# maximum_sales = np.max(new_array)
# for i in new_array:
#     for j in i:
#         if (j>average_sales):
#             print("values :-",j)
#             break
#         else:
#             pass

# print(minimum_sales)
# print(maximum_sales)
# print(total_sales)
# print(average_sales)

# np.random.seed(42)
# price = np.random.uniform(low=200,high=1000,size=10)
# print(price)
# countites = np.random.randint(low=10,high=50,size=10)
# print(countites)


