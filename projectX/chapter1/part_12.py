from manim import *
from project_init import *

class Part12(Scene):
    def shot_12(self, Scene):
        text_voice = """原因在于机械计算器对精密机械加工的要求很高，制造成本极高，维修又困难，导致无法大规模商用。"""
        add_voice(Scene, text_voice)

        voice_time = 5.5
        bg = background("#E8C99B")

        title = title_text("机械计算器的局限性 → 制造与维护成本高", 42)
        title.to_edge(UP)

        abacus_1 = ImageMobject(asset_path("abacus.png"))
        abacus_1.scale(0.68)
        abacus_1.move_to(LEFT * 2 + DOWN * 0.6)

        calculator_old = ImageMobject(asset_path("calculator_old.png"))
        calculator_old.scale(0.48)
        calculator_old.move_to(RIGHT * 2 + DOWN * 0.6)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(title), run_time=0.8)
        Scene.play(FadeIn(abacus_1), run_time=1)
        Scene.play(FadeIn(subtitle_text), run_time=0.5)

        Scene.wait(0.5)

        Scene.play(FadeIn(calculator_old), run_time=0.5)

        # 给机械计算器打一个大叉
        x1 = Line(
            calculator_old.get_corner(UL),
            calculator_old.get_corner(DR),
            stroke_color="#D94A4A",
            stroke_width=8
        )

        x2 = Line(
            calculator_old.get_corner(UR),
            calculator_old.get_corner(DL),
            stroke_color="#D94A4A",
            stroke_width=8
        )

        Scene.play(
            Create(x1),
            Create(x2),
            run_time=0.5
        )

        Scene.wait(voice_time)

        Scene.clear()