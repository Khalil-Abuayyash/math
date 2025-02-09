from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

class IncreasingFunctionScene(Scene):
    def construct(self):
        # Create Cartesian plane
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 5, 1],
            x_length=7,
            y_length=7,
            axis_config={"color": WHITE},
        )
    
        # Add axis labels
        x_label = axes.get_x_axis_label("x").set_color(WHITE)  # Set color after creation
        y_label = axes.get_y_axis_label("y").set_color(WHITE)  # Set color after creation
        axes_labels = VGroup(axes, x_label, y_label)

        # Create x1 and x2 labels
        x1 = 1
        x2 = 2
        x3 = 3
        x1_label = Tex("$x_1$", color=WHITE).next_to(axes.c2p(x1, 0), DOWN)
        x2_label = Tex("$x_2$", color=WHITE).next_to(axes.c2p(x2, 0), DOWN)
        x3_label = Tex("$x_3$", color=WHITE).next_to(axes.c2p(x3, 0), DOWN)

        # Load and position mountain SVG
        mountain = SVGMobject("mountain.svg", color=WHITE).scale(2.5)
        mountain.move_to(axes.c2p(2, 0), aligned_edge=DOWN)  # 2 units from y-axis

        # Calculate y1 and y2 positions
        y1 = mountain.get_center()[1] - axes.c2p(0, 0)[1]  # y-coordinate of the middle of the mountain
        y2 = mountain.get_top()[1] - axes.c2p(0, 0)[1]     # y-coordinate of the top of the mountain
        y3 = mountain.get_top()[1] - axes.c2p(0, 0)[1]     # y-coordinate of the top of the mountain
        
        # Create y1 and y2 labels
        y1_label = Tex("$y_1$", color=WHITE).next_to(axes.c2p(0, 1), LEFT) # type: ignore
        y2_label = Tex("$y_2$", color=WHITE).next_to(axes.c2p(0, 2), LEFT)
        y3_label = Tex("$y_3$", color=WHITE).next_to(axes.c2p(0, 3), LEFT)
        y4_label = Tex("$y_4$", color=WHITE).next_to(axes.c2p(0, 4), LEFT)

        # Load and position person SVG at (x1, y1)
        person = SVGMobject("person.svg", color=WHITE).scale(0.6)
        person.move_to(axes.c2p(x1, y1))  # Start at (x1, y1)

        # Animation sequence
        self.play(Create(axes_labels), run_time=1)
        self.play(Write(x1_label), Write(x2_label),Write(x3_label))
        self.play(Write(y1_label), Write(y2_label), Write(y3_label), Write(y4_label))
        self.play(DrawBorderThenFill(mountain))
        self.play(FadeIn(person), run_time = 1.5)

        height = person.get_top() - person.get_bottom() 
        print(height)
        
        # Animate climbing motion from (x1, y1) to (x2, y2)
        self.play(person.animate.move_to(mountain.get_top() + height/2), run_time=4)
        self.play(person.animate.move_to(axes.c2p(x3, y1)), run_time=4)

        self.wait(2)