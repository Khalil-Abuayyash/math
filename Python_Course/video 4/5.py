from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class ForLoopExplanation(Scene):
    def construct(self):

        code = '''# Adding integers

x = 3
y = 8

sum = x + y # 11
'''
        
        code_block = Code(
            code=code,
            tab_width=4,
            background_stroke_width=0,
            background="terminal",
            language="Python",
            font_size=30,
            line_spacing=1,
            style="native",
            font="Monospace"
        )
        # code_block.move_to(code_background.get_center())
        

        self.play(
            Create(code_block), run_time=4
        )

        self.wait(4)