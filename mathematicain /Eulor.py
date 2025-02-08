from manim import *

class EulerVideo(Scene):
    def construct(self):
        # Configure Arabic font (make sure you have Arabic font installed)
        self.text_dir = "arabic"
        arabic_font = "Amiri"

        # Scene 1: Title
        title = Text("ليونهارت أويلر", font=arabic_font, font_size=60)
        sub_title = Text("عالم الرياضيات العبقري", font=arabic_font, font_size=40)
        group_title = VGroup(title, sub_title).arrange(DOWN)
        self.play(Write(group_title))
        self.wait(2)
        self.play(FadeOut(group_title))

        # Scene 2: Key Facts
        birth = Text("وُلِد في سويسرا ١٧٠٧", font=arabic_font, font_size=35)
        works = Text("أكثر من ٨٠٠ بحث علمي", font=arabic_font, font_size=35)
        group_facts = VGroup(birth, works).arrange(DOWN, buff=1)
        self.play(FadeIn(birth.shift(UP)))
        self.play(FadeIn(works.shift(DOWN)))
        self.wait(2)
        self.play(FadeOut(group_facts))

        # Scene 3: Euler's Formula
        formula = MathTex("e^{i\\pi} + 1 = 0").scale(1.5)
        formula_text = Text("أجمل معادلة رياضية", font=arabic_font, font_size=35)
        group_formula = VGroup(formula, formula_text).arrange(DOWN, buff=1)
        self.play(Write(formula))
        self.play(Write(formula_text))
        self.wait(2)
        self.play(FadeOut(group_formula))

        # Scene 4: Legacy
        blind_text = Text("واصل العمل بعد فقدان البصر", font=arabic_font, font_size=35)
        impact = Text("أساسيات الرياضيات الحديثة", font=arabic_font, font_size=35)
        group_legacy = VGroup(blind_text, impact).arrange(DOWN, buff=1)
        self.play(FadeIn(blind_text.shift(UP)))
        self.play(FadeIn(impact.shift(DOWN)))
        self.wait(2)
        self.play(FadeOut(group_legacy))

        # Final Scene
        final_text = Text("إرثه العلمي ما زال حياً اليوم", font=arabic_font, font_size=45)
        self.play(Write(final_text))
        self.wait(2)
        self.play(FadeOut(final_text))