from manim import *

class FunctionDefinition(Scene):
    def construct(self):
        title = Text("What is a Function?").scale(0.8).to_edge(UP)
        definition = Text("A function is a relation that assigns exactly one output for each input.", font_size=24)
        graph = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )
        function_curve = graph.plot(lambda x: x**2, color=YELLOW)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(definition))
        self.wait(2)
        self.play(Create(graph), Create(function_curve))
        self.wait(3)

class DomainRange(Scene):
    def construct(self):
        title = Text("Domain and Range").scale(0.8).to_edge(UP)
        domain_text = Text("Domain: Set of all possible input values (x-values)", font_size=24).to_edge(LEFT)
        range_text = Text("Range: Set of all possible output values (y-values)", font_size=24).to_edge(RIGHT)
        graph = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": GREEN}
        )
        function_curve = graph.plot(lambda x: x**2, color=RED)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(domain_text), Write(range_text))
        self.wait(2)
        self.play(Create(graph), Create(function_curve))
        self.wait(3)

class VerticalLineTest(Scene):
    def construct(self):
        title = Text("Vertical Line Test").scale(0.8).to_edge(UP)
        explanation = Text("A function passes the test if no vertical line intersects it more than once.", font_size=24)
        graph = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": ORANGE}
        )
        function_curve = graph.plot(lambda x: x**2, color=BLUE)
        vertical_line = DashedLine(start=graph.c2p(1, -3), end=graph.c2p(1, 3), color=WHITE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation))
        self.wait(2)
        self.play(Create(graph), Create(function_curve))
        self.wait(1)
        self.play(Create(vertical_line))
        self.wait(3)

class IncreasingDecreasingFunction(Scene):
    def construct(self):
        title = Text("Increasing & Decreasing Functions").scale(0.8).to_edge(UP)
        increasing_text = Text("Increasing: Function moves up as x increases", font_size=24).to_edge(LEFT)
        decreasing_text = Text("Decreasing: Function moves down as x increases", font_size=24).to_edge(RIGHT)
        graph = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": PURPLE}
        )
        function_curve = graph.plot(lambda x: x**3, color=GREEN)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(increasing_text), Write(decreasing_text))
        self.wait(2)
        self.play(Create(graph), Create(function_curve))
        self.wait(3)

class EvenOddFunction(Scene):
    def construct(self):
        title = Text("Even & Odd Functions").scale(0.8).to_edge(UP)
        even_text = Text("Even: Symmetric about the y-axis", font_size=24).to_edge(LEFT)
        odd_text = Text("Odd: Symmetric about the origin", font_size=24).to_edge(RIGHT)
        graph = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": TEAL}
        )
        even_function = graph.plot(lambda x: x**2, color=RED)
        odd_function = graph.plot(lambda x: x**3, color=BLUE)
        
        self.play(Write(title))
        self.wait(1)
        self.play(Write(even_text), Write(odd_text))
        self.wait(2)
        self.play(Create(graph), Create(even_function))
        self.wait(1)
        self.play(Create(odd_function))
        self.wait(3)
