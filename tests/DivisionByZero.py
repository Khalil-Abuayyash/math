from manim import *

config.pixel_width = 1080   # Video width
config.pixel_height = 1920  # Video height
config.frame_rate = 30      # Frame rate

class DivisionByZero(Scene):
    def construct(self):
        # Example: 6 / 2 = 3
        example_title = Text("Example: 6 ÷ 2 = ?", font_size=60).set_color(YELLOW)
        self.play(Write(example_title))
        self.wait(6)
        self.play(example_title.animate.to_edge(UP))  # Move title to the top

        # Subtraction sequence
        sequence_group = VGroup()  # Group for alignment

        # Step 1: 6 - 2 = 4
        step1 = VGroup(
            Tex("6", font_size=60).set_color(WHITE),
            Tex("- 2", font_size=60).set_color(BLUE),
            Tex("= 4", font_size=60).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5)  # Arrange elements horizontally
        sequence_group.add(step1)

        # Step 2: 4 - 2 = 2
        step2 = VGroup(
            Tex("4", font_size=60).set_color(WHITE),
            Tex("- 2", font_size=60).set_color(BLUE),
            Tex("= 2", font_size=60).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5)  # Arrange elements horizontally
        sequence_group.add(step2)

        # Step 3: 2 - 2 = 0
        step3 = VGroup(
            Tex("2", font_size=60).set_color(WHITE),
            Tex("- 2", font_size=60).set_color(BLUE),
            Tex("= 0", font_size=60).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5)  # Arrange elements horizontally
        sequence_group.add(step3)

        # Position the group vertically
        sequence_group.arrange(DOWN, buff=0.7).move_to(ORIGIN)

        # Animate each step
        for step in sequence_group:
            self.play(Write(step))
            self.wait(4)

        # Answer
        answer = Text("6 ÷ 2 = 3 (3 subtractions)", font_size=50).set_color(PURPLE).next_to(sequence_group, DOWN, buff=1)
        self.play(Write(answer))
        self.wait(3)
