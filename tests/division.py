from manim import *

class DivideByZero(Scene):
    def construct(self):
        # Introduction: Dividing 8 by 4
        equation = MathTex(r"\frac{8}{4} = 2")
        # eq2 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}").set_color(BLUE)
        self.play(Write(equation))
        self.wait(1)
        self.play(FadeOut(equation))

        # Visualize dividing 8 items into 4 groups
        group_1 = Circle(radius=0.5).shift(LEFT*2)
        group_2 = Circle(radius=0.5).shift(LEFT)
        group_3 = Circle(radius=0.5)
        group_4 = Circle(radius=0.5).shift(RIGHT)
        
        self.play(FadeIn(group_1), FadeIn(group_2), FadeIn(group_3), FadeIn(group_4))
        self.wait(1)

        # Transition to division by zero
        self.play(FadeOut(group_1), FadeOut(group_2), FadeOut(group_3), FadeOut(group_4))
        equation2 = MathTex(r"\frac{8}{0} = ?")
        self.play(Write(equation2))
        self.wait(1)

        # Show trying to divide into 0 groups
        empty_text = Text("Trying to divide into zero groups...").shift(DOWN)
        self.play(Write(empty_text))
        self.wait(1)

        # Show the paradox
        self.play(FadeOut(empty_text), FadeOut(equation2))

        # Infinity Concept
        equation3 = MathTex(r"\frac{8}{0.1} = 80")
        self.play(Write(equation3))
        self.wait(1)
        self.play(FadeOut(equation3))

        # Transition to undefined result
        undefined = MathTex(r"\frac{8}{0} \text{ is undefined!}")
        self.play(Write(undefined))
        self.wait(2)