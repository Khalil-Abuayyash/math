from manim import *

config.pixel_width = 1080   # Video width
config.pixel_height = 1920  # Video height
config.frame_rate = 30      # Frame rate

class DivisionByZero(Scene):
    def construct(self):
        # Video title with enhanced animation
        title = Text("What is division?", font_size=70).set_color(BLUE)
        self.play(Write(title))  # Title appears
        self.wait(1)
        self.play(title.animate.to_edge(UP))  # Move title to the top
        self.wait(1)
        
        # First explanatory text: Definition of division
        explanation = Tex(
            r"\text{Division is a mathematical operation aimed at dividing a}\\"
            r"\text{certain quantity into equal parts.}\\"
            r"\text{For example, if we have 6 apples and we want to divide them}\\"
            r"\text{between two people, each person will receive 3 apples.}\\"
            r"\text{This means there is a number, when multiplied by 2,}\\"
            r"\text{gives us 6, which is the number 3.}",
            font_size=50
        ).scale(1).move_to(ORIGIN).set_color(RED)

        # Show first explanation with controlled speed
        
        self.play(Write( explanation, run_time=17))  # Adjust the run_time to control speed
        self.wait()
        self.play(FadeOut(title, explanation))
        
        title1 = Text("Why is division by zero undefined?", font_size=70).set_color(BLUE)
        self.play(Write(title1))  # Title appears
        self.wait(1)
        self.play(title1.animate.to_edge(UP))  # Move title to the top
        self.wait(1)
        
        explanation1 = Tex(
            r"\text{Imagine that 6 ÷ 0 = A, this means A × 0 = 6.}\\"
            r"\text{But this is impossible because multiplying any number}\\"
            r"\text{by zero always gives zero.}\\"
            r"\text{Therefore, division by zero has no mathematical meaning.}",
            font_size=50
        ).scale(1).move_to(ORIGIN).set_color(YELLOW)

        # Show second explanation with controlled speed
        self.play(Write(explanation1, run_time=17))  # Adjust the run_time to control speed
        self.wait()

        # Fade out second explanation
        self.play(FadeOut(title1, explanation1))

        # End with a call to action or a closing title
        closing_title = Text("Thank you for watching!", font_size=60).set_color(GREEN)
        self.play(Write(closing_title))
        self.wait(2)

