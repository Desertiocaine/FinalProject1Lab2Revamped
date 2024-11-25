from typing import List
import tkinter as tk
from tkinter import messagebox

def display_grades(scores: List[int], grades: List[str]) -> None:
    """
    Display each student's scores and corresponding grades.

    Args:
        scores (List[int]): List of student scores.
        grades (List[str]): Corresponding grades for each score.
    """
    # Create the main application window
    root = tk.Tk()
    root.title("Student Grades")

    # Text widget to display scores and grades
    text = tk.Text(root, width=40, height=10)
    text.pack()

    # Insert each student's data into the text widget
    for i, (score, grade) in enumerate(zip(scores, grades), start=1):
        text.insert(tk.END, f"Student {i}: Score = {score}, Grade = {grade}\n")

    # Handle window close event with confirmation
    def on_exit():
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_exit)
    root.mainloop()