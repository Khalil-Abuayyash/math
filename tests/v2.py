from manim import *

class ArrangeInGridExample(Scene):
    def construct(self):
        # Create multiple shapes
        shapes = VGroup(*[Square() for _ in range(9)])

        # Arrange the shapes in a 3x3 grid
        shapes.arrange_in_grid(rows=3, cols=3, buff=0.5)
        self.add(shapes)
        self.wait()
