# def display(n):
#     while True:
#         try:
#             n= n+1
#             if n==21:
#                 raise StopIteration("its are infinite numbers")
#         except StopIteration as e:
#             print(e)
#             break
#         else:
#             print(n,end=" ")

# display(0)

# class rand(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)

# # import random as rands
# # try:
# #     num = rands.random()
# #     if num<0.1:
# #         raise rand("random number genrated less than 0.1")
# # except rand as e:
# #     print(e)
# # else:
# #     print("%.3f"%num)   

# class Errorr(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)
# class name(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)         

# try:
#     names = input("Enter the valid name :- ")
#     if (len(names)==0):
#         raise name("please Enter the valid name")
#     age = int(input("Enter the your vaild age :- "))
#     if(age<18):
#         raise Errorr("sorry! your are not alizeble for vote")

# except name as e:
#     print(e)
# except Errorr as e:
#     print(e)
# else:
#     print("Name = ",names)
#     print("Age = ",age)
#     print("you are eligible for voting")

#############  beginner level projects##############
##### calculater

# class charter(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)

# def calculater(num1,num2,operater):
#     if(operation=="+"):
#         return num1+num2
#     elif(operation=="-"):
#         return num1-num2
#     elif(operation=="*"):
#         return num1*num2
#     elif(operation=="/"):
#         if num2==0:
#             raise ZeroDivisionError("zero are not allows in denomanater")
#         else:
#             return num1/num2    
#     else:
#         return num1%num2
    

# try:
#     num1 = int(input("Enter the any number :- "))
#     num2 = int(input("Enter the any other value :- "))
#     operation = input("Enter a any operation like addition , subtraction , division , multiplication , modulas :- ")
#     if(len(operation)!=1 or operation not in "+-/*%" ):
#         raise charter("please Enter the vaild operater like(+,-,*,/,%)")

#     results = calculater(num1,num2,operation)  
#     print("number1 is {} and number2 is {} then operation is {} = {}".format(num1,num2,str(operation),results))  
# except charter as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("code sucessfully executed")   
# class To_Do_list:
#     def __init__(self):
#         self.taks = []

#     def addtasks(self,task):
#         self.taks.append(task)

#     def removetask(self,index):
#         try:
#             remo=self.taks.pop(index) 
#             print("Task are removed",remo)

#         except IndexError:
#             print("INvaild task number. Please try again") 

#     def viewtask(self):
#         if not self.taks:
#             print("No tasks in the list")
#             return
#         print("\nTo do list :")
#         for i                  

# while True:
#     print("Enter 1 means that Adding tasks")
#     print("Enter 2 means that Removing tasks") 
#     print("Enter 3 means that Marking complete tasks")
#     print("Enter 4 means that Viewing tasks")  
#     print('-'*5,"Exist to press 0",'-'*5)
#     choice = int(input("Enter your choice :- "))
#     if (choice == 1):



