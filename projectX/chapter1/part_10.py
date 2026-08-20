from manim import *
from project_init import *

class Part10(Scene):
    def shot_10_calculator_advantage(self):
        self.add_voice("10.mp3")
        bg = self.background("#E5D6BD")

        calc = self.calculator(0.9)

        calc.move_to(
            RIGHT * 2
        )

        display_result = Text(
            "1234",
            font="Consolas",
            font_size=32,
            color=GREEN
        )

        display_result.move_to(
            calc[3].get_center()
        )

        check = Text(
            "✓ 正确",
            font="Microsoft YaHei",
            font_size=40,
            color=GREEN
        )

        check.move_to(
            LEFT * 3
        )

        subtitle = self.subtitle(
            "齿轮一转，结果就出来了！人为失误大大减少，效率也提高了不少。"
        )

        self.add(bg)

        self.play(
            FadeIn(calc),
            FadeIn(check),
            run_time=1
        )

        self.play(
            Rotate(
                calc[-1],
                PI / 2,
                about_point=calc[-1].get_start()
            ),
            run_time=0.8
        )

        self.play(
            FadeIn(display_result),
            FadeIn(subtitle),
            run_time=0.8
        )

        self.wait(5)

        self.clear()