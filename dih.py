import tkinter as tk
from tkinter import messagebox
import random

# ===================== DATA =====================

FLASHCARDS = [
    ("What is Python?", "A high-level interpreted programming language."),
    ("What is a variable?", "A name used to store data."),
    ("What is a list?", "An ordered and mutable collection."),
    ("What is a tuple?", "An ordered and immutable collection."),
    ("What is a dictionary?", "A collection of key-value pairs."),
    ("What is a function?", "A reusable block of code."),
    ("What does len() do?", "Returns the number of items."),
    ("What is a loop?", "It repeatedly executes code."),
    ("What is an if statement?", "It runs code when a condition is true."),
    ("What is an IDE?", "Integrated Development Environment.")
]

QUESTIONS = [
    ("Which keyword defines a function?", ["func", "define", "def", "function"], 2),
    ("Which type stores True or False?", ["int", "bool", "str", "float"], 1),
    ("Which symbol starts a comment?", ["//", "#", "/*", "--"], 1),
    ("Which function displays output?", ["display()", "show()", "print()", "output()"], 2),
    ("Which is mutable?", ["tuple", "string", "list", "integer"], 2),
    ("What is 2 ** 3?", ["5", "6", "8", "9"], 2),
    ("Which operator performs floor division?", ["/", "//", "%", "**"], 1),
    ("Which loop iterates through a sequence?", ["for", "repeat", "loop", "iterate"], 0),
    ("Which function gives the length of a list?", ["size()", "length()", "len()", "count()"], 2),
    ("What does IDE stand for?", [
        "Internal Development Engine",
        "Integrated Development Environment",
        "Internet Development Editor",
        "Integrated Data Environment"
    ], 1),
    ("Which stores key-value pairs?", ["List", "Tuple", "Dictionary", "Set"], 2),
    ("Which loop runs while a condition is true?", ["for", "while", "during", "repeat"], 1),
    ("Which converts a value to integer?", ["str()", "float()", "int()", "integer()"], 2),
    ("Which operator is used for exponentiation?", ["^", "**", "//", "%%"], 1),
    ("Which statement makes a decision?", ["if", "check", "when", "decide"], 0),
    ("What is the first list index?", ["0", "1", "-1", "None"], 0),
    ("Which method adds an item to a list?", ["add()", "insert()", "append()", "push()"], 2),
    ("Which keyword immediately exits a loop?", ["stop", "exit", "break", "end"], 2),
    ("Which function takes user input?", ["get()", "input()", "read()", "scan()"], 1),
    ("Which is NOT a Python data type?", ["List", "Dictionary", "Tuple", "Character"], 3)
]


# ===================== APP =====================

