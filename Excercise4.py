from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise4(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Solution of $f(x) = \sqrt{x^2 - 3x}$", font_size=50).set_color(BLUE)
        
        # Text for Domain and Range with colors
        domain = Tex(
            r"Domain: $(-\infty, 0] \cup [3, \infty)$", 
            font_size=40
        ).set_color(GREEN)
        
        range_ = Tex(
            r"Range: $[0, \infty)$", 
            font_size=40
        ).set_color(RED)
        
        explanation = Tex(
            r"""
            Explanation: $f(x) = \sqrt{x^2 - 3x}$ is defined when $x^2 - 3x \geq 0$.\\
            Factoring $x^2 - 3x$, we get $x(x - 3) \geq 0$.\\
            This inequality is true when $x \leq 0$ or $x \geq 3$.\\
            \textbf{Domain:} $x \in (-\infty, 0] \cup [3, \infty)$.\\
            \textbf{Range:} The square root function produces non-negative values,
            so $f(x) \in [0, \infty)$.
            """,
            font_size=40
        ).set_color(WHITE)

        explanation.next_to(range_, DOWN * 0.5) 
        # Animations
        self.play(Write(title))
        self.wait(2)  # Wait to match narration for the title
        self.play(title.animate.to_edge(UP))  # Move title to the top edge
        self.wait(0.5)  # Pause for emphasis
        self.play(Write(domain))  # Domain definition appears
        self.wait(3)  # Extended wait to match narration for domain
        self.play(domain.animate.next_to(title, DOWN, buff=1))  # Place domain below the title
        self.play(Write(range_))  # Range definition appears
        self.wait(3)  # Extended wait to match narration for range
        self.play(range_.animate.next_to(domain, DOWN, buff=1))  # Place range below domain
        self.play(Write(explanation))  # Explanation appears
        self.wait(5)
        # self.play(explanation.animate.next_to(range_, DOWN, buff=1))
        self.play(FadeOut(title, domain, range_, explanation))  # Fade out all elements
