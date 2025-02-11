from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60

class Yang(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = BLACK
        
        yang = SVGMobject("yang.svg").scale(2)
        self.play(DrawBorderThenFill(yang))
        yang.add_updater(lambda m, dt: m.rotate(dt * PI).scale(1.005))
        self.wait(5)
        self.play(FadeOut(yang))
