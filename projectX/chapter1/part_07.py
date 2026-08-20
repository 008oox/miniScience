from manim import *
from project_init import *

class Part07(Scene):
    def shot_07_abacus_expand(self):
        self.add_voice("07.mp3")
        bg = self.background("#D6EAC5")

        abacus1 = self.abacus(0.65)
        abacus2 = self.abacus(0.65)

        abacus1.move_to(LEFT * 3)
        abacus2.move_to(RIGHT * 3)

        plus = Text(
            "+",
            font="Consolas",
            font_size=60
        )

        plus.move_to(ORIGIN)

        result = Text(
            "计算范围扩大！",
            font="Microsoft YaHei",
            font_size=42
        )

        result.to_edge(UP)

        subtitle = self.subtitle(
            "要是数太大了怎么办？再拼一架算盘就行，计算范围轻松扩大！"
        )

        self.add(bg)

        self.play(
            FadeIn(abacus1),
            FadeIn(plus),
            run_time=0.8
        )

        self.play(
            abacus2.animate.move_to(RIGHT * 1.8),
            run_time=1
        )

        self.play(
            FadeIn(result),
            FadeIn(subtitle),
            run_time=0.8
        )

        self.wait(5)

        self.clear()