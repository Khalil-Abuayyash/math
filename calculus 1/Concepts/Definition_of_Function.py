from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class FunctionDefinition(Scene):
    def construct(self):
        # Step 1: Create the "Definition:" title and position it at the top
        question_text = Text("Definition", font_size=72, color="#195da4")
        question_text.to_edge(UP)  # Position the text at the top

        # Step 2: Create the mathematical definition of a function
        definition_text = Text(
            "A function maps exactly one input to exactly one output.",
            font_size=40
        )

        # Step 3: Position the definition below the title
        definition_text.next_to(question_text, DOWN, buff=0.5)  # Adjust the vertical spacing

        # Step 4: Display the title and the definition
        self.play(Write(question_text))
        self.wait(1)
        self.play(Write(definition_text))
        self.wait(2)

        # Step 5: Add two SVG images and move them 1 unit down
        left_image = SVGMobject("cloud.svg").scale(1.5).shift(DOWN)
        right_image = SVGMobject("cloud.svg").scale(1.5).shift(DOWN)

        # Position the images
        left_image.to_edge(LEFT, buff=1)
        right_image.to_edge(RIGHT, buff=1)

        # Add labels inside the shapes
        left_points = [
            Text("A", font_size=30).move_to(left_image.get_center() + UP * 0.5 ),
            Text("B", font_size=30).move_to(left_image.get_center()),
            Text("C", font_size=30).move_to(left_image.get_center() + DOWN * 0.5),
        ]
        right_points = [
            Text("1", font_size=30).move_to(right_image.get_center() + UP * 0.5),
            Text("2", font_size=30).move_to(right_image.get_center()),
            Text("3", font_size=30).move_to(right_image.get_center() + DOWN * 0.5),
        ]

        # Create three arrows connecting the points
        arrows = [
            Arrow(start=left_points[i].get_center(), end=right_points[i].get_center(), buff=0.1, color="#195da4")
            for i in range(3)
        ]

        # Animate the SVG images, points, and arrows
        self.play(FadeIn(left_image), FadeIn(right_image))
        self.play(*[Write(label) for label in left_points + right_points])
        self.play(*[Write(arrow) for arrow in arrows])
        self.wait(3)


