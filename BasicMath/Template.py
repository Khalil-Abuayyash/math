from manim import *

# Set the configuration for the video dimensions, frame rate, and background color
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30
config.background_color = "#1e1e2e"

# Adjust the frame width and height to match the aspect ratio of the pixel dimensions
config.frame_width = 9    # Width in scene units
config.frame_height = 16  # Height in scene units

class SpecialBackgroundScene(Scene):
    def construct(self):
        # Parameters for line spacing and position
        horizontal_spacing = 1  # Space between horizontal lines in scene units
        offset_y = -3           # Offset from the top of the frame

        # Calculate the range of y positions for horizontal lines
        top = config.frame_height / 2 + offset_y
        bottom = -config.frame_height / 2
        y_positions = np.arange(top, bottom - horizontal_spacing, -horizontal_spacing)

        # Create horizontal lines at the calculated y positions
        horizontal_lines = VGroup(*[
            Line(
                start=LEFT * config.frame_width / 2,
                end=RIGHT * config.frame_width / 2,
                stroke_width=1,
                color=WHITE
            ).shift(UP * y)
            for y in y_positions
        ])

        # Create the title text and position it initially at the center
        title = Text(
            "Basics of Mathematics",
            font_size=48,
            color=YELLOW
        )
        # title.move_to(ORIGIN)  # Position at the center
        title.shift(UP * 4)

        # Calculate the target position at the first horizontal line from the top
        first_line_y = y_positions[0]  # Y-coordinate of the top horizontal line
        # Adjust the position so that the bottom of the text aligns with the line
        target_y = first_line_y - (title.height / 2)
        target_position = UP * target_y

        # Add the horizontal lines and title to the scene
        self.play(FadeIn(horizontal_lines))
        self.play(Write(title))
        self.wait(1)  # Pause before moving the title

        # Animate the title moving to the top, aligned with the first line
        self.play(title.animate.move_to(target_position))

        # Keep the final frame displayed
        self.wait()