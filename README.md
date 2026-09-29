# Python Learning Hub

A desktop app for learning and practicing Python fundamentals. It includes an interactive flashcard deck and a multiple-choice quiz, built with Python's Tkinter GUI toolkit.

## Features

- Review 10 Python flashcards, flip each card to reveal its answer, and move between cards.
- Take a 20-question multiple-choice quiz.
- Navigate directly to any question, skip questions, and mark questions for review.
- View your score and review either the correct answers or your attempted answers after finishing.

Quiz scoring: correct answers earn 4 points, incorrect answers lose 1 point, and unanswered questions earn 0 points. The maximum score is 80.

## Requirements

- Python 3
- Tkinter, included with most standard Python installations

On some Linux distributions, Tkinter must be installed separately (for example, with the `python3-tk` package).

## Run

From the project directory, run:

```powershell
python dih.py
```

On Windows, you can use `py dih.py` if the `python` command is not available.

## Project Structure

```text
dih.py       Application and quiz/flashcard data
README.md    Project documentation
```