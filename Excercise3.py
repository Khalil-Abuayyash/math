from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class ExerciseSqrtFunction(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Solution of $f(x) = \sqrt{5x + 10}$", font_size=50).set_color(BLUE)
        
        # Text for Domain and Range with colors
        domain = Tex(r"Domain: $[-2, \infty)$", font_size=40).set_color(GREEN)
        range_ = Tex(r"Range: $[0, \infty)$", font_size=40).set_color(RED)
        
        explanation = Tex(
            r"""
            \\ \\ \\ Explanation: $f(x) = \sqrt{5x + 10}$ is defined when $5x + 10 \geq 0$.\\
            Solving $5x + 10 \geq 0$ gives $x \geq -2$.\\
            \textbf{Domain:} $x \in [-2, \infty)$.\\
            \textbf{Range:} Since $\sqrt{5x + 10}$ produces non-negative values,\\
            and increases without bound, $f(x) \in [0, \infty)$.
            """,
            font_size=40
        ).set_color(WHITE)

        explanation.next_to(range_, DOWN, buff = 1)
        # Animations
        self.play(Write(title))
        self.wait(2)  # Wait to match narration for the title
        self.play(title.animate.to_edge(UP))  # Move title to the top edge
        self.wait(0.5)  # Pause for emphasis
        self.play(Write(domain))  # Domain definition appears
        self.wait(4)  # Extended wait to match narration for domain
        self.play(domain.animate.to_edge(UP * 3))
        self.play(Write(range_))  # Range definition appears
        self.wait(4)  # Extended wait to match narration for range
        self.play(range_.animate.to_edge(UP * 5))
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(title, domain, range_, explanation))  # Fade out all elements
