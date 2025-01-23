from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PythonSnakeAnimation(Scene):
    def construct(self):

        # Animate the words "Simple, Flexible, Popular"
        simple_text = Text("Variables", font_size=52, color=GREEN)
        flexible_text = Text("Data Types", font_size=52, color=GREEN).next_to(simple_text, DOWN * 1)
        # popular_text = Text("Popular", font_size=48, color=GREEN)

        self.play(Write(simple_text), run_time=1.5)
        # self.wait(0.5)
        self.play(Write(flexible_text), run_time=1.5)
        self.wait(0.5)
        # self.play(Write(popular_text), run_time=1.5)
        # self.wait(2)
