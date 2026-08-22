from manim import *
from project_init import *

class Part01(Scene):
    def shot_01_intro(self, Scene):
        text_voice = "我是火炬哥！从现在起，我来带大家了解计算机的起源，传统的计算器！"
        add_voice(Scene, text_voice)
        bg = background("#B7E4A8")

        panda = ImageMobject(asset_path("panda.png"))
        panda.scale(0.9)
        panda.move_to(DOWN * 0.4)

        title = title_text(
            "火炬哥课堂之：计算机演化史 序章",
            40
        )

        title.to_edge(UP, buff=0.4)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(
            FadeIn(panda, shift=UP),
            run_time=1
        )

        bubble = RoundedRectangle(
            width=1.7,
            height=0.8,
            corner_radius=0.2,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=BLACK
        )

        hello = Text(
            "嗨！",
            font_size=32,
            fill_color=GREEN
        )

        hello.move_to(bubble.get_center())

        bubble_group = VGroup(
            bubble,
            hello
        )

        bubble_group.next_to(
            panda,
            UP,
            buff=0.3
        )

        Scene.play(
            GrowFromCenter(bubble_group),
            Write(title),
            run_time=1
        )

        Scene.play(
            FadeIn(subtitle_text),
            run_time=0.7
        )

        Scene.wait(4)

        Scene.clear()