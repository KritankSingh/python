# 🏆 KBC-Style Python Quiz Game

A simple console-based quiz game inspired by *Kaun Banega Crorepati
(KBC)*.\
The player answers multiple-choice questions, earns increasing rewards,
and loses the game upon a wrong answer.\
If all questions are answered correctly, the player becomes a
"Crorepati"! 🎉

------------------------------------------------------------------------

## 📌 Features

-   10 multiple-choice questions.
-   Prize money increases with each correct answer.
-   Ends immediately when the player gives a wrong answer.
-   If all questions are correct → Big Win message at the end!

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone or download this repository.

2.  Make sure you have **Python 3.x** installed.

3.  Open a terminal or command prompt and run:

    ``` bash
    python kbc_game.py
    ```

------------------------------------------------------------------------

## 🎮 Game Rules

1.  Each question has **4 options (1--4)**.
2.  Type the number of the correct option and press **Enter**.
3.  If your answer is correct:
    -   You win the reward for that round.
    -   Move to the next question.
4.  If your answer is wrong:
    -   Game ends immediately.
    -   You keep the prize from the **last correct question**.
5.  If you answer **all questions correctly**, you become a
    **Crorepati**! 🎉

------------------------------------------------------------------------

## 🧩 Example Gameplay

    Question: Who invented the light bulb?
    Options:  Edison
    Options:  Newton
    Options:  Einstein
    Options:  Tesla
    choose one option from 1-4: 1
    you answered the question correctly
    Reward for correctly answering this question is:  1000

If you answer everything correctly:

    🎉 Congrats you are our new corerpati 🎉

------------------------------------------------------------------------

## 📂 File Structure

    .
    ├── kbc_game.py   # Main game script
    └── README.md     # Documentation

------------------------------------------------------------------------

## 🔮 Future Enhancements (Optional Ideas)

-   Add **lifelines** (50-50, Ask the Audience, etc.).
-   Save **high scores** of players.
-   Add **timer** for each question.
-   Make it **GUI-based** using Tkinter or PyGame.

------------------------------------------------------------------------

👨‍💻 Developed as a beginner-friendly Python project.
