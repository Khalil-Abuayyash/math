from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate

class PrintStatementIntroduction(Scene):
    def construct(self):
        # **FRAME SETUP**
        # Background to simulate a code editor
        editor_background = Rectangle(
            width=12, height=21, color=WHITE, fill_opacity=0.1, stroke_width=0
        ).move_to(ORIGIN)

        # Header bar
        header_bar = Rectangle(
            width=13, height=0.8, color=GRAY, fill_opacity=0.2, stroke_width=0
        ).move_to([0, 12, 0])  # Position at the top

        # Window buttons (simulated)
        green_circle = Circle(radius=0.2, color=GREEN, fill_opacity=1).move_to([4, 12, 0])
        yellow_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([5, 12, 0])
        red_circle = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([6, 12, 0])

        # File name
        file_name = Text("hello_world.py", font_size=50, color=WHITE).move_to([-5, 12, 0])

        # Content area (optional rectangle)
        content_area = Rectangle(
            width=13, height=22, color=WHITE, fill_opacity=0
        ).move_to(ORIGIN)

        # **CONTENT AREA ENHANCEMENTS**
        # Define the code lines
        line0 = Text('print("Hello, World!")', font_size=40, color=WHITE)

        # Position the code line at the top inside the content area, aligned to the left
        line0.next_to(content_area.get_top(), DOWN, buff=1).to_edge(LEFT, buff=1.5)

        # Add frame elements to the scene
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)

        # **Animate the Code Line**
        self.play(Write(line0))
        self.wait(0.5)

        # **Highlight the print statement**
        print_highlight = self.create_highlight(line0, color=YELLOW)
        self.play(FadeIn(print_highlight))
        self.wait(0.5)

        # **Create an output box to display the output**
        output_box = Rectangle(
            width=8, height=3, color=WHITE, fill_opacity=0.1, stroke_width=1
        ).move_to([0, -3, 0])

        # Output box title
        output_title = Text("Output", font_size=30, color=WHITE).next_to(output_box, UP)
        self.add(output_box, output_title)

        # **Display the output of the print statement**
        # Animate the print action
        output_text = Text("Hello, World!", font_size=40, color=WHITE)
        output_text.move_to(output_box.get_center())

        # Simulate pressing Enter/Running the code
        enter_text = Text("Running code...", font_size=30, color=GREEN)
        enter_text.next_to(line0, DOWN, buff=0.5).align_to(line0, LEFT)
        self.play(Write(enter_text))
        self.wait(1)
        self.play(FadeOut(enter_text))

        # Show the output appearing in the output box
        self.play(FadeIn(output_text))
        self.wait(2)

        # **Conclusion**
        conclusion_text = Text(
            'The print statement displays text on the screen!', 
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