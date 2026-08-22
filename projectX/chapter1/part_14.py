from manim import *
from project_init import *

class Part14(Scene):
    def shot_14(self, Scene):
        text_voice = "感谢收看！下一章，聊电子计算器，咱们不见不散。"
        add_voice(Scene, text_voice)
        voice_time = 2
        bg = background("#B7E4A8")

        calculator = ImageMobject(asset_path("calculator.png"))
        calculator.scale(0.9)
        calculator.move_to(DOWN * 0.4)

        title = title_text("火炬哥课堂之：下一章 电子计算器的崛起",40)

        title.to_edge(UP, buff=0.4)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(title),run_time=0.8)

        Scene.play(FadeIn(calculator),run_time=1)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        Scene.wait(voice_time)

        Scene.clear()