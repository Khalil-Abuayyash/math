from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class EvenFunctionVisualization(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = BLACK

        # Create axes
        axes = Axes(
            x_range=[-1, 1, 1],
            y_range=[-5, 5, 5],
            axis_config={"color": WHITE},
            x_length=5,
            y_length=10,
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)").set_color(WHITE)

        # Add axes to the scene
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        # Load and position the original human SVG
        human_svg = SVGMobject("human.svg").scale(1.5)
        human_svg.move_to(axes.c2p(0, 0))

        # Add the original human SVG
        self.play(FadeIn(human_svg))
        self.wait(1)

        # Create two copies and position them symmetrically
        left_human = SVGMobject("left.svg").scale(1.5)
        right_human = SVGMobject("right.svg").scale(1.5)
        
        # Group left and right humans together initially
        human = VGroup(left_human, right_human)
        human.arrange(RIGHT, buff=0)

        # Transition from original to split humans
        self.play(FadeOut(human_svg), FadeIn(human))
        self.wait(1)

        # Position copies symmetrically
        left_human.move_to(axes.c2p(-0.5, 0))
        right_human.move_to(axes.c2p(0.5, 0))

        # Animate left and right humans moving apart
        self.play(left_human.animate.shift(LEFT ), right_human.animate.shift(RIGHT ))
        self.wait(4)
