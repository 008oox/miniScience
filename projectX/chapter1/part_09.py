from manim import *
from project_init import *

class Part09(Scene):
    def shot_09_calculator(self):
        self.add_voice("09.mp3")
        bg = self.background("#D7C6B0")

        title = self.title_text(
            "17世纪 · 欧洲书房",
            42
        )

        title.to_edge(UP)

        desk = Rectangle(
            width=10,
            height=1.2,
            fill_color="#6B4528",
            fill_opacity=1,
            stroke_width=0
        )

        desk.to_edge(DOWN, buff=1)

        calc = self.calculator(1.0)

        calc.move_to(
            DOWN * 0.5
        )

        subtitle = self.subtitle(
            "到了17世纪，欧洲人发明了机械计算器！"
        )

        self.add(bg)

        self.play(
            FadeIn(title),
            FadeIn(desk),
            run_time=0.8
        )

        self.play(
            FadeIn(calc, shift=UP),
            run_time=1
        )

        self.play(
            Rotate(
                calc[-1],
                PI / 2,
                about_point=calc[-1].get_start()
            ),
            run_time=1
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(5)

        self.clear()