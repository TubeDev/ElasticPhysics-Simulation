# 🟦 Elastic Physics Simulation

This project is a simple 2D elastic collision simulation built with `pygame-ce`. It demonstrates the fundamentals of motion, boundary interactions, and elastic collisions between blocks.

Blocks bounce around the screen, interact with the edges, and collide with each other following elastic physics rules. Users can also dynamically add, remove, and reset blocks, or adjust their velocities using the keyboard.

## ✨ Features

- **Elastic Collisions**  
Blocks transfer velocity when colliding, simulating elastic physics.

- **Dynamic Block Control**  
  - ➕ Add new blocks with `↑` (Up Arrow)
  - ➖ Remove blocks with `↓` (Down Arrow)
  - ⏹ Reset all blocks with `SPACE`

- **Velocity Adjustment**  
  - ⬅️ Decrease velocity `←` (Left Arrow)
  - ➡️ Increase velocity `→` (Right Arrow)

- **Window Resizing**  
The simulation adapts to different window sizes (`pygame.RESIZABLE`).

- **Simple & Extensible**  
Built with clean, object-oriented design (`Block` class). Easy to expand with new behaviors, shapes, or physics.

### 🎮 Controls

| Key            | Action            |
| -------------- | ----------------- |
| ⬆️ Up Arrow    | Add a new block   |
| ⬇️ Down Arrow  | Remove the last block (if more than one) |
| ⬅️ Left Arrow  | Decrease velocity of all blocks |
| ➡️ Right Arrow | Increase velocity of all blocks |
| ⏏️ SPACE       | Reset all blocks to defaults |
| ❌ Close Window | Quit simulation |

## 🛠️ Tech Highlights

- Pygame library for rendering, event handling, and collision management.
- Efficient use of `pygame.Rect` for hitbox calculations.
- Object-oriented design (`Block` class) for easy extension.
- Velocity swapping algorithm for block–block collision response.

## 🖼️ Gallery

<p align="left">
  <img width="500" alt="image" src="https://github.com/user-attachments/assets/7721a419-a7d9-4047-90a8-009ee59500fc"/>
  <img width="300" alt="Block Simulation" src=""/>
</p>

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/TubeDev/ElasticPhysics-Simulation.git
   cd ElasticPhysics-Simulation
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ```bash
   python main.py
   ```

After running the main script, a window should open displaying the simulation. Use the keyboard controls to interact with the blocks!

---

### 📜 License

This project is licensed under the [**MIT License**](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute this project as permitted by the license.

![TubeDev](https://img.shields.io/badge/TubeDev--lime)
![Python](https://img.shields.io/badge/Python--blue?logo=python&logoColor=white)
![MIT](https://img.shields.io/badge/License-MIT-gold)

<p align="left">
  <img width="500" src="https://github.com/user-attachments/assets/f5a0f154-dee7-4653-9451-caa52513573a" alt="logo" />
</p>