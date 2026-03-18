import matplotlib.pyplot as plt
import numpy as np

#Constants
g = 9.81
cd = 0.5
rho = 1.225
A = 0.3

#Rocket parameters
mass = int(input("Enter the mass of the rocket (kg): "))
thrust = int(input("Enter the thrust of the rocket (N): "))

#Time step
dt = 0.1
time = 0
height = 0
velocity = 0

times = []
heights = []

while height >= 0 and time < 200:
    #Calculate forces
    weight = mass * g
    drag = 0.5 * cd * rho * A * velocity * abs(velocity)
    net_force = thrust - weight - drag
    
    #Update velocity and height
    acceleration = net_force / mass
    velocity += acceleration * dt
    height += velocity * dt
    
    #Update time and store data
    time += dt
    times.append(time)
    heights.append(height)

#Plotting the results
plt.plot(times, heights)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Rocket Simulation')
plt.grid(True)
plt.show()