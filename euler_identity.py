from manim import *
import numpy as np


class EulerIdentityNoLatex(Scene):
    def construct(self):

        plane = ComplexPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        ).add_coordinates()
        
        circle = Circle(radius=1, color=YELLOW).set_stroke(opacity=0.5)
        
        theta = ValueTracker(0)
        
        vector = always_redraw(lambda: Vector(
            plane.n2p(np.exp(1j * theta.get_value())),
            color=WHITE
        ))
        
        label = always_redraw(lambda: Text(
            f"e^(i*{theta.get_value():.2f})",
            font_size=24,
            color=WHITE
        ).next_to(vector.get_end(), UR, buff=0.1))

        cos_line = always_redraw(lambda: Line(
            start=plane.n2p(0),
            end=plane.n2p(np.cos(theta.get_value())),
            color=GREEN,
            stroke_width=6
        ))
        
        sin_line = always_redraw(lambda: Line(
            start=plane.n2p(np.cos(theta.get_value())),
            end=plane.n2p(np.cos(theta.get_value()) + 1j * np.sin(theta.get_value())),
            color=RED,
            stroke_width=6
        ))

        formula_text = Text("e^(i*theta) = cos(theta) + i*sin(theta)", font_size=36).to_edge(UP)
        formula_text[12:22].set_color(GREEN)
        formula_text[23:].set_color(RED)

        self.add(plane, circle, formula_text)
        self.play(Create(vector), Write(label))
        self.add(cos_line, sin_line)
        
        self.play(
            theta.animate.set_value(2 * PI),
            run_time=8,
            rate_func=linear
        )
        self.wait(2)


class EulerIdentity(Scene):
    def construct(self):
        # 1. Setup
        plane = ComplexPlane(x_range=[-2, 2, 1], y_range=[-2, 2, 1]).add_coordinates()
        circle = Circle(radius=1, color=YELLOW).set_stroke(opacity=0.5)
        theta = ValueTracker(0)
        
        # 2. Moving parts
        vector = always_redraw(lambda: Vector(
            plane.n2p(np.exp(1j * theta.get_value())),
            color=WHITE
        ))
        
        # Simple label to avoid formatting crashes
        label = always_redraw(lambda: MathTex(
            rf"e^{{i \cdot {theta.get_value():.2f}}}",
            color=WHITE,
            font_size=36
        ).next_to(vector.get_end(), UR, buff=0.1))

        cos_line = always_redraw(lambda: Line(
            plane.n2p(0),
            plane.n2p(np.cos(theta.get_value())),
            color=GREEN, stroke_width=6
        ))
        
        sin_line = always_redraw(lambda: Line(
            plane.n2p(np.cos(theta.get_value())),
            plane.n2p(np.cos(theta.get_value()) + 1j * np.sin(theta.get_value())),
            color=RED, stroke_width=6
        ))

        # 3. Fixed Formula (The fix for your error)
        # We define the formula first, THEN color the parts
        formula = MathTex(r"e^{i\theta} = ", r"\cos(\theta)", r" + ", r"i\sin(\theta)")
        formula.set_color_by_tex(r"\cos(\theta)", GREEN)
        formula.set_color_by_tex(r"i\sin(\theta)", RED)
        formula.to_edge(UP)

        # 4. Animation
        self.add(plane, circle, formula)
        self.play(Create(vector), Write(label))
        self.add(cos_line, sin_line)
        
        self.play(theta.animate.set_value(2 * PI), run_time=10, rate_func=linear)
        self.wait(2)

