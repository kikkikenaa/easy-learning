import sys
from manim import *

class DigestiveSystemAnimation(Scene):
    def construct(self):
        stomach = Circle(radius=1, color=BLUE).shift(LEFT*2)
        intestines = Rectangle(width=3, height=1, color=GREEN).shift(RIGHT*2)
        stomach_label = Text("Stomach").next_to(stomach, UP)
        intestines_label = Text("Intestines").next_to(intestines, UP)

        food = Dot(color=RED).move_to(stomach)
        self.play(Create(stomach), Create(stomach_label))
        self.wait(1)
        self.play(food.animate.move_to(intestines), run_time=2)
        self.play(Create(intestines), Create(intestines_label))
        self.wait(2)

class CirculatorySystemAnimation(Scene):
    def construct(self):
        heart = SVGMobject("heart.svg").scale(2)
        self.play(DrawBorderThenFill(heart))
        self.wait(1)

        blood = Dot(color=RED).move_to(heart.get_center())
        blood_path = ArcBetweenPoints(start=heart.get_center() + LEFT, end=heart.get_center() + RIGHT)
        
        self.play(MoveAlongPath(blood, blood_path), run_time=3)
        self.wait(2)

# Detect the animation to run
if __name__ == "__main__":
    system = sys.argv[1] if len(sys.argv) > 1 else "biology_digestive"

    if system == "biology_digestive":
        DigestiveSystemAnimation().render()
    elif system == "biology_circulatory":
        CirculatorySystemAnimation().render()
