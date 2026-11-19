def factorial(num):
    res = 1
    for i in range(1,num+1):
        res*=i
    return res
num =  int(input("enter a number:"))
if num<0:
    print("Factorial is not defined for negative numbers!")
else:
    print("Factorial: ",factorial(num))