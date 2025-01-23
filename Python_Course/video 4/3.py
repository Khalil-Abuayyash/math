from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class CombAttractsWater(Scene):
    def construct(self):
        data = SVGMobject("data.svg")
        self.play(Create(data), run_time=2)
        self.wait(1)