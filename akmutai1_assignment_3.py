student_name = "Adams Mutai"  
current_gpa = 3.5
study_hours = 4
social_points = 76
stress_level = 50

print(f"Welcome! {student_name}")
print("Here are your stats:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")


print("Choose your course difficulty:")
print("A) Light (12 credits)")  
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    study_hours += 5
    stress_level -= 10
    print("You chose a light course load, you have more free time and less stress")

elif choice == "B":
    if current_gpa >= 3.0:
        study_hours += 10
        stress_level += 5
        print("You handle the standard load well.")
    else:
        study_hours += 15
        stress_level += 15
        print("The standard load is negativley affecting your GPA.")

elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 20
        stress_level += 10
        print("You chose a very difficult course load and you are excelling!")
    else:
        study_hours += 25
        stress_level += 25
        print("The heavy load is detrimental to your current GPA.")

else:
    print("Invalid choice. Please select A, B, or C.")