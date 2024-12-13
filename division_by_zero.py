from manim import *

config.pixel_width = 1080   # Set width (e.g., Full HD resolution)
config.pixel_height = 1920  # Set height
config.frame_rate = 60      # Set frame rate
config.background_color = "#1e1e2e"  # Dark background for better contrast

class DividingByZeroScene(Scene):
    def construct(self):

        # Main title
        main_title = Text("Why Division by Zero is Not Allowed", font_size=70, gradient=(BLUE, PURPLE))
        main_title.to_edge(UP)

        # Section 1 Title: Division is the Reverse of Multiplication
        section_1_title = Text("Section 1: Division is the Reverse of Multiplication", font_size=60, color=YELLOW)
        section_1_title.next_to(main_title, DOWN, buff=0.5)

        # Section 1 Explanation
        division_reverse_text = MathTex("a \\div b = c \\iff a = b \\times c")
        division_reverse_text.font_size = 50
        division_reverse_text.set_color(WHITE)
        division_reverse_text.next_to(section_1_title, DOWN, buff=0.5)

        # Section 2 Title: Division by Zero Leads to Contradiction
        section_2_title = Text("Section 2: Division by Zero Leads to Contradiction", font_size=60, color=YELLOW)
        section_2_title.next_to(main_title, DOWN, buff=0.5)

        # Section 2 Explanation
        contradiction_text_1 = Text("Let us assume division by zero is possible.", font_size=50)
        contradiction_text_1.set_color(WHITE)

        contradiction_text_2 = Text("For example, let’s assume", font_size=50)
        contradiction_text_2.set_color(WHITE)

        contradiction_text_3 = MathTex("5 \\div 0 = x")
        contradiction_text_3.set_color(WHITE)

        contradiction_text_4 = Text("This means:", font_size=50)
        contradiction_text_4.set_color(WHITE)

        contradiction_text_5 = MathTex("5 = 0 \\times x")
        contradiction_text_5.set_color(WHITE)

        contradiction_text_6 = Text("But 0 multiplied by any number is 0!", font_size=50)
        contradiction_text_6.set_color(WHITE)

        contradiction_text_7 = Text("This leads to a contradiction, so division by zero is not allowed.", font_size=50)
        contradiction_text_7.set_color(WHITE)

        # Arrange the texts in vertical groups for Section 2
        contradiction_group = VGroup(
            contradiction_text_1, contradiction_text_2, contradiction_text_3,
            contradiction_text_4, contradiction_text_5, contradiction_text_6, contradiction_text_7
        )
        contradiction_group.arrange(DOWN, buff=0.5)
        contradiction_group.next_to(section_2_title, DOWN, buff=0.5)

        # Section 1 animations
        self.play(Write(main_title))
        self.play(Write(section_1_title))
        self.play(Write(division_reverse_text))

        self.play(
            FadeOut(section_1_title),
            # Transform(section_1_title, section_2_title),  # Replace main title with section 2 title
            FadeOut(division_reverse_text),
            Write(contradiction_group, run_time=5)  # Show contradiction explanation
        )