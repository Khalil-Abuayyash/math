from manim import *
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class OddEvenReel(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Title
        title = Text("Odd vs. Even Functions", font_size=48, color=YELLOW)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Even function: y = x^2
        even_graph = axes.plot(lambda x: x**2, color=GREEN)
        even_label = axes.get_graph_label(even_graph, label="y = x^2")
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(even_graph), Write(even_label))
        self.wait(1)

        # Show y-axis symmetry
        y_axis_line = DashedLine(start=axes.c2p(0, -5), end=axes.c2p(0, 5), color=YELLOW)
        self.play(Create(y_axis_line))
        self.play(FadeOut(y_axis_line))
        even_text = Text("Even: Symmetric about y-axis", font_size=32, color=GREEN)
        self.play(Write(even_text))
        self.wait(2)
        self.play(FadeOut(even_text), FadeOut(even_graph), FadeOut(even_label))

        # Odd function: y = x^3
        odd_graph = axes.plot(lambda x: x**3, color=RED)
        odd_label = axes.get_graph_label(odd_graph, label="y = x^3")
        self.play(Create(odd_graph), Write(odd_label))
        self.wait(1)

        # Show origin symmetry
        origin = Dot(axes.c2p(0, 0), color=ORANGE)
        self.play(Create(origin))
        self.play(Rotate(odd_graph, angle=PI, about_point=origin.get_center()))
        odd_text = Text("Odd: Symmetric about origin", font_size=32, color=RED)
        self.play(Write(odd_text))
        self.wait(2)

        # Closing comparison
        self.play(FadeOut(odd_text), FadeOut(odd_graph), FadeOut(odd_label), FadeOut(origin))
        self.play(Create(even_graph), Create(odd_graph))
        comparison_text = Text("Odd or Even? Comment below!", font_size=36, color=WHITE)
        self.play(Write(comparison_text))
        self.wait(2)

# To render the scene, use the following command in your terminal:
# manim -pql odd_even_reel.py OddEvenReel