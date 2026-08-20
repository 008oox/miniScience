from manim import *
from project_init import *

class Part14(Scene):
    def shot_14_ending(self):
        self.add_voice("14.mp3")
        bg = self.background("#B7E4A8")

        bamboo_l = self.bamboo(
            -5,
            -3,
            1
        )

        bamboo_r = self.bamboo(
            5,
            -3,
            1
        )

        panda, hand = self.panda(0.9)

        panda.move_to(
            DOWN * 0.4
        )

        ending = Text(
            "未完待续",
            font="Microsoft YaHei",
            font_size=65,
            color="#D64545"
        )

        ending.move_to(
            RIGHT * 3 + UP * 1
        )

        subtitle = self.subtitle(
            "下次，我们再看看更神奇的机器！拜拜～"
        )

        beads = VGroup()

        for i in range(8):

            bead = Circle(
                radius=0.13,
                fill_color="#D34B3E",
                fill_opacity=1,
                stroke_width=0
            )

            bead.move_to(
                [
                    -3 + i * 0.8,
                    -2.7 + 0.3 * (i % 2),
                    0
                ]
            )

            beads.add(bead)

        self.add(bg)

        self.play(
            FadeIn(bamboo_l),
            FadeIn(bamboo_r),
            run_time=0.8
        )

        self.play(
            FadeIn(panda, shift=UP),
            run_time=1
        )

        self.play(
            FadeIn(ending),
            run_time=1
        )

        self.play(
            Rotate(
                hand,
                PI / 3,
                about_point=hand.get_center()
            ),
            run_time=0.4
        )

        self.play(
            FadeIn(beads),
            FadeIn(subtitle),
            run_time=0.8
        )

        self.wait(4)