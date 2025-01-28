from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30


class FunctionExplanation(Scene):
    def construct(self):
        # Load SVG Assets
        machine = SVGMobject("machine.svg").scale(2)
        person = SVGMobject("person.svg").scale(1)
     
        group = VGroup(machine, person)
        group.arrange(LEFT, buff=2)
        group.move_to(ORIGIN)
        
        coin = SVGMobject("coin.svg").scale(0.5).next_to(person, RIGHT, buff=0.1)
        cola = SVGMobject("cola.svg").scale(0.7).move_to(machine.get_center())

        # Display Initial Objects
        self.play(FadeIn(person), FadeIn(machine))
        self.wait(2)
        
        positon_words = machine.get_top() + UP*1
        # Add Text for Explanation
        input_text = Text("Input: Coin", font_size=40, color = BLUE).move_to(LEFT * 5 + positon_words)
        function_text = Text("Function: Machine", font_size=40, color = BLUE).shift(positon_words)
        output_text = Text("Output: Cola", font_size=40, color = BLUE).move_to(LEFT * 5 + positon_words)

        # Animate Coin Moving to Machine
        self.play(FadeIn(coin), Write(input_text))
        self.play(coin.animate.move_to(machine.get_center()), run_time=2)
        self.wait(3)

        # Replace Coin with Cola
        self.play(FadeOut(coin), FadeIn(cola), Transform( input_text,function_text))
        self.wait(3)

        # Animate Cola Moving to Person
        self.play(cola.animate.move_to(person.get_right()), Transform(input_text, output_text))
        self.wait(3)

        # Clean up
        self.play(FadeOut(person), FadeOut(machine), FadeOut(cola), FadeOut(output_text), FadeOut(input_text))
