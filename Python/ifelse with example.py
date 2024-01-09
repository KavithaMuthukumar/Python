#1 Get input for variable mark. If mark > 35, Print pass else fail

mark = input("Enter the mark: ")
if(mark > "35"):
    print("Pass")
else:
    print("Fail")
    
#------------------------------------------------------------------------------

#2 Get input for variable income, if income > 7000, scholarship is available. else not scholarship.

income = int(input("Enter the income: "))

if(income > 7000):
    print("Scholarship Available");
else:
    print("No Scholarship Available");
    
#------------------------------------------------------------------------------


#3 Get input for a number and check whether it is divisible by both 3 and 5. if Yes, print divisible else print not divisible.

number = int(input("Enter the number: "))
if((number%3)==0 and (number%5)==0):
    print("Divisible")
else:
    print("Not Divisible")

#------------------------------------------------------------------------------


#4 Get input for a number and find it is even or odd

number = int(input("Enter number: "))
if(number%2==0):
    print("Even")
else:
    print("Odd")

#------------------------------------------------------------------------------


#5 Get input for a score out of 100. if score < 35, "Poor" ; score > 35 < 70, "Average"; score > 70, "Good"

score = int(input("Enter score: "))
if(score < 35):
    print("Poor Student")
if(score > 35 and score < 70):
    print("Average student")
if(score > 70):
    print("Good Student")

#------------------------------------------------------------------------------


#6 Get a mini Calculator. Get 2 inputs a,b; Get input to add/sub/mul/div ; Do operations and Print 

a = int(input("Enter A: "))
b = int(input("Enter B: "))

operation = input("add / sub / mul / div: ")
if(operation == "add"):
    print(a+b)
elif(operation == "sub"):
    print(a-b)
elif(operation == "mul"):
    print(a*b)
elif(operation == "div"):
    print(a/b)
else:
    print("Invalid operation")

#------------------------------------------------------------------------------


#7 Get a input for score percentage. Only if the percentage is greater than 70, get input for his name, department and location. Then print you are eligible. If not print, you are not eligible.

score = int(input("Enter score percentage: "))
if(score > 70):
    input("Enter name: ")
    input("Enter Department: ")
    input("Enter Location: ")
    print("You are Eligible")
else:
    print("You are not Eligible")

#------------------------------------------------------------------------------

#8 Get input for salary and age.
    #if salary >= 20000 || age <= 25, get input for required loan amount.
        #if not print, you are not eligible for loan.
    #if required loan amount <= 50000, print you are eligible for loan.
    #if required loan amount > 50000, print maximum loan amount is 50000salary = int(input("Enter salary:"))

age = int(input("Enter age:"))
if(salary >= 20000 or age <= 25):
    loanamt = int(input("Required loan amount: "))
    if(loanamt > 50000):
        print("maximum loan amount is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you are not eligible for loan")
    
#------------------------------------------------------------------------------

#9 Get input for 5 subject marks. Add all of it and find average.
    #If average < 35, print "Additional class is required",
    #else, print, "You are good."

sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))
sub4 = int(input("Enter sub4 marks: "))
sub5 = int(input("Enter sub5 marks: "))
total = sub1+sub2+sub3+sub4+sub5;
average = total/5;

if(average < 35):
    print("Additional class is required")
else:
    print("You are good.")


#------------------------------------------------------------------------------

























