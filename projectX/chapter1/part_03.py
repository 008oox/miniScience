from manim import *
from project_init import *

class Part03(Scene):
    def shot_03(self, Scene):
        text_voice = """因为人类正好有十根手指，所以“十进制”就这样自然地诞生了！可是，计数越来越大以后，
        光靠手指可就不够用了，人们开始思考：有没有一种工具，能帮我们更快、更准确地计数呢？"""
        
        add_voice(Scene, text_voice)
        voice_time = 13.5
        bg = background("#6B91F3")

        title = title_text( "十根手指 → 10,如果数字太大就无法用双手表示了", 30)

        title.move_to(UP * 2)

        fingers = ImageMobject(asset_path("finger.png"))
        fingers.scale(0.8)
        fingers.move_to(DOWN * 0.3)

        number = Text(
            "10",
            font="Consolas",
            font_size=100
        )

        number.move_to(
            DOWN * 1.8
        )

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(fingers),run_time=0.8)

        Scene.play(FadeIn(title),FadeIn(subtitle_text),run_time=0.8)

        Scene.wait(voice_time)

        Scene.clear()