from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PendulumScene(Scene):
    def construct(self):
        pendulum = Line(ORIGIN, 2*DOWN).rotate(PI/6)
        bob = Dot(pendulum.get_end(), color=RED)
        pivot = Dot(pendulum.get_start())
        self.add(pendulum, bob, pivot)
        p = VGroup(pendulum, bob)

        count = 0
        while count < 20:
            self.play(Rotate(p, angle=-PI/3, about_point=pivot.get_center(), run_time=2, rate_func=there_and_back))
            count += 1