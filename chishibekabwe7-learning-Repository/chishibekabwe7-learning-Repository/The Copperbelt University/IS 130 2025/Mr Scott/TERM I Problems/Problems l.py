#!/bin/python3

#Problem 13
"""
Write a progam that will display the university you will be going to,based on the following conditinos:
IF the university is CBU and status is "Accepted" then display "The copperbelt University" if the uniersity is UNZA and status is 'Accepted'
then display The university of Zambia. Else if the university is MU and status is 'Accepted' then display Mulungushi University.
"""
institution = str(input("Enter the University you wish to go to:"))
Status_1 = "Yes"
Status_2 = "No"
status = str(input("Do you have an addimissions Letter at that school? Yes/No:"))
if institution == "CBU" and status == Status_1:
    print("Your going to the Copperbelt Univeristy")
elif institution == "UNZA" and status == Status_1:
    print("Your Going to the University of Zambia")
elif institution == "MU" and status == Status_1:
    print("Your going to Mulungushi University")
else:
    print("Your not eligile to the institution")
 
    


#Problem 12
"""
Write a program that asks for the user for their age,and whether they have their
drivers License. The program should then print out if they are eligible to rent a car or not.
"""
age = int(input("Enter Age:"))
Yes = "Yes"
No = "No"
drivers_License = str(input("Do you have a Driver's License? Yes/No:"))
if age > 21 and drivers_License == Yes:
    print("You are eligible to rent a car")
else:
    print("You are not eligible to rent a car")




#Problem 11
"""
Write a Program that will ask for user input and  deterimines if a number is negative,possitive,or zero.
"""
Number = int(input("Enter Number"))
if Number > 0:
    print("This is a positive Value")
elif Number == 0:
    print("This Number is Zero")
else:
    print("This is a negative Value")

#Problem 10
"""
You are required to write a program that will display the current weather condition and your clothing
based on the current temperature. Your program will recieve the current temperature as the input and 
check for the following. If the current temperature < 10 then it's freezing and clothing is a Jersey.
Else if the current temperature > 30 then it's hot and clothing is a T-shirt,Else if the current 
temperature is normal then the clothing is a suit.
"""
Current_temperature = float(input("Enter the current temperature:"))
if Current_temperature < 10:
    current_weather = "FREEZING"
    clothing = "Jersey"
elif Current_temperature > 30:
    current_weather = "HOT"
    clothing = "T-Shirt"
else:
    current_weather = "NORMAL"
    clothing = "Suit"
print(f"The current temperature is {current_weather} and the preffered outfit is {clothing}")


 


#Problem 9
"""
Write a program that will display the current wheather conditions based on the current temperature,
our program will recieve he current temperature as an input and will check for the following, if the
current temperature is less than 10, display "FREEZING", if the current temperature is less than 10,
display "HOT" else display normal.
"""
current_temperature = int(input("Enter the Current temperature:"))
if current_temperature < 10:
    print("FREEZING")
elif current_temperature > 30:
    print("HOT")
else:
    print("NORMAL")




#Problem 8
"""
Write a program that will calculate the VAT that will be paid for Tax purchased items, The program
should recieve the price of each item and sum them up together. If the sum is greater than 50, VAT
will be calculated as the sim multiplied by 0.16 else VAT will be calculated as the sum times 0.05.
"""
Price_1 = int(input("Enter the first Price:"))
Price_2 = int(input("Enter the Second Price:")) 
sum = Price_1 + Price_2
if sum > 50:
    VAT = sum * 0.16
else:
    VAT = sum * 0.03
print(VAT)

#Problem 7
"""
#Zambia recognises 2 types of genders,Male and female,write a program that will ask the user to
#enter either M for Male and F for Female, the should should check the gender entered and output
#male if the gender is M else ouput female.
"""
Gender = input("Enter Your Gender:")
Gender2 = "Male"
if Gender == Gender2:
   print("Male")
else:
    print("Female")


#Problem 6
"""
Write a program that will find out if a vehicle is overspeeding or not,The maximum speed
limit in residential areas is 40km/h write a program that will recieve the speed limit of the vehicle,
and if the speed of the vehicle is greater than the maximum speed limit, output overspeeding.
"""
Speed = int(input("Enter the speed of a vehicle:"))
if Speed > 40:
    print("The Vehicle is OverSpeeding!")
else:
    print("Normal Speed!")    

#Write a Program that will calculate the fine, due to overdue books.
Overdue_days = int(input("Enter the Number of days a book is overdue:"))
Daily_fine_rate = float(input("Enter the Fine rate:"))
Overdue_fine = Overdue_days * Daily_fine_rate
print(f"The Overdue fine is {Overdue_fine}")

#Problem 4
#Write a Program that will find the total retail price of a product
retail_price = int(input("Enter the Retail Price:"))
VAT_rate = float(input("Enter the VAT rate:"))
total_retail_price = retail_price * 1 + VAT_rate
print(f"The Total Retail Price is {total_retail_price}")

#Problem 3
#Write a Program that will find the Perimeter of a rectangle
length = int(input("Enter the length:"))
width = int(input("Enter the Width:"))
Perimeter =  2 * length + width
print(f"The Perimeter is {Perimeter}")


#Problem 2 
#Write a program that will add two numbers entered by the user
Num1 = int(input("Enter the first Number:"))
Num2 = int(input("Enter the Second Number:"))
Sum = Num1 + Num2
print(f"The Sum is {Sum}")

#Problem 1
#Write a Program that calculates the area of the paraellegram when the values of the height 
# and base are given as inputs.
breadth = float(input("Enter the base:"))
height = float(input("Enter the height:"))
Area = 0.5 * breadth * height
print(f"The Area is {Area}")


