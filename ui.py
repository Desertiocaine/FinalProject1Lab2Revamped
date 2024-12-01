from typing import List
import tkinter as tk
from tkinter import messagebox

def display_grades(scores: List[int], grades: List[str]) -> None:
    """
    Display each student's scores and corresponding grades using a Tkinter GUI.

    Args:
        scores (List[int]): List of student scores.
        grades (List[str]): Corresponding grades for each score.
    """
    # Create the main application window
    root = tk.Tk()
    root.title("Student Grades")  # Set window title

    # Create a text widget with custom font and background color
    text = tk.Text(root, width=40, height=10, font=("Helvetica", 12), bg="#e0f7da")
    text.pack()  # Add the text widget to the window

    # Insert each student's data into the text widget
    for i, (score, grade) in enumerate(zip(scores, grades), start=1):
        text.insert(tk.END, f"Student {i}: Score = {score}, Grade = {grade}\n")

    def on_exit():
        """
        Handle window close event with confirmation.
        """
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            root.destroy()  # Close the window

    # Bind the on_exit function to the window close event
    root.protocol("WM_DELETE_WINDOW", on_exit)

    root.mainloop()  # Start the application loop