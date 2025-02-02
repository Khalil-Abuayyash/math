from manim import *
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class EvenFunctionVisualization(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = BLACK

        # Create axes
        axes = Axes(
            x_range=[-1, 1, 1],
            y_range=[-5, 5, 5],
            axis_config={"color": WHITE},
            x_length=5,
            y_length=10,
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)").set_color(WHITE)

        # Add axes to the scene
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)

        # Load and position the original human SVG
        human_svg = SVGMobject("human.svg").scale(1.5)
        human_svg.move_to(axes.c2p(0, 0))

        # Add the original human SVG
        self.play(FadeIn(human_svg))
        self.wait(1)


        # Create two copies and position them symmetrically
        left_human = SVGMobject("left.svg").scale(1.5)
        right_human = SVGMobject("right.svg").scale(1.5)
        right_human.next_to(left_human.get_right())
        
        print(len(left_human))
        
        
        self.play(FadeOut(human_svg), FadeIn(right_human), FadeIn(left_human))
        
        
        
        # Position copies 0.5 units left/right from y-axis
        # left_human.move_to(axes.c2p(-0.5, 1))
        # right_human.move_to(axes.c2p(0.5, 1))

        # Create a black mask for the right half of the right human
        # mask = Rectangle(
        #     width=right_human.width / 2,  # Half the width of the human SVG
        #     height=right_human.height,
        #     fill_color=BLACK,
        #     fill_opacity=1,
        #     stroke_color=BLACK,
        # )
        # # Align the mask to cover the right half of the right human
        # left_mask = mask.copy()
        # mask.next_to(right_human.get_center(), LEFT, buff=0)
        # left_mask.next_to(left_human.get_center(), RIGHT, buff=0) 
        
        

        # self.wait(0.5)
        # self.play(FadeOut(axes), FadeOut(axes_labels))
        # self.wait(1)
        

        # # Create symmetry line
        # symmetry_line = DashedLine(
        #     start=axes.c2p(0, -5),
        #     end=axes.c2p(0, 5),
        #     color=BLUE,
        #     stroke_width=2,
        # )
        # self.play(Create(symmetry_line))
        # self.wait(1)


        # Fade out everything
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
        # self.wait(1)" 


