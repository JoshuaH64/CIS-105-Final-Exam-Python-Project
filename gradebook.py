"""
Student Gradebook Application
A Python program to manage student grades and calculate averages.
"""

def display_menu():
    """Display the main menu options to the user."""
    print("\n" + "="*50)
    print("        STUDENT GRADEBOOK APPLICATION")
    print("="*50)
    print("1. Add Student and Grades")
    print("2. View All Students")
    print("3. Calculate Class Average")
    print("4. View Student Details")
    print("5. Save Gradebook to File")
    print("6. Load Gradebook from File")
    print("7. Exit")
    print("="*50)

def add_student(gradebook):
    """Add a new student with their grades."""
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Student name cannot be empty.")
            return

        if name in gradebook:
            print(f"Student '{name}' already exists. Use a different name or update existing student.")
            return

        grades = []
        print(f"Enter grades for {name} (enter 'done' when finished):")

        while True:
            grade_input = input("Enter grade (or 'done'): ").strip().lower()
            if grade_input == 'done':
                break

            try:
                grade = float(grade_input)
                if 0 <= grade <= 100:
                    grades.append(grade)
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid grade. Please enter a number or 'done'.")

        if grades:
            gradebook[name] = grades
            print(f"Successfully added {name} with {len(grades)} grades.")
        else:
            print("No grades entered. Student not added.")

    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_students(gradebook):
    """Display all students and their average grades."""
    if not gradebook:
        print("No students in the gradebook yet.")
        return

    print("\n" + "-"*60)
    print("STUDENT GRADEBOOK SUMMARY")
    print("-"*60)
    print("<25")
    print("-"*60)

    for name, grades in gradebook.items():
        avg = sum(grades) / len(grades)
        print("<25")

def calculate_class_average(gradebook):
    """Calculate and display the overall class average."""
    if not gradebook:
        print("No students in the gradebook yet.")
        return

    all_grades = []
    for grades in gradebook.values():
        all_grades.extend(grades)

    if all_grades:
        class_avg = sum(all_grades) / len(all_grades)
        print(".2f")
        print(f"Total grades recorded: {len(all_grades)}")
        print(f"Number of students: {len(gradebook)}")
    else:
        print("No grades found in the gradebook.")

def view_student_details(gradebook):
    """View detailed information for a specific student."""
    if not gradebook:
        print("No students in the gradebook yet.")
        return

    name = input("Enter student name to view details: ").strip()

    if name not in gradebook:
        print(f"Student '{name}' not found in gradebook.")
        return

    grades = gradebook[name]
    avg = sum(grades) / len(grades)

    print(f"\nDetailed Report for {name}")
    print("-" * (20 + len(name)))
    print(f"Number of grades: {len(grades)}")
    print(f"Grades: {', '.join(f'{g:.1f}' for g in grades)}")
    print(".2f")
    print(f"Highest grade: {max(grades):.1f}")
    print(f"Lowest grade: {min(grades):.1f}")

def save_gradebook(gradebook, filename="gradebook.txt"):
    """Save the gradebook to a file."""
    try:
        with open(filename, 'w') as file:
            for name, grades in gradebook.items():
                grades_str = ','.join(str(grade) for grade in grades)
                file.write(f"{name}:{grades_str}\n")
        print(f"Gradebook saved to {filename}")
    except Exception as e:
        print(f"Error saving gradebook: {e}")

def load_gradebook(filename="gradebook.txt"):
    """Load the gradebook from a file."""
    gradebook = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if ':' in line:
                    name, grades_str = line.split(':', 1)
                    grades = [float(g.strip()) for g in grades_str.split(',') if g.strip()]
                    gradebook[name] = grades
        print(f"Gradebook loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty gradebook.")
    except Exception as e:
        print(f"Error loading gradebook: {e}")
    return gradebook

def main():
    """Main function to run the gradebook application."""
    gradebook = load_gradebook()

    print("Welcome to the Student Gradebook Application!")
    print("Manage student grades, calculate averages, and generate reports.")

    while True:
        display_menu()

        try:
            choice = input("Enter your choice (1-7): ").strip()

            if choice == '1':
                add_student(gradebook)
            elif choice == '2':
                view_all_students(gradebook)
            elif choice == '3':
                calculate_class_average(gradebook)
            elif choice == '4':
                view_student_details(gradebook)
            elif choice == '5':
                save_gradebook(gradebook)
            elif choice == '6':
                gradebook = load_gradebook()
            elif choice == '7':
                save_choice = input("Save gradebook before exiting? (y/n): ").strip().lower()
                if save_choice == 'y':
                    save_gradebook(gradebook)
                print("Thank you for using the Student Gradebook Application!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Saving gradebook...")
            save_gradebook(gradebook)
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()