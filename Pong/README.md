
# Pong Game in Python

## Overview
This project is a Pong game implemented using Python and the Pygame library. The game can be played in two modes:
- **2-Player Mode**: Two players control paddles and compete to score points.
- **AI Mode**: A player competes against an AI-controlled opponent with adjustable difficulty levels.

## Features
- **Two Game Modes**: Single-player against AI or two-player local multiplayer.
- **Adjustable AI Difficulty**: The AI opponent can be set to different difficulty levels: Easy, Medium, or Hard.
- **Dynamic Scoring System**: The game keeps track of the score, and the player who reaches a score of 7 wins the game.
- **Series Play**: Multiple games can be played in a series, and the first player to reach a certain number of wins (set by MAX_GAMES) wins the series.
- **Control Instructions**: Clear and intuitive controls for both players and easy switching between game modes.
- **Sound Effects**: Custom sounds for paddle hits and score events.

## Controls
- **Player 1 (Paddle 1)**: Use **W** to move up and **S** to move down.
- **Player 2 (Paddle 2)**: Use the **Up Arrow** to move up and the **Down Arrow** to move down.
- **AI Mode**: The AI will automatically control the second paddle with difficulty settings.
- **Start Game**: Select game mode (AI or 2-Player) and difficulty level for AI in the main menu.
- **Restart Game**: Press **'Y'** after a game ends to play again, or **'N'** to quit the game.

## Installation
### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Pygame**: Install the Pygame library using pip:
```bash
pip install pygame
```
- **paddle_hit.mp3** & **score.mp3**: The soundbites used in this project. (Copyright Free)

### Running the Game
1. Clone the repository or download the `pong_game.py` file.
2. Navigate to the directory where the file is located.
3. Run the game using Python:

```bash
python pong_game.py
```

## Customizing the Game
- **Max Games**: The number of games in the series can be customized by changing the `MAX_GAMES` variable in the code.
- **AI Difficulty**: The AI difficulty can be adjusted to Easy, Medium, or Hard in the `select_mode` function.
- **Sounds**: Custom sound effects were added by placing audio files in the appropriate directory and linking them in the code.

## Code Structure
- **Main Game Loop**: Handles user input, updates game state, and renders the game to the screen.
- **Game Mechanics**: Includes paddle movement, ball physics, score tracking, and collision detection.
- **AI Behavior**: Adjusts the AI paddle movement based on the difficulty level (Easy, Medium, or Hard).
- **Winner Display**: Displays the winner of the series and prompts the user to play again.

## Skills Demonstrated:
- Game Development with Pygame:
  - Handling basic game loops, sprite rendering, and collision detection.
  - Implementing physics for ball movement and paddle collisions.
  - Creating a playable game using a graphical interface.

- Artificial Intelligence (AI): 
   - Implementing AI with varying difficulty levels based on reaction time and paddle speed.
   - Adapting AI behavior based on randomness and the distance between the ball and paddle.

- Game Design:
  - Designing the logic to handle scoring, reset conditions, and the concept of series.
  - Adding features such as difficulty levels and a re-playable series mode.

- User Input Handling:
  - Reading user input from the keyboard to control the paddles in both 2-player and AI modes.
  - Allowing the user to restart or quit the game via the "Y" and "N" options after a series ends.

- Sound Integration:
  - Incorporating sound effects for paddle hits and scoring events to enhance the user experience.

- State Management:
  - Managing game state transitions (e.g., from playing to game over, displaying winner, resetting scores).


## License
This project is licensed under the MIT License.

