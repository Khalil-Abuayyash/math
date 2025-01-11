from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class ResistancesExplained(Scene):
    def construct(self):
        # Title
        title = Text("Resistances in Series and Parallel", font_size=60).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Resistances in Series
        series_title = Text("In Series", font_size=50).to_edge(UP, buff=1.5)
        self.play(Transform(title, series_title))

        # # Drawing series resistances
        # resistor_1 = self.draw_resistor(LEFT * 3, label="R1")
        # resistor_2 = self.draw_resistor(ORIGIN, label="R2")
        # resistor_3 = self.draw_resistor(RIGHT * 3, label="R3")

        # # Connecting wires
        # wire_left = Line(LEFT * 5, resistor_1.get_start(), color=WHITE)
        # wire_middle1 = Line(resistor_1.get_end(), resistor_2.get_start(), color=WHITE)
        # wire_middle2 = Line(resistor_2.get_end(), resistor_3.get_start(), color=WHITE)
        # wire_right = Line(resistor_3.get_end(), RIGHT * 5, color=WHITE)

        # series_group = VGroup(wire_left, resistor_1, wire_middle1, resistor_2, wire_middle2, resistor_3, wire_right)
        # self.play(Create(series_group))

        # Drawing series resistances
        resistor_1, start_1, end_1 = self.draw_resistor(LEFT * 3, label="R1")
        resistor_2, start_2, end_2 = self.draw_resistor(ORIGIN, label="R2")
        resistor_3, start_3, end_3 = self.draw_resistor(RIGHT * 3, label="R3")

        # Connecting wires
        wire_left = Line(LEFT * 5, start_1, color=WHITE)
        wire_middle1 = Line(end_1, start_2, color=WHITE)
        wire_middle2 = Line(end_2, start_3, color=WHITE)
        wire_right = Line(end_3, RIGHT * 5, color=WHITE)

        # Group all elements
        series_group = VGroup(wire_left, resistor_1, wire_middle1, resistor_2, wire_middle2, resistor_3, wire_right)
        self.play(Create(series_group))

        self.wait(1)

        # Merging and finding equivalent resistance in series
        self.play(FadeOut(wire_middle1, wire_middle2), run_time=1)
        merged_resistor = self.draw_resistor(ORIGIN, label="R_eq", color=YELLOW)
        merged_resistor = self.draw_resistor(ORIGIN, label="R_eq")[0]
        series_resistors = VGroup(resistor_1[0], resistor_2[0], resistor_3[0])
        # self.play(Transform(VGroup(resistor_1, resistor_2, resistor_3), merged_resistor))
        self.play(Transform(series_resistors, merged_resistor))
        series_formula = MathTex("R_{eq} = R_1 + R_2 + R_3", font_size=40).next_to(merged_resistor, DOWN)
        self.play(Write(series_formula))
        self.wait(2)

        # Transition to Parallel
        self.play(FadeOut(series_group, series_formula))
        parallel_title = Text("In Parallel", font_size=50).to_edge(UP, buff=1.5)
        self.play(Transform(title, parallel_title))

        # Drawing parallel resistances
        resistor_1_parallel = self.draw_resistor(UP * 2, label="R1")[0]
        resistor_2_parallel = self.draw_resistor(ORIGIN, label="R2")[0]
        resistor_3_parallel = self.draw_resistor(DOWN * 2, label="R3")[0]

        # Connecting wires in parallel
        wire_top = Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(UP * 2.5)
        wire_middle = Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(DOWN * 2.5)
        vertical_lines = VGroup(
            Line(wire_top.get_start(), wire_middle.get_start(), color=WHITE),
            Line(wire_top.get_end(), wire_middle.get_end(), color=WHITE),
        )

        parallel_group = VGroup(
            wire_top, wire_middle, vertical_lines,
            resistor_1_parallel, resistor_2_parallel, resistor_3_parallel
        )
        self.play(Create(parallel_group))
        self.wait(1)

        # Merging and finding equivalent resistance in parallel
        self.play(FadeOut(vertical_lines), run_time=1)
        merged_parallel = self.draw_resistor(ORIGIN, label="R_eq", color=YELLOW)[0]
        self.play(Transform(VGroup(resistor_1_parallel[0], resistor_2_parallel[0], resistor_3_parallel[0]), merged_parallel))
        parallel_formula = MathTex(r"\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}", font_size=40).next_to(merged_parallel, DOWN)
        self.play(Write(parallel_formula))
        self.wait(2)

        # End Scene
        self.play(FadeOut(parallel_group, parallel_formula, title))
        thank_you = Text("Thank you for watching!", font_size=60).move_to(ORIGIN)
        self.play(Write(thank_you))
        self.wait(2)

    # def draw_resistor(self, position, label, color=BLUE):
    #     """Helper function to draw a resistor with a label."""
    #     resistor = Line(LEFT, RIGHT, color=color).move_to(position)
    #     zigzag = VGroup(
    #         Line(LEFT * 0.4, LEFT * 0.2 + UP * 0.2, color=color),
    #         Line(LEFT * 0.2 + UP * 0.2, RIGHT * 0.2 + DOWN * 0.2, color=color),
    #         Line(RIGHT * 0.2 + DOWN * 0.2, RIGHT * 0.4, color=color),
    #     ).move_to(resistor)
    #     label_text = Text(label, font_size=30).next_to(zigzag, UP)
    #     return VGroup(resistor, zigzag, label_text)

    # def draw_resistor(self, position, label, color=BLUE):

    # # Define the zigzag resistor
    #     zigzag = VGroup(
    #         Line(LEFT * 0.4, LEFT * 0.2 + UP * 0.2, color=color),
    #         Line(LEFT * 0.2 + UP * 0.2, RIGHT * 0.2 + DOWN * 0.2, color=color),
    #         Line(RIGHT * 0.2 + DOWN * 0.2, RIGHT * 0.4, color=color),
    #     )
        
    #     # Add wires on both ends
    #     left_wire = Line(LEFT, LEFT * 0.4, color=color)
    #     right_wire = Line(RIGHT * 0.4, RIGHT, color=color)
        
    #     # Combine all components into one resistor object
    #     resistor = VGroup(left_wire, zigzag, right_wire).move_to(position)
        
    #     # Add a label above the resistor
    #     label_text = Text(label, font_size=30).next_to(resistor, UP)
        
    #     # Return the complete Mobject
    #     return VGroup(resistor, label_text)


    def draw_resistor(self, position, label, color=BLUE):
        """Helper function to draw a resistor with proper start and end points."""
        # Create the zigzag (resistor body)
        zigzag = VGroup(
            Line(LEFT * 0.3, LEFT * 0.1 + UP * 0.2, color=color),
            Line(LEFT * 0.1 + UP * 0.2, RIGHT * 0.1 + DOWN * 0.2, color=color),
            Line(RIGHT * 0.1 + DOWN * 0.2, RIGHT * 0.3, color=color),
        )
        
        # Add wires on both sides to define start and end points
        left_wire = Line(LEFT * 0.5, LEFT * 0.3, color=color)
        right_wire = Line(RIGHT * 0.3, RIGHT * 0.5, color=color)
        
        # Combine all parts into a single resistor object
        resistor = VGroup(left_wire, zigzag, right_wire).move_to(position)
        
        # Add a label above the resistor
        label_text = Text(label, font_size=24).next_to(resistor, UP)
        
        # Return both resistor and its start/end points
        return resistor, left_wire.get_start(), right_wire.get_end()

