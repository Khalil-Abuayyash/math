from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate

class WhileLoopExplanation(Scene):
    def construct(self):
        # **FRAME SETUP**
        # Background to simulate code editor
        editor_background = Rectangle(
            width=12, height=21, color=WHITE, fill_opacity=0.1, stroke_width=0
        ).move_to(ORIGIN)

        # Header bar
        header_bar = Rectangle(
            width=13, height=0.8, color=GRAY, fill_opacity=0.2, stroke_width=0
        ).move_to([0, 12, 0])  # Position at the top

        # Window buttons
        green_circle = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to([4, 12, 0])
        yellow_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([5, 12, 0])
        red_circle = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([6, 12, 0])

        # File name
        file_name = Text("while_loop.py", font_size=50, color=WHITE).move_to([-5, 12, 0])

        # Content area (optional rectangle)
        content_area = Rectangle(
            width=13, height=22, color=WHITE, fill_opacity=0
        ).move_to(ORIGIN)

        # **CONTENT AREA ENHANCEMENTS**
        # Define code lines
        line0 = Text("count = 0", font_size=40, color=WHITE)
        line1 = Text("while count < 5:", font_size=40, color=WHITE)
        line2 = Text("print(count)", font_size=40, color=WHITE)
        line3 = Text("count += 1", font_size=40, color=WHITE)

        # Indentation unit
        indent_unit = RIGHT * 0.5

        # **Align Code Statements**
        # Position line0 at the top, aligned to the left
        line0.next_to(content_area.get_top(), DOWN, buff=1).to_edge(LEFT, buff=1.5)

        # Position subsequent lines with indentation
        line1.next_to(line0, DOWN, aligned_edge=LEFT, buff=0.3)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.3).shift(indent_unit)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.3).shift(indent_unit)

        # Add frame elements
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)

        # **Animate Code Lines**
        # Write 'count = 0'
        self.play(Write(line0))
        self.wait(0.5)

        # Highlight variable initialization
        count_highlight = self.create_highlight(line0, color=YELLOW)
        self.play(FadeIn(count_highlight))
        self.wait(0.5)
        self.play(FadeOut(count_highlight))

        # Write 'while count < 5:'
        self.play(Write(line1))
        self.wait(0.5)

        # Write 'print(count)'
        self.play(Write(line2))
        self.wait(0.5)

        # Write 'count += 1'
        self.play(Write(line3))
        self.wait(0.5)

        # **Create an output box to display the outputs**
        output_box = Rectangle(
            width=6, height=4, color=WHITE, fill_opacity=0.1, stroke_width=1
        ).move_to([0, -3, 0])

        # Output box title
        output_title = Text("Output", font_size=30, color=WHITE).next_to(output_box, UP)
        self.add(output_box, output_title)

        # **Visualize the Variable 'count'**
        # Display 'count = 0' positioned to the right of the while loop code
        count_value = Text("count = 0", font_size=40, color=WHITE)
        count_value.next_to(line1, RIGHT, buff=3)  # Adjusted position
        self.play(FadeIn(count_value))
        self.wait(0.5)

        # **Animate the While Loop Execution**
        count = 0
        output_texts = VGroup()
        max_iterations = 5
        while count < max_iterations:
            # Highlight 'while count < 5:'
            while_highlight = self.create_highlight(line1, color=YELLOW)
            self.play(FadeIn(while_highlight))
            self.wait(0.2)

            # Check condition
            condition_text = Text(f"Is {count} < 5?", font_size=30, color=YELLOW)
            condition_text.next_to(while_highlight, RIGHT, buff=0.5)
            self.play(FadeIn(condition_text))
            self.wait(0.5)
            self.play(FadeOut(condition_text))
            self.play(FadeOut(while_highlight))

            # Highlight 'print(count)'
            print_highlight = self.create_highlight(line2, color=RED)
            self.play(FadeIn(print_highlight))
            self.wait(0.2)

            # Display output
            output_line = Text(str(count), font_size=30, color=WHITE)
            if len(output_texts) == 0:
                output_line.next_to(output_box.get_top(), DOWN, buff=0.2).align_to(
                    output_box.get_left(), LEFT
                ).shift(RIGHT * 0.2)
            else:
                output_line.next_to(output_texts[-1], DOWN, aligned_edge=LEFT)
            output_texts.add(output_line)

            # Animate the Output Line
            self.play(Write(output_line))
            self.wait(0.5)
            self.play(FadeOut(print_highlight))

            # Highlight 'count += 1'
            increment_highlight = self.create_highlight(line3, color=BLUE)
            self.play(FadeIn(increment_highlight))
            self.wait(0.2)
            self.play(FadeOut(increment_highlight))

            # Update 'count' value display
            count += 1
            new_count_value = Text(f"count = {count}", font_size=40, color=WHITE)
            new_count_value.move_to(count_value)
            self.play(Transform(count_value, new_count_value))
            self.wait(0.5)

        # **After Loop Ends**
        # Indicate that the condition is no longer true
        end_text = Text(f"Is {count} < 5? False", font_size=30, color=RED)
        end_text.next_to(while_highlight, RIGHT, buff=0.5)
        self.play(FadeIn(end_text))
        self.wait(1)
        self.play(FadeOut(end_text))

        # Conclusion
        conclusion = Text("Loop exited when count = 5", font_size=35, color=GREEN)
        conclusion.next_to(output_box, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)

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