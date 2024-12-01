 # Final Project: Student Grades Management System

## Overview

This project manages and displays student grades using Python. It allows input of scores, calculates grades, stores data in an SQLite database, and displays results in a GUI.

## Project Structure

```
/FinalProject1Lab2Revamped
│
├── data.py                 # Handles data input and validation
├── database.py             # Manages SQLite database operations
├── grades.py               # Calculates grades from scores
├── ui.py                   # Displays grades using Tkinter GUI
├── main.py                 # Main execution flow of the program
├── test_grades.py          # Unit tests for the grading logic
│
├── Project 1.docx          # Project documentation file
├── README.md               # Project overview and instructions
├── students.db             # SQLite database file storing student records
└── config.ini              # Configuration settings (if applicable)
```

## Features

1. **Data Input**:
   - Input scores for a specified number of students with validation.

2. **Grading Calculation**:
   - Calculates grades based on scores using a relative grading scale.

3. **Database Management**:
   - Stores and retrieves student scores and grades using SQLite.

4. **Graphical Display**:
   - Displays scores and grades using a Tkinter-based GUI.

5. **Testing**:
   - Includes unit tests to verify grading logic.

## How to Run

1. Ensure all required Python packages are installed:
   - `sqlite3`
   - `tkinter`

2. Execute the main program:
   ```bash
   python main.py
   ```

3. Run tests to verify functionality:
   ```bash
   python test_grades.py
   ```

## Further Assistance

For issues or further functionality, please consult the documentation or reach out to the project contributors.

## Contributors

- Kenneth Parrack
- Farrel Aflagah
