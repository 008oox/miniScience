from manim import *
from project_init import *

class Part08(Scene):
    def shot_08_abacus_error(self):
        self.add_voice("08.mp3")
        bg = self.background("#D9D1C7")

        abacus = self.abacus(0.9)

        abacus.move_to(
            LEFT * 2
        )

        error = Text(
            "？",
            font="Consolas",
            font_size=90,
            color=RED
        )

        error.move_to(
            RIGHT * 3
        )

        hourglass_top = Triangle(
            fill_color="#C6A15B",
            fill_opacity=1,
            stroke_color="#765B30"
        )

        hourglass_top.scale(0.7)
        hourglass_top.move_to(
            RIGHT * 3 + DOWN * 1.2
        )

        title = self.title_text(
            "拨错了……",
            45
        )

        title.to_edge(UP)

        subtitle = self.subtitle(
            "不过嘛，人难免会拨错，而且一颗一颗拨……确实有点慢。"
        )

        self.add(bg)

        self.play(
            FadeIn(abacus),
            run_time=1
        )

        self.play(
            abacus.animate.rotate(
                5 * DEGREES
            ),
            run_time=0.5
        )

        self.play(
            FadeIn(error),
            FadeIn(title),
            run_time=0.7
        )

        self.play(
            Rotate(
                hourglass_top,
                PI,
                run_time=2
            )
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(5)

        self.clear()