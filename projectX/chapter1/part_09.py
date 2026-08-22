from manim import *
from project_init import *

class Part09(Scene):
    def shot_09(self, Scene):
        text_voice = """在17世纪时，欧洲人曾发明了机械计算器，这是一种替代算盘的尝试。"""
        add_voice(Scene, text_voice)
        voice_time = 4
        bg = background("#AAC5F4")
        
        market = title_text("机械计算器 → 新的尝试",42)

        market.to_edge(UP)

        abacus = ImageMobject(asset_path("calculator_old.png"))

        abacus.move_to(DOWN * 0.2)

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