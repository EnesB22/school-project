import tkinter as tk
from tkinter import messagebox

questions = [
    ("What is 5 + 5?", 10),
    ("What is 8 * 3?", 24),
    ("What is 15 - 7?", 8),
    ("What is 12 + 9?", 21),
    ("What is 6 * 4?", 24),
    ("What is 20 - 11?", 9),
    ("What is 18 + 7?", 25),
    ("What is 9 * 5?", 45),
    ("What is 14 - 6?", 8),
    ("What is 11 + 8?", 19),
    ("What is 7 * 3?", 21),
    ("What is 25 - 13?", 12),
    ("What is 16 + 6?", 22),
    ("What is 10 * 4?", 40),
    ("What is 22 - 15?", 7),
    ("What is 13 + 9?", 22),
    ("What is 8 * 7?", 56),
    ("What is 19 - 11?", 8),
    ("What is 15 + 8?", 23),
    ("What is 6 * 6?", 36),
    ("What is 21 - 14?", 7),
    ("What is 17 + 5?", 22),
    ("What is 9 * 6?", 54),
    ("What is 24 - 18?", 6),
    ("What is 14 + 7?", 21),
    ("What is 11 * 4?", 44),
    ("What is 28 - 15?", 13),
    ("What is 18 + 6?", 24),
    ("What is 10 * 5?", 50),
    # Add more questions here...
]

class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Quiz")

        self.question_index = 0

        self.question_label = tk.Label(master, text="", font=("Arial", 18))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.question_index < len(questions):
            question_text = questions[self.question_index][0]
            self.question_label.config(text=question_text)
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_game_completed()

    def check_answer(self):
        user_answer = self.answer_entry.get()

        if user_answer.isdigit():
            user_answer = int(user_answer)
            correct_answer = questions[self.question_index][1]

            if user_answer == correct_answer:
                messagebox.showinfo("Correct", "Great job! Your answer is correct.")
                self.question_index += 1
                self.load_question()
            else:
                messagebox.showerror("Incorrect", "Oops! Your answer is incorrect. Game over.")
                self.master.destroy()
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def show_game_completed(self):
        messagebox.showinfo("Game Completed", "Congratulations! You completed the game.")
        self.master.destroy()

def main():
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

