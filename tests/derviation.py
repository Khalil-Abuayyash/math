from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class EquationScene(Scene):
    def construct(self):
        equation = MathTex("f(x) = x^2 + 2x + 1")
        self.play(Write(equation))
        self.wait()

        derivation = MathTex("f'(x) = 2x + 2")
        self.play(Transform(equation, derivation))
        self.wait()
