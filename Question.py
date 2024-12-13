from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Question(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Find the natural domain and \\ graph the functions in Exercises 15-20", font_size=50).set_color(BLUE)
        
        
        self.play(Write(title))
        self.wait(4)  # Wait to match narration for the title
        