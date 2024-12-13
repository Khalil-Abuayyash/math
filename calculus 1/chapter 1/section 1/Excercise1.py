from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise1(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Solution of $f(x) = 1 + x^2$", font_size=50).set_color(BLUE)
        
        # Text for Domain and Range with colors
        domain = Tex(r"Domain: The set of all real numbers $\mathbb{R}$", font_size=40).set_color(GREEN)
        range_ = Tex(r"Range: $[1, \infty)$", font_size=40).set_color(RED)
        
        explanation = Tex(
            r"Explanation: $x^2 \geq 0$, so $f(x) = 1 + x^2 \geq 1$.\\"
            r"\textbf{Domain:} Since $x$ can be any real number, the domain is $x \in \mathbb{R}$.\\"
            r"\textbf{Range:} The output $y$ starts at $1$ and increases without bound, so $y \geq 1$.",
            font_size=40
        ).set_color(WHITE)

        # Animations
        self.play(Write(title))
        self.wait(2)  # Wait to match narration for the title
        self.play(title.animate.to_edge(UP))  # Move title to the top edge
        self.wait(0.5)  # Pause for emphasis
        self.play(Write(domain))  # Domain definition appears
        self.wait(3)  # Extended wait to match narration for domain
        self.play(domain.animate.to_edge(UP*3))
        self.play(Write(range_))  # Range definition appears
        self.wait(3)  # Extended wait to match narration for range
        self.play(range_.animate.to_edge(UP*5))
        self.play(Write(explanation))
        self.wait(5)
        self.play(FadeOut(title, domain, range_, explanation ))  # Fade out all elements
