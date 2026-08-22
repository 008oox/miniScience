from manim import *
from project_init import *

class Part04(Scene):
    def shot_04(self, Scene):
        text_voice = """于是，算盘出现了。算盘是一种古代的计数器，在中国算盘有几千年的使用历史。"""
        add_voice(Scene, text_voice)
        voice_time = 5
        bg = background("#E8C99B")
        
        market = title_text("古代中国柱算 → 算盘",42)

        market.to_edge(UP)

        shop = Rectangle(
            width=6,
            height=2.5,
            fill_color="#8B5A2B",
            fill_opacity=1,
            stroke_color="#543416"
        )

        shop.move_to(DOWN * 0.8)

        abacus = ImageMobject(asset_path("abacus.png"))

        abacus.move_to(DOWN * 0.6)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(
            FadeIn(market),
            FadeIn(shop),
            run_time=0.8
        )

        Scene.play(FadeIn(abacus),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(voice_time)

        Scene.clear()