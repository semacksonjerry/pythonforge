#!/usr/bin/python3

full_name = str(input("Enter your full name: "))
age = int(input("Enter your age: "))
school = str(input("Enter your school: "))
subject = str(input("Enter your favorite subject: "))

print("\n \n")

print(f"===== STUDENT PROFILE =====")
print(f"Name: {full_name}")
print(f"School: {school}")
print(f"Favourite: {subject}")

print(f"Name in uppercase: {full_name.upper()} \n")

print(f"Fisrt 3 Characters: {full_name[:3]} \n")

print(f"Last 3 Characters: {full_name[-3:]} \n")

print(f"Your age after 5 yaers will be: {age + 5} \n")

print(f"Total Characters in your name: {len(full_name)} \n")