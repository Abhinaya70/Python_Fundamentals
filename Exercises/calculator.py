# n1 = 40
# n2 = 30
n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

# Arithmetic operators

print("Addition:",n1+n2)
print("Subtraction:",n1-n2)
print("Multiplication:",n1*n2)

# checking divisibility with zero---------------
if n2 != 0:
    div = n1/n2
    print("Division:",n1/n2)
else:
    print("Division is not possible!")

# ternary operator-----------
print("Modulous:", n1%n2 if n2 !=0 else "Not possible")
print("Exponent: ",n1**n2)