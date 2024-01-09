"""
def painter():
    print("Painting")
painter()
"""
#------------------------
"""
#Create a function add(),sub(),mul(),div() with inputs a,b inside every function

a=int(input("Enter a: "))
b=int(input("Enter b: "))

def add():
    print("A+B = ",a+b)
def sub():
    print("A-B = ",a-b)
def mul():
    print("A*B = ",a*b)
def div():
    print("A/B = ",a/b)

add()
sub()
mul()
div()
"""
#------------------------
#Get a integer number from user and pass it to a function called findevenorodd().
#Let the function print whether the number is even or odd
"""
num = int(input("Enter a number: "))
def findevenorodd():
    if((num)%2==0):
        print("Even")
    else:
        print("Odd")

findevenorodd()
"""
#------------------------
#Get a integer number from user and pass it to a function called findpassorfail().
#Let the function print whether it is pass or fail.
"""
mark = int(input("Enter the mark: "))
def findpassorfail():
    if(mark>=35):
        print("Pass")
    else:
        print("Fail")

findpassorfail()
"""
#------------------------
#Get input for a and b. Pass to function printrange(). Print numbers from a to b
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))

def printrange():
    for i in range(a,b):
        print(i)

printrange()
"""
#------------------------
























