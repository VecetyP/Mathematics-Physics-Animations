from manim import *
import numpy as np


class FourierTransform(ThreeDScene):
    def construct(self):
        axisXYZ = ThreeDAxes(x_range=[0, 40, 1], y_range=[-10, 10, 1], z_range=[-10, 10, 1], 
                          x_length=20, y_length=10, z_length=20)
        axisXYZ.scale(.5)
        self.wait(1)
        self.play(Create(axisXYZ))

        xz_plane = NumberPlane(
            x_range=[0, 10, 1], 
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )

        xz_plane.rotate(90 * DEGREES, axis=RIGHT)
        xz_plane.move_to(axisXYZ.c2p(20, 0, 0))

        self.add(xz_plane)



        time = ValueTracker(0)

        graph = always_redraw(lambda: axisXYZ.plot(lambda x: 
                          np.sin(3*(x - time.get_value()) + 2)*2 +
                          np.sin(2*(x - time.get_value()) + 1)*3 +
                          np.sin(5*(x - time.get_value()) + 3) +
                          np.sin((x - time.get_value()) + 2.5)*2.5 +
                          np.sin(2.5*(x - time.get_value()) + 1.5)*1.5 +
                          np.sin(4*(x - time.get_value()) + 5) +
                          np.sin(4.5*(x - time.get_value()) + 1)*1.5,
                          color=ORANGE))
        self.play(Create(graph))

        self.move_camera(
            phi=-20 * DEGREES,
            run_time=5,
            rate_func=smooth,
            added_anims=[time.animate.set_value(40)]
        )

        sin1 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(3*(x - time.get_value()) + 2)*2, color=GREEN).shift(3*OUT))
        sin2 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(2*(x - time.get_value()) + 1)*3, color=RED).shift(2*OUT))
        sin3 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(5*(x - time.get_value()) + 3), color=YELLOW).shift(1*OUT))
        sin4 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin((x - time.get_value()) + 2.5)*2.5, color=BLUE))
        sin5 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(2.5*(x - time.get_value()) + 1.5)*1.5, color=PURPLE).shift(-1*OUT))
        sin6 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(4*(x - time.get_value()) + 5), color=LIGHT_BROWN).shift(-2*OUT))
        sin7 = always_redraw(lambda: axisXYZ.plot(lambda x: np.sin(4.5*(x - time.get_value()) + 1)*1.5, color=PINK).shift(-3*OUT))

        sineGraphs = VGroup(sin7, sin6, sin5, sin4, sin3, sin2, sin1)
        self.play(ReplacementTransform(graph, sineGraphs), run_time=2, rate_func=rush_from)
        self.play(time.animate.set_value(80), run_time=5, rate_func=smooth)


        self.wait(2)

