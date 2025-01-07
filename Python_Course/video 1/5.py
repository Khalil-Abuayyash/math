from manim import *

# Set up the configuration for YouTube Shorts (1920x1080, 30fps)
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class PythonSnakeAnimation(Scene):
    def construct(self):
        # Create the word "Python"

        # Draw a path to represent the learning journey
        path = VMobject(color=BLUE)
        path.set_points_smoothly([
            LEFT * 4 + DOWN * 2,  # Start of the path
            LEFT * 2 + DOWN * 1.5,
            ORIGIN + DOWN * 1,
            RIGHT * 2 + DOWN * 1.5,
            RIGHT * 4 + DOWN * 2  # End of the path
        ])

        # Add milestones along the path
        milestones = [Dot(point, color=RED) for point in path.get_points()]  # Dots for milestones
        print(len(milestones))
        milestone_texts = [
            Text("Basics", font_size=24).next_to(milestones[0], UP),
            Text("Lists", font_size=24).next_to(milestones[4], UP),
            Text("Loops", font_size=24).next_to(milestones[8], UP),
            Text("Functions", font_size=24).next_to(milestones[12], UP),
            Text("Projects", font_size=24).next_to(milestones[-1], UP)
        ]
        milestones = [milestones[0], milestones[4], milestones[8], milestones[12], milestones[-1]]
        # Animate the path and milestones
        self.play(Create(path), run_time=3)
        for milestone, text in zip(milestones, milestone_texts):
            self.play(FadeIn(milestone), Write(text), run_time=1)

        # Final message: "Start your Python journey today!"
        final_text = Text("Start your Python journey today!", font_size=36, color=YELLOW)
        final_text.shift(DOWN * 3)
        self.play(Write(final_text), run_time=2)

        self.wait(2)

        
        '''
        # Define the labels (stations) for the Python journey
        text1 = Text("Print", font_size=35, color=YELLOW)
        text2 = Text("Variables", font_size=35, color=YELLOW)
        text3 = Text("Lists", font_size=35, color=YELLOW)
        text4 = Text("Loops", font_size=35, color=YELLOW)
        text5 = Text("Functions", font_size=35, color=YELLOW)
        text6 = Text("Classes", font_size=35, color=YELLOW)
        text7 = Text("Exceptions", font_size=35, color=YELLOW)

        track_left = VMobject(color=WHITE)
        track_left.set_points_smoothly([
            LEFT * 4 + UP * 6.5,      # Start
            LEFT * 3 + UP * 7,        # First peak
            LEFT * 2 + UP * 5,        # Valley
            LEFT * 1 + UP * 6,        # Peak
            RIGHT * 0 + UP * 3.5,       # Valley
            RIGHT * 1 + UP * 4,       # Peak
            RIGHT * 2 + UP * 2,       # Valley
            RIGHT * 3 + UP * 3,       # Peak
            RIGHT * 4 + UP * 1        # End point
        ])
        
        track_right = VMobject(color=WHITE)
        track_right.set_points_smoothly([
            LEFT * 4 + UP * 6.5,      # Start
            LEFT * 3 + UP * 7.3,      # First peak (slightly lower)
            LEFT * 2 + UP * 4.8,      # Valley
            LEFT * 1 + UP * 5.8,      # Peak
            RIGHT * 0 + UP * 3.3,     # Valley
            RIGHT * 1 + UP * 3.8,     # Peak
            RIGHT * 2 + UP * 1.8,     # Valley
            RIGHT * 3 + UP * 2.8,     # Peak
            RIGHT * 4 + UP * 0.8      # End point
        ])

        # Get the total length of the track_left path
        track_points = track_left.get_points()
        num_points = len(track_points)

        # Define positions for each station (distribute evenly)
        stations_positions = [track_points[int(i * (num_points - 1) / 6)] for i in range(7)]

        # Position the texts (stations) based on the proportion of the track length
        text_objects = [text1, text2, text3, text4, text5, text6, text7]
        
        # Alternate the position of the text (left or right of the track)
        # for i, text in enumerate(text_objects):
        #     # Alternate text position
        #     if i % 2 == 0:
        #         text.move_to(stations_positions[i]).shift(UP * 0.5)  # Left side
        #     else:
        #         text.move_to(stations_positions[i]).shift(DOWN * 0.5)  # Right side

        for i, text in enumerate(text_objects):
            pos = stations_positions[i]
            # Get y-coordinates of adjacent points
            if i > 0 and i < len(stations_positions) - 1:
                prev_y = stations_positions[i-1][1]
                curr_y = pos[1]
                next_y = stations_positions[i+1][1]
                
                # If current point is higher than both neighbors -> peak
                if curr_y > prev_y and curr_y > next_y:
                    text.move_to(pos).shift(UP * 1)
                # If current point is lower than both neighbors -> valley
                elif curr_y < prev_y and curr_y < next_y:
                    text.move_to(pos).shift(DOWN * 1)
                else:
                    text.move_to(pos)
            else:
                # Handle first and last points
                text.move_to(pos)

        # Animate the track and stations along the way
        self.play(Write(text1))
        self.play(Create(track_left), Create(track_right), run_time=3)
        for text in text_objects[1:]:
            self.play(Write(text))

        # Pause at the end
        self.wait(2)
        '''