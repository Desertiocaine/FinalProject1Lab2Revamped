# Student Grades Management System

## Overview

This project started as a simple script to calculate and display student grades based on scores. Over time, it evolved into a robust application with advanced features like database integration, graphical user interface, and enhanced validation logic.

## Features

1. **Dynamic User Interface**:
   - Implemented using Tkinter, the application provides a dynamic and user-friendly GUI.
   - Dynamic input fields for grades based on user input.
   - Brighter and aesthetically pleasing design with color-coded error messages.

2. **Advanced Validation**:
   - Validates student names to ensure they consist only of alphabetic characters and spaces.
   - Validates score inputs to ensure they are numerical and fall within an acceptable range.

3. **Database Integration**:
   - Uses SQLite for efficient storage and retrieval of student names, scores, and grades.
   - Ensures unique student names are recorded to prevent duplicates.

4. **Additional Functionalities**:
   - Calculates final grades using various methods, with flexibility for future expansion.
   - Provides feedback through color-coded messages for errors, ensuring user awareness and direction.

5. **Scalable and Maintainable Design**:
   - Modular structure separates concerns across multiple Python modules.
   - Well-documented code with extensive docstrings and comments for easy understanding and future development.

## Initial Version

The initial version was a simple script that:

- Used standard input/output for data collection and display.
- Calculated grades using a basic relative grading system.
- Did not include advanced user interactions or persistent storage.

## Improvements Made

1. **Refined UI Design**:
   - Improved aesthetics with colors and styles.
   - Added functionality for using the Enter key to navigate fields.
   
2. **Enhanced Validation**:
   - Comprehensive validation for names and numeric fields.

3. **Error Handling**:
   - Introduced exception handling throughout the application.

4. **Code Refactoring**:
   - Separated logic into clear modules/classes to ensure readability and maintainability.
   - Added detailed README and inline comments for clarity.

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Desertiocaine/FinalProject1Lab2Revamped.git
   cd FinalProject1Lab2Revamped
   ```

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
   ```

4. **Run the Application**:
   Execute the main script to start the application.
   ```bash
   python main.py
     ```

## Conclusion

This project demonstrates significant growth, transforming from a basic console application to a fully-featured, interactive application. Future plans may include more grade calculation strategies and advanced data visualization techniques.

---

Feel free to adjust the content as per your specific enhancements and personal touches!

## Contributors

- Kenneth Parrack
- Farrel Aflagah
