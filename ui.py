import tkinter as tk
from tkinter import messagebox
import re
from database import DatabaseHandler
from grades import calculate_final_grade

class StudentGradeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Grade App")
        self.center_window()
        self.create_widgets()
        self.score_entries = []
        self.score_labels = []  # Store references to score labels
        self.db = DatabaseHandler()  # Initialize the database handler

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')

    def create_widgets(self):
        # Add labels and entries for first name, last name, and student ID
        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name_label.pack(pady=5, padx=10, anchor='w')

        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack(pady=5, padx=10, fill='x')

        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name_label.pack(pady=5, padx=10, anchor='w')

        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack(pady=5, padx=10, fill='x')

        self.student_id_label = tk.Label(self.root, text="Student ID:")
        self.student_id_label.pack(pady=5, padx=10, anchor='w')

        self.student_id_entry = tk.Entry(self.root)
        self.student_id_entry.pack(pady=5, padx=10, fill='x')

        # Existing widgets for scores
        self.scores_label = tk.Label(self.root, text="Number of Scores:")
        self.scores_label.pack(pady=5, padx=10, anchor='w')

        self.scores_entry = tk.Entry(self.root)
        self.scores_entry.pack(pady=5, padx=10, fill='x')

        self.create_scores_button = tk.Button(self.root, text="Create Score Fields", command=self.create_score_fields, bg="#add8e6", font=("Helvetica", 10, "bold"))
        self.create_scores_button.pack(pady=10, padx=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit, bg="green")
        self.submit_button.pack(pady=10, padx=10)
        self.submit_button.pack_forget()  # Hide the submit button initially

    def create_score_fields(self):
        # Validate number of scores
        try:
            num_scores = int(self.scores_entry.get())
            if num_scores < 1 or num_scores > 5:
                raise ValueError
        except ValueError:
            self.show_error("Invalid number of scores. Enter a number between 1 and 5.", "light blue")
            return

        # Clear previous score entries and labels
        for label in self.score_labels:
            label.destroy()
        for entry in self.score_entries:
            entry.destroy()
        self.score_labels = []
        self.score_entries = []

        # Create new score entries
        for i in range(num_scores):
            label = tk.Label(self.root, text=f"Score {i + 1}:")
            label.pack(pady=5, padx=10, anchor='w')
            entry = tk.Entry(self.root)
            entry.pack(pady=5, padx=10, fill='x')
            self.score_labels.append(label)
            self.score_entries.append(entry)

        self.submit_button.pack(pady=10, padx=10)  # Show the submit button

    def submit(self):
        # Validate first name, last name, and student ID
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        student_id = self.student_id_entry.get().strip()

        if not re.match(r"^[A-Za-z\s]+$", first_name) or not re.match(r"^[A-Za-z\s]+$", last_name):
            self.show_error("Invalid name. Only letters and spaces are allowed.", "red")
            return

        if not student_id.isdigit() or not (10000 <= int(student_id) <= 99999):
            self.show_error("Student ID must be a number between 10000 and 99999.", "red")
            return

        # Validate scores
        scores = []
        for entry in self.score_entries:
            try:
                score = int(entry.get())
                if score < 0 or score > 100:
                    raise ValueError
                scores.append(score)
            except ValueError:
                self.show_error("Invalid score. Enter a number between 0 and 100.", "light blue")
                return

        # Calculate final grade and letter grade
        final_grade, letter_grade = calculate_final_grade(scores)

        # Insert data into the database
        try:
            self.db.add_student(first_name, last_name, student_id, scores, final_grade, letter_grade)
            messagebox.showinfo("Success", f"Student {first_name} {last_name} submitted successfully!")
        except sqlite3.IntegrityError:
            self.show_error("Student ID already exists. Please use a unique ID.", "red")
            return

        # Clear all fields after successful submission
        self.clear_fields()

    def show_error(self, message, bg_color):
        messagebox.showerror("Error", message)
        self.root.configure(bg=bg_color)

    def clear_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.student_id_entry.delete(0, tk.END)
        self.scores_entry.delete(0, tk.END)
        for label in self.score_labels:
            label.destroy()  # Destroy the label widgets
        for entry in self.score_entries:
            entry.destroy()  # Destroy the entry widgets
        self.submit_button.pack_forget()  # Hide the submit button again
        self.score_labels = []  # Clear the list of score labels
        self.score_entries = []  # Clear the list of score entries

    def get_student_data(self):
        """
        Retrieve the student data from the UI.
        """
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        student_id = self.student_id_entry.get().strip()
        scores = [int(entry.get()) for entry in self.score_entries]
        return first_name, last_name, student_id, scores

    def display_grades(self, stored_data):
        """
        Display the stored student grades in a message box.
        """
        grades_message = "\n".join([f"{record[0]} {record[1]} (ID: {record[2]}): Final Grade: {record[4]}, Letter Grade: {record[5]}" for record in stored_data])
        messagebox.showinfo("Stored Grades", grades_message)

if __name__ == "__main__":
    app = StudentGradeApp()
    app.root.mainloop()