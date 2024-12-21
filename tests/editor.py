from manim import *

# Configure resolution for a vertical (portrait) video
config.pixel_width = 1080
config.pixel_height = 1920

class CodeEditorFrame(Scene):
    def construct(self):
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

        file_name = Text("code.py", font_size=50, color=WHITE).move_to([-5, 12, 0])

        # Main content area (optional rectangle to highlight the "code area")
        content_area = Rectangle(
            width=13, height=22, color=WHITE, fill_opacity=0
        ).move_to(ORIGIN)

        output_area = Rectangle(
            width=5, height=5, color=YELLOW, fill_opacity=0.5
        ).move_to(ORIGIN)

        line0 = Text("nums = [0,1,2,3,4,5]", font_size=40, color=WHITE)
        line1 = Text("for num in nums:", font_size=40, color=WHITE)
        line2 = Text("print(num * 2)", font_size=40, color=WHITE)
        line3 = Text("print('Hello World')", font_size=40, color=WHITE)
        line4 = Text("elif string == 'Bye':", font_size=40, color=WHITE)
        line5 = Text("break", font_size=40, color=WHITE)

        group = VGroup(line0, line1, line2)
        # group = VGroup(line0, line1, line2, line3, line4, line5)
        group.arrange(direction=DOWN, buff=0.5)
        top = group.get_top()
        position = np.array([-3, 10, 0])
        
        # left = group.get_left()
        # for text in [line0, line1, line2, line3, line4, line5]:
        for text in [line0, line1, line2]:
            text.align_to(ORIGIN, LEFT)


        group.move_to(position - top)
        # group.add(line3)
        # group.arrange(DOWN, buff=0.5)

        line2.shift(RIGHT * 0.5)
        line3.shift(RIGHT * 1)
        line4.shift(RIGHT * 0.5)
        line5.shift(RIGHT * 1)

        # Add all elements to the scene
        self.add(editor_background)
        self.add(header_bar)
        self.add(green_circle, yellow_circle, red_circle)
        self.add(file_name)
        self.add(content_area)
        # self.play(FadeIn(line))
        self.play(Write(group))
        self.wait()
        self.play(FadeIn(output_area))
        self.wait()