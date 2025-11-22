# grade-generator.py
# Author: Eden Oliver
# This script collects assignment scores with categories (FA/SA) and weights,
# validates inputs, calculates weighted grades, GPA, pass/fail status,
# prints a summary, and saves everything into grades.csv.

import csv

class Assignment:
    """Represents an assignment with category, score, weight, and weighted grade."""
    def __init__(self, name, category, score, weight):
        self.name = name
        self.category = category.upper()
        self.score = score
        self.weight = weight
        self.weighted_grade = (score / 100) * weight

def get_valid_float(prompt, min_val=None, max_val=None):
    """Collect a float input with validation for range."""
    while True:
        try:
            value = float(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Value must be between {min_val} and {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== Welcome to Grade Generator Calculator ===")
    assignments = []

    while True:
        name = input("Enter assignment name: ").strip()

        # Collect category FA or SA
        category = input("Enter category (FA/SA): ").strip().upper()
        while category not in ("FA", "SA"):
            print("Invalid category! Must be FA or SA.")
            category = input("Enter category (FA/SA): ").strip().upper()

        # Collect score
        score = get_valid_float("Enter grade obtained (0-100): ", 0, 100)

        # Collect weight
        weight = get_valid_float("Enter weight (positive number): ", 0.01)

        assignments.append(Assignment(name, category, score, weight))

        more = input("Add another assignment? (y/n): ").strip().lower()
        if more != 'y':
            break

    # Calculate totals for FA and SA
    total_fa = sum(a.weighted_grade for a in assignments if a.category == "FA")
    total_sa = sum(a.weighted_grade for a in assignments if a.category == "SA")
    final_grade = total_fa + total_sa

    # Calculate GPA (scale 0–5)
    gpa = (final_grade / 100) * 5.0

    # Check pass/fail for each category
    fa_weight_total = sum(a.weight for a in assignments if a.category == "FA")
    sa_weight_total = sum(a.weight for a in assignments if a.category == "SA")
    fa_pass = total_fa >= (fa_weight_total * 0.5)
    sa_pass = total_sa >= (sa_weight_total * 0.5)
    status = "PASS" if fa_pass and sa_pass else "FAIL"

    # Print summary
    print("\n--- Grade Summary ---")
    for a in assignments:
        print(f"{a.name} ({a.category}): Grade={a.score}, Weight={a.weight}, Weighted={a.weighted_grade:.2f}")
    print(f"\nTotal Formative: {total_fa:.2f}")
    print(f"Total Summative: {total_sa:.2f}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Status: {status}")

    # Save CSV
    csv_filename = "grades.csv"
    with open(csv_filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Assignment", "Category", "Grade", "Weight"])
        for a in assignments:
            writer.writerow([a.name, a.category, a.score, a.weight])

    print(f"\nAll assignment data saved to {csv_filename}")

if __name__ == "__main__":
    main()
