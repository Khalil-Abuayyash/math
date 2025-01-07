from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PythonSnakeAnimation(Scene):
    def construct(self):
        # Create the word "Python"
        # python_text = Text("Python", font_size=72, color=BLUE)
        # self.play(Write(python_text))
        # self.wait(1)

        # Create the snake as a curve
        # snake_body = VMobject(color=GREEN)
        # snake_body.set_points_smoothly([
        #     python_text.get_left() + LEFT * 2 + UP * 0.5,  # Start of the snake
        #     python_text.get_left() + UP * 0.5,
        #     python_text.get_center() + UP * 0.75,  # Around the center of the text
        #     python_text.get_right() + UP * 0.5,
        #     python_text.get_right() + RIGHT * 2 + UP * 0.5  # End of the snake
        # ])

        # # Create the snake head (circle)
        # snake_head = Circle(radius=0.2, color=GREEN).move_to(snake_body.get_end())

        # gif_animation = ImageSequenceMobject("python.gif")  # Path to your GIF
        gif_animation = ImageMobject("python.gif")  # Path to your GIF
        # gif_animation.scale(2)  # Scale if needed
        # gif_animation.playback_rate = 1  # Adjust playback speed (default is 1)

        svg_object = SVGMobject("python.svg")  # Path to your SVG file
        # svg_object.set_color(BLUE)  # Optional: Set the color of the SVG
        svg_object.scale(2)  # Optional: Scale the SVG
        # svg_object.to_edge(UP)  # Optional: Position the SVG

        # Animate the snake wrapping around the text
        # self.play(Create(snake_body), run_time=4)
        # self.play(FadeIn(snake_head), run_time=1)
        # self.add(gif_animation)
        self.play(Create(svg_object), run_time=2)
        # self.play(gif_animation.animate)  # Play the animation

        # Final wait before ending the scene
        self.wait(2)
