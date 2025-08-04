# 🐍 Snake Game using Turtle 🐢

A retro-style **Snake Game** built with Python's `turtle` module. Eat poop, grow longer, and avoid hitting walls or yourself. One bite of the wall—or your tail—and it's game over!

![Python](https://img.shields.io/badge/Made%20With-Python3-blue?style=flat-square)
![Game](https://img.shields.io/badge/Type-Arcade%20Game-green?style=flat-square)
![Difficulty](https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square)

---

## 🎮 Game Description

In **Snake Game**, you control a snake that moves around the screen eating randomly placed poop. Every time it eats, it grows in length. The challenge is to keep it alive as long as possible without:

- Crashing into the screen borders 🚫
- Biting its own tail 🐍☠️

---

---

## 🚀 Features

- Fully functioning Snake game with score tracking
- Custom window title and background color
- Responsive controls (Arrow keys)
- Collision detection with food, walls, and tail
- Fun visual growth of the snake
- Clean separation of logic across classes (`Snake`, `Food`, `Score`)

---

## 🕹 Controls

Use the arrow keys to control the snake:

- 🔼 Up Arrow — Move Up  
- 🔽 Down Arrow — Move Down  
- ◀️ Left Arrow — Move Left  
- ▶️ Right Arrow — Move Right  

---

## 🍔 Gameplay Logic

- Snake eats poop placed randomly on the screen.
- Each poop increases the snake's length and the score.
- Hitting the wall or yourself ends the game.
- The score is displayed and updated in real time.
- On game over, a message is shown.

---

## 📦 Requirements

- Python 3.x
- No external dependencies (uses built-in `turtle`, `time`, and `random`)

---

## ▶️ How to Run

1. Clone or download this repository.
2. Make sure the files `snake.py`, `food.py`, and `scoreboard.py` are in the same folder.
3. Run the game:

```bash
python main.py

