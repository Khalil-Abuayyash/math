from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920

class CodeEditorFrame(Scene):
    def construct(self):
        # **FRAME SETUP (Same as your original code)**
        # Add a background rectangle to simulate the editor
        editor_background = Rectangle(
            width=12, height=21, color=WHITE, fill_opacity=0.1, stroke_width=0
        ).set_color(WHITE).move_to(ORIGIN)
    
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
        line0 = Text("nums = [0,1,2,3,4,5]", font_size=40, color=WHITE)
        line1 = Text("for num in nums:", font_size=40, color=WHITE)
        line2 = Text("print(num * 2)", font_size=40, color=WHITE)
    
        # Determine the indentation unit (adjust as needed)
        indent_unit = RIGHT * 0.5  # You can adjust 0.5 to change indent size
    
        # Indent the print statement by shifting it to the right by 1 step
        line2.shift(indent_unit)
    
        # Position line0 at the top inside the content area
        line0.next_to(content_area.get_top(), DOWN, buff=1)
        line0.shift(LEFT * 4)
        
        # Position line1 below line0, aligned to the left of line0
        line1.next_to(line0, DOWN, aligned_edge=LEFT, buff=0.3)
        
        # Position line2 below line1, aligned to its own left (already shifted)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.3)
    
        # Add all elements to the scene
        # **Add the frame elements first (without any changes)**
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)
    
        # **Add the content (code lines) after the whole frame is set up**
        self.play(Write(line0))
        self.wait(0.5)
    
        # Highlight 'nums = [0,1,2,3,4,5]' to indicate variable assignment
        nums_rect = SurroundingRectangle(line0, color=YELLOW, buff=0.1)
        self.play(Create(nums_rect))
        self.wait(0.5)
        self.play(FadeOut(nums_rect))
    
        # Write 'for num in nums:'
        self.play(Write(line1))
        self.wait(0.5)
    
        # Write 'print(num * 2)' shifted by the desired indentation
        line2.shift(indent_unit)
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
    
        # List to keep track of output lines
        output_texts = VGroup()
    
        # Simulate the execution of the loop
        nums = [0, 1, 2, 3, 4, 5]
        for num in nums:
            # Highlight 'for num in nums:'
            loop_rect = SurroundingRectangle(line1, color=YELLOW, buff=0.1)
            self.play(Create(loop_rect))
            self.wait(0.2)
            self.play(FadeOut(loop_rect))
    
            # Highlight 'print(num * 2)'
            print_rect = SurroundingRectangle(line2, color=YELLOW, buff=0.1)
            self.play(Create(print_rect))
            self.wait(0.2)
    
            # Display output in output box
            output_line = Text(str(num * 2), font_size=30, color=WHITE)
            if len(output_texts) == 0:
                output_line.next_to(output_box.get_top(), DOWN, buff=0.2).align_to(output_box.get_left(), LEFT).shift(RIGHT * 0.2)
            else:
                output_line.next_to(output_texts[-1], DOWN, aligned_edge=LEFT)
            output_texts.add(output_line)
            self.play(Write(output_line))
            self.wait(0.2)
    
            self.play(FadeOut(print_rect))
    
        self.wait(2)