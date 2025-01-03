from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate

class VariablesIntroduction(Scene):
    def construct(self):
        # **FRAME SETUP**
        # Simulate a code editor
        editor_background = Rectangle(
            width=12, height=21, color=WHITE, fill_opacity=0.1, stroke_width=0
        ).move_to(ORIGIN)

        # Header bar
        header_bar = Rectangle(
            width=13, height=0.8, color=GRAY, fill_opacity=0.2, stroke_width=0
        ).move_to([0, 12, 0])  # Position at the top

        # Window buttons
        green_circle = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to([4, 12, 0])
        yellow_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([5, 12, 0])
        red_circle = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([6, 12, 0])

        # File name
        file_name = Text("variables.py", font_size=50, color=WHITE).move_to([-5, 12, 0])

        # Content area
        content_area = Rectangle(
            width=13, height=22, color=WHITE, fill_opacity=0
        ).move_to(ORIGIN)

        # **CODE LINES**
        line0 = Text('x = 5', font_size=40, color=WHITE)
        line1 = Text('y = 10', font_size=40, color=WHITE)
        line2 = Text('z = x + y', font_size=40, color=WHITE)
        line3 = Text('print(z)', font_size=40, color=WHITE)

        # Positioning code lines
        line0.next_to(content_area.get_top(), DOWN, buff=1).to_edge(LEFT, buff=1.5)
        line1.next_to(line0, DOWN, aligned_edge=LEFT, buff=0.3)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.3)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.3)

        # **ADD FRAME ELEMENTS**
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)

        # **ANIMATE CODE LINES**
        self.play(Write(line0))
        self.wait(0.5)

        # Highlight x = 5
        x_highlight = self.create_highlight(line0, color=BLUE)
        self.play(FadeIn(x_highlight))
        self.wait(0.5)
        self.play(FadeOut(x_highlight))

        self.play(Write(line1))
        self.wait(0.5)

        # Highlight y = 10
        y_highlight = self.create_highlight(line1, color=GREEN)
        self.play(FadeIn(y_highlight))
        self.wait(0.5)
        self.play(FadeOut(y_highlight))

        self.play(Write(line2))
        self.wait(0.5)

        # Highlight z = x + y
        z_highlight = self.create_highlight(line2, color=YELLOW)
        self.play(FadeIn(z_highlight))
        self.wait(0.5)
        self.play(FadeOut(z_highlight))

        self.play(Write(line3))
        self.wait(0.5)

        # **Create an output box to display the output**
        output_box = Rectangle(
            width=8, height=3, color=WHITE, fill_opacity=0.1, stroke_width=1
        ).move_to([0, -3, 0])

        # Output box title
        output_title = Text("Output", font_size=30, color=WHITE).next_to(output_box, UP)
        self.add(output_box, output_title)

        # **Simulate Running the Code**
        run_text = Text("Running code...", font_size=30, color=GREEN)
        run_text.next_to(line3, DOWN, buff=0.5).align_to(line3, LEFT)
        self.play(Write(run_text))
        self.wait(1)
        self.play(FadeOut(run_text))

        # **Display the output of print(z)**
        output_text = Text("15", font_size=40, color=WHITE)
        output_text.move_to(output_box.get_center())
        self.play(FadeIn(output_text))
        self.wait(2)

        # **Conclusion**
        conclusion_text = Text(
            'Variables store values we can use!', 
            font_size=35, color=GREEN
        )
        conclusion_text.next_to(output_box, DOWN, buff=1)
        self.play(Write(conclusion_text))
        self.wait(3)

    def create_highlight(self, mobject, color=YELLOW):
        """Utility function to create a highlight rectangle around a code line."""
        highlight = Rectangle(
            width=mobject.width + 0.5,
            height=mobject.height + 0.2,
            color=color,
            fill_opacity=0.2,
            stroke_width=0,
        ).move_to(mobject)
        return highlight