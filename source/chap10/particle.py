import tkinter as tk
import random

class Particle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.size = random.randint(3, 10)
        self.color = self.random_color()
    def random_color(self):
        return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def draw(self):
        x1, y1 = self.x - self.size, self.y - self.size
        x2, y2 = self.x + self.size, self.y + self.size
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

class ParticleSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Particle System Animation")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()
        self.particles = []
        self.create_particles()
        self.animate_particles()
    def create_particles(self):
        for _ in range(100):
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            particle = Particle(self.canvas, x, y)
            self.particles.append(particle)
    def animate_particles(self):
        self.canvas.delete("all")
        for particle in self.particles:
            particle.move()
            particle.draw()
        self.root.after(50, self.animate_particles)

root = tk.Tk()
app = ParticleSystemApp(root)
root.mainloop()
