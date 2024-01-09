# Set s_username = “EMC” s_password = “123”
# Get input for username and password
# Create a function called validate
# If username and password matches, return true else false.
"""
s_username = "EMC"
s_password = "123"

uname = input("Enter username: ")
pswd = input("Enter password: ")

def validate():
    if(s_username == uname and s_password == pswd):
        return True
    else:
        return False

check = validate()
print(check)
"""
#--------------------------------------------------------------------------
# (a+b)*c. Get input for a,b and call add() to return sum of a+b.
# multiply that sum with c

def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a+b

def mul():
    c = int(input("Enter c: "))
    return add()*c

print("The value of (a+b)*c: ",mul())
