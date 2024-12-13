from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise2(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Solution of $f(x) = 1 - \sqrt{x}$", font_size=50).set_color(BLUE)
        
        # Text for Domain and Range with colors
        domain = Tex(r"Domain: The set of non-negative real numbers $[0, \infty)$", font_size=40).set_color(GREEN)
        range_ = Tex(r"Range: $(-\infty, 1]$", font_size=40).set_color(RED)
        
        explanation = Tex(
            r"Explanation: $\sqrt{x}$ is defined only for $x \geq 0$, so the domain is $x \in [0, \infty)$.\\"
            r"\textbf{Domain:} Since $x \geq 0$, the domain is the set of non-negative real numbers.\\"
            r"\textbf{Range:} The output $y = 1 - \sqrt{x}$ starts at $1$ (when $x = 0$) and decreases without bound as $x$ increases."
            ,
            font_size=40
        ).set_color(WHITE)

        # Animations
        self.play(Write(title))
        self.wait(2)  # Wait to match narration for the title
        self.play(title.animate.to_edge(UP))  # Move title to the top edge
        self.wait(0.5)  # Pause for emphasis
        self.play(Write(domain))  # Domain definition appears
        self.wait(3)  # Extended wait to match narration for domain
        self.play(domain.animate.to_edge(UP * 3))
        self.play(Write(range_))  # Range definition appears
        self.wait(3)  # Extended wait to match narration for range
        self.play(range_.animate.to_edge(UP * 5))
        self.play(Write(explanation))
        self.wait(5)
        self.play(FadeOut(title, domain, range_, explanation))  # Fade out all elements
