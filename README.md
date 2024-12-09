# Student Grades Management System

## Overview

This project is a comprehensive application for managing student grades. It includes features such as a dynamic user interface, advanced validation, and database integration.

## Features

1. **Dynamic User Interface**:
   - Implemented using Tkinter, providing a user-friendly GUI.
   - Dynamic input fields for grades based on user input.
   - Color-coded error messages for better user experience.

2. **Advanced Validation**:
   - Validates student names to ensure they consist only of alphabetic characters and spaces.
   - Validates score inputs to ensure they are numerical and within an acceptable range.

3. **Database Integration**:
   - Uses SQLite for efficient storage and retrieval of student data.
   - Ensures unique student IDs to prevent duplicates.

4. **Additional Functionalities**:
   - Calculates final grades using various methods.
   - Provides feedback through color-coded messages for errors.

5. **Scalable and Maintainable Design**:
   - Modular structure with clear separation of concerns.
   - Well-documented code with extensive comments.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Desertiocaine/FinalProject1Lab2Revamped.git
   cd FinalProject1Lab2Revamped
   
2. **Install Dependencies**:
   Ensure you have Python installed. Required standard libraries include `sqlite3` and `tkinter`.

3. **Configuration**:
   Edit `config.ini` to adjust database and GUI settings.

   ```ini
   [Database]
   name = students.db

   [GUI]
   width = 300
   height = 200

4. **Run the Application**:
   ```bash
   python main.py

5. **Use the Application**:
    - The application will open with a blank student list.
    - You can add, remove, and edit students as needed.
    - The final grade will be calculated automatically based on the scores entered.
6. **Add Students**:
   - Click the "Add Student" button.
   - Enter the student's name and scores.
   - Click "Save" to add the student to the database.

## Contributors

- Kenneth Parrack
- Farrel Aflagah
