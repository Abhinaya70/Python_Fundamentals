students ={}
def add_student():
    student_id = input("enter student_id: ")
    if student_id in students:
        print("Student id already exists!")
        return
    name = input("enter name: ")
    age = int(input("enter age: "))
    course = input("enter the course: ")
    percentage = float(input("enter the percentage: "))
    students[student_id] = {"Name":name,"Age":age,"Course":course,"Percentage":percentage}
    print("Student added successfully")
def view_student():
    if not students:
        print("No record found!")
        return 
    for student_id,details in students.items():
        print("Student ID: ",student_id)
        for k,v in details.items():
            print(k,":",v)
def search_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student_details: ",students[student_id])
    else:
        print("Student not found!")
def update_student():
    student_id = input("enter student_ID: ")
    if student_id in students:
        print("\n What would you like to update? ")
        print("1. Name")
        print("2. Age")
        print("3. Course")
        print("4. Percentage")
        choice = input("Enter your choice: ")
        if choice == "1":
            students[student_id]["name"] = input("Enter new name: ")
        elif choice == "2":
            students[student_id]["age"] = int(input("enter new age: "))
        elif choice == "3":
            students[student_id]["course"] = int(input("enter new course: "))
        elif choice == "4":
            students[student_id]["percentage"] = float(input("enter new percentage: "))

        else:
            print("Invalid choice.")
            return
        print("Student details updated successfully!")
    else:
        print("Student not found!")
def main():
    while True:
        print("\n ------ Student Management ------")
        print("1. Add Student")
        print("2. View Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")
        choice = input("enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid choice. Try Again!")
if __name__ == "__main__":
        main()