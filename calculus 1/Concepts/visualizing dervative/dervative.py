from manim import *

class DerivativeGraph(Scene):
    def construct(self):
        # Define your function here (user can change this)
        f = lambda x: x**2
        
        # Set up axes
        axes_left = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 10, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
        ).shift(LEFT*3)
        
        axes_right = Axes(
            x_range=[-3, 3, 1],
            y_range=[-5, 10, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": WHITE},
        ).shift(RIGHT*3)
        
        # Calculate numerical derivative using central difference
        h = 0.001
        df = lambda x: (f(x + h) - f(x - h)) / (2*h)
        
        # Create graphs
        graph_f = axes_left.plot(f, color=BLUE)
        graph_df = axes_right.plot(df, color=RED)
        
        # Labels
        label_f = axes_left.get_graph_label(graph_f, "f(x)", direction=UP)
        label_df = axes_right.get_graph_label(graph_df, "f'(x)", direction=UP)
        
        # Titles
        title_left = Text("Function").next_to(axes_left, UP)
        title_right = Text("Derivative").next_to(axes_right, UP)
        
        # Animation sequence
        self.play(Create(axes_left), Create(axes_right), run_time=2)
        self.play(Write(title_left), Write(title_right))
        self.play(Create(graph_f), Create(graph_df), run_time=3)
        self.play(Write(label_f), Write(label_df))
        self.wait(3)