from manim import *
from project_init import *

class Part11(Scene):
    def shot_11(self, Scene):
        text_voice = """相比算盘，机械计算器操作方便，做复杂计算的效率高，减少了人为错误。但他并没大规模替代算盘。"""
        add_voice(Scene, text_voice)

        voice_time = 5.5
        bg = background("#E8C99B")

        title = title_text("机械计算器 → 优势", 42)
        title.to_edge(UP)

        abacus_1 = ImageMobject(asset_path("abacus.png"))
        abacus_1.scale(0.68)
        abacus_1.move_to(LEFT * 2 + DOWN * 0.6)

        calculator_old = ImageMobject(asset_path("calculator_old.png"))
        calculator_old.scale(0.48)
        calculator_old.move_to(RIGHT * 2 + DOWN * 0.6)

        calculator_old.shift(RIGHT * 3)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(title),run_time=0.8)

        Scene.play(FadeIn(abacus_1),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(0.5)

        Scene.play(calculator_old.animate.shift(LEFT * 3),run_time=1.2)

        Scene.wait(voice_time)

        Scene.clear()