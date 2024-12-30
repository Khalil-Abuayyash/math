# from manim import *
# from math import sin, cos, radians

# class DrawCircleWithMultipleAngleLines(Scene):
#     def construct(self):
#         # Draw the initial circle
#         circle = Circle(radius=3, color=YELLOW)
#         self.play(Create(circle))
#         self.wait(1)

#         # Define the number of divisions for the lines (representing angles)
#         num_lines = 2  # This number can be increased to make the lines more dense

#         # Draw lines at the specified angles
#         for i in range(num_lines):
#             angle_degrees = (i * 18) / num_lines  # Spread the angles evenly across 360 degrees
#             angle_radians = radians(angle_degrees)  # Convert to radians

#             # Calculate the endpoint of the line using the angle
#             x = 3 * cos(angle_radians)  # Radius (2) * cos(angle)
#             y = 3 * sin(angle_radians)  # Radius (2) * sin(angle)

#             # Draw the line at the specified angle
#             line = Line(start=ORIGIN, end=[x, y, 0], color=RED)
#             self.add((line))  # Adjust speed of animation
#             self.wait(0)  # Adjust pause time if needed
        
#         self.play(FadeOut(line))
 
from manim import *
from math import sin, cos, radians

config.pixel_height = 1080  # Set height
config.pixel_width = 1920   # Set width (e.g., Full HD resolution)
config.frame_rate = 30      # Frame rate

class DrawCircleWithTwoSectors(Scene):
    def construct(self):
        # Draw the initial circle
        circle = Circle(radius=3, color=YELLOW)
        self.play(Create(circle))
        self.wait(1)

        # Define the angles for the two sectors (180 degrees apart)
        angles_degrees = [0, 180]  # Two angles: one at 0° and one at 180°

        # Draw the lines at the specified angles to create two sectors
        for angle_degrees in angles_degrees:
            angle_radians = radians(angle_degrees)  # Convert to radians

            # Calculate the endpoint of the line using the angle
            x = 3 * cos(angle_radians)  # Radius (3) * cos(angle)
            y = 3 * sin(angle_radians)  # Radius (3) * sin(angle)

            # Draw the line at the specified angle
            line = Line(start=[-x, -y, 0], end=[x, y, 0], color=RED)
            self.add((line))
            self.wait(2)


