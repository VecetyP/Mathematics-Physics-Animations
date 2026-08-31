from manim import *

# manim playground :)


class demo(Scene):
    def construct(self):
        t = Text("Hello").shift(UP)
        t2 = Text("World").shift(DOWN)
        self.play(Write(t), Write(t2))
        self.wait(3)


class LaTeXTest(Scene):
    def construct(self):
        tex = MathTex(r"e^{i\pi} + 1 = 0")
        self.play(Write(tex))
        self.wait()

