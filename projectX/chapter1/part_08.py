from manim import *
from project_init import *

class Part08(Scene):
    def shot_08(self, Scene):
        text_voice = """算盘有很多缺点，计算慢，操作复杂，培养一个熟练的算盘手需要很长时间，还容易因操作失误导致计算错误。"""
        add_voice(Scene, text_voice)
        voice_time = 7.5
        bg = background("#AAC5F4")
        
        market = title_text("算盘 → 缺点不少",42)

        market.to_edge(UP)

        abacus = ImageMobject(asset_path("abacus.png"))

        abacus.move_to(DOWN * 0.6)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(market),run_time=0.8)

        Scene.play(FadeIn(abacus),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(voice_time)

        Scene.clear()