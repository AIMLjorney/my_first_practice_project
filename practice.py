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


##################### Number Guessing game ################
# class maxnumber(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)
        

# class minnumber(Exception):
#     def __init__(self,message):
#         self.message = message
#         super().__init__(self.message)
        
# max = 100
# while True:
#     try:
#         num = int(input("Enter the guessing value of your : "))
#         if (num == max):
#             print("wow ! what`s great guess ")
#             print("you winner")
#             break

#         elif(num<max):
#             raise maxnumber("Your guess value is small long")

#         elif(num>max):
#             raise minnumber("Ypur guess values is too long")

#     except maxnumber as e:
#         print(e)
#         print("Try again !")
#         print()

#     except minnumber as e:
#         print(e)
#         print("Try again !")
#         print()

#     else:
#         print("Code is well executed")                   


##############  quiz application ##########################
# def app():
#     questions = [
#         {
#             "question":"What is the capital of France?",
#             "options":["A. Paris", "B. Madrid", "C. Rome", "D. Berlin"],
#             "answer": "A"
#         },
#         {
#             "question": "Which programming language is known as the 'language of AI'?",
#             "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
#             "answer": "B"
#         },
#         {
#             "question": "What is 5 + 3?",
#             "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
#             "answer": "D"
#         },
#         {
#             "question": "Which planet is known as the Red Planet?",
#             "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
#             "answer": "C"
#         }
#     ]
#     scores = 0
#     print("Welcome to the Quiz App!") 
#     for i,q in enumerate(questions,start=1):
#         print(f"question {i} : {q['question']}")
#         for j in q["options"]:
#             print(j)
#         ans = input("Enter your answer(A,B,C,D):- ")
#         if (ans==q["answer"]):
#             print("Correct !") 
#             scores+=1
#         else:
#             print("Wrong ! the correct answer was {}".format(q["answer"]))       
#         print() 
#         print()   
#     return (scores,i)
# num="yes"
# while num=="yes":
#     qiz,total_ques = app()
#     print(qiz,total_ques)
#     percentaze = qiz/total_ques
#     print(f"Your percentage : {percentaze*100}%") 
#     num = input("Do you want to play again?(yes/no):- ")
#     if (num=='yes'):
#         num = "yes"
#     else:
#         print("Thanks for playing! Goodbye!") 
#         num = "no"
#         print()
#         break   


import turtle as t
import time as ti
# t.forward(50)
# ti.sleep(2)
# t.backward(20)



# t.bgcolor("black")
# t.color("red","blue")
# t.pensize(1)
# for angle in range(0,400,30):
#     t.seth(angle)
#     t.circle(100)
# ti.sleep(3)   
# 

# t.color("green")
# t.forward(70)
# t.left(120)
# t.forward(70)
# t.left(120)
# t.forward(80)
# ti.sleep(5) 
  
# t.forward(100)
# t.left(70)
# t.forward(70)
# t.left(70) 

# def bubble_sort(arr):
#     leng = len(arr)
#     for i in range(leng):
#         for j in range(0,leng-i-1):
#             if (arr[j]>arr[j+1]):
#                  sw = arr[j]
#                  arr[j] = arr[j+1]
#                  arr[j+1] = sw
#     return arr
# print(bubble_sort([12,34,5,6,7]))

# def indertion_sort(arr):
#     leng =        

import tkinter as tk

# Step 1: Create the main window (root window)
root = tk.Tk()
root.title("Tkinter Basic Example")

root.mainloop()



