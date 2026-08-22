from manim import *
from project_init import *

class Part06(Scene):
    def shot_06(self, Scene):
        text_voice = """当计数超出了算盘的计算范围时，人们可以拼接算盘，来进行更大数字的计算。"""
        add_voice(Scene, text_voice)

        voice_time = 3
        bg = background("#E8C99B")

        title = title_text("计数超出范围 → 算盘的扩容", 42)
        title.to_edge(UP)

        abacus_1 = ImageMobject(asset_path("abacus.png"))
        abacus_1.scale(0.48)
        abacus_1.move_to(LEFT * 1.6 + DOWN * 0.6)

        abacus_2 = ImageMobject(asset_path("abacus.png"))
        abacus_2.scale(0.48)
        abacus_2.move_to(RIGHT * 1.6 + DOWN * 0.6)

        abacus_2.shift(RIGHT * 3)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(title),run_time=0.8)

        Scene.play(FadeIn(abacus_1),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(0.5)

        Scene.play(abacus_2.animate.shift(LEFT * 3),run_time=1.2)

        Scene.wait(voice_time)

        Scene.clear()