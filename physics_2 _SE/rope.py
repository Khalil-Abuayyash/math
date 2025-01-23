from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 9.0
config.frame_width = 16.0
config.frame_rate = 30

class RubberRodExperiment3D(ThreeDScene):
    def construct(self):

        ceiling = Rectangle(
            width=6, height=3, color=LIGHT_GREY, fill_opacity=1
        ).shift(UP * 3).rotate(PI / 2, axis=RIGHT)

        hanging_rope = Cylinder(radius=0.05, height=2.5, color=GRAY, fill_opacity=1)
        hanging_rope.move_to(ceiling.get_bottom() + DOWN * 0.25)

        # Create the diagonal ropes
        left_rope = Line3D(start=hanging_rope.get_bottom(), end=LEFT * 1 + DOWN * 1.25, color=GRAY)
        right_rope = Line3D(start=hanging_rope.get_bottom(), end=RIGHT * 1 + DOWN * 1.25, color=GRAY)

        # Create the hanging rubber rod
        hanging_rod = Cylinder(radius=0.1, height=1.9, color=WHITE, fill_opacity=1)
        hanging_rod.rotate(PI / 2, axis=UP)  # Align horizontally
        hanging_rod.shift(DOWN * 1.25)

        # Create the approaching rubber rod
        approaching_rod = Cylinder(radius=0.1, height=1.9, color=WHITE, fill_opacity=1)
        approaching_rod.rotate(PI / 2, axis=UP)  # Align horizontally
        approaching_rod.shift(OUT * 5 + LEFT * 1.5 + DOWN * 1.5)  # Start far from the scene

        # Add an animation to move the approaching rod closer
        approaching_rod_target = approaching_rod.copy().shift(IN * 4)

        # Add arrows for forces
        force1 = Arrow3D(
            start=hanging_rod.get_left(), 
            end=hanging_rod.get_left() + IN * 1, 
            color=BLUE
        )
        force2 = Arrow3D(
            start=approaching_rod.get_center(), 
            end=approaching_rod.get_center() + RIGHT * 0.5 + DOWN * 0.2, 
            color=BLUE
        )

        # Add labels
        label_hanging = Text("Hanging Rubber", font_size=18).move_to(hanging_rod.get_center() + UP * 0.5)
        label_approaching = Text("Approaching Rubber", font_size=18).move_to(approaching_rod.get_center() + OUT * 0.5)
        force_label1 = MathTex("\\vec{F}").move_to(force1.get_end() + LEFT * 0.2)
        force_label2 = MathTex("\\vec{F}").move_to(force2.get_end() + RIGHT * 0.2)

        # Add all objects to the scene
        self.add(ceiling, hanging_rope, left_rope, right_rope, hanging_rod)
  
        # # Animate the approaching rod
        self.play(FadeIn(approaching_rod))
        self.play(approaching_rod.animate.move_to(approaching_rod_target))
        self.play(hanging_rod.animate.rotate(0.5, axis=DOWN), left_rope.animate.rotate(0.5, axis=DOWN),right_rope.animate.rotate(0.5, axis=DOWN))
        # self.add(force1, force2,force_label1, force_label2)

        self.wait(5)
