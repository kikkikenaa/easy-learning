import sys
from manim import *

class ElectricityAnimation(Scene):
    def construct(self):
        wire = Line(LEFT * 4, RIGHT * 4, color=GRAY)
        self.play(Create(wire))

        electron = Dot(color=BLUE).move_to(wire.get_start())
        self.play(MoveAlongPath(electron, wire), run_time=3)
        self.wait(1)

class MagnetismAnimation(Scene):
    def construct(self):
        magnet = SVGMobject("magnet.svg").scale(2)
        self.play(DrawBorderThenFill(magnet))
        self.wait(1)

        field_lines = []
        for i in range(-2, 3):
            field_lines.append(Arrow(LEFT*3, RIGHT*3, color=YELLOW).shift(UP*i*0.5))
        
        self.play(*[Create(line) for line in field_lines])
        self.wait(2)

if __name__ == "__main__":
    topic = sys.argv[1] if len(sys.argv) > 1 else "physics_electricity"

    if topic == "physics_electricity":
        ElectricityAnimation().render()
    elif topic == "physics_magnetism":
        MagnetismAnimation().render()
