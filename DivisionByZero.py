from manim import *

config.pixel_width = 1080   # Set width (e.g., Full HD resolution)
config.pixel_height = 1920  # Set height
config.frame_rate = 30      # Set frame rate


# Hamada 
class DivisionByZero(Scene):
    def construct(self):
        # Title
        title = Text("Why Dividing by 0 is Undefined", font_size=60).set_color(BLUE)

        # Explanation Text
        explanation = Tex(
            r"When dividing a number by 0, the operation has no meaning.\\"
            r"\text{Mathematically, division is finding how many times}\\"
            r"0 fits into a number, which is impossible.",
            font_size=50
        ).set_color(RED).shift(UP * 1)

        # Example: 5 ÷ 0
        example = MathTex(r"5 \div 0 \text{ is undefined}", font_size=48).set_color(RED).shift(DOWN * 1)

        # Animations
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))  # Move title to the top
        self.play(Write(explanation))
        self.wait(3)
        self.play(Write(example))
        self.wait(2)

        # Emphasizing the "undefined"
        undefined_text = Text("Undefined!", font_size=60, color=YELLOW).scale(1.2).next_to(example, DOWN)
        self.play(Write(undefined_text))
        self.wait(3)

        # Fade out
        self.play(FadeOut(title, explanation, example, undefined_text))
