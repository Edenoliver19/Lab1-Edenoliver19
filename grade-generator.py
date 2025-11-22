# grade-generator.py
# Author: Eden Oliver
# This script collects assignment scores and weights, validates them,
# calculates a weighted grade, GPA, and pass/fail status, and saves
# everything into a CSV file.

import csv

def get_float_input(prompt):
    """Safely collect a float input with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_gpa(final_grade):
    """Convert a percentage grade into a 4.0 scale GPA."""
    if final_grade >= 90:
        return 4.0
    elif final_grade >= 80:
        return 3.0
    elif final_grade >= 70:
        return 2.0
    elif final_grade >= 60:
        return 1.0
    return 0.0

def main():
    print("=== Grade Generator ===")

    student_name = input("Student Name: ")

    assignments = []
    total_weight = 0

    # Collect scores until the weight reaches 100%
    while total_weight < 100:
        score = get_float_input("Enter assignment score: ")
        weight = get_float_input("Enter assignment weight (%): ")

        # Ensure weights don’t exceed 100%
        if total_weight + weight > 100:
            print("Total weight cannot exceed 100%. Try again.")
            continue

        assignments.append((score, weight))
        total_weight += weight

    # Calculate weighted final grade
    final_grade = sum(score * (weight / 100) for score, weight in assignments)
    gpa = calculate_gpa(final_grade)
    status = "Pass" if final_grade >= 50 else "Fail"

    print(f"\nFinal Grade: {final_grade}")
    print(f"GPA: {gpa}")
    print(f"Status: {status}")

    # Save results to CSV
    with open("grades.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Assignment", "Score", "Weight"])
        for i, (score, weight) in enumerate(assignments, start=1):
            writer.writerow([f"Assignment {i}", score, weight])
        writer.writerow(["Final Grade", final_grade])
        writer.writerow(["GPA", gpa])
        writer.writerow(["Status", status])

    print("Saved to grades.csv")

if __name__ == "__main__":
    main()
