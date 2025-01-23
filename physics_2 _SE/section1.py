from manim import *

config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16.0
config.frame_height = 9.0
config.frame_rate = 30

class SectionOne(Scene):

    def construct(self):
        title = Text("Section 22.1: Properties of Electric Charges", font="Arial").scale(1)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        explaination_points = VGroup()
        points = [
            Text("• بعض الظواهر اليومية تثبت وجود القوة الكهربائية", font="Arial").scale(0.7),
            Text("من الأمثلة عليها التصاق القصاصات الورقية ببالون مطاطي، وتنافر شعر الإنسان", font="Arial").scale(0.4),
            Text("يمكن تفسير هذه الظواهر بوجود الشحنات الكهربائية والقوة الكهربائية", font="Arial").scale(0.4),
            Text("بسبب وجود التنافر والتجاذب فهذا يعني وجود شحنتين مختلفتين ", font="Arial").scale(0.4),
        ]

        for i, point in enumerate(points):
            # explaination_points.add(point[::-1].scale((0.7)))
            explaination_points.add(point[::-1])

        explaination_points.arrange(DOWN, buff=0.5).to_edge(RIGHT)

        
        for i, point in enumerate(points):
            explaination_points[i].to_edge(RIGHT)
            self.play(Write(explaination_points[i]))
            self.wait(1)

        self.wait(2)