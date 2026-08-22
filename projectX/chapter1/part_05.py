from manim import *
from project_init import *


class Part05(Scene):
    def shot_05(self, Scene):
        text_voice = """中国古代重量单位使用16进制，官方的计数单位统一为10进制，算盘可以兼容这两种计数方式。"""
        add_voice(Scene, text_voice)

        voice_time = 8
        bg = background("#E8C99B")

        title = title_text("古代算盘 → 进制切换", 42)
        title.to_edge(UP)

        # -------------------------
        # 左侧：算盘
        # -------------------------
        abacus = ImageMobject(asset_path("abacus.png"))
        abacus.scale(0.62)
        abacus.move_to(LEFT * 2.2 + DOWN * 0.7)

        # -------------------------
        # 右侧：示意区域
        # -------------------------
        demo_group = VGroup()

        demo_title = Text("""同一根算盘柱""",font_size=20,color="#543416")

        demo_title.move_to(RIGHT * 3.4 + UP * 1.5)

        # 一根算盘柱
        rod = Line(
            RIGHT * 0.9,
            LEFT * 0.9,
            color="#543416",
            stroke_width=5
        )
        rod.rotate(PI / 2)
        rod.move_to(RIGHT * 3.4 + DOWN * 0.1)

        # 上珠
        bead1 = Ellipse(
            width=0.65,
            height=0.38,
            fill_color="#4A2418",
            fill_opacity=1,
            stroke_color="#2E160F"
        )
        bead1.move_to(RIGHT * 3.4 + UP * 0.45)

        bead2 = Ellipse(
            width=0.65,
            height=0.38,
            fill_color="#4A2418",
            fill_opacity=1,
            stroke_color="#2E160F"
        )
        bead2.move_to(RIGHT * 3.4 + UP * 0.85)

        # 下方珠子
        lower_beads = VGroup()

        for i in range(4):
            bead = Ellipse(
                width=0.65,
                height=0.38,
                fill_color="#4A2418",
                fill_opacity=1,
                stroke_color="#2E160F"
            )
            bead.move_to(
                RIGHT * 3.4 +
                DOWN * (0.45 + i * 0.42)
            )
            lower_beads.add(bead)

        # -------------------------
        # 第一阶段：十进制
        # -------------------------
        decimal_label = Text("十进制",font_size=20,color="#543416")
        decimal_label.move_to(RIGHT * 3.4 + DOWN * 2.1)

        decimal_value = Text("上珠 1 颗 = 5， 上珠只使用一颗",font_size=26,color="#543416")
        decimal_value.next_to(decimal_label, DOWN, buff=0.2)

        # -------------------------
        # 第二阶段：十六进制
        # -------------------------
        hex_label = Text("十六进制",font_size=20,color="#543416")
        hex_label.move_to(decimal_label)

        hex_value = Text("上珠 2 颗 = 10， 上珠使用两颗",font_size=26,color="#543416")
        hex_value.next_to(hex_label, DOWN, buff=0.2)

        # -------------------------
        # 开场
        # -------------------------
        Scene.add(bg)

        Scene.play(
            FadeIn(title),
            FadeIn(abacus),
            run_time=1
        )

        Scene.play(
            FadeIn(demo_title),
            Create(rod),
            FadeIn(lower_beads),
            FadeIn(bead1),
            FadeIn(decimal_label),
            FadeIn(decimal_value),
            run_time=1
        )

        # -------------------------
        # 十进制 → 十六进制
        # -------------------------
        Scene.wait(3)

        Scene.play(
            FadeIn(bead2),
            Transform(decimal_label, hex_label),
            Transform(decimal_value, hex_value),
            run_time=1
        )

        # -------------------------
        # 最后的结论
        # -------------------------
        result = Text("一把算盘，兼容两种计数方式",font_size=28,color="#543416")

        result.move_to(RIGHT * 3.4 + DOWN * 3.1)

        Scene.play(FadeIn(result),run_time=0.8)

        Scene.wait(voice_time - 6)

        Scene.clear()