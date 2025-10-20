'''NAME: MANPREET KAUR
   COURSE: B.TECH CSE CORE 
   SECTION: A
   SEMESTOR: 1
   SUBJECT: PROGRAMMING FOR PROBLEM SOLVING USING PYTHON
   COURSE CODE:ETCCPP102
   ROLL NO.: 2501010070
   PROJECT TITLE: DAILY CALORIE TRACKER
   DATE OF SUBMISSION: 20 OCTOBER 2025
   SUBMITTED BY: MANPREET KAUR
   SUBMITTED TO: FEROZ AHMAD SIR
'''

# TASK-1 :- Set up and Introduction

print("Welcome to our daily calorie tracker !!")
print("This program will take user input of the meal name and its calories \
and after this the program will return the Total calories taken, the average \
calories of your daily meal intake. This program will also return the \
table containing the meal name and its corresponding calories.")

# TASK-2 :- Input and data collection

num_meal=int(input("Enter number of meals you have taken:")) # user will enter the number of meals taken in a day.
cpnum_meal=num_meal # Creating a copy of num_meal for calculating average
meal_lst=[] # an empty list for storing the values of the meals taken.
calorie_lst=[] # an empty list for storing the values of the calories of the corresponding meal.

while num_meal>0: # loops for taking input from the user.
    meal_name=input("Enter the meal name:") # input meal name.
    calorie_amt=float(input("Enter the calorie amount of your meal:")) # input its amount of calories.
    meal_lst.append(meal_name) # adding the meal names into an empty list meal_lst.
    calorie_lst.append(calorie_amt) # adding the corresponding amount of calories to an empty list calorie_amt.  
    num_meal=num_meal-1 # decreasing the num_meal value by one after entering one entity.

# TASK-3 :- Calorie Calculations

tot_calorie=sum(calorie_lst)
avg_calorie=tot_calorie/cpnum_meal # calculating the average amount of calories.
print("your today's total calorie intake is:",tot_calorie)
print("your today's average calorie intake is:",avg_calorie)
calorie_limit=float(input("Enter your daily calorie limit:"))

# TASK-4 :- Exceed limit warning system

if tot_calorie>calorie_limit:
    print("WARNING !!")
    print("you have exceeded your daily calorie intake:")
else:
    print("HURRAY !!")
    print("you have completed your target.")
 
# TASK-5 :- Neatly formatted output

print("MEAL NAME" +" "*10+ "CALORIES")
print("----------------------------")
for i in range(len(meal_lst)):
    print(f"{meal_lst[i]}" + " " * (20-len(meal_lst[i])) +f"{calorie_lst[i]}")
print("Total calories"+" "*(20-len("Total_calories"))+f"{tot_calorie}")
print("Average calories"+" "*(20-len("average calories"))+f"{avg_calorie}")
