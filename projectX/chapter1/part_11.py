from manim import *
from project_init import *

class Part11(Scene):
    def shot_11_calculator_easy(self):
        self.add_voice("11.mp3")
        bg = self.background("#DCEAD4")

        person = Circle(
            radius=0.8,
            fill_color="#F0C49A",
            fill_opacity=1,
            stroke_color=BLACK
        )

        person.move_to(
            LEFT * 2
        )

        manual = Rectangle(
            width=2.5,
            height=3,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=BLACK
        )

        manual.move_to(
            RIGHT * 1
        )

        ok = Text(
            "OK!",
            font="Consolas",
            font_size=50,
            color=GREEN
        )

        ok.move_to(
            RIGHT * 3.5
        )

        subtitle = self.subtitle(
            "培训也更简单了，不用背复杂的口诀，摇一摇就行！"
        )

        self.add(bg)

        self.play(
            FadeIn(person),
            FadeIn(manual),
            run_time=1
        )

        self.play(
            FadeIn(ok),
            run_time=0.8
        )

        self.play(
            FadeIn(subtitle),
            run_time=0.5
        )

        self.wait(6)

        self.clear()