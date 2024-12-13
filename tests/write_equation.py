from manim import *

config.pixel_width = 1920
config.pixel_height = 1080 

class MultipleEquations(Scene):
    def construct(self):
        eq1 = MathTex(r"E = mc^2").set_color(RED)
        eq2 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}").set_color(BLUE)
        eq3 = MathTex(r"F = ma").set_color(GREEN)

        # Display equations one by one
        self.play(Write(eq1))
        self.wait(1)
        self.play(Transform(eq1, eq2))  # Transition to the next equation
        self.wait(1)
        self.play(Transform(eq1, eq3))  # Transition to the final equation
        self.wait(2)

class ArrangeEquations(Scene):
    def construct(self):
        eq1 = MathTex(r"E = mc^2").set_color(RED).scale(2)
        eq2 = MathTex(r"\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}").set_color(BLUE).scale(2)
        eq3 = MathTex(r"F = ma").set_color(GREEN).scale(2)

        # Arrange equations vertically
        equations = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.8)
        self.play(Write(equations,  run_time=5))
        self.wait(2)

class NewtonSecondLaw(Scene):
    def construct(self):
        # Title of the Scene
        title = Text("Newton's Second Law: F = ma", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Display the problem
        problem_text = Text("A car of mass 1500 kg accelerates to 20 m/s in 10 seconds.", font_size=28)
        problem_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(problem_text))
        self.wait(1)

        # Display given values
        mass_label = Text("Mass (m) = 1500 kg", font_size=24).to_edge(LEFT, buff=1)
        velocity_label = Text("Final Velocity (v_f) = 20 m/s", font_size=24).next_to(mass_label, DOWN, buff=0.3)
        time_label = Text("Time (t) = 10 s", font_size=24).next_to(velocity_label, DOWN, buff=0.3)
        
        self.play(Write(mass_label), Write(velocity_label), Write(time_label))
        self.wait(1)

        # Calculate the acceleration
        acceleration_text = MathTex(r"a = \frac{\Delta v}{\Delta t} = \frac{20 - 0}{10} = 2 \, \text{m/s}^2", font_size=36)
        acceleration_text.next_to(time_label, DOWN, buff=0.8)
        self.play(Write(acceleration_text))
        self.wait(1)

        # Display the final equation for force
        force_text = MathTex(r"F = ma = 1500 \times 2 = 3000 \, \text{N}", font_size=36)
        force_text.next_to(acceleration_text, DOWN, buff=0.8)
        self.play(Write(force_text))
        self.wait(2)

        # Display the result in a larger, bold format
        final_result = Text("Net Force = 3000 N", font_size=48, color=RED).next_to(force_text, DOWN, buff=1)
        self.play(Write(final_result))
        self.wait(2)

        # End the scene
        self.play(FadeOut(title), FadeOut(problem_text), FadeOut(mass_label), FadeOut(velocity_label),
                  FadeOut(time_label), FadeOut(acceleration_text), FadeOut(force_text))

class NewtonsSecondLawExample(Scene):
    def construct(self):
        # Create the equation (MathTex)
        equation = MathTex("t = 10s")

        # Create a circle that will circle the equation
        circle = Circle(radius=1, color=BLUE)

        # Position the equation and the circle
        equation.move_to(ORIGIN)
        circle.move_to(equation.get_center())  # Position the circle around the equation

        # Add the circle and the equation to the scene
        self.play(Create(circle), Write(equation))
        self.wait(1)

        # Create a new equation for t = 12s
        new_equation = MathTex("t = 12s")
        new_equation.move_to(equation.get_center())  # Position the new equation at the same spot

        # Animate the change in the equation (from t = 10s to t = 12s)
        self.play(Transform(equation, new_equation), run_time=2)

        # Remove the circle after the equation becomes t = 12s
        self.play(FadeOut(circle))

        self.wait(1)

