from manim import *

class ChargingByFriction(Scene):
    def construct(self):
        # Glass rod and silk representation
        glass_rod = Rectangle(width=2, height=0.4, color=BLUE).shift(LEFT * 3)
        silk = Rectangle(width=2, height=0.4, color=RED).shift(RIGHT * 3)

        # Labels
        glass_label = Text("Glass Rod", font_size=24).next_to(glass_rod, UP)
        silk_label = Text("Silk", font_size=24).next_to(silk, UP)

        # Electrons (small blue dots)
        electrons = VGroup(*[Dot(color=BLUE).scale(0.5) for _ in range(6)])
        for i, electron in enumerate(electrons):
            electron.move_to(glass_rod.get_center() + DOWN * 0.2 + RIGHT * (i * 0.3 - 0.75))

        # Add initial setup to the scene
        self.play(Create(glass_rod), Create(silk), Write(glass_label), Write(silk_label))
        self.play(FadeIn(electrons))
        self.wait(1)

        # Animation: Rubbing the glass rod with silk
        self.play(ApplyWave(glass_rod), ApplyWave(silk), run_time=2)
        self.wait(1)

        # Animation: Electrons moving from glass to silk
        electron_animations = [
            electron.animate.move_to(silk.get_center() + DOWN * 0.2 + RIGHT * (i * 0.3 - 0.75))
            for i, electron in enumerate(electrons)
        ]
        self.play(*electron_animations, run_time=3)

        # Add final charges
        positive_charges = VGroup(*[Text("+", font_size=24, color=YELLOW).move_to(electron.get_center()) for electron in electrons])
        self.play(FadeIn(positive_charges), run_time=2)

        # Explanation Text
        explanation = Text(
            "Electrons are transferred from the glass rod to the silk,\n"
            "leaving the rod positively charged and the silk negatively charged.",
            font_size=24,
            color=WHITE
        ).to_edge(DOWN)
        self.play(Write(explanation), run_time=4)

        self.wait(2)
