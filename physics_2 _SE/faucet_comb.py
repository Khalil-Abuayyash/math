from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0
config.frame_rate = 30

class CombAttractsWater(Scene):
    def construct(self):

        faucet = SVGMobject("faucet.svg")
        faucet.to_edge(UP).shift(DOWN * 0.5)
        self.add(faucet)
        
        shift = [1, -0.5,0]
        start = faucet.get_bottom() + shift
        end = faucet.get_bottom() + DOWN * 3
        end += shift
        
        drops_num = 15
        water_drops = VGroup(*[Dot(color=BLUE) for _ in range(drops_num)])
        for i, drop in enumerate(water_drops):
            drop.move_to(start + DOWN * (i * 0.5))

        comb = SVGMobject("comb.svg").scale(0.5)
        comb.move_to(water_drops.get_right() + [3, 0, 0])
        self.add(comb)
        self.wait()

        def animate_droplets(drops):
            animations = []
            for drop in drops:
                animations.append(
                    drop.animate.move_to(drop.get_center() + DOWN * 5).set_opacity(0)
                )
            return animations
        
        self.add(water_drops)

        for _ in range(3):  # Adjust for more repetitions
            self.play(*animate_droplets(water_drops), run_time=2, rate_func=linear)
            self.play(*[drop.animate.set_opacity(1).move_to(start + DOWN * (i * 0.5))
                        for i, drop in enumerate(water_drops)], run_time=0.1)



        # Comb moves closer to the water
        self.play(comb.animate.shift(LEFT * 1.7), run_time=2)
        
        deflected_water_drops = VGroup(*[Dot(color=BLUE) for _ in range(drops_num)])
        
        for i, drop in enumerate(deflected_water_drops):
            if i < 4:
                drop.move_to(start + DOWN * (i * 0.5) + + RIGHT * i * 0.05)
            if 4 <= i < 11:
                drop.move_to(start + DOWN * (i * 0.5) + RIGHT * i * 0.1)
            if i >= 11:
                drop.move_to(start + DOWN * (i * 0.5) + RIGHT * i * 0.15)
            # drop.move_to(start + DOWN * (i * 0.5) + RIGHT * i * 0.1)
            

        self.play(Transform(water_drops, deflected_water_drops), run_time=1.5)
        
        self.wait()
