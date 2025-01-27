from manim import *

config.pixel_width = 1920   
config.pixel_height = 1080

class VectorAcademyIntro(ThreeDScene):
    def construct(self):
        # Step 1: Set up 3D Axes
        axes = ThreeDAxes()
        # self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        self.add(axes)

        # Step 2: Create 3D Vectors for Math, Physics, and CS
        vector_math = Arrow3D(
            start=ORIGIN, end=[2, 0, 0], color=RED,
        ).set_stroke(width=8)
        vector_physics = Arrow3D(
            start=ORIGIN, end=[0, 2, 0], color=GREEN,
        ).set_stroke(width=8)
        vector_cs = Arrow3D(
            start=ORIGIN, end=[0, 0, 2], color=BLUE,
        ).set_stroke(width=8)

        # Labels for each vector
        label_math = Text("Math", color=RED).scale(0.5).next_to(vector_math, RIGHT)
        label_physics = Text("Physics", color=GREEN).scale(0.5).next_to(vector_physics, UP)
        label_cs = Text("CS", color=BLUE).scale(0.5).next_to(vector_cs, OUT)

        # Add vectors and labels to the scene
        self.play(Create(vector_math), Write(label_math))
        self.play(Create(vector_physics), Write(label_physics))
        self.play(Create(vector_cs), Write(label_cs))
        self.wait(1)

        # Step 3: Add Binary Numbers
        binary_numbers = VGroup(
            Text("001", color=WHITE).scale(0.5).shift([2.5, 0, 0]),
            Text("010", color=WHITE).scale(0.5).shift([0, 2.5, 0]),
            Text("100", color=WHITE).scale(0.5).shift([0, 0, 2.5]),
        )
        self.play(FadeIn(binary_numbers))
        self.wait(1)

        # Step 4: Transform Vectors into Pillars
        pillars = VGroup(
            Cylinder(radius=0.2, height=3, color=RED).move_to([1, 0, 0]),
            Cylinder(radius=0.2, height=3, color=GREEN).move_to([0, 1, 0]),
            Cylinder(radius=0.2, height=3, color=BLUE).move_to([0, 0, 1]),
        )
        self.play(Transform(vector_math, pillars[0]))
        self.play(Transform(vector_physics, pillars[1]))
        self.play(Transform(vector_cs, pillars[2]))
        self.wait(1)

        # Step 5: Morph Pillars into the House of Three Pillars SVG
        svg_house = SVGMobject("three_pillars.svg").scale(3).rotate(PI / 2).move_to(ORIGIN)
        self.play(Transform(pillars, svg_house))
        self.wait(1)

        # Step 6: Add Text "Vector Academy"
        text = Text("Vector Academy!", font_size=48, color=YELLOW).move_to([0, -2, 0])
        self.play(Write(text))
        self.wait(2)

        # Rotate the camera around the structure for a dynamic finish
        # self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
