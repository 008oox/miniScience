from manim import *
from project_init import *

class Part07(Scene):
    def shot_07(self, Scene):
        text_voice = """在中国直到上世纪90年代前，人们还在普遍使用算盘来进行核算。"""
        add_voice(Scene, text_voice)
        voice_time = 3.5
        bg = background("#AAC5F4")
        
        market = title_text("算盘 → 真的用了很久",42)

        market.to_edge(UP)

        abacus = ImageMobject(asset_path("abacushand.png"))

        abacus.move_to(DOWN * 0.6)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(
            FadeIn(market),
            run_time=0.8
        )

        Scene.play(FadeIn(abacus),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(voice_time)

        Scene.clear()