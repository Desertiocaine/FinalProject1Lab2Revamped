import tkinter as tk
from tkinter import messagebox

class StudentGradeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Grades")
        self.root.configure(bg='#f0f0f0')

        # Styling configuration
        style = {
            'font': ('Helvetica', 12),
            'padx': 10,
            'pady': 5,
            'bg': '#f0f0f0'
        }

        # Student Name
        tk.Label(self.root, text="Student Name:", **style).pack(anchor='w', padx=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(fill='x', pady=5, padx=10)
        self.name_entry.bind("<Return>", self.focus_next_widget)

        # Number of Scores
        tk.Label(self.root, text="Number of Scores:", **style).pack(anchor='w', padx=10)
        self.scores_entry = tk.Entry(self.root)
        self.scores_entry.pack(fill='x', pady=5, padx=10)
        self.scores_entry.bind("<FocusOut>", self.create_score_entries)
        self.scores_entry.bind("<Return>", self.focus_next_widget)

        # Container for dynamic score entries
        self.score_entries_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.score_entries_frame.pack(pady=5, padx=10, fill='x')

        # Submit Button
        submit_button = tk.Button(self.root, text="SUBMIT", command=self.submit, bg='#4CAF50', fg='white')
        submit_button.pack(pady=10, padx=10)

        self.root.mainloop()

    def create_score_entries(self, event=None):
        # Clean up existing score entries
        for widget in self.score_entries_frame.winfo_children():
            widget.destroy()

        try:
            num_scores = int(self.scores_entry.get())
            if 1 <= num_scores <= 4:
                for i in range(num_scores):
                    tk.Label(self.score_entries_frame, text=f"Score {i+1}:", bg='#f0f0f0').pack(anchor='w')
                    entry = tk.Entry(self.score_entries_frame)
                    entry.bind("<Return>", self.focus_next_widget)
                    entry.pack(fill='x', pady=2)
                self.root.geometry("")
        except ValueError:
            self.show_error("Please enter a valid number of scores.", 'gold')

    def focus_next_widget(self, event=None):
        event.widget.tk_focusNext().focus()
        return "break"

    def submit(self):
        student_name = self.name_entry.get().strip()
        if not student_name or not all(part.isalpha() for part in student_name.split()):
            self.show_error("Name must contain only letters and spaces.", 'lightcoral')
            return

        score_values = []
        for widget in self.score_entries_frame.winfo_children():
            if isinstance(widget, tk.Entry):
                score_str = widget.get().strip()
                if not score_str.isdigit() or not (0 <= int(score_str) <= 100):
                    self.show_error("Scores must be numbers between 0 and 100.", 'gold')
                    return
                score_values.append(int(score_str))

        if score_values:
            messagebox.showinfo("Success", f"Submitted: {student_name} with scores {score_values}")
        else:
            self.show_error("Please enter valid scores.", 'lightcoral')

    def show_error(self, message, bg_color):
        error_window = tk.Toplevel(self.root)
        error_window.configure(bg=bg_color)
        tk.Label(error_window, text=message, bg=bg_color, font=('Helvetica', 12)).pack(padx=20, pady=10)
        tk.Button(error_window, text="OK", command=error_window.destroy, bg='#4CAF50', fg='white').pack(pady=5)

# Run the application
if __name__ == '__main__':
    StudentGradeApp()