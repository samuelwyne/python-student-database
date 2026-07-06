while True:
    try:
        num=int(input("Enter the student number: "))
    
        if num>0:
            break
        else:
            print("Enter correct number of students")
    except ValueError:
        print("Enter correct number of student:") 

students=[]
for i in range(num):
    student={}
    student["name"]=input("Enter student's name: ")
   
    while True:
     try:
        student["age"]=int(input("Enter student's age: "))
     
        if student["age"]>0:
            break
        else:
            print("Enter correct age of student: ")
     except ValueError:
        print("Enter correct age of student:") 
    student["course"]=input("Enter students's course: ")    
    while True:
     try:
        student["marks"]=int(input("Enter student's marks: "))
     
        if student["marks"]>0:
            break
        else:
            print("Enter correct marks of student: ")
     except ValueError:
        print("Enter correct marks of student:")
    student["grade"]=input("Enter student's grade: ")
    students.append(student)
print()
print(f"{"="*7}student records {"="*7}")
print(f"name{" "*3}age{" "*3}marks{" "*3}grade")
for student in students:
    print(f"{student["name"]}{" "*5}{student["age"]}{" "*5}{student["marks"]}{" "*5}{student["grade"]}") 
print(f"name{"="*5}age{"="*5}marks{"="*5}grade")
for student in students:
    print(f"{student["name"]}{" "*5}{student["age"]}{" "*5}{student["marks"]}{" "*5}{student["grade"]}") 
