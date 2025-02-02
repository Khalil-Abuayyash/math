from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class FunctionExplanation(Scene):
    def construct(self):
        # Load SVG Assets
        youtube = SVGMobject("youtube-svgrepo-com.svg").scale(2)
        brain1 = SVGMobject("brain-svgrepo-com (1).svg").scale(1)
        brain2 = SVGMobject("brain-svgrepo-com (2).svg").scale(1)
     
        # Arrange SVGs (Brain on the left, YouTube in the center, and another Brain on the right)
        group = VGroup(brain1, youtube, brain2)
        group.arrange(RIGHT, buff=2)
        group.move_to(ORIGIN)
        
        # Display Initial Objects
        self.play(FadeIn(brain1), FadeIn(youtube), FadeIn(brain2))
        self.wait(2)
        
        positon_words = youtube.get_top() + UP*1
        # Add Text for Explanation
        input_text = Text("Input: Your Brain", font_size=40, color=BLUE).move_to(LEFT)
        function_text = Text("Function: Subscribe", font_size=40, color=BLUE).shift(positon_words)
        output_text = Text("Output: Your Brain", font_size=40, color=BLUE).move_to(LEFT )

        # Animate Your Brain Moving to YouTube
        self.play(Write(input_text))
        self.play(input_text.animate.move_to(brain1.get_center()), run_time=2)
        self.wait(3)

        # Replace Your Brain with "Subscribe" Function
        self.play(FadeOut(input_text), FadeIn(function_text))
        self.wait(3)

        # Animate "Your Brain" Moving to Second Brain
        self.play(function_text.animate.move_to(brain2.get_center()), run_time=2)
        self.wait(3)

        # Replace Function with Output (Your Brain)
        self.play(FadeOut(function_text), FadeIn(output_text))
        self.wait(3)

        # Clean up
        self.play(FadeOut(brain1), FadeOut(youtube), FadeOut(brain2), FadeOut(output_text), FadeOut(input_text))
