from manim import *
import random

#Finial file

# Configure the video for a reel (1080x1920, 30fps) in portrait mode
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class FunctionStory(Scene):
    def construct(self):
        # Intro Section
        # Add SVG assets for intro (e.g., question mark, light bulb)
        intro_question = Text("What is Function?", font_size=50, color="#2ca9bc").to_edge(UP)
        light_bulb = SVGMobject("parabolic_function.svg").scale(2).next_to(intro_question, DOWN, buff=1)

        # Intro Animation
        self.play(Write(intro_question))  # Title animation at the top
        self.wait(1)
        self.play(FadeIn(light_bulb, scale=0.5))  # Bring in the SVG below the title
        self.wait(2)
        self.play(FadeOut(intro_question), FadeOut(light_bulb))  # Fade out title and SVG
        
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
        
        
        
        definition_word = Text("Definition:", font_size=50, color="#2ca9bc").to_edge(UP)
        definition1 = Text("A function is a rule that assigns", font_size=50, color="#2ca9bc")
        definition2 = Text("one element from the domain", font_size=50, color="#2ca9bc")
        definition3 = Text("to exact element in the codomain", font_size=50, color="#2ca9bc")

        # Position the text objects below each other
        definition1.next_to(definition_word, DOWN, buff=0.2)  # Shift definition1 down below definition_word
        definition2.next_to(definition1, DOWN, buff=0.2)  # Shift definition2 down below definition1
        definition3.next_to(definition2, DOWN, buff=0.2)  # Shift definition2 down below definition1

        # Play the animations
        self.play(Write(definition_word))  # Title animation at the top
        self.wait(1)
        self.play(Write(definition1))  # Write the first line
        self.wait(1)
        self.play(Write(definition2))  # Write the second line
        self.wait(1)
        self.play(Write(definition3))  # Write the third line
        self.wait(1)
        

        # Load SVG images
        svg1 = SVGMobject("blob-5-svgrepo-com (1).svg").scale(1.5)
        svg2 = SVGMobject("blob-5-svgrepo-com.svg").scale(1.5)

        # Arrange SVGs next to each other
        group = VGroup(svg1, svg2).arrange(RIGHT, buff=3)  # Adjust spacing with buff

        # Center the group on the screen
        group.move_to(ORIGIN)
        group.shift(DOWN * 2)

        # Function to get center point and place points inside the SVG
        def get_point_inside_svg(svg):
            # Get the center of the SVG (this is the geometric center)
            center = svg.get_center()

            # Get the width and height of the bounding box
            width = svg.get_width()
            height = svg.get_height()

            # Define an offset (adjust this to control the point placement inside the shape)
            offset_x = random.uniform(-width/4, width/4)  # Random offset within 1/4th of the width
            offset_y = random.uniform(-height/4, height/4)  # Random offset within 1/4th of the height
            
            # Calculate the point inside the SVG by adding the offset to the center
            point = center + np.array([offset_x, offset_y, 0])

            return point

        # Get points inside the shapes
        point1 = get_point_inside_svg(svg1)
        point2 = get_point_inside_svg(svg2)
        point3 = get_point_inside_svg(svg1)  # Another point inside the second SVG
        point4 = get_point_inside_svg(svg2)  # Another point inside the second SVG

        # Create arrows connecting the points
        arrow1 = Arrow(
            start=point1,
            end=point2,
            stroke_width=5,
            buff=0,
            color=BLUE,
            path_arc=PI / 3,  # Curve the arrow with a specific arc
        )
        
        arrow2 = Arrow(
            start=point3,
            end=point4,
            stroke_width=5,
            buff=0,
            color=BLUE,
            path_arc=-PI / 3,  # Adjust the arc direction for variety
        )


        # Add SVGs and arrows to the scene
        self.play(FadeIn(group))
        self.wait(1)

        # Highlight points and connect them
        dot1 = Dot(point1, color=RED)
        dot2 = Dot(point2, color=RED)
        dot3 = Dot(point3, color=RED)  # Third point
        dot4 = Dot(point4, color=RED)  # Forth point
        self.play(FadeIn(dot1), FadeIn(dot2), FadeIn(dot3), FadeIn(dot4))
        self.wait(1)

        # Draw the curved arrows
        self.play(Create(arrow1), Create(arrow2))
        self.wait(2)

        # Fade out everything
        # self.play(FadeOut(group), FadeOut(dot1), FadeOut(dot2), FadeOut(dot3), FadeOut(dot4) , FadeOut(arrow1), FadeOut(arrow2))