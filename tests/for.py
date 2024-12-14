from manim import *

config.pixel_width = 1080   # Set width (e.g., Full HD resolution)
config.pixel_height = 1920  # Set height

class ForLoopExplanation(Scene):
    def construct(self):
        # Create a small yellow circle
        circle = Circle(radius=0.2, color=YELLOW, fill_opacity=1)
        
        # Move the circle to the top-left corner
        circle.to_corner(UL)  # UL stands for "Upper Left"
        
        # Add the circle to the scene
        self.play(FadeIn(circle))
        self.wait(2)  # Keep it on the screen for 2 seconds
        
        # Set up a title
        title = Text("Understanding the for loop in Python", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Code lines
        code_lines = [
            "# Example of a for loop",  # Comment
            "numbers = [1, 2, 3, 4, 5]",  # Variable definition
            "for num in numbers:",  # For loop header
            "    print(num)  # Output each number",  # Loop body
        ]

        # Positions for lines in the 'code editor'
        start_y = 2.5  # Starting height for the code lines
        line_positions = [start_y - i for i in range(len(code_lines))]

        code_texts = []
        for i, line in enumerate(code_lines):
            code = Text(line, font_size=24, font="Courier", color=WHITE).move_to(
                UP * line_positions[i]
            )
            code_texts.append(code)
            if line.startswith("#"):
                code.set_color(GREEN)  # Comments in green

        # Animating lines of code
        for code in code_texts:
            self.play(Write(code))

        # Explanation highlights
        explanation_box = RoundedRectangle(corner_radius=0.2, width=4, height=1, color=YELLOW)
        explanation_text = Text("", font_size=18, color=WHITE).move_to(explanation_box)
        explanation_group = VGroup(explanation_box, explanation_text).to_edge(UP, buff=1.5)
        
        self.play(FadeIn(explanation_group))

        # Output Box
        output_box = RoundedRectangle(corner_radius=0.2, width=4, height=2, color=BLUE)
        output_box.to_edge(DOWN, buff=1.5)
        output_title = Text("Output:", font_size=18).next_to(output_box.get_top(), DOWN * 0.5, aligned_edge=LEFT)
        output_text = Text("", font_size=24).move_to(output_box.get_center())

        self.play(FadeIn(output_box), Write(output_title), Write(output_text))

        # Highlight rectangle
        highlight_rect = SurroundingRectangle(code_texts[0], color=YELLOW, buff=0.1)
        self.play(FadeIn(highlight_rect))

        # Iterating through the lines
        for i in range(2, 4):  # Loop through the relevant lines of code
            self.play(Transform(highlight_rect, SurroundingRectangle(code_texts[i], color=YELLOW, buff=0.1)))
            
            if i == 2:  # For loop initialization
                self.play(
                    Transform(explanation_text, Text("The 'for' loop starts iterating.", font_size=18).move_to(explanation_box))
                )
                self.wait(1)
            elif i == 3:  # Loop body execution
                # Simulate the loop execution
                for j in range(1, 6):  # Loop over numbers
                    self.play(
                        Transform(explanation_text, Text(f"Currently printing: {j}", font_size=18).move_to(explanation_box)),
                        Transform(output_text, Text("\n".join(str(x) for x in range(1, j + 1)), font_size=24).move_to(output_box.get_center())),
                        Indicate(code_texts[3], color=YELLOW),
                    )
                    self.wait(0.5)

        # Closing Message
        closing_text = Text("That's how the for loop works in Python!", font_size=24).next_to(output_box, DOWN)
        self.play(Write(closing_text))
        self.wait(2)