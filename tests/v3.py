from manim import *

class NestedVGroupExample(Scene):
    def construct(self):
        # Create two groups
        group1 = VGroup(Circle(), Square()).arrange(DOWN)
        group2 = VGroup(Triangle(), Circle()).arrange(DOWN)

        # Combine them into another group
        main_group = VGroup(group1, group2).arrange(RIGHT, buff=1)

        self.add(main_group)
        self.play(main_group.animate.shift(UP))
