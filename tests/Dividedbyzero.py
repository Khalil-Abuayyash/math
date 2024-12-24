from manim import *
from math import sin, cos, radians

class DrawCircleWithMultipleAngleLines(Scene):
    def construct(self):
        # Draw the initial circle
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        self.wait(2)

        # Define the angles in degrees
        angles_degrees = [60, 120, 180, 240,300 ,360]

        # Draw lines at the specified angles
        for angle_degrees in angles_degrees:
            angle_radians = radians(angle_degrees)  # Convert to radians

            # Calculate the endpoint of the line using the angle
            x = 2 * cos(angle_radians)  # Radius (2) * cos(angle)
            y = 2 * sin(angle_radians)  # Radius (2) * sin(angle)

            # Draw the line at the specified angle
            line = Line(start=ORIGIN, end=[x, y, 0], color=YELLOW)
            self.play(Create(line))
            self.wait(1)
