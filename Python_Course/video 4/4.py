from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

# config.background_color = YELLOW

class CombAttractsWater(Scene):
    def construct(self):

        container1 = SVGMobject("container1.svg").shift(UP * 4).shift(RIGHT * 1)
        self.play(Create(container1), run_time=1)
        string = Text("String", font_size=52, color=GREEN).next_to(container1, LEFT * 2)
        self.play(Write(string))

        container2 = SVGMobject("container2.svg").next_to(container1, DOWN * 1)
        self.play(Create(container2), run_time=1)
        integer = Text("integer", font_size=52, color=GREEN).next_to(container2, LEFT * 2)
        self.play(Write(integer))

        container3 = SVGMobject("container3.svg").next_to(container2, DOWN * 1)
        self.play(Create(container3), run_time=1)
        decimal = Text("decimal", font_size=52, color=GREEN).next_to(container3, LEFT * 2)
        self.play(Write(decimal))

        container4 = SVGMobject("container4.svg").next_to(container3, DOWN * 1)
        self.play(Create(container4), run_time=1)
        boolean = Text("boolean", font_size=52, color=GREEN).next_to(container4, LEFT * 2)
        self.play(Write(boolean))

        self.wait(1)