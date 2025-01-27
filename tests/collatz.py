from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 30

class CollatzConjecture(Scene):

    def collatz_steps(self, n):
        steps = []
        while n != 1:
            steps.append(n)
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
        steps.append(1)  # Add the final step (1)
        return steps

    def construct(self):

        # Title in the center
        title = Text("حدسية كولاتز", font="Arial", color=YELLOW, weight=BOLD).scale(1.8)
        self.play(Write(title[::-1]), run_time=2)
        self.wait(1)

        # Move title to the top
        self.play(title.animate.shift(UP * 8), run_time=1)
        self.wait(1)

        # First number (5) and its steps
        steps = self.collatz_steps(5)
        circles = []
        arrows = []

        # Create circles for each step
        for step in steps:
            circle = Circle(color=BLUE, radius=0.6)
            text = Text(str(step), font="Arial", color=WHITE).scale(1.5).move_to(circle)
            group = VGroup(circle, text)
            circles.append(group)

        # Position the circles
        # positions = [(-5, 3, 0), (-3, 5, 0), (0, 3, 0), (-2, 1, 0), (2, 1, 0), (0, 0, 0)]

        # Generate positions with custom logic for 4, 2, and 1
        positions = []
        for i, step in enumerate(steps):
            if step == 4:
                positions.append(np.array([-2, -3, 0]))  # Position for 4
            elif step == 2:
                positions.append(np.array([2, -3, 0]))  # Position for 2
            elif step == 1:
                positions.append(np.array([0, -6, 0]))  # Position for 1
            else:
                positions.append(np.array([(-1) ** i * (i % 3) * 2, 3 - i, 0]))


        for circle, pos in zip(circles, positions):
            circle.move_to(pos)

        # Create arrows between circles dynamically based on their positions
        for i in range(len(circles) - 1):
            start_pos = circles[i].get_center()
            end_pos = circles[i + 1].get_center()

            if np.isclose(start_pos[1], end_pos[1], atol=0.1):  # Same horizontal level
                arrow = Arrow(
                    start=circles[i].get_right() ,  # Exit from the left of the current circle
                    end=circles[i + 1].get_left() ,   # Enter from the right of the next circle
                    color=WHITE,
                    buff=0.2,
                )
            elif start_pos[1] > end_pos[1]:  # Current circle is higher
                arrow = Arrow(
                    start=start_pos + DOWN * 0.6,  # Exit from the bottom of the current circle
                    end=end_pos + UP * 0.6,       # Enter from the top of the next circle
                    color=WHITE,
                    buff=0.2,
                )
            else:  # Current circle is lower
                arrow = Arrow(
                    start=start_pos + UP * 0.6,    # Exit from the top of the current circle
                    end=end_pos + DOWN * 0.6,     # Enter from the bottom of the next circle
                    color=WHITE,
                    buff=0.2,
                )
            arrows.append(arrow)

        # Display the circles and arrows step by step
        for i in range(len(circles)):
            if i > 0:
                self.play(GrowArrow(arrows[i - 1]), run_time=0.5)
            self.play(FadeIn(circles[i]), run_time=0.5)
        
        last_arrow = Arrow(
                    start=circles[-1].get_top(),    # Exit from the top of the current circle
                    end=circles[-3].get_bottom(),     # Enter from the bottom of the next circle
                    color=WHITE,
                    buff=0.2,
                )
        self.play(GrowArrow(last_arrow), run_time=0.5)

        loop_circle1 = Circle(color=GOLD, radius=0.6).move_to(positions[-1])
        loop_circle2 = Circle(color=GOLD, radius=0.6).move_to(positions[-2])
        loop_circle3 = Circle(color=GOLD, radius=0.6).move_to(positions[-3])
        self.play(Transform(circles[-1][0], loop_circle1), Transform(circles[-2][0], loop_circle2), Transform(circles[-3][0], loop_circle3), run_time=1.5)
        self.wait(1)
    
        # Arrows for the loop between 1, 2, and 4 with a different color
        loop_arrows = [arrows[-2], arrows[-1], last_arrow]
        for arrow in loop_arrows:
            arrow.set_color(YELLOW)
            self.wait(0.5)
            # self.play(GrowArrow(arrow), run_time=0.5)


        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        # Ask the question
        question = Text("هل جميع الأرقام", font="Arial", color=YELLOW).scale(1.8).to_edge(DOWN, buff=1)
        question1 = Text("تعود إلى الواحد؟", font="Arial", color=YELLOW).scale(1.8).to_edge(DOWN, buff=1)
        questions = VGroup(question[::-1], question1[::-1])
        questions.arrange(DOWN, buff=0.5)

        self.play(Write(questions), run_time=2)
        self.wait(1)
