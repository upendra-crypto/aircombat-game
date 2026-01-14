# ✈️ Aircraft Shooter Game (Python Turtle)

A classic **2D aircraft shooter game** built using **Python Turtle**, where the player controls an aircraft, shoots incoming enemies, and tries to achieve the highest score possible.

This project focuses on **game logic, collision detection, event-driven programming, and clean code structure**.

---

## 🎮 Gameplay Overview

* Control an aircraft at the bottom of the screen
* Shoot bullets to destroy enemy aircraft
* Enemies spawn continuously from the top
* Score increases when enemies are destroyed
* Game ends when an enemy collides with the player
* High score is saved and persists across runs

---

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics**
* **winsound** (for sound effects – Windows)

---

## 🚀 Features

* Smooth aircraft movement using keyboard controls
* Bullet firing mechanism
* Continuous enemy spawning
* Bullet–enemy collision detection
* Player–enemy collision (Game Over)
* Score and **persistent high score system**
* Sound effects for shooting and collisions
* Proper game loop using `ontimer()` (no lag)

---

## 🎮 Controls

| Key            | Action              |
| -------------- | ------------------- |
| ⬅️ Left Arrow  | Move aircraft left  |
| ➡️ Right Arrow | Move aircraft right |
| Space          | Fire bullet         |

---

## 📁 Project Structure

```
aircraft_game/
│
├── main.py               # Main game loop and logic
├── aircraft_manager.py   # Player aircraft class
├── bullets.py            # Bullet class
├── enemy.py              # Enemy aircraft class
├── scoreboard.py         # Score & high score handling
├── high_score.txt        # Stores highest score
```

---

## ▶️ How to Run the Game

1. Make sure **Python 3** is installed
2. Clone this repository:

   ```bash
   git clone <your-repo-link>
   ```
3. Navigate to the project folder:

   ```bash
   cd aircraft_game
   ```
4. Run the game:

   ```bash
   python main.py
   ```

> ⚠️ Note: `winsound` works on **Windows only**.

---

## 🧠 What I Learned

* Event-driven programming using Turtle
* Managing multiple moving objects with lists
* Collision detection using distance calculations
* Building a smooth game loop with `ontimer()`
* Structuring a Python project into multiple modules
* Saving and reading data from files (high score)

---

## 🔮 Future Improvements

* Difficulty scaling based on score
* Lives system instead of instant game over
* Different enemy types
* Restart option
* Custom sprites and animations

---

## 📌 About This Project

This project was built as part of my **Python learning journey**, after creating classic games like **Pong** and **Snake**, to explore more advanced game mechanics.

---

