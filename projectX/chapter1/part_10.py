from manim import *
from project_init import *

class Part10(Scene):
    def shot_10(self, Scene):
        text_voice = """机械计算器就简单多了，输入数字、转动旁边的手柄，结果就自动算出来了，也大大减少了人工计算出错的可能。"""
        add_voice(Scene, text_voice)
        voice_time = 6
        bg = background("#DCEAD4")

        title = title_text("机械计算器 → 简单、可靠", 42)
        title.to_edge(UP)

        calculator = ImageMobject(asset_path("calculator_old.png"))
        calculator.scale(0.65)
        calculator.move_to(DOWN * 0.4)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg)

        Scene.play(FadeIn(title),FadeIn(calculator),run_time=1.2)

        Scene.play(FadeIn(subtitle_text),run_time=0.5)

        # -------------------------
        # 1. 输入数字
        # -------------------------
        input_box = Rectangle(
            width=1.9,
            height=1.3,
            stroke_color=YELLOW,
            stroke_width=5,
            fill_opacity=0
        )

        input_box.move_to(calculator.get_center() + DOWN * 1.35 + LEFT * 0.15)

        input_text = Text("输入数字",font_size=28,color="#543416")

        input_text.next_to(input_box,DOWN,buff=0.15)

        Scene.play(Create(input_box),FadeIn(input_text),run_time=0.6)

        # 模拟按键
        key_1 = Circle(
            radius=0.08,
            fill_color=YELLOW,
            fill_opacity=0.8,
            stroke_width=0
        )

        key_2 = key_1.copy()
        key_3 = key_1.copy()

        key_1.move_to(calculator.get_center() + DOWN * 1.15 + LEFT * 0.35)

        key_2.move_to(calculator.get_center() + DOWN * 1.15)

        key_3.move_to(calculator.get_center() + DOWN * 1.15 + RIGHT * 0.35)

        Scene.play(FadeIn(key_1), run_time=0.5)

        Scene.play(FadeOut(key_1),FadeIn(key_2),run_time=0.5)

        Scene.play(FadeOut(key_2),FadeIn(key_3),run_time=0.5)

        Scene.play(FadeOut(key_3),run_time=0.5)

        # -------------------------
        # 2. 摇一摇
        # -------------------------
        Scene.play(FadeOut(input_box), FadeOut(input_text), run_time=0.3)

        shake_text = Text("摇动手柄", font_size=32, color="#543416")
        shake_text.next_to(calculator, RIGHT, buff=0.3)

        shake_box = Rectangle(width=0.2, height=1, stroke_color= YELLOW, stroke_width=3, fill_opacity=0)
        shake_box.move_to(calculator.get_center() + RIGHT * 2 + UP * 0.7)

        Scene.play(FadeIn(shake_text), Create(shake_box), run_time=0.2)

        # 模拟机械计算器被摇动YELLOW
        Scene.play(calculator.animate.shift(UP * 0.08), run_time=0.6)
        Scene.play(calculator.animate.shift(DOWN * 0.16), run_time=0.6)
        Scene.play(calculator.animate.shift(UP * 0.16), run_time=0.6)
        Scene.play(calculator.animate.shift(DOWN * 0.08), run_time=0.6)
        Scene.play(FadeOut(shake_box), run_time=0.2)

        # -------------------------
        # 3. 结果自动显示
        # -------------------------
        result_box = Rectangle(
            width=4.2,
            height=0.65,
            stroke_color=GREEN,
            stroke_width=5,
            fill_opacity=0
        )

        result_box.move_to(
            calculator.get_center()
            + UP * 1.35
        )

        result_text = Text(
            "结果自动显示",
            font_size=30,
            color="#543416"
        )

        result_text.next_to(
            result_box,
            UP,
            buff=0.12
        )

        Scene.play(
            FadeOut(shake_text),
            Create(result_box),
            FadeIn(result_text),
            run_time=0.6
        )

        # -------------------------
        # 4. 减少人工错误
        # -------------------------
        accuracy = Text(
            "✓ 减少人工计算错误",
            font_size=34,
            color=GREEN
        )

        accuracy.move_to(
            DOWN * 2.7
        )

        Scene.play(
            FadeIn(accuracy),
            run_time=0.7
        )

        Scene.wait(1)

        Scene.clear()