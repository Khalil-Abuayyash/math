from manim import *
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

class IncreasingFunctionScene(Scene):
    def construct(self):
        # Add title
        title = Tex("Increasing and Decreasing Functions", color=WHITE).scale(1.5)
        title.to_edge(UP)
        
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
        
        # Create x1, x2, and x3 labels
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
        
        # Create y1, y2, y3, and y4 labels
        y1_label = Tex("$y_1$", color=WHITE).next_to(axes.c2p(0, 1), LEFT) # type: ignore
        y2_label = Tex("$y_2$", color=WHITE).next_to(axes.c2p(0, 2), LEFT)
        y3_label = Tex("$y_3$", color=WHITE).next_to(axes.c2p(0, 3), LEFT)
        y4_label = Tex("$y_4$", color=WHITE).next_to(axes.c2p(0, 4), LEFT)
        
        # Load and position person SVG at (x1, y1)
        person = SVGMobject("person.svg", color=WHITE).scale(0.6)
        person.move_to(axes.c2p(x1, y1))  # Start at (x1, y1)
        
        # Create circles
        circle1 = Circle(color=RED, radius=0.2)
        circle1.move_to(axes.c2p(x1, y1) + 1*DOWN)
        circle1.set_fill(RED, opacity=1)
        
        circle2 = Circle(color=GRAY, radius=0.2)
        circle2.move_to(mountain.get_top())
        circle2.set_fill(GRAY, opacity=1)
        
        circle3 = Circle(color=YELLOW, radius=0.2)
        circle3.move_to(axes.c2p(3, 2))
        circle3.set_fill(YELLOW, opacity=1)
        
        # Group all objects that need to be moved down
        graph_group = VGroup(
            axes_labels,
            x1_label, x2_label, x3_label,
            y1_label, y2_label, y3_label, y4_label,
            mountain,
            person,
            circle1, circle2, circle3
        )
        
        # Shift the entire group one unit down
        graph_group.shift(2*DOWN)
        
        # Animation sequence
        self.play(Write(title))  # Display the title
        self.play(Write(axes_labels))
        self.play(Write(x1_label), Write(x2_label), Write(x3_label), 
                  Write(y1_label), Write(y2_label), Write(y3_label), Write(y4_label))
        self.play(DrawBorderThenFill(mountain))
        
        # Fade in circles
        self.play(FadeIn(circle1), FadeIn(circle2), FadeIn(circle3))
        
        # Draw paths A and B after circles are displayed
        path_A = Line(circle1.get_center(), circle2.get_center(), color=BLUE)
        path_B = Line(circle2.get_center(), circle3.get_center(), color=GREEN)
        
        label_A = Tex("A", color=BLUE).next_to(path_A, LEFT)
        label_B = Tex("B", color=GREEN).next_to(path_B, RIGHT)
        
        # Animate drawing paths and labels
        self.play(Create(path_A))
        self.play(Write(label_A))
        self.wait(0.5)
        
        self.play(Create(path_B))
        self.play(Write(label_B))
        self.wait(0.5)
        
        # Introduce the person
        self.play(FadeIn(person), run_time=1.5)
        
        # Define step length
        step_length = 0.5
        
        # Define the path from (x1, y1) to the top of the mountain
        start_point = axes.c2p(x1, y1)
        end_point = mountain.get_top() 
        
        # Calculate the number of steps needed
        total_distance = np.linalg.norm(end_point - start_point)
        num_steps = int(total_distance / step_length)
        
        # Create intermediate points for the step function
        step_points = [
            start_point + (end_point - start_point) * (i / num_steps)
            for i in range(num_steps + 1)
        ]
        
        height = person.get_top() - person.get_bottom()
        # Animate the person moving in steps
        for i in range(1, len(step_points)):
            self.play(person.animate.move_to(step_points[i]), run_time=0.5) 
            self.wait(0.2)  # Pause briefly at each step
        self.play(person.animate.move_to(mountain.get_top() + height/2)) 
        self.wait(0.2)
        
        # Define the path from the top of the mountain to the final position
        start_point_down = mountain.get_top()
        end_point_down = axes.c2p(x3, y1)
        # Calculate the number of steps needed for the downward movement
        total_distance_down = np.linalg.norm(end_point_down - start_point_down)
        num_steps_down = int(total_distance_down / step_length)
        # Create intermediate points for the downward step function
        step_points_down = [
            start_point_down + (end_point_down - start_point_down) * (i / num_steps_down)
            for i in range(num_steps_down + 1)
        ]
        # Animate the person moving down in steps
        for i in range(1, len(step_points_down)):
            self.play(person.animate.move_to(step_points_down[i]), run_time=0.5)
            self.wait(0.2)  # Pause briefly at each step
        # Final adjustment to ensure the person lands exactly at the end point
        self.play(person.animate.move_to(end_point_down), run_time=0.5)
        
        # Wait at the end
        self.wait(2)