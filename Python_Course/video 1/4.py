from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PythonSnakeAnimation(Scene):
    def construct(self):
        # Create the word "Python"
        python_text = Text("Python", font_size=72, color=BLUE)
        # self.play(Write(python_text))
        # self.wait(1)

        # snake_body = VMobject(color=GREEN)
        # snake_body.set_points_smoothly([
        #     python_text.get_left() + LEFT * 2 + UP * 0.5,  # Start of the snake
        #     python_text.get_left() + UP * 0.5,
        #     python_text.get_center() + UP * 0.75,  # Around the center of the text
        #     python_text.get_right() + UP * 0.5,
        #     python_text.get_right() + RIGHT * 2 + UP * 0.5  # End of the snake
        # ])

        
        text1 = Text("Auto Tasks", font_size=40, color=BLUE)
        text2 = Text("AI", font_size=40, color=BLUE)

        snake_body = VMobject(color=GREEN)
        snake_body.set_points_smoothly([
            LEFT * 2 + UP * 4,  # Start of the snake
            UP * 2,
            UP * 1,
            UP * 0.5,
            RIGHT * 2 + UP * 0.5  # End of the snake
        ])

        snake_head = Circle(radius=0.2, color=GREEN).move_to(snake_body.get_end())

        text1.move_to(snake_body.get_start()).shift(UP * 0.5)
        text2.move_to(snake_body.get_end()).shift(RIGHT * 0.7)

        # Animate the snake wrapping around the text
        self.play(Write(text1))
        self.play(Create(snake_body), run_time=2)
        self.play(FadeIn(snake_head), run_time=1)
        self.play(Write(text2))

        self.wait(2)