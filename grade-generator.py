# grade-generator.py

import csv

class Assignment:
    def __init__(self, name, category, grade, weight):
        self.name = name
        self.category = category.upper()
        self.grade = grade
        self.weight = weight
        self.weighted_grade = (grade / 100) * weight

def get_valid_input(prompt, type_func, condition_func, error_msg):
    """Helper function for validated input"""
    while True:
        try:
            value = type_func(input(prompt))
            if condition_func(value):
                return value
            else:
                print(error_msg)
        except ValueError:
            print("Invalid input type. Please try again.")

def main():
    print("=== Welcome to Grade Generator Calculator ===")
    assignments = []

    while True:
        name = input("Enter assignment name: ").strip()

        category = input("Enter category (FA/SA): ").strip().upper()
        while category not in ("FA", "SA"):
            print("Invalid category! Must be FA or SA.")
            category = input("Enter category (FA/SA): ").strip().upper()

        grade = get_valid_input(
            "Enter grade obtained (0-100): ",
            float,
            lambda x: 0 <= x <= 100,
            "Grade must be between 0 and 100."
        )

        weight = get_valid_input(
            "Enter weight (positive number): ",
            float,
            lambda x: x > 0,
            "Weight must be a positive number."
        )

        assignments.append(Assignment(name, category, grade, weight))

        more = input("Add another assignment? (y/n): ").strip().lower()
        if more != 'y':
            break

    # Calculate category totals
    total_fa = sum(a.weighted_grade for a in assignments if a.category == "FA")
    total_sa = sum(a.weighted_grade for a in assignments if a.category == "SA")
    final_grade = total_fa + total_sa
    gpa = (final_grade / 100) * 5.0

    # Pass/fail
    fa_weight_total = sum(a.weight for a in assignments if a.category == "FA")
    sa_weight_total = sum(a.weight for a in assignments if a.category == "SA")
    fa_pass = total_fa >= (fa_weight_total * 0.5)
    sa_pass = total_sa >= (sa_weight_total * 0.5)
    status = "PASS" if fa_pass and sa_pass else "FAIL"

    # Print summary
    print("\n--- Grade Summary ---")
    for a in assignments:
        print(f"{a.name} ({a.category}): Grade={a.grade}, Weight={a.weight}, Weighted={a.weighted_grade:.2f}")
    print(f"\nTotal Formative: {total_fa:.2f}")
    print(f"Total Summative: {total_sa:.2f}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")

    # Save CSV
    csv_filename = "grades.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Assignment", "Category", "Grade", "Weight"])
        for a in assignments:
            writer.writerow([a.name, a.category, a.grade, a.weight])

    print(f"\nAll assignment data saved to {csv_filename}")

if __name__ == "__main__":
    main()
