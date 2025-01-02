from manim import *

config.pixel_width = 1080
config.pixel_height = 1920 

class Stacking(Scene):
    def construct(self):
        # Create the MathTex equation
        equation = MathTex(r"h \propto \frac{1}{\sigma^2}").set(height=4)
        
        # Set color to blue
        equation.set_color(BLUE)
        
        # Position and display the equation on the screen
        self.play(Write(equation), run_time=5)
        self.wait(3)