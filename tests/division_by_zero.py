from manim import *

print("Script is running!")  # Debugging line

class DrawCircle(Scene):
    def construct(self):
        print("DrawCircle class is being constructed!")  # Debugging line
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        self.wait(1)
