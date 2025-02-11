from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_rate = 30

class XSquared(Scene):
    def construct(self):
        # Title
        title = Tex(r"Even Functions: $f(x) = f(-x)$", font_size=50)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Create Axes
        axes = Axes(
            x_range=[-4, 4, 1], y_range=[0, 16, 1],
            axis_config={"color": BLUE}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Plot function
        graph = axes.plot(lambda x: x**2, color=YELLOW)

        # Key points
        xs = [-4,-3,-2,-1,0,1,2,3,4]
        points = list(map(lambda x: (x, x**2), xs))
        dots = VGroup(*[Dot(axes.c2p(x, y), color=RED) for x, y in points])
        # self.play(*[FadeIn(dot) for dot in dots])
        mid = len(dots) // 2
        self.play(FadeIn(dots[mid]))
        for i in range(1, mid+1):
            self.play(FadeIn(dots[mid - i]), FadeIn(dots[mid + i]))

        # Animate graph drawing
        self.play(Create(graph), run_time=3)
        self.wait(2)

        # Reflection effect
        reflection_text = Tex(r"Symmetry: $f(x) = f(-x)$", font_size=40)
        reflection_text.to_edge(DOWN)
        self.play(Write(reflection_text))

        self.wait(3)
