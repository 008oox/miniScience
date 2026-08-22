from project_init import *
from manim import *

from chapter1.part_01 import Part01
from chapter1.part_02 import Part02
from chapter1.part_03 import Part03
from chapter1.part_04 import Part04
from chapter1.part_05 import Part05
from chapter1.part_06 import Part06
from chapter1.part_07 import Part07
from chapter1.part_08 import Part08
from chapter1.part_09 import Part09
from chapter1.part_10 import Part10
from chapter1.part_11 import Part11
from chapter1.part_12 import Part12
from chapter1.part_13 import Part13
from chapter1.part_14 import Part14

class AllScenes(Scene):
    def construct(self):
        Part01().shot_01_intro(self)
        Part02().shot_02(self)
        Part03().shot_03(self)
        Part04().shot_04(self)
        Part05().shot_05(self)
        Part06().shot_06(self)
        Part07().shot_07(self)
        Part08().shot_08(self)
        Part09().shot_09(self)
        Part10().shot_10(self)
        Part11().shot_11(self)
        Part12().shot_12(self)
        Part13().shot_13(self)
        Part14().shot_14(self)
        