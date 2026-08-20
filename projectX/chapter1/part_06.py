from manim import *
from project_init import *

class Part06(Scene):
    def shot_06_place_value(self):
        self.add_voice("06.mp3")
        bg = self.background("#F1E4C8")

        abacus = self.abacus(0.9)

        abacus.move_to(
            DOWN * 0.4
        )

        labels = VGroup()

        names = [
            "个",
            "十",
            "百",
            "千"
        ]

        for i, name in enumerate(names):

            t = Text(
                name,
                font="Microsoft YaHei",
                font_size=35
            )

            t.move_to(
                [-3 + i * 2, 2, 0]
            )

            labels.add(t)

        subtitle = self.subtitle(
            "而且，中国算盘大多是十进制的，和我们平时数数一模一样，特别好理解！"
        )

        self.add(bg)

        self.play(
            FadeIn(abacus),
            run_time=1
        )

        self.play(
            LaggedStart(
                *[
                    FadeIn(x)
                    for x in labels
                ],
                lag_ratio=0.3
            ),
            run_time=1.5
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(5)

        self.clear()