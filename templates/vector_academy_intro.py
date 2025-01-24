from manim import *

# Custom configuration for Full HD resolution and desired frame rate
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

class VectorAcademyIntro(Scene):
    def construct(self):
        # Total duration management
        total_duration = 0

        # 1. Welcome Animation (Approx. 5 seconds)
        welcome_text = Text("Welcome to", font_size=72, color=YELLOW)
        academy_text = Text("Vector Academy", font_size=96, t2c={"Vector": BLUE, "Academy": GREEN})
        intro_group = VGroup(welcome_text, academy_text).arrange(DOWN, buff=0.2)
        intro_group.move_to(ORIGIN)

        # Animate the introduction
        self.play(FadeIn(intro_group))
        self.wait(2)  # Hold on screen
        total_duration += 2 + intro_group.get_animation_time()

        self.play(FadeOut(intro_group))
        total_duration += intro_group.get_animation_time()

        # 2. Transition to Graph Animations (Approx. 10 seconds)
        # Set up the coordinate plane
        plane = NumberPlane(x_range=[-5, 5], y_range=[-5, 5], background_line_style={
            "stroke_color": BLUE_E,
            "stroke_width": 1,
            "stroke_opacity": 0.5
        })
        self.play(Create(plane))
        total_duration += plane.get_animation_time()

        # Define functions to plot
        functions = [
            lambda x: x,                     # Linear function
            lambda x: x**2,                  # Quadratic function
            lambda x: x**3 / 5,              # Cubic function
            lambda x: np.cos(x),             # Cosine function (Even function)
            lambda x: np.sin(x),             # Sine function (Odd function)
        ]
        function_labels = [
            "Linear Function",
            "Quadratic Function",
            "Cubic Function",
            "Even Function",
            "Odd Function"
        ]
        colors = [RED, GREEN, ORANGE, PURPLE, TEAL]

        # Plot functions one by one
        for func, label, color in zip(functions, function_labels, colors):
            graph = plane.get_graph(func, color=color)
            graph_label = MathTex(label, font_size=36).next_to(graph, UP)
            self.play(Create(graph), Write(graph_label))
            self.wait(0.5)  # Brief pause to appreciate the graph
            total_duration += graph.get_animation_time() + graph_label.get_animation_time() + 0.5
            # Optional: Fade out previous graph and label to avoid clutter
            self.play(FadeOut(graph), FadeOut(graph_label))
            total_duration += graph.get_animation_time() + graph_label.get_animation_time()

        # 3. Chapter Introduction (Approx. 5 seconds)
        chapter_text = Text("Calculus - Chapter 1: Functions", font_size=64, color=YELLOW)
        chapter_text.to_edge(UP)
        self.play(Write(chapter_text))
        self.wait(2)
        total_duration += chapter_text.get_animation_time() + 2

        # Fade out everything to conclude the intro
        self.play(FadeOut(plane), FadeOut(chapter_text))
        total_duration += plane.get_animation_time() + chapter_text.get_animation_time()

        # Ensure total duration is under 20 seconds
        print(f"Total duration: {total_duration} seconds")