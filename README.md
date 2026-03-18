# 🚀 Rocket Flight Simulation (Python)

## 📌 Overview
This project simulates the vertical motion of a rocket using basic physics principles. It considers **thrust, gravity, and air resistance (drag)** to compute the rocket's height over time.

The simulation numerically updates velocity and position and visualizes the trajectory using a graph.

---

## ⚙️ Features

- Simulates 1D vertical rocket motion
- Includes:
  - Thrust force
  - Gravitational force
  - Air drag
- Uses numerical integration (Euler method)
- Real-time user input for rocket parameters
- Graphical output using matplotlib

---

## 🧠 Physics Behind the Simulation

### Forces Acting on the Rocket

- **Thrust (T)** → Upward force
- **Weight (mg)** → Downward force
- **Drag (D)** → Opposes motion

### Drag Equation
D = 0.5 × Cd × ρ × A × v²

### Net Force
F = T - mg - D

### Motion Equations
- acceleration = F / m  
- velocity = velocity + acceleration × dt  
- height = height + velocity × dt  

---

## 📂 Project Structure
