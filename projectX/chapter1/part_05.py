from manim import *
from project_init import *

class Part05(Scene):
    def shot_05_abacus_easy(self, Scene):
        text_voice = "首先，它学起来不难，新手也能很快上手！"
        add_voice(Scene, text_voice)
        bg = background("#DCEFD2")

        desk = Rectangle(
            width=9,
            height=1.2,
            fill_color="#9B6A3B",
            fill_opacity=1,
            stroke_width=0
        )

        desk.to_edge(DOWN, buff=1.3)

        abacus = self.abacus(0.75)
        abacus.move_to(RIGHT * 2)

        teacher = Circle(
            radius=0.7,
            fill_color="#F0C49A",
            fill_opacity=1,
            stroke_color=BLACK
        )

        teacher.move_to(LEFT * 3 + UP * 0.8)

        child = Circle(
            radius=0.6,
            fill_color="#F0C49A",
            fill_opacity=1,
            stroke_color=BLACK
        )

        child.move_to(ORIGIN + UP * 0.8)

        stars = Text(
            "★ ★ ★",
            font="Consolas",
            font_size=35,
            color=YELLOW
        )

        stars.next_to(
            child,
            UP
        )

        subtitle = self.subtitle(
            "首先，它学起来不难，新手也能很快上手！"
        )

        self.add(bg)

        self.play(
            FadeIn(desk),
            FadeIn(teacher),
            FadeIn(child),
            FadeIn(abacus),
            run_time=1
        )

        self.play(
            abacus.animate.shift(RIGHT * 0.5),
            run_time=0.8
        )

        self.play(
            FadeIn(stars),
            FadeIn(subtitle),
            run_time=0.8
        )

        self.wait(5)

        self.clear()