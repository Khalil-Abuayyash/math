from manim import *

config.pixel_width = 1080
config.pixel_height = 1920

class NewYearMisconception(Scene):
    def construct(self):
        # Set up scene dimensions for a YouTube short

        # Title
        title = Text("Are We Celebrating \n New Year's Wrong?").scale(1)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # 365 vs 365.24 Explanation
        calendar_text1 = Text("A year isn’t exactly").scale(1)
        calendar_text2 = Text("365 days...").scale(1)
        calendar_text = VGroup(calendar_text1, calendar_text2)
        calendar_text.arrange(direction=DOWN, buff=0.5)
        precise_time = Text("365.24 days...").scale(1.5)
        self.play(Write(calendar_text))
        self.wait(1)
        self.play(FadeOut(calendar_text))
        self.play(Write(precise_time))
        self.wait(1)
        self.play(FadeOut(precise_time))

        # Leap Year Explanation
        leap_year_text = Text("To fix this,\n we add a day \n every 4 years \n — a Leap Year!").scale(1).to_edge(UP)
        leap_year_example = Text("2020, 2024, 2028...").next_to(leap_year_text, DOWN)
        self.play(Write(leap_year_text))
        # self.wait(1)
        self.play(Write(leap_year_example))
        # self.wait(1)
        self.play(FadeOut(leap_year_text, leap_year_example))

        # Not perfectly synced
        synced_text = Text("Even with Leap Years, \n we’re not perfectly synced!").scale(1).to_edge(UP)
        orbit_diagram = Circle().scale(1.5).shift(LEFT * 2)  # Represents Earth's orbit
        earth_dot = Dot(orbit_diagram.point_at_angle(PI / 4)).set_color(BLUE).scale(2)  # Earth
        sun_dot = Dot().set_color(YELLOW).shift(RIGHT * 2).scale(3)  # Sun
        self.play(Write(synced_text))
        # self.wait(1)
        self.play(Create(orbit_diagram), FadeIn(earth_dot, sun_dot))
        self.wait(2)
        self.play(FadeOut(synced_text, orbit_diagram, earth_dot, sun_dot))

        # Timing of New Year
        timing_text = Text("The exact 'New Year' \n moment doesn’t \n land at").scale(1).to_edge(UP)
        clock = SVGMobject("clock.svg").scale(1).set_color(WHITE)  # Requires clock.svg in the folder
        midnight_label = Text("Midnight").next_to(clock, DOWN)
        self.play(Write(timing_text))
        self.wait(1)
        self.play(FadeIn(clock, midnight_label))
        self.wait(2)
        self.play(FadeOut(timing_text, clock, midnight_label))

        # Closing
        closing_text = Text("So, next time you \n ring in the New Year \n remember, it’s not quite \n as precise as we think!").scale(1).to_edge(UP)
        happy_new_year = Text("Happy New Year!").set_color(YELLOW).scale(1).next_to(closing_text, DOWN)
        confetti = SVGMobject("confetti.svg").scale(1).next_to(happy_new_year)
        self.play(Write(closing_text))
        self.wait(2)
        self.play(FadeOut(closing_text))
        self.play(Write(happy_new_year))
        self.play(FadeIn(confetti))
        # self.wait(1)
        self.play(FadeOut(happy_new_year, confetti))
