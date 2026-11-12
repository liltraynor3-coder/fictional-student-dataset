# Fictional Student Dataset

## Project overview
This project contains a fictional dataset of 30 students. It was created for an academic data-handling exercise using Python.

## Dataset fields
- **Student ID** — unique fictional identifier for each student
- **Department** — student's academic department
- **Level** — academic level (100, 200, 300, or 400)
- **Attendance Percentage** — attendance rate, from 0 to 100
- **Average Examination Score** — average exam score, from 0 to 100

## Files
- `student_dataset.csv` — the generated dataset
- `generate_dataset.py` — Python script used to generate the dataset

## How to regenerate the dataset
1. Install Python 3 if it is not already installed.
2. Open a terminal in this project folder.
3. Run:

```bash
python generate_dataset.py
```

The script uses a fixed random seed so the generated records are reproducible.

## Note
All records are fictional and do not represent real students or academic results.