class QuizApp:

    def __init__(self, root):
        self.root = root
        root.title("Python Learning Hub")
        root.geometry("800x600")
        root.resizable(False, False)

        self.bg = "#080B18"
        self.panel = "#11182B"
        self.blue = "#00D9FF"
        self.purple = "#A855F7"
        self.white = "#F5F7FF"
        self.gray = "#9CA8C7"
        self.green = "#22C55E"
        self.red = "#EF4444"

        self.canvas = tk.Canvas(root, bg=self.bg, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        for _ in range(35):
            x, y = random.randrange(800), random.randrange(600)
            self.canvas.create_oval(x, y, x+3, y+3,
                                    fill=random.choice(
                                        [self.blue, self.purple, "#38BDF8"]),
                                    outline="")

        self.content = tk.Frame(root, bg=self.bg)
        self.content.place(relwidth=1, relheight=1)

        self.home()


    # ===================== HELPERS =====================

    def clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def title(self, text, size=28):
        tk.Label(
            self.content, text=text,
            font=("Arial", size, "bold"),
            fg=self.blue, bg=self.bg
        ).pack(pady=20)

    def button(self, parent, text, command, width=18):
        b = tk.Button(
            parent, text=text, command=command,
            width=width, height=2,
            font=("Arial", 10, "bold"),
            fg=self.white, bg="#17213A",
            activebackground="#293B66",
            activeforeground=self.white,
            relief="flat", cursor="hand2"
        )
        b.bind("<Enter>", lambda e: b.config(bg="#293B66"))
        b.bind("<Leave>", lambda e: b.config(bg="#17213A"))
        return b


    # ===================== HOME =====================

    def home(self):
        self.clear()

        self.title("PYTHON LEARNING HUB", 30)

        tk.Label(
            self.content,
            text="LEARN • PRACTICE • MASTER PYTHON",
            font=("Arial", 12, "bold"),
            fg=self.gray, bg=self.bg
        ).pack()

        frame = tk.Frame(self.content, bg=self.bg)
        frame.pack(pady=30)

        self.button(
            frame, "⚡ FLASHCARDS", self.flashcards
        ).pack(pady=8)

        self.button(
            frame, "🧠 START 20 QUESTION QUIZ", self.start_quiz
        ).pack(pady=8)

        self.button(
            frame, "✕ EXIT", self.root.destroy
        ).pack(pady=8)


    # ===================== FLASHCARDS =====================

    def flashcards(self):
        self.clear()
        self.title("PYTHON FLASHCARDS", 25)

        i = [0]
        flipped = [False]

        card = tk.Frame(
            self.content, bg=self.panel,
            padx=30, pady=40
        )
        card.pack(fill="both", expand=True, padx=60, pady=10)

        heading = tk.Label(
            card, font=("Arial", 18, "bold"),
            fg=self.blue, bg=self.panel
        )
        heading.pack(pady=20)

        text = tk.Label(
            card, wraplength=600,
            font=("Arial", 16),
            fg=self.white, bg=self.panel
        )
        text.pack(expand=True)

        count = tk.Label(
            self.content, fg=self.gray, bg=self.bg
        )
        count.pack()

        def update():
            q, a = FLASHCARDS[i[0]]
            heading.config(text="ANSWER" if flipped[0] else "QUESTION")
            text.config(text=a if flipped[0] else q)
            count.config(text=f"CARD {i[0]+1}/{len(FLASHCARDS)}")

        def move(n):
            i[0] = (i[0] + n) % len(FLASHCARDS)
            flipped[0] = False
            update()

        controls = tk.Frame(self.content, bg=self.bg)
        controls.pack(pady=8)

        self.button(
            controls, "← Previous",
            lambda: move(-1), 12
        ).pack(side="left", padx=3)

        self.button(
            controls, "↻ Flip",
            lambda: (flipped.__setitem__(0, not flipped[0]), update()),
            12
        ).pack(side="left", padx=3)

        self.button(
            controls, "Next →",
            lambda: move(1), 12
        ).pack(side="left", padx=3)

        self.button(
            controls, "⌂ Home",
            self.home, 12
        ).pack(side="left", padx=3)

        update()


    # ===================== QUIZ START =====================

    def start_quiz(self):
        self.index = 0
        self.answers = [None] * len(QUESTIONS)
        self.review = set()
        self.show_question()


    # ===================== QUESTION =====================

    def show_question(self):
        self.clear()

        q, options, correct = QUESTIONS[self.index]

        self.title(
            f"QUESTION {self.index+1} / {len(QUESTIONS)}",
            22
        )

        tk.Label(
            self.content,
            text="+4 Correct   •   -1 Wrong   •   0 Unanswered",
            font=("Arial", 10, "bold"),
            fg=self.gray, bg=self.bg
        ).pack()

        # Progress
        bar = tk.Frame(self.content, bg="#202B45", height=6)
        bar.pack(fill="x", padx=60, pady=12)

        tk.Frame(
            bar, bg=self.blue, height=6
        ).place(
            relwidth=(self.index + 1) / len(QUESTIONS),
            relheight=1
        )

        card = tk.Frame(
            self.content, bg=self.panel,
            padx=25, pady=20
        )
        card.pack(fill="x", padx=55, pady=10)

        tk.Label(
            card, text=q,
            wraplength=650,
            font=("Arial", 17, "bold"),
            fg=self.white, bg=self.panel
        ).pack()

        selected = tk.IntVar(
            value=-1 if self.answers[self.index] is None
            else self.answers[self.index]
        )

        for i, option in enumerate(options):
            tk.Radiobutton(
                self.content,
                text=f"{chr(65+i)}. {option}",
                variable=selected, value=i,
                font=("Arial", 12),
                fg=self.white, bg=self.bg,
                activebackground=self.bg,
                activeforeground=self.blue,
                selectcolor="#1B2744",
                anchor="w", width=48
            ).pack(pady=4)

        if self.index in self.review:
            tk.Label(
                self.content,
                text="★ MARKED FOR REVIEW",
                fg="#FBBF24", bg=self.bg,
                font=("Arial", 10, "bold")
            ).pack(pady=4)

        # ---------- Controls ----------

        controls = tk.Frame(self.content, bg=self.bg)
        controls.pack(pady=10)

        def save():
            self.answers[self.index] = (
                None if selected.get() == -1
                else selected.get()
            )

        def next_q():
            save()
            if self.index < 19:
                self.index += 1
                self.show_question()
            else:
                self.finish()

        def previous():
            save()
            if self.index:
                self.index -= 1
                self.show_question()

        def skip():
            self.answers[self.index] = None
            if self.index < 19:
                self.index += 1
                self.show_question()

        def mark():
            save()
            if self.index in self.review:
                self.review.remove(self.index)
            else:
                self.review.add(self.index)
            self.show_question()

        if self.index:
            self.button(
                controls, "← Previous",
                previous, 11
            ).pack(side="left", padx=3)

        self.button(
            controls, "★ Review",
            mark, 11
        ).pack(side="left", padx=3)

        self.button(
            controls, "Skip →",
            skip, 11
        ).pack(side="left", padx=3)

        self.button(
            controls,
            "FINISH" if self.index == 19 else "Next →",
            next_q, 11
        ).pack(side="left", padx=3)

        # ---------- Question navigation ----------

        nav = tk.Frame(self.content, bg=self.bg)
        nav.pack(pady=5)

        for i in range(20):

            if i == self.index:
                color = self.blue
            elif i in self.review:
                color = "#FBBF24"
            elif self.answers[i] is not None:
                color = self.green
            else:
                color = "#334155"

            tk.Button(
                nav, text=str(i+1),
                width=3, bg=color,
                fg=self.white, relief="flat",
                command=lambda x=i: self.jump(x)
            ).grid(
                row=i//10,
                column=i%10,
                padx=2, pady=2
            )


    def jump(self, number):
        self.index = number
        self.show_question()


    # ===================== FINISH =====================

    def finish(self):

        correct = wrong = unanswered = 0

        for i, answer in enumerate(self.answers):

            if answer is None:
                unanswered += 1

            elif answer == QUESTIONS[i][2]:
                correct += 1

            else:
                wrong += 1

        self.correct = correct
        self.wrong = wrong
        self.unanswered = unanswered
        self.score = correct * 4 - wrong

        self.results()


    # ===================== RESULTS =====================

    def results(self):
        self.clear()

        self.title("🎉 QUIZ COMPLETED!", 28)

        tk.Label(
            self.content,
            text=f"{self.score} / 80",
            font=("Arial", 40, "bold"),
            fg=self.blue, bg=self.bg
        ).pack()

        tk.Label(
            self.content,
            text="FINAL SCORE",
            font=("Arial", 11, "bold"),
            fg=self.gray, bg=self.bg
        ).pack(pady=(0, 15))

        card = tk.Frame(
            self.content, bg=self.panel,
            padx=40, pady=18
        )
        card.pack()

        for text, color in [
            (f"✓ Correct      : {self.correct}", self.green),
            (f"✕ Wrong        : {self.wrong}", self.red),
            (f"○ Unanswered   : {self.unanswered}", self.gray),
            (f"★ Score        : {self.score}", self.blue)
        ]:
            tk.Label(
                card, text=text,
                font=("Arial", 14, "bold"),
                fg=color, bg=self.panel
            ).pack(pady=4)

        bottom = tk.Frame(self.content, bg=self.bg)
        bottom.pack(fill="x", padx=35, pady=25)

        self.button(
            bottom,
            "✓ ALL CORRECT ANSWERS",
            self.correct_answers,
            22
        ).pack(side="left")

        self.button(
            bottom,
            "▣ MY ATTEMPTED ANSWERS",
            self.attempted,
            22
        ).pack(side="right")

        self.button(
            self.content, "⌂ HOME",
            self.home, 15
        ).pack()


    # ===================== ANSWER PAGE =====================

    def make_scroll_page(self, title):

        self.clear()
        self.title(title, 24)

        canvas = tk.Canvas(
            self.content, bg=self.bg,
            highlightthickness=0
        )

        scroll = tk.Scrollbar(
            self.content,
            command=canvas.yview
        )

        frame = tk.Frame(canvas, bg=self.bg)

        frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0), window=frame,
            anchor="nw", width=700
        )

        canvas.configure(
            yscrollcommand=scroll.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(35, 0)
        )

        scroll.pack(
            side="right",
            fill="y",
            padx=(0, 35)
        )

        return frame


    def correct_answers(self):

        frame = self.make_scroll_page(
            "✓ ALL CORRECT ANSWERS"
        )

        for i, (q, options, answer) in enumerate(QUESTIONS):

            box = tk.Frame(
                frame, bg=self.panel,
                padx=15, pady=10
            )
            box.pack(fill="x", pady=4)

            tk.Label(
                box,
                text=f"Q{i+1}. {q}",
                wraplength=640,
                justify="left",
                fg=self.white,
                bg=self.panel,
                font=("Arial", 10, "bold")
            ).pack(anchor="w")

            tk.Label(
                box,
                text=f"✓ {chr(65+answer)}. {options[answer]}",
                fg=self.green,
                bg=self.panel,
                font=("Arial", 10, "bold")
            ).pack(anchor="w", pady=(4, 0))

        self.button(
            self.content,
            "← BACK TO RESULTS",
            self.results, 15
        ).pack(pady=6)


    # ===================== ATTEMPTED PAGE =====================

    def attempted(self):

        frame = self.make_scroll_page(
            "▣ MY ATTEMPTED ANSWERS"
        )

        for i, (q, options, correct) in enumerate(QUESTIONS):

            box = tk.Frame(
                frame, bg=self.panel,
                padx=15, pady=10
            )
            box.pack(fill="x", pady=4)

            tk.Label(
                box,
                text=f"Q{i+1}. {q}",
                wraplength=640,
                justify="left",
                fg=self.white,
                bg=self.panel,
                font=("Arial", 10, "bold")
            ).pack(anchor="w")

            answer = self.answers[i]

            if answer is None:

                text = "○ UNANSWERED  |  0 marks"
                color = self.gray

            elif answer == correct:

                text = (
                    f"✓ Your Answer: {chr(65+answer)}. "
                    f"{options[answer]}  |  +4 marks"
                )
                color = self.green

            else:

                text = (
                    f"✕ Your Answer: {chr(65+answer)}. "
                    f"{options[answer]}  |  -1 mark"
                )
                color = self.red

            tk.Label(
                box, text=text,
                fg=color, bg=self.panel,
                font=("Arial", 10, "bold")
            ).pack(anchor="w", pady=(4, 0))

            if answer is not None and answer != correct:

                tk.Label(
                    box,
                    text=(
                        f"Correct: {chr(65+correct)}. "
                        f"{options[correct]}"
                    ),
                    fg=self.blue,
                    bg=self.panel
                ).pack(anchor="w")

        self.button(
            self.content,
            "← BACK TO RESULTS",
            self.results, 15
        ).pack(pady=6)


# ===================== RUN =====================

if __name__ == "__main__":
    root = tk.Tk()
    QuizApp(root)
    root.mainloop()