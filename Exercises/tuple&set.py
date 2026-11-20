# t = int(input("enter how many elements for  the tuple: "))
# l= []
# for i in range(t):
#     val = int(input("enter a number: "))
#     l.append(val)
# my_tup = tuple(l)
# print("Tuple: ",my_tup)
# print("first_element: ",my_tup[0] if my_tup else "Tuple is empty.")
# print("Length of my tuple: ",len(my_tup))

# --------- SET -------------------------

n1 = int(input("How many elements for set1?: "))
s1 = set()
for i in range(n1):
    val = int(input("enter a number for set1: "))
    s1.add(val)
n2 = int(input("How many elements for set2?: "))
s2 = set()
for i in range(n2):
    val2 = int(input("enter a number for set2: "))
    s2.add(val2)
print("first set: ",s1)
print("second set: ",s2)
print("Union of two sets: ",s1.union(s2))  
print("Difference b/w 2 sets: ",s1.difference(s2)) 
print("Difference b/w 2 sets: ",s2.difference(s1))