import tkinter as tk
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float

WIDTH, HEIGHT = 800, 800
BACKGROUND = "black"
FOREGROUND = "#00FF00"

# Create the main window
window = tk.Tk()

# Create a canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg=BACKGROUND)
canvas.pack()

# simple 3d to 2d projection
# x = x/z
# y = y/z

def screen(p: Point) -> Point:
    # -1..1 => 0..W/H
    x = (p.x + 1)/2 * WIDTH
    y = (1 - (p.y + 1)/2) * HEIGHT
    return Point(x, y)

def point(p: Point, size=5, color=FOREGROUND) -> int:
    return canvas.create_rectangle(p.x - size/2, p.y - size/2, p.x + size, p.y + size, fill=color, outline="")

def project(p: Point, z=1.0) -> Point:
    return Point(p.x / z, p.y / z)

# draw
# point(screen(project(Point(1, 0), 100)))

FPS = 60
delta_z = 1

point1 = point(Point(0,0))  
point2 = point(Point(0,0))
point3 = point(Point(0,0))
point4 = point(Point(0,0))

p1 = screen(project(Point(0.5,0.5), 1 + delta_z))
p2 = screen(project(Point(-0.5, 0.5), 1 + delta_z))
p3 = screen(project(Point(0.5, -0.5), 1 + delta_z))
p4 = screen(project(Point(-0.5, -0.5), 1 + delta_z))

canvas.coords(point1, p1.x - 5, p1.y - 5, p1.x + 5, p1.y + 5)
canvas.coords(point2, p2.x - 5, p2.y - 5, p2.x + 5, p2.y + 5)
canvas.coords(point3, p3.x - 5, p3.y - 5, p3.x + 5, p3.y + 5)
canvas.coords(point4, p4.x - 5, p4.y - 5, p4.x + 5, p4.y + 5)

def animate():
    global delta_z
    delta_time = 1 / FPS
    delta_z += 1 * delta_time
    # Update positions of existing points
    p1 = screen(project(Point(0.5, 0.5), 1 + delta_z))
    p2 = screen(project(Point(-0.5, 0.5), 1 + delta_z))
    p3 = screen(project(Point(0.5, -0.5), 1 + delta_z))
    p4 = screen(project(Point(-0.5, -0.5), 1 + delta_z))

    canvas.coords(point1, p1.x - 5, p1.y - 5, p1.x + 5, p1.y + 5)
    canvas.coords(point2, p2.x - 5, p2.y - 5, p2.x + 5, p2.y + 5)
    canvas.coords(point3, p3.x - 5, p3.y - 5, p3.x + 5, p3.y + 5)
    canvas.coords(point4, p4.x - 5, p4.y - 5, p4.x + 5, p4.y + 5)

    window.after(int(1000 / FPS), animate)  # Schedule the next frame

# animate()  # Start the animation

# Start the Tkinter event loop
window.mainloop()

