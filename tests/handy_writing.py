from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

def hand_write_text(obj, text, font="Kalam", font_size=60):
    # Use the Kalam font for text
    handwritten_text = Text(
        text,
        font=font,
        font_size=font_size
    )
    handwritten_text.set_color(WHITE)

    # Position the text
    handwritten_text.move_to(ORIGIN)

    # Create a pointer (dot)
    pointer = Dot(color=YELLOW).scale(0.5)

    # Add the text and pointer to the scene
    obj.add(pointer)

    # Animate each letter
    for char in handwritten_text:
        # Convert the character into a VMobject to access its path
        letter_path = VMobject().set_points_as_corners([
            *char.get_all_points()
        ])

        # Place the pointer at the starting point of the letter path
        pointer.move_to(letter_path.get_start() + (pointer.get_height() / 2) * UP)

        # Animate the pointer tracing the letter
        obj.play(
            MoveAlongPath(pointer, letter_path),
            Create(char),  # Reveal the letter as the pointer moves
            run_time=0.7
        )

    obj.wait(2)

class Function(Scene):
    def construct(self):
        hand_write_text(self, "f(x) = 2x + 1")

class Equation(Scene):
    def construct(self):
        hand_write_text(self, "4x = 2x + 1")
