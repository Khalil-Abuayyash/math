from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class SolarCellSurface(Scene):
    def construct(self):
        # Title
        title = Text("Solar Cell Surface", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Draw the grid representing the solar cell surface
        cell_width = 0.5
        cell_height = 0.5
        rows = 12
        cols = 18

        grid = VGroup()

        for i in range(rows):
            for j in range(cols):
                rect = Rectangle(
                    width=cell_width, height=cell_height,
                    color=BLUE, fill_opacity=0.7
                ).shift(
                    LEFT * cols * cell_width / 2 + RIGHT * j * cell_width + 
                    UP * rows * cell_height / 2 - DOWN * i * cell_height
                )
                grid.add(rect)

        self.play(FadeIn(grid, lag_ratio=0.1))
        self.wait(1)

        # Add labels for rows and columns
        row_labels = VGroup(
            *[Text(f"R{i+1}", font_size=24).next_to(
                grid[i * cols].get_left(), LEFT
            ) for i in range(rows)]
        )

        col_labels = VGroup(
            *[Text(f"C{j+1}", font_size=24).next_to(
                grid[j].get_top(), UP
            ) for j in range(cols)]
        )

        self.play(Write(row_labels), Write(col_labels))
        self.wait(1)

        # Shadow example (a rectangle over some cells)
        shadow = Rectangle(
            width=4 * cell_width, height=3 * cell_height,
            color=BLACK, fill_opacity=0.5
        ).move_to(
            grid[5 * cols + 8].get_center()
        )

        self.play(FadeIn(shadow))
        self.wait(1)

        # Label the shadow
        shadow_label = Text("Shadow", font_size=36, color=RED).next_to(shadow, UP)
        self.play(Write(shadow_label))
        self.wait(2)

        # Fade out
        self.play(FadeOut(grid, row_labels, col_labels, shadow, shadow_label, title))
