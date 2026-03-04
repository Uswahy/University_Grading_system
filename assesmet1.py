#University Grading System
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_scholarship(score):   
    if score >= 90:
        return "80% Scholarship"
    elif score >= 80:
        return "50% Scholarship"
    else:
        return "No Scholarship"

def calculate_total(marks):
    return sum(marks)
    
def calculate_average_marks(sum_marks, num_subjects):
    return sum_marks / num_subjects

def calculate_percentage(sum_marks, max_marks):
    return (sum_marks / max_marks) * 100



while True:
        student_name = input("Enter the student's name: ")
        student_id = input("Enter the student's ID: ")

        marks = []

        for mar in range(5):
            subject = int(str(input(f"Enter the name of subject {mar+1}: ")))
            mark = int(str(input(f"Enter marks for {subject}: ")))
            marks.append(mark)
# calcuATIONS
        total = calculate_total(marks)
        average_marks = calculate_average_marks(total, 5)
        percentage = calculate_percentage(total, 500)

        grade = calculate_grade(percentage)
        scholarship = calculate_scholarship(percentage)


        print("\n--- Student Result ---")
        print(f"Student Name: {student_name}")
        print(f"Student ID: {student_id}")
        print("Total marks =", total)
        print("Average Marks =", average_marks)
        print("Percentage =", percentage)
        print("Grade =", grade)
        print("Scholarship =", scholarship)
        continue_input = input("Do you want to enter another student details: ").strip().lower()
if continue_input == 'yes':
        # Call the main function to input another student's result
        pass
elif continue_input == 'no':
        print("Exiting the program. Goodbye!")
else:
        print("Invalid input. Please enter 'yes' or 'no'.")
