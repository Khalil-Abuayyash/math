from manim import *

config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.pixel_height = 1080  # Set height
config.frame_rate = 30      # Set frame rate (optional)

class Excercise19(Scene):
    def construct(self):
        # Title
        title = Tex(r"Solution to $F(t) = \frac{t}{|t|}$", font_size=50).set_color(BLUE)
        title1 = Tex(r"The Graph of $F(t) = \frac{t}{|t|}$", font_size=50).set_color(BLUE)
        
        # Natural Domain
        domain_text = Tex(
            r"Natural Domain: $(-\infty, 0) \cup (0, \infty)$ (all real numbers except 0)", 
            font_size=40
        ).set_color(GREEN)
        
        # Explanation
        explanation = Tex(
            r"""
            Explanation: $F(t) = \frac{t}{|t|}$ is undefined at $t = 0$ since division by zero is not allowed.\\
            Therefore, the natural domain is $(-\infty, 0) \cup (0, \infty)$.
            """,
            font_size=40
        ).set_color(WHITE)
        
        # Axes and Graph
        axes = Axes(
            x_range=[-5, 5, 1],  # x-axis range
            y_range=[-2, 2, 1],  # y-axis range
            tips=True
        ).add_coordinates()
        
        axes.shift(DOWN * 1)
        
        # Function for F(t) = t / |t|
        def F(t):
            return np.sign(t)  # np.sign(t) returns -1 for negative, 1 for positive, and 0 for zero

        graph = axes.plot(
            F,
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
