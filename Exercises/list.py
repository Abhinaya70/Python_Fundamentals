l = []
n= int(input("How many elements do you want in the list?:"))
for i in range(n):
    num = int(input("enter a number: "))
    l.append(num)
print(l)
# Access elements ----------

print("First_element:",l[0] if l else "List is empty")

# adding elements---------
new_ele = int(input("enter a number to add:"))
l.append(new_ele)
print("New_list : ",l)
# remove elements --------------
remove_ele = int(input("entetr a num to remove:"))
if remove_ele in l:
    l.remove(remove_ele)
else:
    print("element is not in the list!")

# built-in func----------
print("SUM: ",sum(l))
print("Largest_element: ",max(l))
print("Smallest_element: ",min(l))