import tkinter as tk
from math import cos, sin, pi
from time import localtime

def update_time():
    current_time = localtime()
    hours, minutes, seconds = current_time.tm_hour, current_time.tm_min, current_time.tm_sec

    draw_clock_hands(hours, minutes, seconds)
    canvas.after(1000, update_time)

def draw_clock_outline():
    
    canvas.create_oval(WIDTH/2 - 120, HEIGHT/2 - 120, WIDTH/2 + 120, HEIGHT/2 + 120, width=2)
 
    for i in range(12):
        angle = pi / 6 * i
        x1 = WIDTH / 2 + 90 * cos(angle)
        y1 = HEIGHT / 2 - 90 * sin(angle)
        x2 = WIDTH / 2 + 100 * cos(angle)
        y2 = HEIGHT / 2 - 100 * sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=2)

    for i in range(60):
        angle = pi / 30 * i
        x1 = WIDTH / 2 + 95 * cos(angle)
        y1 = HEIGHT / 2 - 95 * sin(angle)
        x2 = WIDTH / 2 + 100 * cos(angle)
        y2 = HEIGHT / 2 - 100 * sin(angle)
        canvas.create_line(x1, y1, x2, y2, width=1)

def draw_hand(angle, length, color, width):
    x = WIDTH / 2 + length * cos(angle)
    y = HEIGHT / 2 - length * sin(angle)
    canvas.create_line(WIDTH / 2, HEIGHT / 2, x, y, fill=color, width=width, tags="hands")

def draw_clock_hands(hours, minutes, seconds):
    canvas.delete("hands")

    hour_angle = pi / 2 - hours % 12 * (pi / 6) - minutes % 60 * (pi / 360)
    draw_hand(hour_angle, 50, "blue", 4)

    minute_angle = pi / 2 - minutes % 60 * (pi / 30) - seconds % 60 * (pi / 1800)
    draw_hand(minute_angle, 80, "green", 2)

    second_angle = pi / 2 - seconds % 60 * (pi / 30)
    draw_hand(second_angle, 100, "red", 1)

root = tk.Tk()
root.title("Analog Clock with Hands")

WIDTH, HEIGHT = 400, 400

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

draw_clock_outline()

update_time()

root.mainloop()