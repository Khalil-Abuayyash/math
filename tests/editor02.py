from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30  # Optional: Set frame rate


class CodeEditorFrame(Scene):
    def construct(self):
        # **FRAME SETUP**
        # Add a background rectangle to simulate the editor
        editor_background = Rectangle(
            width=12, height=21, color=WHITE, fill_opacity=0.1, stroke_width=0
        ).move_to(ORIGIN)

        # Create a header bar
        header_bar = Rectangle(
            width=13, height=0.8, color=GRAY, fill_opacity=0.2, stroke_width=0
        ).move_to([0, 12, 0])  # Position the bar at the top

        # Add circles to simulate window buttons
        green_circle = Circle(radius=0.2, color=BLUE, fill_opacity=1).move_to([4, 12, 0])
        yellow_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1).move_to([5, 12, 0])
        red_circle = Circle(radius=0.2, color=RED, fill_opacity=1).move_to([6, 12, 0])

        # File name
        file_name = Text("code.py", font_size=50, color=WHITE).move_to([-5, 12, 0])

        # Main content area (optional rectangle to highlight the "code area")
        content_area = Rectangle(
            width=13, height=22, color=WHITE, fill_opacity=0
        ).move_to(ORIGIN)

        # **CONTENT AREA ENHANCEMENTS**
        # Define code lines
        line0 = Text("nums = [0, 1, 2, 3, 4, 5]", font_size=40, color=WHITE)
        line1 = Text("for num in nums:", font_size=40, color=WHITE)
        line2 = Text("print(num * 2)", font_size=40, color=WHITE)

        # Determine the indentation unit (adjust as needed)
        indent_unit = RIGHT * 0.5  # Adjust to change indent size

        # **1. Aligning Code Statements to Appear from the Left**
        # Position line0 at the top inside the content area, aligned to the left edge of the header bar
        # Calculate the left edge of the header bar
        header_left_edge = header_bar.get_left() + RIGHT * 1  # Adjust buff as needed

        # Position line0 aligned to the left edge
        line0.next_to(content_area.get_top(), DOWN, buff=1).to_edge(LEFT, buff=1.5)
        # Remove the shift to the right (indent_unit) to align to the left
        # If indentation is needed, apply it to subsequent lines only

        # Position line1 below line0, aligned to the left of line0
        line1.next_to(line0, DOWN, aligned_edge=LEFT, buff=0.3)

        # Position line2 below line1, aligned to its own left (apply indentation)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.3)
        line2.shift(indent_unit)  # Indentation applied only to line2

        # Add all elements to the scene
        # Add the frame elements first (without any changes)
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)

        # **Add the content (code lines) after the whole frame is set up**
        self.play(Write(line0))
        self.wait(0.5)

        # **Replace SurroundingRectangle with Yellow Highlight**
        # Highlight 'nums = [0, 1, 2, 3, 4, 5]' to indicate variable assignment
        nums_highlight = Rectangle(
            width=line0.width + 0.5,  # Add some padding
            height=line0.height + 0.2,
            color=YELLOW,
            fill_opacity=0.2,  # Semi-transparent
            stroke_width=0,
        ).move_to(line0)  # Align the highlight with the text
        self.play(FadeIn(nums_highlight))
        self.wait(0.5)
        self.play(FadeOut(nums_highlight))

        # Write 'for num in nums:'
        self.play(Write(line1))
        self.wait(0.5)

        # Write 'print(num * 2)' shifted by the desired indentation
        self.play(Write(line2))
        self.wait(0.5)

        # **Emphasize the importance of indentation**
        # Create a brace pointing to the indentation
        indent_brace = BraceBetweenPoints(
            line1.get_left(), line2.get_left(), direction=RIGHT, color=YELLOW
        )
        indent_text = Text("Indentation is important!", font_size=30, color=YELLOW)
        indent_brace.next_to(indent_brace, RIGHT, buff=3.8)
        indent_text.next_to(indent_brace, RIGHT, buff=0.5)

        # Animate the brace and text
        self.play(Create(indent_brace), Write(indent_text))
        self.wait(2)
        self.play(FadeOut(indent_brace), FadeOut(indent_text))

        # **Create an output box to display the outputs**
        output_box = Rectangle(
            width=6, height=4, color=WHITE, fill_opacity=0.1, stroke_width=1
        ).move_to([0, -3, 0])  # Move to center below the code

        # Output box title
        output_title = Text("Output", font_size=30, color=WHITE).next_to(output_box, UP)
        self.add(output_box, output_title)

        # **Step 1: Visualize the nums array**
        nums_array = VGroup(
            *[
                Text(str(num), font_size=40, color=WHITE)
                for num in [0, 1, 2, 3, 4, 5]
            ]
        ).arrange(RIGHT, buff=1).shift(UP * 3)  # Position above the code area

        # Add brackets to resemble an array
        left_bracket = Text("[", font_size=40, color=WHITE).next_to(nums_array, LEFT, buff=0.1)
        right_bracket = Text("]", font_size=40, color=WHITE).next_to(nums_array, RIGHT, buff=0.1)

        # Group the array elements and brackets
        nums_visual = VGroup(left_bracket, nums_array, right_bracket)

        # Add the visual nums array to the scene
        self.play(FadeIn(nums_visual))
        self.wait(1)

        # **Step 2: Add the Pointer (Arrow Above Numbers)**
        # Create a downward-pointing arrow above the first element with increased size
        pointer = Arrow(
            start=nums_array[0].get_top() + UP * 0.8,  # Increased UP multiplier for higher position
            end=nums_array[0].get_top() + UP * 0.2,    # Pointing down to the number
            buff=0,
            color=YELLOW,
            stroke_width=20,      # Increased stroke width for thickness
            tip_length=0.5,      # Increased tip length for a larger arrowhead
        ).scale(1.5)  # Scaled the arrow to make it larger overall
        self.play(GrowArrow(pointer))
        self.wait(1)

        # **List to keep track of output lines**
        output_texts = VGroup()

        # **Step 3: Animate the Pointer with the Loop**
        nums = [0, 1, 2, 3, 4, 5]
        for i, num in enumerate(nums):
            target = nums_array[i]

            # **Move the Pointer to the Current Element**
            # Recalculate start and end positions for the arrow
            new_start = target.get_top() + UP * 0.8  # Higher above the number
            new_end = target.get_top() + UP * 0.2    # Pointing down to the number
            self.play(pointer.animate.put_start_and_end_on(new_start, new_end), run_time=0.5)
            self.wait(0.3)

            # **Highlight 'for num in nums:'**
            # Replace SurroundingRectangle with Yellow Highlight
            loop_highlight = Rectangle(
                width=line1.width + 0.5,
                height=line1.height + 0.2,
                color=YELLOW,
                fill_opacity=0.2,
                stroke_width=0,
            ).move_to(line1)
            self.play(FadeIn(loop_highlight))
            self.wait(0.2)
            self.play(FadeOut(loop_highlight))

            # **Highlight 'print(num * 2)'**
            # Replace SurroundingRectangle with Yellow Highlight
            print_highlight = Rectangle(
                width=line2.width + 0.5,
                height=line2.height + 0.2,
                color=YELLOW,
                fill_opacity=0.2,
                stroke_width=0,
            ).move_to(line2)
            self.play(FadeIn(print_highlight))
            self.wait(0.2)

            # **Display Output in Output Box**
            output_line = Text(str(num * 2), font_size=30, color=WHITE)
            if len(output_texts) == 0:
                output_line.next_to(output_box.get_top(), DOWN, buff=0.2).align_to(output_box.get_left(), LEFT).shift(RIGHT * 0.2)
            else:
                output_line.next_to(output_texts[-1], DOWN, aligned_edge=LEFT)
            output_texts.add(output_line)
            self.play(Write(output_line))
            self.wait(0.2)

            # Fade out the print highlight
            self.play(FadeOut(print_highlight))

        # Optional: Fade out the pointer after the loop completes
        self.play(FadeOut(pointer))
        self.wait(2)