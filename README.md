# Tetris Game

A simple Tetris implementation using Python and Pygame.

## Description
This project is a classic Tetris game built with Python's Pygame library. It features all standard Tetris gameplay mechanics including piece movement, rotation, line clearing, and score tracking.

## Installation

### Prerequisites
- Python 3.12 or higher
- Pygame library

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tetris-python.git
   cd tetris-python
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play
1. Run the game:
   ```bash
   python3 tetris.py
   ```

2. Press Enter to start a new game when the game over screen appears.

## Controls
- **Left Arrow**: Move piece left
- **Right Arrow**: Move piece right
- **Down Arrow**: Move piece down faster
- **Space**: Rotate piece clockwise
- **Close Window**: Quit game

## Project Structure
- `tetris.py`: Main entry point, handles game loop and user input
- `game.py`: Core game logic and rendering
- `piece.py`: Tetromino piece definitions and behavior
- `requirements.txt`: Project dependencies

## License
This project is open source and available under the MIT License.