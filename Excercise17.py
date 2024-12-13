from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise17(Scene):
    def construct(self):
        # Title
        title = Tex(r"Solution to $g(x) = \sqrt{|x|}$", font_size=50).set_color(BLUE)
        title1 = Tex(r"The Graph of $g(x) = \sqrt{|x|}$", font_size=50).set_color(BLUE)
        
        # Natural Domain
        domain_text = Tex(
            r"Natural Domain: $(-\infty, \infty)$ (all real numbers)", 
            font_size=40
        ).set_color(GREEN)
        
        # Explanation
        explanation = Tex(
            r"""
            Explanation: $g(x) = \sqrt{|x|}$ is defined for all real numbers.\\
            Since $|x|$ is always non-negative,\\
            and the square root is defined for non-negative values,\\
            the natural domain is $(-\infty, \infty)$.
            """,
            font_size=40
        ).set_color(WHITE)
        
        # Axes and Graph
        axes = Axes(
            x_range=[-5, 5, 1],  # x-axis range
            y_range=[-1, 3, 1],  # y-axis range
            tips=True
        ).add_coordinates()
        
        axes.shift(DOWN * 1)
        
        graph = axes.plot(
            lambda x: (abs(x))**0.5,  # sqrt(abs(x))
            color=RED, 
            x_range=[-5, 5]
        )
        
        # Animations
        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))  # Move title up
        self.play(Write(domain_text))
        self.wait(2)
        self.play(domain_text.animate.next_to(title, DOWN, buff=1))
        self.play(Write(explanation))
        self.wait(5)
        self.play(FadeOut(title, domain_text, explanation))
        self.play(Write(title1))
        self.wait(2)
        self.play(title1.animate.to_edge(UP))  
        self.play(Create(axes), Create(graph))  # Create axes and graph
        self.wait(7)
        self.play(FadeOut(axes, graph))  # Fade out all elements
