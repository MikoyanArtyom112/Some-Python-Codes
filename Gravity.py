import pygame
import sys
import math

# Constants
G = 0.1  # Gravitational constant
DT = 0.1  # Time step

# Colors
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Light Blue color
GRID_COLOR = (50, 50, 50)  # Color of the grid lines

# Ball class
class Ball:
    def __init__(self, x, y, radius, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.vx = 0  # Initial velocity in x direction
        self.vy = 0  # Initial velocity in y direction

    def update_position(self):
        self.x += self.vx * DT
        self.y += self.vy * DT

    def apply_gravity(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        force = (G * self.mass * other.mass) / (distance**2)
        angle = math.atan2(dy, dx)

        # Update velocities
        self.vx += force * math.cos(angle) / self.mass * DT
        self.vy += force * math.sin(angle) / self.mass * DT

# Create planets with different distances and moments of circulation
central_planet = Ball(400, 300, 20, 1000)
planets = [
    Ball(400 + 100, 300, 10, 500),  # Planet closer to the center
    Ball(400 + 200, 300, 15, 800),  # Planet in between
    Ball(400 + 300, 300, 12, 600)   # Planet farther from the center
]

# Create a Pygame window
pygame.init()
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravitational Simulation")

# Main loop
clock = pygame.time.Clock()
running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravitational forces
    for planet in planets:
        planet.apply_gravity(central_planet)

    # Update planet positions
    central_planet.update_position()
    for planet in planets:
        planet.x = central_planet.x + planet.radius * math.cos(time)
        planet.y = central_planet.y + planet.radius * math.sin(time)

    # Draw on the window
    win.fill(BLACK)

    # Draw grid lines
    grid_spacing = 50
    for x in range(0, width, grid_spacing):
        pygame.draw.line(win, GRID_COLOR, (x, 0), (x, height))
    for y in range(0, height, grid_spacing):
        pygame.draw.line(win, GRID_COLOR, (0, y), (width, y))

    # Draw central planet
    pygame.draw.circle(win, LIGHT_BLUE, (int(central_planet.x), int(central_planet.y)), central_planet.radius)

    # Draw other planets
    for planet in planets:
        pygame.draw.circle(win, LIGHT_BLUE, (int(planet.x), int(planet.y)), planet.radius)

    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)  # Adjust the frame rate if needed
    time += 0.01  # Increment time for circular motion

pygame.quit()
sys.exit()
