from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30


class VectorAcademyIntro(Scene):
    def construct(self):
        # Math Element: Parametric Curve
        math_curve = ParametricFunction(
            lambda t: np.array([
                np.sin(t),
                np.cos(t),
                0
            ]),
            t_range=np.array([0, 2 * PI]),
            color=BLUE
        ).scale(2)

        # Physics Element: Vectors
        physics_vector = Arrow(ORIGIN, LEFT + DOWN, buff=0, color=YELLOW)
        programming_vector = Arrow(ORIGIN, RIGHT, buff=0, color=GREEN)
        math_vector = Arrow(ORIGIN, UP, buff=0, color=RED)

        # Group vectors
        vectors = VGroup(math_vector, physics_vector, programming_vector)

        # Labels for each vector
        math_label = Text("Math", font_size=24, color=RED).next_to(math_vector.get_end(), UP)
        physics_label = Text("Physics", font_size=24, color=YELLOW).next_to(physics_vector.get_end(), LEFT)
        programming_label = Text("Programming", font_size=24, color=GREEN).next_to(programming_vector.get_end(), RIGHT)

        # Combine into a Brain Shape
        brain_outline = SVGMobject("brain.svg").set_color(WHITE).scale(2)
        brain_outline.set_fill(opacity=0.1)

        # Animation Sequence
        self.play(Create(math_vector), Write(math_label), run_time=2)
        self.play(Create(physics_vector), Write(physics_label), run_time=2)
        self.play(Create(programming_vector), Write(programming_label), run_time=2)
        self.wait(1)

        # Merge into the Brain
        self.play(Transform(vectors, brain_outline),
                  Transform(VGroup(math_label, physics_label, programming_label), brain_outline),
                  run_time=3)

        # Reveal the Channel Name
        channel_name = Text("Vector Academy", font_size=48, color=WHITE)
        channel_name.next_to(brain_outline, DOWN)
        self.play(Write(channel_name), run_time=2)

        # Add Tagline
        # tagline = Text("Your ultimate physics, math, and CS platform", 
        #                font_size=24, color=GRAY)
        # tagline.next_to(channel_name, DOWN)
        # self.play(FadeIn(tagline, shift=UP), run_time=2)

        # Final Glow Effect
        self.play(Indicate(brain_outline, color=BLUE, scale_factor=1.1), run_time=2)
        self.wait(2)
