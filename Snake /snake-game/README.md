# Snake Game

A simple Snake game implemented using the Pygame library. This project features a clean and modular structure, separating the snake's movement logic from the rendering loop.

## Project Structure

```
snake-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game
│   │   ├── __init__.py  # Game package marker
│   │   ├── snake.py     # Snake class for managing snake properties and movement
│   │   ├── food.py      # Food class for generating food items
│   │   └── game_logic.py # Game logic functions for managing game state
│   └── utils
│       ├── __init__.py  # Utils package marker
│       └── settings.py   # Configuration settings for the game
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to have Python and Pygame installed. You can install the required dependencies using:

```
pip install -r requirements.txt
```

## How to Run

To start the game, run the following command in your terminal:

```
python src/main.py
```

## Features

- Classic Snake gameplay
- Modular code structure
- Easy to extend and modify

Feel free to contribute to the project or modify it for your own use!