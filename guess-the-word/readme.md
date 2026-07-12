# Guess The Word (Python)

A terminal-based **Word Guessing Game** inspired by Wordle, built using **Python**. Test your vocabulary by guessing randomly generated English words with the help of color-coded hints.

---

## Features

- Four difficulty levels:
  - Easy (5-letter words)
  - Medium (6-letter words)
  - Hard (8-letter words)
  - Extreme (8-letter words with only 8 attempts)

- Color-coded feedback:
  - 🟩 Green – Correct letter in the correct position
  - 🟨 Yellow – Letter exists in the word but is in the wrong position
  - 🟥 Red – Letter does not exist in the word

-  Random word generation using the `random-word` package

-  Simple and interactive terminal interface

---

## Technologies Used

- Python 3
- random-word
- colorama

---

## Installation

Clone this repository:

```bash
git clone https://github.com/your-username/guess-the-word.git
```

Move into the project folder:

```bash
cd guess-the-word
```

Install the required packages:

```bash
pip install random-word colorama
```

Run the program:

```bash
python main.py
```

---

## Project Structure

```
Guess-The-Word/
│
├── main.py
├── README.md
└── screenshots/
```

---

## How to Play

1. Run the program.
2. Select a difficulty level.
3. Enter a word of the required length.
4. Use the colored hints to guess the correct word.

### Hint Meaning

| Color | Meaning |
|--------|---------|
| 🟩 Green | Correct letter in the correct position |
| 🟨 Yellow | Correct letter, wrong position |
| 🟥 Red | Letter is not present in the word |

---

## Future Improvements

Some features planned for future updates:

- Input validation using a real English dictionary
- Hint system
- Score tracking
- Statistics (Wins/Losses)
- Timer mode
- Save game progress
- GUI version using Tkinter
- Multiplayer mode

---

## Screenshots

Add screenshots of your game inside the **screenshots/** folder and display them here.

Example:

```
screenshots/
├── menu.png
├── gameplay.png
└── extreme-mode.png
```

---

## License

This project is created for learning and educational purposes.

---

## Author

**Krish**

Computer Science Engineering Student

Always learning, building, and improving through projects.

---
Future updates comming soon...
---



---
Updates after first version
---

## Current Features

- Multiple game modes:
  - Easy (5-letter words)
  - Medium (6-letter words)
  - Hard (8-letter words)
  - Extreme Mode (limited attempts)
- Timer Mode with multiple time limits
- Surprise Mode that randomly selects a game mode
- Two Player Mode
- Match History that saves previous game results
- Color-coded feedback:
  - 🟩 Green – Correct letter in the correct position
  - 🟨 Yellow – Correct letter in the wrong position
  - 🟥 Red – Letter not present in the word
- Progressive hint system for longer games
- Score system based on the number of attempts
- Custom word length support in Timer Mode
- Simple and interactive command-line interface

---

## Future Improvements

- Player statistics (games played, wins, average attempts, etc.)
- Highest score leaderboard
- Save and display personal best scores
- Validate guesses using a proper English dictionary
- More game modes and challenges
- Enhanced multiplayer experience
- Better input validation and error handling
- Improved terminal interface and animations
- Difficulty progression and achievements
- Additional gameplay features as I continue learning Python
