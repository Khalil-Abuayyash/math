from manim import *
import numpy as np  # Import numpy for array definitions

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate

class PythonIntroduction(Scene):
    def construct(self):
        # **Scene 1: What is Python?**
        self.intro_scene()
        self.wait(1)

        # **Scene 2: What can Python do?**
        self.what_can_python_do()
        self.wait(1)

        # **Scene 3: Why Python?**
        self.why_python()
        self.wait(1)

        # **Scene 4: Good to Know**
        self.good_to_know()
        self.wait(1)

        # **Scene 5: Python Syntax vs Other Languages**
        self.syntax_comparison()
        self.wait(2)

    def intro_scene(self):
        # Title
        title = Text("What is Python?", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Python logo replacement
        python_logo = Circle(radius=2, color=BLUE)
        python_text = Text("Python", font_size=50, color=WHITE).move_to(python_logo.get_center())
        python_logo_group = VGroup(python_logo, python_text).next_to(title, DOWN, buff=1)
        self.play(FadeIn(python_logo_group))
        self.wait(1)

        # Explanation text
        explanation = Text(
            "Python is a popular programming language \n used to create software, websites, games, and more!",
            font_size=40,
            color=WHITE
        ).next_to(python_logo_group, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(3)

    def what_can_python_do(self):
        # Clear previous scene
        self.clear()

        # Title
        title = Text("What can Python do?", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # List of things Python can do
        points = VGroup(
            Text("- Build websites", font_size=40),
            Text("- Develop games", font_size=40),
            Text("- Analyze data", font_size=40),
            Text("- Control robots", font_size=40),
            Text("- Create apps", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=2)

        # Simple shapes corresponding to each point
        shapes = VGroup(
            Square(side_length=0.5, color=BLUE),
            Circle(radius=0.25, color=GREEN),
            Triangle().scale(0.5).set_color(RED),
            self.create_diamond().set_color(PURPLE).scale(0.5),
            RegularPolygon(n=6).set_color(ORANGE).scale(0.5),
        ).arrange(DOWN, buff=0.75).next_to(points, LEFT, buff=1)

        # Animate items with shapes
        for shape, point in zip(shapes, points):
            self.play(FadeIn(shape), Write(point))
            self.wait(0.5)

    def create_diamond(self):
        # Define a diamond shape using Polygon
        diamond = Polygon(
            np.array([0, 0.5, 0]),  # Top point
            np.array([0.5, 0, 0]),  # Right point
            np.array([0, -0.5, 0]), # Bottom point
            np.array([-0.5, 0, 0])  # Left point
        )
        return diamond

    def why_python(self):
        # Clear previous scene
        self.clear()

        # Title
        title = Text("Why Python?", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Reasons to love Python
        reasons = VGroup(
            Text("- Easy to read and write code", font_size=40),
            Text("- Huge community and support", font_size=40),
            Text("- Lots of libraries and tools", font_size=40),
            Text("- Great for beginners and pros", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=2)

        # Animate reasons
        for reason in reasons:
            self.play(Write(reason))
            self.wait(0.5)

    def good_to_know(self):
        # Clear previous scene
        self.clear()

        # Title
        title = Text("Good to Know", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Tips about Python
        tips = VGroup(
            Text("- Python is free and open-source", font_size=40),
            Text("- Named after Monty Python!", font_size=40),
            Text("- Used by companies like Google and NASA", font_size=40),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(title, DOWN, buff=1).to_edge(LEFT, buff=2)

        # Animate tips
        for tip in tips:
            self.play(Write(tip))
            self.wait(0.5)

    def syntax_comparison(self):
        # Clear previous scene
        self.clear()

        # Title
        title = Text("Python Syntax vs Others", font_size=60, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Python code example
        python_code = Text(
            'print("Hello, World!")',
            font_size=50,
            color=WHITE
        ).to_edge(LEFT, buff=2).shift(UP * 1)

        python_label = Text("Python", font_size=40, color=BLUE).next_to(python_code, UP, buff=0.5)

        # Other language code example (e.g., Java)
        java_code = Text(
            'System.out.println("Hello, World!");',
            font_size=40,
            color=WHITE
        ).next_to(python_code, DOWN, buff=2).align_to(python_code, LEFT)

        java_label = Text("Java", font_size=40, color=GREEN).next_to(java_code, UP, buff=0.5)

        # Animate code examples
        self.play(Write(python_label), Write(python_code))
        self.wait(1)
        self.play(Write(java_label), Write(java_code))
        self.wait(1)

        # Highlight simplicity
        simple_arrow = Arrow(
            start=python_code.get_right() + RIGHT * 0.5,
            end=java_code.get_right() + RIGHT * 0.5,
            stroke_width=5,
            color=YELLOW
        ).scale(1.5)

        simple_text = Text("Simpler!", font_size=40, color=YELLOW).next_to(simple_arrow, RIGHT, buff=0.5)

        self.play(GrowArrow(simple_arrow), Write(simple_text))
        self.wait(2)

        # Conclusion
        conclusion = Text(
            "Python's syntax is cleaner and easier to learn!",
            font_size=35,
            color=GREEN
        ).next_to(java_code, DOWN, buff=2).to_edge(LEFT, buff=2)
        self.play(Write(conclusion))
        self.wait(3)