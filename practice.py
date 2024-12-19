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

class charter(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

def calculater(num1,num2,operater):
    if(operation=="+"):
        return num1+num2
    elif(operation=="-"):
        return num1-num2
    elif(operation=="*"):
        return num1*num2
    elif(operation=="/"):
        return num1/num2
    else:
        return num1%num2
    

try:
    num1 = int(input("Enter the any number :- "))
    num2 = int(input("Enter the any other value :- "))
    operation = input("Enter a any operation like addition , subtraction , division , multiplication , modulas :- ")
    if (len(operation)==0 or len(operation)>1):
        raise charter("please Enter the vaild operater like(+,-,*,/,%)")
except charter as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    num = calculater(num1,num2,operation) 
    print("number1 is {} and number2 is {} then operation is {} = {}".format(num1,num2,str(operation),num))   


    


