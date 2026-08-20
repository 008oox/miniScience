from manim import *
from project_init import *

class Part12(Scene):
    def shot_12_calculator_error(self):
        self.add_voice("12.mp3")
        bg = self.background("#D2D0CC")

        calc = self.calculator(0.9)

        calc.move_to(
            LEFT * 2
        )

        error = Text(
            "ERROR",
            font="Consolas",
            font_size=42,
            color=RED
        )

        error.move_to(
            RIGHT * 3
        )

        smoke = VGroup()

        for i in range(5):

            s = Circle(
                radius=0.25,
                fill_color="#777777",
                fill_opacity=0.5,
                stroke_width=0
            )

            s.move_to(
                [
                    1 + i * 0.35,
                    1 + i * 0.25,
                    0
                ]
            )

            smoke.add(s)

        subtitle = self.subtitle(
            "但它也有短板：算不了太大的数，而且……咔咔咔，还是不够快。"
        )

        self.add(bg)

        self.play(
            FadeIn(calc),
            run_time=1
        )

        self.play(
            Rotate(
                calc[-1],
                PI / 4,
                about_point=calc[-1].get_start()
            ),
            run_time=1
        )

        self.play(
            FadeIn(error),
            FadeIn(smoke),
            run_time=0.8
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(5)

        self.clear()