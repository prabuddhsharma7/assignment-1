# Simple Progress Report Analyzer

# Enter student details
name = input("Enter student name: ")
registration_no=input("enter registration no.")

# Enter marks for subjects
calculus = int(input("Enter marks in calculus: "))
bioengineering = int(input("Enter marks in bioengineering: "))
computational_chemistry = int(input("Enter marks in computational chemistry: "))
programming= int(input("Enter marks in programming: "))

# Calculate total and average
total = calculus + bioengineering + computational_chemistry + programming
average = total / 4

# Decide grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Print report
print("\n--- Progress Report ---")
print("Name:", name)
print("registration no:",registration_no) 
print("Math:", calculus)
print("Science:", bioengineering)
print("English:", computational_chemistry)
print("History:", programming)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)