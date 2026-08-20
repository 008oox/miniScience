from manim import *
from project_init import *

class Part02(Scene):

    def shot_02_fingers(self, Scene):

        text_voice = "很久很久以前，人们习惯于数数时，用掰手指的方式计数：一、二、三、四、五、六、七、八、九、十！"
        add_voice(Scene, text_voice)

        bg = background("#C7A77A")

        cave = Circle(radius=3.5, fill_color="#70513A", fill_opacity=1, stroke_width=0)
        cave.move_to(UP * 0.5)

        cave_text = title_text("很久很久以前", 40)
        cave_text.move_to(UP * 2.5)

        fingers = ImageMobject(asset_path("finger.png"))
        fingers.scale(0.8)
        fingers.move_to(DOWN * 0.3)

        subtitle_text = subtitle(text_voice)

        Scene.add(bg, cave)

        Scene.play(FadeIn(cave_text), run_time=0.8)

        Scene.play(FadeIn(fingers), FadeIn(subtitle_text), run_time=0.8)

        # 10 根手指的指尖位置（按照 finger.png 图片坐标）
        finger_pixels = [
            (18, 177),   # 左手拇指
            (75, 94),    # 左手食指
            (125, 61),   # 左手中指
            (207, 78),   # 左手无名指
            (283, 191),  # 左手小指
            (312, 178),  # 右手拇指
            (367, 95),   # 右手食指
            (433, 80),   # 右手中指
            (489, 113),  # 右手无名指
            (553, 188),  # 右手小指
        ]

        # 图片像素坐标 → Manim 坐标
        center = fingers.get_center()
        cx = center[0]
        cy = center[1]
        w, h = fingers.get_width(), fingers.get_height()

        finger_points = [
            np.array([
                cx + (x / 564 - 0.5) * w,
                cy + (0.5 - y / 375) * h,
                0
            ])
            for x, y in finger_pixels
        ]

        number = Text("1", font="Microsoft YaHei", font_size=42)
        number.to_edge(RIGHT, buff=0.8)
        number.shift(UP * 0.5)

        Scene.play(FadeIn(number), run_time=3.5)

        for i, point in enumerate(finger_points):

            ring = Circle(
                radius=0.15,
                stroke_color=YELLOW,
                stroke_width=5,
                fill_color=YELLOW,
                fill_opacity=0.18
            )

            ring.move_to(point)

            Scene.play(
                ShowPassingFlash(
                    ring.copy().scale(1.4),
                    time_width=0.4
                ),
                FadeIn(ring, scale=0.5),
                run_time=0.3
            )

            if i < 9:
                new_number = Text(
                    str(i + 2),
                    font="Microsoft YaHei",
                    font_size=42
                )
                new_number.move_to(number.get_center())

                Scene.play(
                    Transform(number, new_number),
                    run_time=0.35
                )

        Scene.wait(0.7)

        Scene.clear()