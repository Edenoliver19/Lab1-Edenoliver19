# Lab1: Grade Generator and Organizer Scripts
**Name:** Eden Oliver
## Submission Files
This repository includes the following files:

- `grade-generator.py` – Python script that collects assignment grades, calculates weighted grades, GPA, and pass/fail status, and saves all data to a CSV file (`grades.csv`).
- `organizer.sh` – Bash script that finds CSV files, renames them with a timestamp, moves them to an `archive/` folder, and logs all actions in `organizer.log`.
- `README.md` – This documentation file explaining how to run the scripts and showing example outputs.
- `archive/` – Folder created automatically when `organizer.sh` is run. 

## 1. grade-generator.py
Calculates weighted grades, GPA, and pass/fail status. Saves all assignment data to `grades.csv`.

### How to run:

python3 grade-generator.py

### Example:
Python Lab (FA): Grade=80.0, Weight=30.0, Weighted=24.0
Linux Quiz (SA): Grade=90.0, Weight=40.0, Weighted=36.0
Total Formative: 24.0
Total Summative: 36.0
Final Grade: 60.0
GPA: 3.0
Status: PASS
Saved to grades.csv

## 2. organizer.sh

Archives CSV files by renaming them with a timestamp, moves them to an archive/ folder, and logs the actions in organizer.log.

## How to run:
chmod +x organizer.sh
./organizer.sh

### Example:
Archiving grades.csv as grades-20251122-230001.csv
Archiving complete. Check archive/ and organizer.log


#Folder Structure

├── grade-generator.py
├── organizer.sh
├── README.md
└── archive/      # This  one is created automatically when organizer.sh runs



