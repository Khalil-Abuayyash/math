from manim import *

class VGroupAddExample(Scene):
    def construct(self):
        # Create initial objects
        circle = Circle().set_color(BLUE)
        square = Square().set_color(RED)

        # Create a VGroup and add initial objects
        group = VGroup(circle, square)
        group.arrange(RIGHT, buff=0.5)  # Arrange side by side

        # Add the group to the scene
        self.add(group)
        self.wait()

        # Create a new object to add
        triangle = Triangle().set_color(GREEN)
        
        # Add the new object to the group
        group.add(triangle)
        group.arrange(RIGHT, buff=0.5)  # Rearrange after adding

        # Animate the addition
        self.play(FadeIn(triangle), group.animate.arrange(RIGHT, buff=0.5))
        # self.play(FadeIn(triangle))
        self.wait()
