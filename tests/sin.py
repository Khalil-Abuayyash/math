from manim import *


config.pixel_width = 1080   # Set width (e.g., Full HD resolution)
config.pixel_height = 1920  # Set height
config.frame_rate = 30


class LimitOfSinXOverX(Scene):
    def construct(self):
        # Impressive opening sentence
        opening_text = Text(
            "Unlocking the Mysteries of Calculus",
            font_size=48
        )
        self.play(FadeIn(opening_text, scale=0.5))
        self.wait(2)

        # Transition to Title 1
        title1 = Text("Why does\nlim₍ₓ→₀₎ sin(x)/x = 1?", font_size=64)
        self.play(Transform(opening_text, title1))
        self.wait(2)

        # Transform Title 1 to Title 2 on the same screen
        title2 = Text("What is the Concept of the Limit?", font_size=48)
        self.play(Transform(opening_text, title2))
        self.wait(2)

        # Move Title 2 to the top of the screen
        self.play(opening_text.animate.to_edge(UP))
        self.wait(1)

        # Explain the concept of the limit
        explanation = Text(
            "A limit describes the value that a function approaches\n"
            "as the input approaches some value.",
            font_size=36
        )
        self.play(Write(explanation))
        self.wait(3)

        # Main explanation about lim(x→0) sin(x)/x = 1
        self.play(FadeOut(explanation))

        # Show the graph of sin(x)/x
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-0.5, 1.5, 0.5],
            x_length=10,
            y_length=6,
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="x", y_label="sin(x)/x")

        sinx_over_x = axes.plot(
            lambda x: np.sinc(x / np.pi),  # np.sinc(x) = sin(pi x)/(pi x)
            color=BLUE
        )

        horizontal_line = DashedLine(
            axes.c2p(-10, 1),
            axes.c2p(10, 1),
            color=YELLOW
        )
        one_label = MathTex("y = 1").next_to(horizontal_line, RIGHT)

        self.play(Create(axes), Create(labels))
        self.play(Create(sinx_over_x), run_time=2)
        self.wait(1)
        self.play(Create(horizontal_line), Write(one_label))
        self.wait(2)

        # Highlight the limit as x approaches 0
        dot = Dot(color=RED).move_to(axes.c2p(0, 1))
        self.play(FadeIn(dot))
        self.wait(2)

        main_explanation = Text(
            "As x approaches 0,\n"
            "sin(x)/x approaches 1.",
            font_size=36
        ).next_to(axes, DOWN)
        self.play(Write(main_explanation))
        self.wait(4)

        # End with 'Thank you for watching'
        self.play(FadeOut(VGroup(
            axes, labels, sinx_over_x, horizontal_line, one_label, dot, main_explanation
        )))
        thank_you = Text("Thank you for watching!", font_size=48)
        self.play(Write(thank_you))
        self.wait(2)
        self.play(FadeOut(thank_you))