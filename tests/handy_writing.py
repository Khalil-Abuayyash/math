from manim import *

config.background_color = "#000000"

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30 

class CellPlasmaMembrane(Scene):
    def construct(self):
        # Title for the animation
        title = Text("Cells are outlined by a plasma membrane", font_size=36).to_edge(UP)
        self.play(Write(title))
        
        # Load the SVG file
        cell_svg = SVGMobject("cell-svgrepo-com.svg").scale(3)
        
        # Animate drawing the cell SVG
        self.play(DrawBorderThenFill(cell_svg), run_time=2)
        self.wait(1)
        
        # Highlight the plasma membrane
        plasma_membrane = cell_svg[0]  # Assuming the first path in SVG represents the plasma membrane
        self.play(plasma_membrane.animate.set_color(BLUE), run_time=2)
        
        # Add annotation
        annotation = Text("Plasma Membrane", font_size=24, color=WHITE).next_to(plasma_membrane, RIGHT)
        self.play(Write(annotation))
        self.wait(1)
        
        # Show selective permeability concept
        incoming_particle = Circle(color=GREEN, fill_opacity=0.8).scale(0.3)
        incoming_particle.move_to(LEFT * 3 + DOWN)
        blocked_particle = incoming_particle.copy().set_color(RED)

        self.play(incoming_particle.animate.move_to(ORIGIN))
        self.play(FadeOut(incoming_particle), run_time=1)  # Particle passes through

        original = blocked_particle.get_center()
        left = plasma_membrane.get_left()
        self.play(blocked_particle.animate.move_to(left))
        self.play(blocked_particle.animate.move_to(original))
        self.play(FadeOut(blocked_particle))

        # Add caption for selective permeability
        caption = Text(
            "Selective Permeability: Monitors what enters and exits",
            font_size=28
        )
        caption.next_to(plasma_membrane, LEFT)
        self.play(Write(caption))
        
        self.play(FadeOut(annotation, caption, title))

        # Create a circular lipid bilayer representation
        lipid_bilayer_outer = VGroup()
        lipid_bilayer_inner = VGroup()
        num_lipids = 20  # Number of lipid molecules in the circle
        outer_radius = 2.5 # Radius of the outer layer
        inner_radius = 2  # Radius of the inner layer

        for i in range(num_lipids):
            # Angle for each lipid
            angle = TAU / num_lipids * i

            # Outer lipid layer
            outer_head = Circle(color=YELLOW, fill_opacity=0.8).scale(0.15)
            outer_tail = Line(ORIGIN, DOWN * 0.3, color=YELLOW).rotate(PI)  # Tail outward
            outer_lipid = VGroup(outer_head, outer_tail)
            outer_lipid.move_to(UP * outer_radius).rotate(angle, about_point=ORIGIN)
            lipid_bilayer_outer.add(outer_lipid)

            # Inner lipid layer
            inner_head = Circle(color=YELLOW, fill_opacity=0.8).scale(0.15)
            inner_tail = Line(ORIGIN, UP * 0.3, color=YELLOW)  # Tail inward
            inner_lipid = VGroup(inner_head, inner_tail)
            inner_lipid.move_to(UP * inner_radius).rotate(angle, about_point=ORIGIN)
            lipid_bilayer_inner.add(inner_lipid)

        # Group the bilayers
        lipid_bilayer = VGroup(lipid_bilayer_outer, lipid_bilayer_inner)

        # Position the circular bilayer around the cell SVG
        lipid_bilayer.move_to(plasma_membrane.get_center())
        
        self.play(FadeIn(lipid_bilayer), FadeOut(plasma_membrane), run_time=2)
        self.wait(1)

        # Add caption about lipid bilayer
        bilayer_caption = Text(
            "Lipid Bilayer: Provides structure and regulates entry",
            font_size=28,
            color=WHITE
        )
        bilayer_caption.next_to(plasma_membrane, DOWN)
        self.play(Write(bilayer_caption))
        self.wait(3)

        # Fade out the lipid bilayer and its caption
        self.play(FadeOut(lipid_bilayer, bilayer_caption))

        # End scene
        self.play(FadeOut(plasma_membrane, annotation, caption, cell_svg))
