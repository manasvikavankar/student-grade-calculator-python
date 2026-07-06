student = input("Enter your name: ")

print("--Kindly Enter Your All Subject Marks To calculate the Result--")

eng = int(input("English: "))
math = int(input("Maths: "))
sci = int(input("Science: "))
dbms = int(input("DBMS: "))
os = int(input("OS: "))

total = eng + math + sci + dbms + os
percentage = (total/500)*100

print(f"Student: {student}") 
print(f"Total: {total}") 
print(f"Percentage: {percentage:.2f}%") 

if(percentage >= 90.0):
    print("Grade: A")
elif(percentage >= 80.0):
    print("Grade: B")
elif(percentage >= 70.0):
    print("Grade: C")
elif(percentage >= 60.0):
    print("Grade: D")
elif(percentage >= 50.0):
    print("Grade: E")
else:
    print("Grade: F")
    

if(percentage >= 35.0):
    print("Result: Pass")
else:
    print("Result: Fail")