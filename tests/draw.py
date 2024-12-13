from manim import *

class DoubleLinedU(Scene):
    def construct(self):
        # Define parameters for the "U" shape
        height = 4  # Height of the U
        width = 2   # Width of the U
        thickness = 0.3  # Thickness of the double lines

        # Create outer U shape
        outer_left_line = Line(LEFT * width + UP * height, LEFT * width + DOWN * height)
        outer_bottom_line = Line(LEFT * width + DOWN * height, RIGHT * width + DOWN * height)
        outer_right_line = Line(RIGHT * width + UP * height, RIGHT * width + DOWN * height)

        # Create inner U shape
        inner_left_line = Line(
            LEFT * (width - thickness) + UP * (height - thickness),
            LEFT * (width - thickness) + DOWN * (height - thickness)
        )
        inner_bottom_line = Line(
            LEFT * (width - thickness) + DOWN * (height - thickness),
            RIGHT * (width - thickness) + DOWN * (height - thickness)
        )
        inner_right_line = Line(
            RIGHT * (width - thickness) + UP * (height - thickness),
            RIGHT * (width - thickness) + DOWN * (height - thickness)
        )

        # Group outer and inner shapes
        outer_U = VGroup(outer_left_line, outer_bottom_line, outer_right_line)
        inner_U = VGroup(inner_left_line, inner_bottom_line, inner_right_line)

        # Subtract inner U from outer U to form the empty space
        double_lined_U = VGroup(outer_U, inner_U)

        # Add the double-lined U to the scene
        self.play(Create(double_lined_U))
        self.wait(2)
