from manim import *

# Set the pixel width and height of the video
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

# for cusom Tex template and custom font
# config.tex_engine = "lualatex"
# # Define a custom TexTemplate
# kalam_template = TexTemplate(tex_compiler='lualatex')
# kalam_template.add_to_preamble(r"""
# \usepackage{fontspec}
# \setmainfont{Kalam}
# """)

# Function to hand write text
def hand_write_text(obj, text, font="Kalam", font_size=60, color=WHITE, pointer_color=YELLOW, char_time=0.7):
    # Use the Kalam font for text
    handwritten_text = Text(
        text,
        font=font,
        font_size=font_size
    )
    handwritten_text.set_color(color)

    # Position the text
    handwritten_text.move_to(ORIGIN)

    # Create a pointer (dot)
    pointer = Dot(color=pointer_color).scale(0.5)

    # Add the text and pointer to the scene
    obj.add(pointer)

    # Animate each letter
    for char in handwritten_text:
        # Convert the character into a VMobject to access its path
        letter_path = VMobject().set_points_as_corners([
            *char.get_all_points()
        ])

        # Place the pointer at the starting point of the letter path
        pointer.move_to(letter_path.get_start())

        # Animate the pointer tracing the letter
        obj.play(
            MoveAlongPath(pointer, letter_path),
            Create(char),  # Reveal the letter as the pointer moves
            run_time=char_time
        )

    obj.wait(2)

# Function to hand write LaTeX
# ecf fonts are the best for hand writing
# ecf_augie, ecf_jd, ecf_skeetch, ecf_tall_paul, ecf_webster
def hand_write_latex(obj, text, font_size=60, template = TexFontTemplates.ecf_jd):

    handwritten_text = MathTex(
        text,
        tex_template=template,
        font_size=font_size
    )

    handwritten_text = handwritten_text[0]

    handwritten_text.set_color(WHITE)

    # Position the text
    handwritten_text.move_to(ORIGIN)

    # Create a pointer (dot)
    pointer = Dot(color=YELLOW).scale(0.5)

    # Add the text and pointer to the scene
    obj.add(pointer)

    # Animate each letter
    
    for part in handwritten_text:

        # Convert the character into a VMobject to access its path
        letter_path = VMobject().set_points_as_corners([
            *part.get_all_points()
        ])

        # Place the pointer at the starting point of the letter path
        pointer.move_to(letter_path.get_start())

        # Animate the pointer tracing the letter
        obj.play(
            MoveAlongPath(pointer, letter_path),
            Create(part),  # Reveal the letter as the pointer moves
            run_time=0.7
        )

    obj.wait(2)

class Function(Scene):
    def construct(self):
        hand_write_latex(self, r"f(x) = 2x^2 + 1")

class Equation(Scene):
    def construct(self):
        hand_write_text(self, "4x = 2x + 1")
