from manim import *

def background(color="#DDF3D5"):
    bg = Rectangle(
        width=14.3,
        height=8.2,
        fill_color=color,
        fill_opacity=1,
        stroke_width=0
    )
    bg.move_to(ORIGIN)
    return bg

def subtitle(text):
    box = RoundedRectangle(
        width=12.5,
        height=0.85,
        corner_radius=0.15,
        fill_color=BLACK,
        fill_opacity=0.72,
        stroke_width=0
    )

    t = Text(
        text,
        font="Microsoft YaHei",
        font_size=25,
        color=WHITE
    )

    if t.width > 11.8:
        t.scale_to_fit_width(11.8)

    group = VGroup(box, t)
    t.move_to(box.get_center())

    group.to_edge(DOWN, buff=0.15)

    return group

def title_text(text, size=42):
    t = Text(
        text,
        font="Microsoft YaHei",
        font_size=size
    )

    if t.width > 11.5:
        t.scale_to_fit_width(11.5)

    return t