# Snake Water Gun

A simple command-line game built with Python — my take on the classic Rock-Paper-Scissors, but with Snake, Water, and Gun instead. This is one of my first mini projects while learning Python!

## How to Play

You play against the computer. Each round, you and the computer pick one of three options:

- **Snake** drinks **Water** → Snake wins
- **Water** short-circuits **Gun** → Water wins
- **Gun** kills **Snake** → Gun wins

If both players pick the same thing, it's a draw.

You keep playing rounds until you choose to stop, and the game keeps a running score.

## Requirements

- Python 3.x
- No external libraries needed (only uses the built-in `random` module)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/snake-water-gun.git
   cd snake-water-gun
   ```
2. Run the script:
   ```bash
   python snake_water_gun.py
   ```
3. When prompted, type your choice as `snake`, `water`, or `gun`.
4. After each round, choose `1` to keep playing or `2` to stop and see the final result.

## Example Round

```
========================================
     SNAKE  •  WATER  •  GUN
========================================

Enter your choice: snake
You:  snake
Computer:  gun
You win!
                                  You: 1  |  Computer: 0

Do you want to continue?
1. Yes
2. No
```

## Features

- Play against the computer
- Two-player mode
- Hidden player input using `getpass`
- Running scoreboard
- Main menu
- Exit confirmation
- Clean terminal interface

## Known Limitations / Ideas for Improvement

Since this is a learning project, there's room to grow:

- No input validation yet — entering something other than `snake`, `water`, or `gun` will crash the game
- Could add a "best of N rounds" mode
- Could add color output using a library like `colorama`
- Could refactor the win logic into a lookup table for clarity

## About

Built while learning Python as a hands-on way to practice loops, dictionaries, functions, and basic game logic.

## License

This project is open source and available under the [MIT License](LICENSE).
