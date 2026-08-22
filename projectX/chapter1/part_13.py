from manim import *
from project_init import *

class Part13(Scene):
    def shot_13(self, Scene):
        text_voice = """从掰手指，拨算盘到摇机械计算器，人类一直在寻找更好的计算工具，来帮助我们进行复杂的计算。"""
        add_voice(Scene, text_voice)

        voice_time = 6
        bg = background("#E8C99B")

        title = title_text("计算器具序章 → 总结", 42)
        title.to_edge(UP)

        fingers = ImageMobject(asset_path("finger.png"))
        fingers.scale(0.5)
        fingers.move_to(LEFT * 3 + DOWN * 0.6)

        abacus_1 = ImageMobject(asset_path("abacus.png"))
        abacus_1.scale(0.48)
        abacus_1.move_to(DOWN * 0.6)

        calculator_old = ImageMobject(asset_path("calculator_old.png"))
        calculator_old.scale(0.4)
        calculator_old.move_to(RIGHT * 3 + DOWN * 0.6)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)
        
        Scene.play(FadeIn(subtitle_text),run_time=0.1)

        Scene.play(FadeIn(title),run_time=0.1)

        Scene.play(FadeIn(fingers), run_time=0.5)

        Scene.play(FadeIn(abacus_1),run_time=0.9)

        Scene.play(FadeIn(calculator_old),run_time=1.3)

        Scene.wait(voice_time)

        Scene.clear()