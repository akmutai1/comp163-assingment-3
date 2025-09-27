student_name = "Adams Mutai"  
current_gpa = 3.5
study_hours = 4
social_points = 76
stress_level = 50
study_options = ["Programming", "Math", "English", "History"]


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
print("Choose a study focus from the following options:")
print(study_options)
study_choice = input("Your study choice: ")

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

if study_choice in study_options:

    if (study_choice == "Programming" or study_choice == "Math") and current_gpa < 3.5:
        current_gpa += 0.2
        social_points -= 10
        print("You have a rigorous study, your gpa is up but your social life is down.")

    elif (study_choice == "English" or study_choice == "History") and social_points <= 60:
        current_gpa += 0.1
        social_points += 5
        print("Your work-life is more balanced and your gpa is slightly up, and your social life is fine.")

    elif study_choice == "Programming" and current_gpa >= 3.5:
        current_gpa += 0.3
        print("Studying programming has made you excel!")

    else:
        print("You study hard, but results are average.")

else study_choice not in study_options:
    print("Invalid choice. Please select a valid study option.")