#1 Get input for number a,b. Print the number between a and b.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(a+1,b):
    print(i)


#-------------------------------------------------------------------------

#2 Print the even numbers between 1 and 10

for i in range(1,11):
    if(i%2==0):
        print(i)
     

#-------------------------------------------------------------------------

#3 Count the odd numbers between 1 and 10

count = 0
for i in range(1,11):
    if(i%2!=0):
        count = count+1
print(count)
    

#-------------------------------------------------------------------------

#4 Count the number of odd and even numbers between 1 and 10

counteven = 0
countodd = 0

for i in range(1,11):
    if(i%2!=0):
        countodd = countodd+1
    elif(i%2==0):
        counteven = counteven+1
print("Odd: ",countodd)
print("Even: ",counteven)

#-------------------------------------------------------------------------

#5 Count the number which are divisible by 3 and 5. Range 1 to 100

count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count = count+1
print(count)


#-------------------------------------------------------------------------















