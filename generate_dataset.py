"""
Generate a fictional student dataset and save it as student_dataset.csv.
Run with: python generate_dataset.py
"""
import csv
import random

random.seed(42)

departments = [
    "Computer Science", "Accounting", "Business Administration",
    "Economics", "Mass Communication", "Biochemistry",
    "Mathematics", "Political Science"
]
levels = [100, 200, 300, 400]

students = []
for i in range(1, 31):
    students.append({
        "Student ID": f"STU{2026}{i:03d}",
        "Department": departments[(i * 3 + i // 4) % len(departments)],
        "Level": random.choice(levels),
        "Attendance Percentage": round(random.uniform(62, 100), 1),
        "Average Examination Score": round(random.uniform(45, 96), 1),
    })

with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

print(f"Created student_dataset.csv with {len(students)} fictional records.")
