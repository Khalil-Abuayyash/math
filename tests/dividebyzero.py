from manim import *

# Set the configuration for vertical video (YouTube Shorts)
config.pixel_height = 1920  # Height for vertical video
config.pixel_width = 1080   # Width for vertical video
config.frame_rate = 30

class DivideByZero(Scene):
    def construct(self):
        # Colors
        title_color = YELLOW
        text_color = WHITE
        important_text_color = RED
        equation_color = BLUE

        # Show title "Why dividing by zero breaks math" in the center, then move it to the top
        title1 = Text("Why dividing by zero breaks math", font_size=60, color=title_color)
        self.play(Write(title1))
        self.wait(1)
        self.play(title1.animate.to_edge(UP))
        self.wait(0.5)

        # Animation of 1 / 0, the 1 should appear, then the sign, then the zero
        one = Text("1", font_size=96, color=equation_color)
        division_sign = Text("÷", font_size=96, color=equation_color)
        zero = Text("0", font_size=96, color=equation_color)
        equation = VGroup(one, division_sign, zero).arrange(RIGHT, buff=0.2).shift(UP*0.5)

        self.play(Write(one))
        self.wait(0.5)
        self.play(Write(division_sign))
        self.wait(0.5)
        self.play(Write(zero))
        self.wait(1)

        # Highlight the equation
        self.play(Indicate(equation, scale_factor=1.2, color=important_text_color))
        self.wait(1)

        # Remove all things
        self.play(FadeOut(equation))
        self.wait(0.5)

        # Transform title to "What is division?", move it to the top
        title2 = Text("What is division?", font_size=60, color=title_color)
        self.play(Transform(title1, title2))
        self.wait(1)
        self.play(title1.animate.to_edge(UP))
        self.wait(0.5)

        # Division using multiplication, provide examples
        # Example 1: 6 ÷ 2 = 3 because 3 × 2 = 6
        division_example = MathTex("6 \\div 2 = 3", font_size=72, color=equation_color)
        multiplication_relation = MathTex("3 \\times 2 = 6", font_size=60, color=text_color)
        example_group = VGroup(division_example, multiplication_relation).arrange(DOWN, buff=0.5).shift(UP*0.5)

        self.play(Write(division_example))
        self.wait(1)
        self.play(Write(multiplication_relation))
        self.wait(2)

        # Example 2: 15 ÷ 5 = 3 because 3 × 5 = 15
        division_example2 = MathTex("15 \\div 5 = 3", font_size=72, color=equation_color)
        multiplication_relation2 = MathTex("3 \\times 5 = 15", font_size=60, color=text_color)
        example_group2 = VGroup(division_example2, multiplication_relation2).arrange(DOWN, buff=0.5).next_to(example_group, DOWN, buff=1)

        self.play(Write(division_example2))
        self.wait(1)
        self.play(Write(multiplication_relation2))
        self.wait(2)

        # Emphasize the concept
        self.play(Circumscribe(VGroup(example_group, example_group2), color=important_text_color, fade_out=True))
        self.wait(1)

        # Remove examples and title
        self.play(FadeOut(example_group), FadeOut(example_group2), FadeOut(title1))
        self.wait(0.5)

        # New title: "Why can't we divide by zero?"
        title3 = Text("Why can't we divide by zero?", font_size=60, color=title_color)
        self.play(Write(title3))
        self.wait(1)
        self.play(title3.animate.to_edge(UP))
        self.wait(0.5)

        # Show attempting to solve 1 ÷ 0 = x
        problem = MathTex("1 \\div 0 = x", font_size=72, color=equation_color)
        implied_equation = MathTex("\\Rightarrow x \\times 0 = 1", font_size=60, color=equation_color).next_to(problem, DOWN, buff=0.5)
        self.play(Write(problem))
        self.wait(1)
        self.play(Write(implied_equation))
        self.wait(2)

        # Emphasize that x * 0 = 1 has no solution
        no_solution = Text("No real number x satisfies this equation", font_size=48, color=important_text_color).next_to(implied_equation, DOWN, buff=0.5)
        self.play(Write(no_solution))
        self.wait(2)

        # Visual cue that it's impossible
        self.play(Flash(implied_equation, color=RED, flash_radius=0.5))
        self.wait(1)

        # Fade out all except the title
        self.play(FadeOut(problem), FadeOut(implied_equation), FadeOut(no_solution))
        self.wait(0.5)

        # Conclusion
        conclusion = Text("Dividing by zero is undefined", font_size=60, color=equation_color)
        reason = Text("It leads to contradictions in arithmetic", font_size=48, color=text_color)
        conclusion_group = VGroup(conclusion, reason).arrange(DOWN, buff=0.5).shift(UP*0.5)

        self.play(Write(conclusion_group))
        self.wait(3)

        # Final highlight
        self.play(Circumscribe(conclusion_group, color=important_text_color, fade_out=True))
        self.wait(2)

        # Fade out conclusion
        self.play(FadeOut(conclusion_group))

        # Closing Message
        closing_message = Text("Thank you for watching!", font_size=60, color=YELLOW)
        closing_subtext = Text("Subscribe for more!", font_size=48, color=WHITE)
        closing_group = VGroup(closing_message, closing_subtext).arrange(DOWN, buff=0.5)

        self.play(Write(closing_group))
        self.wait(3)

        # End with a fade out
        self.play(FadeOut(closing_group))
        self.wait(1)