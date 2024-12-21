from manim import *

config.pixel_width = 1080   # Set width (e.g., Full HD resolution)
config.pixel_height = 1920  # Set height

class Corners(Scene):
    def construct(self):
    # Create circles with different colors at the specified coordinates
        green = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([-6.5, 12, 0])  # Top-left
        yellow = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([-5.5, 12, 0])
        red = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to([-4.5, 12, 0])
        # yellow = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([6, 11, 0])  # Top-right
        # blue = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to([-6, -11, 0])    # Bottom-left
        # red = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([6,-11, 0])       # Bottom-right
        # center = Circle(radius=0.2, color=PURPLE, fill_opacity=1).move_to([0, 0, 0])  # Center
        
        # Add circles to the scene
        # self.play(FadeIn(green, yellow, blue, red, center))
        self.add(green, yellow, red)