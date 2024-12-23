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

# import tkinter as tk

# Step 1: Create the main window (root window)
# root = tk.Tk()
# root.title("Tkinter Basic Example")

# root.mainloop()
 

 ##################  Rocks , Paper , Sessions  #########################
# import random as r

# choi = ("Rock", "Paper", "Scissors")

# class Rps:
#     def __init__(self):
#         self.user_score = 0
#         self.computer_score = 0

#     def check(self, user):
#         computer = r.choice(choi)
#         print(f"Computer chose: {computer}")
#         if (
#             (user == "Rock" and computer == "Scissors") or
#             (user == "Paper" and computer == "Rock") or
#             (user == "Scissors" and computer == "Paper")
#         ):
#             self.user_score += 1
#             print("Congratulations! You win!")
#         elif user == computer:
#             print("It's a tie! Try again!")
#         else:
#             self.computer_score += 1
#             print("You lose! Better luck next time!")

#     def display(self):
#         print(f"Your Score: {self.user_score}")
#         print(f"Computer's Score: {self.computer_score}")


# # Main Game Loop
# c1 = Rps()
# while True:
#     choice = input("""Enter your choice ("Rock", "Paper", "Scissors") or 'quit' to exit: """).capitalize()

#     if choice == 'Quit':
#         print("You quit the game! Thank you for playing.")
#         c1.display()
#         break
#     elif choice not in choi:
#         print("Invalid choice! Please select from 'Rock', 'Paper', or 'Scissors'.")
#         continue
#     else:
#         c1.check(choice)
#         c1.display()

##########  password genrater ########################
# import random as r
# import string as s
# def password(length,upper_char,lower_char,digit,specific_char):
#     upper_charter = s.ascii_uppercase
#     lower_charter = s.ascii_lowercase
#     digits = s.digits
#     special = "~`!@#$%^&*:;?"

#     poolcharter = ""
#     if upper_char:
#         poolcharter+=upper_charter
#     if lower_char:
#         poolcharter+=lower_charter
#     if digit:
#         poolcharter+=digits
#     if specific_char:
#         poolcharter+=special

#     if not poolcharter:
#         raise ValueError("Please fill form correctly!")    

#     passwordsss = []
#     if upper_char:
#         passwordsss.append(r.choice(upper_charter))
#     if lower_char:
#         passwordsss.append(r.choice(lower_charter))  
#     if digit:
#         passwordsss.append(r.choice(digits)) 
#     if specific_char:
#         passwordsss.append(r.choice(special)) 
    
    
#     while (len(passwordsss) < length): 
#         passwordsss.append(r.choice(poolcharter)) 

#     r.shuffle(passwordsss)
#     return "".join(passwordsss)     
    

# try:

#     passward_length = int(input("Enter the desired password length:-"))
#     uppercase_letter = input("include uppercase letters? (y/n):-").strip().lower() == 'y'
#     lower_letters = input("include lowercase letters? (y/n):-").strip().lower() == 'y'
#     digits = input("include lowercase letters? (y/n):-").strip().lower() == 'y'
#     specific_char = input("include special characters? (y/n) :-").strip().lower() == 'y'
#     w = password(passward_length,uppercase_letter,lower_letters,digits,specific_char)
#     print(w)
# except ValueError as e:
#     print("Error : {}".format(e))  
# except Exception as e:
#     print(e)  

# class converts:
#     def __init__(self,choi,value): 
#         self.choi = choi
#         self.value = value

#     def distances(self):
#         if(self.choi==1):
#             return (self.value*0.621371)
#         elif(self.choi == 2):
#             return (self.value*1.60934)
#         else:
#             return ("Enter the valid key")

#     def temperatures(self):
#         if(self.choi==1):
#             return (self.value*(9/5)+32)
#         elif(self.choi == 2):
#             return ((self.value-32)*5/9)
#         else:
#             return ("Enter the valid key")  

#     def weights(self):
#         if(self.choi==1):
#             return (self.value*2.20462)
#         elif(self.choi == 2):
#             return ((self.value-32)*0.4533592)
#         else:
#             return ("Enter the valid key")                             


# while(True):
#    print("") 
#    print("Distance convert one units to another units then type distance")
#    print("Temperture convert one units to another units then type temperture")
#    print("Weight convert one units to another units then type weight")
#    print("if your qick this menu then type qick")
#    choice = (input("Enter the your choice :- ")).lower()
#    if (choice == "distance"):
#         print("convert kilomerter -> miles then press 1")
#         print("convert miles -> kilometer then press 2")
#         choi = int(input("Enter your choices key :- "))
#         value = float(input("Enter the value whicn are you change :- "))
#         c1 = converts(choi,value)
#         print(c1.distances())
#         print()

#    elif (choice =="temperture"):
#           print("convert fahrenhit -> celsius then press 1")
#           print("convert celsius -> fahrenhit then press 2")
#           choi = int(input("Enter your choices key :- ")) 
#           value = float(input("Enter the value whicn are you change :- "))
#           c1 = converts(choi,value)
#           print(c1.temperatures())
#           print()

#    elif (choice =="weight"):
#           print("convert kilograms -> pounds then press 1")
#           print("convert pounds -> kilograms then press 2")
#           choi = int(input("Enter your choices key :- "))
#           value = float(input("Enter the value whicn are you change :- "))
#           c1 = converts(choi,value)
#           print(c1.weight())
#           print()

#    elif(choice=="qick"):
#            print("------- quick ------")
#            break   
#    else:
#         print("please Enter given choices! thank you")
#         print()                

##############  daily expences ####################

