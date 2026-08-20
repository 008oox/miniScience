from manim import *
from project_init import *

class Part13(Scene):
    def shot_13_tunnel(self):
        self.add_voice("13.mp3")
        bg = self.background("#17152B")

        tunnel = VGroup()

        for r in [1, 2, 3, 4, 5]:

            circle = Circle(
                radius=r,
                stroke_color=PURPLE,
                stroke_width=3,
                fill_opacity=0
            )

            tunnel.add(circle)

        panda, hand = self.panda(0.65)

        panda.move_to(
            DOWN * 0.4
        )

        abacus = self.abacus(0.35)
        abacus.move_to(
            LEFT * 4
        )

        calc = self.calculator(0.35)
        calc.move_to(
            RIGHT * 4
        )

        old_computer = Rectangle(
            width=1.5,
            height=1.2,
            fill_color="#555555",
            fill_opacity=0.8
        )

        old_computer.move_to(
            LEFT * 2 + UP * 1.5
        )

        phone = RoundedRectangle(
            width=0.9,
            height=1.6,
            corner_radius=0.12,
            fill_color="#444444",
            fill_opacity=0.8
        )

        phone.move_to(
            RIGHT * 2 + UP * 1.5
        )

        title = self.title_text(
            "从手指 → 算盘 → 机械计算器",
            38
        )

        title.to_edge(UP)

        subtitle = self.subtitle(
            "从手指到算盘，再到机械计算器，人类从没停止追求更快的计算！"
        )

        self.add(bg)

        self.play(
            FadeIn(tunnel),
            run_time=1
        )

        self.play(
            FadeIn(abacus),
            FadeIn(calc),
            FadeIn(old_computer),
            FadeIn(phone),
            run_time=1
        )

        self.play(
            FadeIn(panda),
            FadeIn(title),
            run_time=1
        )

        self.play(
            Rotate(
                hand,
                PI / 3,
                about_point=hand.get_center()
            ),
            run_time=0.5
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(5)

        self.clear()