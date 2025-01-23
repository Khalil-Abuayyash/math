from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PythonSnakeAnimation(Scene):
    def construct(self):
        
        text1 = Text("Integers", font_size=40, color=BLUE)
        text2 = Text("Strings", font_size=40, color=BLUE)

        snake_body = VMobject(color=GREEN)
        snake_body.set_points_smoothly([
            LEFT * 2 + UP * 4,  # Start of the snake
            UP * 2,
            UP * 1,
            UP * 0.5,
            RIGHT * 2 + UP * 0.5  # End of the snake
        ])

        # snake_head = Circle(radius=0.2, color=GREEN).move_to(snake_body.get_end())

        text1.move_to(snake_body.get_start()).shift(UP * 0.5)
        text2.move_to(snake_body.get_end()).shift(RIGHT * 0.9)

        # Animate the snake wrapping around the text
        self.play(Write(text1))
        self.play(Create(snake_body), run_time=2)
        # self.play(FadeIn(snake_head), run_time=1)
        self.play(Write(text2))

        self.wait(2)