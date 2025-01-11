from manim import *

class DerivativeRateOfChange(Scene):
    def construct(self):
        # Step 1: Introduction
        equation = MathTex("A = \\frac{\\pi}{4} D^2")
        self.play(Write(equation))
        self.wait(2)

        # Step 2: Visualizing the Circle and Its Area
        circle = Circle(radius=2, color=BLUE)
        diameter_line = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        diameter_label = MathTex("D").next_to(diameter_line, DOWN)
        self.play(Create(circle), Create(diameter_line), Write(diameter_label))
        self.wait(2)

        area_label = MathTex("A").move_to(circle.get_center() + UP * 2.5)
        self.play(Write(area_label))
        self.wait(2)

        # Step 3: Introduce the derivative formula
        derivative_formula = MathTex(
            "\\frac{dA}{dD} = \\frac{\\pi}{4} \\cdot 2D = \\frac{\\pi D}{2}"
        ).next_to(equation, DOWN, buff=1.5)
        self.play(Transform(equation.copy(), derivative_formula))
        self.wait(2)

        # Step 4: Substituting D = 10
        substitution = MathTex(
            "\\frac{dA}{dD} = \\frac{\\pi (10)}{2} = 5\\pi \\approx 15.71 \\, \\text{m}^2/\\text{m}"
        ).next_to(derivative_formula, DOWN, buff=1.5)
        self.play(Write(substitution))
        self.wait(2)

        # Step 5: Dynamic Visualization
        self.play(FadeOut(area_label))
        self.play(circle.animate.scale(1.5), diameter_line.animate.scale(1.5))

        # Show A changing dynamically
        dynamic_area = always_redraw(lambda: MathTex(
            f"A = \\frac{{\\pi}}{{4}} ({diameter_line.get_length():.1f})^2"
        ).next_to(circle, UP))

        self.add(dynamic_area)
        self.wait(3)

        # Graph of A vs D
        axes = Axes(
            x_range=[0, 15, 5], y_range=[0, 1000, 250],
            x_length=6, y_length=4,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT)
        graph = axes.plot(lambda x: (PI / 4) * x**2, color=BLUE, x_range=[0, 15])
        tangent_line = axes.get_secant_slope_group(
            10, graph, dx=0.1, secant_line_color=GREEN
        )

        self.play(Create(axes), Create(graph))
        self.play(Create(tangent_line))
        self.wait(3)

        # Step 6: Conclusion
        summary = MathTex(
            "\\text{At } D = 10: \\, \\text{Rate of Change} = 15.71 \\text{m}^2/\\text{m}"
        ).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(3)
