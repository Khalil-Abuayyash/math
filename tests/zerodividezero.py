from manim import *

# Set the configuration for vertical video (YouTube Shorts)
config.pixel_height = 1920  # Height for vertical video
config.pixel_width = 1080   # Width for vertical video
config.frame_rate = 30

class ZeroDividedByZero(Scene):
    def construct(self):
        # Colors
        title_color = YELLOW
        text_color = WHITE
        important_text_color = RED
        equation_color = BLUE

        # Show title "Why 0 divided by 0 is undefined" in the center, then move it to the top
        title = Text("Why 0 divided by 0 is undefined", font_size=60, color=title_color)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Present 0 ÷ 0
        zero1 = Text("0", font_size=96, color=equation_color)
        division_sign = Text("÷", font_size=96, color=equation_color)
        zero2 = Text("0", font_size=96, color=equation_color)
        equation = VGroup(zero1, division_sign, zero2).arrange(RIGHT, buff=0.2).shift(UP*0.5)
        self.play(Write(zero1))
        self.wait(0.5)
        self.play(Write(division_sign))
        self.wait(0.5)
        self.play(Write(zero2))
        self.wait(1)

        # Highlight the equation
        self.play(Indicate(equation, scale_factor=1.2, color=important_text_color))
        self.wait(1)

        # Transform title to "Understanding 0 ÷ 0"
        new_title = Text("Understanding 0 ÷ 0", font_size=60, color=title_color)
        self.play(Transform(title, new_title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.wait(0.5)

        # Explain division as "How many times does divisor fit into dividend?"
        explanation = Text(
            "Division asks: How many times does the divisor fit into the dividend?",
            font_size=48, color=text_color, line_spacing=1).shift(UP*0.5)
        self.play(Write(explanation))
        self.wait(3)

        # Apply this to 0 ÷ 0
        self.play(FadeOut(explanation))
        self.wait(0.5)

        question = Text(
            "So, how many times does 0 fit into 0?",
            font_size=54, color=text_color).shift(UP*0.5)
        self.play(Write(question))
        self.wait(2)

        # Possible answers
        possible_answers = VGroup(
            Text("0", font_size=72, color=equation_color),
            Text("1", font_size=72, color=equation_color),
            Text("Any number", font_size=72, color=equation_color),
            Text("Undefined", font_size=72, color=important_text_color)
        ).arrange(DOWN, buff=0.5).shift(DOWN*0.5)
        self.play(Write(possible_answers[0]))
        self.wait(1)
        self.play(Write(possible_answers[1]))
        self.wait(1)
        self.play(Write(possible_answers[2]))
        self.wait(1)

        # Explain why each answer doesn't work
        # Option 0
        self.play(Circumscribe(possible_answers[0], color=RED, fade_out=True))
        explanation0 = Text(
            "0 × 0 = 0 ✔", font_size=48, color=GREEN
        ).next_to(possible_answers[0], RIGHT, buff=0.5)
        self.play(Write(explanation0))
        self.wait(2)

        # Option 1
        self.play(Circumscribe(possible_answers[1], color=YELLOW, fade_out=True))
        explanation1 = Text(
            "1 × 0 = 0 ✔", font_size=48, color=GREEN
        ).next_to(possible_answers[1], RIGHT, buff=0.5)
        self.play(Write(explanation1))
        self.wait(2)

        # Option "Any number"
        self.play(Circumscribe(possible_answers[2], color=BLUE, fade_out=True))
        explanation2 = Text(
            "Any number × 0 = 0 ✔", font_size=48, color=GREEN
        ).next_to(possible_answers[2], RIGHT, buff=0.5)
        self.play(Write(explanation2))
        self.wait(2)

        # Point out the contradiction
        contradiction = Text(
            "Contradiction! Multiple answers.", font_size=48, color=important_text_color
        ).shift(DOWN*2)
        self.play(Write(contradiction))
        self.wait(2)

        # Highlight "Undefined" option
        self.play(Circumscribe(possible_answers[3], color=important_text_color, fade_out=True))
        self.wait(1)
        self.play(Indicate(possible_answers[3], color=important_text_color))
        self.wait(1)

        # Conclude that 0 ÷ 0 is undefined
        self.play(FadeOut(question), FadeOut(possible_answers[0:3]), FadeOut(explanation0), FadeOut(explanation1), FadeOut(explanation2), FadeOut(contradiction))
        self.wait(0.5)
        conclusion = Text(
            "Therefore, 0 ÷ 0 is undefined.",
            font_size=60, color=equation_color
        ).shift(UP*0.5)
        self.play(Transform(possible_answers[3], conclusion))
        self.wait(2)

        # Additional explanation
        additional_explanation = Text(
            "It doesn't have a unique value and leads to contradictions.",
            font_size=48, color=text_color, line_spacing=1).next_to(conclusion, DOWN, buff=0.5)
        self.play(Write(additional_explanation))
        self.wait(3)

        # Fade out and display gratitude
        self.play(FadeOut(title), FadeOut(conclusion), FadeOut(additional_explanation))
        self.wait(0.5)

        # Closing Message
        closing_message = Text("Thank you for watching!", font_size=60, color=YELLOW)
        closing_subtext = Text("Subscribe for more!", font_size=48, color=WHITE)
        closing_group = VGroup(closing_message, closing_subtext).arrange(DOWN, buff=0.5)
        self.play(Write(closing_group))
        self.wait(3)

        # End with a fade out
        self.play(FadeOut(closing_group))
        self.wait(1)