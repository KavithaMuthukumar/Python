#1 Create a class called Student. Create a var name, regno using constructor.
#Create a function called display which should display the name and regno of the student.
"""
class student:
    def __init__(self):
        self.name="EMC"
        self.regno=123
    def display(self):
        print("Name: ",self.name)
        print("Reg No: ",self.regno)

s1=student()
s1.display()
"""
#------------------------------------------------------

#2 Create a class called Fruit. 
# Create a variable called color using __init__ method.
# Create a object called apple "Pass the color variable as a parameter through object"

class fruit:
    def __init__(self):
        self.color = "Red"

apple = fruit(color)
print(apple.color)
