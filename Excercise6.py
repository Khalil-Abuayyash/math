from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise6(Scene):
    def construct(self):
        # Title with color
        title = Tex(r"Solution of $G(t) = \frac{2}{t^2 - 16}$", font_size=50).set_color(BLUE)
        
        # Text for Domain and Range with colors
        domain = Tex(
            r"Domain: $(-\infty, -4) \cup (4, \infty)$", 
            font_size=40
        ).set_color(GREEN)
        
        range_ = Tex(
            r"Range: $(-\infty, 0) \cup (0, \infty)$", 
            font_size=40
        ).set_color(RED)
        
        explanation = Tex(
            r"""
            Explanation: $G(t) = \frac{2}{t^2 - 16}$ is defined when the denominator is non-zero.\\
            The denominator $t^2 - 16$ factors as $(t - 4)(t + 4)$.\\
            Therefore, $t^2 - 16 = 0$ when $t = \pm 4$, so $t \neq \pm 4$.\\
            \textbf{Domain:} All real numbers except $t = -4$ and $t = 4$,\\
            so $t \in (-\infty, -4) \cup (4, \infty)$.\\
            \textbf{Range:} Since $G(t)$ is a rational function, it produces all real values\\
            except zero. Thus, the range is $(-\infty, 0) \cup (0, \infty)$.
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
        self.wait(6)
        # self.play(explanation.animate.next_to(range_, DOWN, buff=1))
        self.play(FadeOut(title, domain, range_, explanation))  # Fade out all elements
