from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class ForLoopExplanation(Scene):
    def construct(self):
        # Define consistent colors
        # LOOP_COLOR = GREEN
        LOOP_COLOR = YELLOW
        OUTPUT_COLOR = RED
        VS_CODE_BG = "#1E1E1E"
        VS_CODE_TEXT = "#D4D4D4"
        VS_CODE_KEYWORD = "#C586C0"  # for 'for' keyword
        VS_CODE_BUILTIN = "#DCDCAA"  # for 'print', 'range'
        VS_CODE_NUMBER = "#B5CEA8"   # for numbers

        # Code Section with VS Code styling
        code_background = RoundedRectangle(
            height=3.8,
            width=7,
            fill_color=VS_CODE_BG,
            fill_opacity=1,
            corner_radius=0.1,
            stroke_width=0
        )
        code_background.to_edge(UP, buff=1)

        bg_top_left = code_background.get_corner(UL)

        tab = VGroup()
        tab_body = Rectangle(
            width=2,
            height=0.4,
            fill_color=VS_CODE_BG,
            fill_opacity=1,
            stroke_width=0
        )
        tab_bottom = Rectangle(
            width=2,
            height=0.25,
            fill_color=VS_CODE_BG,
            fill_opacity=1,
            stroke_width=0
        )

        tab_top = Rectangle(
            width=1.9,
            height=0.05,
            fill_color=BLUE,
            fill_opacity=1,
        )
        
        left_triangle = Polygon(
            tab_body.get_bottom() + UP * 0.12,
            tab_body.get_bottom() + LEFT * 0.12,
            tab_body.get_bottom(),
            fill_color=VS_CODE_BG,
            fill_opacity=1,
            stroke_width=0,
        )
        
        right_triangle = Polygon(
            tab_body.get_bottom() + UP * 0.12,
            tab_body.get_bottom() + RIGHT * 0.12,
            tab_body.get_bottom(),
            fill_color=VS_CODE_BG,
            fill_opacity=1,
            stroke_width=0,
        )

        # Position and combine tab parts
        tab_body.next_to(bg_top_left, UP, buff=0.15)
        tab_bottom.next_to(tab_body, DOWN, buff=-0.1)
        tab_top.next_to(tab_body, UP, buff=0)

        left_triangle.next_to(tab_body, LEFT, buff=0)
        left_triangle.align_to(tab_body, DOWN).shift(DOWN * 0.2)

        right_triangle.next_to(tab_body, RIGHT, buff=0)
        right_triangle.align_to(tab_body, DOWN).shift(DOWN * 0.2)  
        tab.add(tab_body, tab_bottom, tab_top, left_triangle, right_triangle)
        tab.align_to(code_background, LEFT)
        tab.shift(RIGHT * 0.2)   
        file_name = Text("hello.py", font_size=23, color=WHITE)
        file_name.move_to(tab.get_center())

        circles_group = VGroup()
        for color in [RED, YELLOW, BLUE]:
            circle = Circle(radius=0.12, color=color, fill_opacity=1)
            circles_group.add(circle)
        circles_group.arrange(RIGHT, buff=0.2)

        circles_group.move_to(tab.get_center())
        circles_group.align_to(tab, RIGHT).shift(RIGHT * 4.4)

        code ='''print("Hello, World!")'''
        
        code_block = Code(
            code=code,
            tab_width=4,
            background_stroke_width=0,
            background="terminal",
            language="Python",
            font_size=30,
            line_spacing=1,
            style="native",
            font="Monospace"
        )
        code_block.move_to(code_background.get_center())
        
        # Output Section - Moved down and right
        output_box = VGroup(
            Rectangle(height=4, width=4.5, color=OUTPUT_COLOR),
            Text("Output", font_size=24, color=VS_CODE_TEXT).next_to(Rectangle(height=4, width=3.5), UP, buff=0.1)
        )
        output_box.next_to(code_background, DOWN, buff=2.5)
        # output_box.shift(RIGHT * 2)

        # Show initial setup
        self.play(
            Create(code_background),
            Create(tab),
            Create(file_name),
            Create(circles_group),
            Create(code_block),
            Create(output_box),
            # Create(variables_box)
        )

        # Output display
        outputs = VGroup()
        output_pointer = Triangle(color=OUTPUT_COLOR).scale(0.2).rotate(-PI/2)
        output_pointer.move_to(output_box.get_center() + LEFT * 1.5)

        array_elements = VGroup()
        explanation_texts = [
            "The print function displays", "text on the screen.",
            "The text to be displayed", "is enclosed in \"\".",
            "This tells Python it is", "a string of characters.",
            'In the example, the text', '"Hello, World!" is printed.'
        ]
        
        # Create the first text
        text_obj = Text(explanation_texts[0], font_size=34, color=VS_CODE_TEXT)
        array_elements.add(text_obj)
        text_obj.next_to(code_background, DOWN, buff=1)

        self.play(Create(array_elements))  # Display the first text
        self.wait(2)  # Wait before transitioning

        # Transition to the next text
        for idx in range(1, len(explanation_texts)):
            new_text = Text(explanation_texts[idx], font_size=34, color=VS_CODE_TEXT)
            new_text.move_to(array_elements[0].get_center())  # Move to the same position
            self.play(Transform(array_elements[0], new_text))  # Transition the old text to the new one
            self.wait(2)  # Wait before transitioning to the next explanation
        
        # Animation for each iteration
        for i in range(1):
            # Highlight for loop line
            self.play(code_block.code[0].animate.set_color(LOOP_COLOR))
            self.wait(0.5)
            
            # Return for loop line to original color
            self.play(code_block.code[0].animate.set_color(VS_CODE_TEXT))
            
            # Update output
            # new_output = Text(str(i), font_size=36, color=VS_CODE_NUMBER)
            new_output = Text("Hello, World!", font_size=30, color=VS_CODE_NUMBER)
            new_output.move_to(output_box.get_center() + UP * (1 - i * 0.5))
            
            # Show output
            self.play(
                FadeIn(new_output),
                output_pointer.animate.next_to(new_output, LEFT, buff=0.2)
            )

        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        