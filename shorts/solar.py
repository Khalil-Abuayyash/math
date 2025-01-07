from manim import *

class SolarCell(Scene):
    def construct(self):
        # Title
        title = Text("How a Solar Cell Works", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Draw the solar cell layers
        layers = VGroup()

        # Top contact (grid-like structure)
        top_contact = Rectangle(width=6, height=0.3, color=GRAY, fill_opacity=0.7).shift(UP*2)
        grid_lines = VGroup(
            *[Line(start=top_contact.get_left() + RIGHT * i * 0.5, 
                   end=top_contact.get_right() - RIGHT * (6 - i) * 0.5,
                   color=GRAY)
              for i in range(1, 6)]
        )
        grid = VGroup(top_contact, grid_lines)
        layers.add(grid)

        # Anti-reflective coating
        coating = Rectangle(width=6, height=0.3, color=BLUE, fill_opacity=0.5).next_to(top_contact, DOWN, buff=0.05)
        layers.add(coating)

        # N-type silicon layer
        n_type = Rectangle(width=6, height=1, color=BLUE_A, fill_opacity=0.6).next_to(coating, DOWN, buff=0)
        layers.add(n_type)

        # P-type silicon layer
        p_type = Rectangle(width=6, height=1, color=ORANGE, fill_opacity=0.6).next_to(n_type, DOWN, buff=0)
        layers.add(p_type)

        # Bottom contact
        bottom_contact = Rectangle(width=6, height=0.3, color=GRAY, fill_opacity=0.7).next_to(p_type, DOWN, buff=0.05)
        layers.add(bottom_contact)

        # Add layers to scene
        self.play(FadeIn(layers, lag_ratio=0.2))
        self.wait(1)

        # Label each layer
        labels = VGroup(
            Text("Top Contact", font_size=24).next_to(top_contact, UP),
            Text("Anti-reflective Coating", font_size=24).next_to(coating, LEFT, buff=0.5),
            Text("N-type Silicon", font_size=24).next_to(n_type, LEFT, buff=0.5),
            Text("P-type Silicon", font_size=24).next_to(p_type, LEFT, buff=0.5),
            Text("Bottom Contact", font_size=24).next_to(bottom_contact, DOWN)
        )

        for label in labels:
            self.play(Write(label))
            self.wait(0.5)

        # Show light ray hitting the solar cell
        light_ray = Arrow(start=UP*3, end=coating.get_top() + UP*0.1, color=YELLOW, buff=0.1)
        self.play(GrowArrow(light_ray))
        self.wait(1)

        # Show electron movement (simplified)
        electron = Dot(color=BLUE).move_to(p_type.get_center())
        self.play(electron.animate.move_to(n_type.get_center()), run_time=2)
        self.wait(1)

        # Fade out
        self.play(FadeOut(layers, labels, light_ray, electron, title))
