from manim import *
import numpy as np


class StreamLine_VectorField(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )

        self.wait(1)

        self.play(Create(plane), run_time=1)

        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT

        vector_field = ArrowVectorField(
            func,
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
        )

        stream_lines = StreamLines(
            func,
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            color=BLUE,
            stroke_width=2,
        )

        self.wait(1)

        self.play(Create(vector_field), run_time=1)

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=3, time_width=0.8, rate_func=linear)
        self.wait(5)
        self.play(stream_lines.end_animation())
        self.wait(0.5)


class GravityField(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.move_camera(zoom=0.7)
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            tips = False,
            axis_config={
                "stroke_color": WHITE,
                "stroke_width": 3,
                "stroke_opacity": 0.8
            }
        )
        self.play(Create(axes))
        planet = Sphere(radius=1, color=BLUE)
        planet.move_to([0, 0, 0])
        self.play(Create(planet))
        self.wait(1)

        gravityfunc = lambda pos: (
            -20 * pos / ((np.linalg.norm(pos) + 1e-6)**3)
            if np.linalg.norm(pos) > 1.0 else np.array([0, 0, 0])
        )

        vector_field = ArrowVectorField(
            gravityfunc,
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            opacity=0.9,
            vector_config={
                "stroke_width": 3
            }
        )

        self.play(Create(vector_field), run_time=1)

        stream_lines = StreamLines(
            gravityfunc,
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            color=YELLOW,
            stroke_width=4,
            opacity=0.7
        )

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1, time_width=0.03, rate_func=linear)
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        stream_lines.end_animation()
        self.play(FadeOut(stream_lines))
        self.wait(1)


        #begin the cool orbit stuff
        t = ValueTracker(0)

        def get_grav_func():
            center = planet.get_center()
            return lambda pos: (
                -20 * (pos - center) / ((np.linalg.norm(pos - center) + 0.1)**3)
                if np.linalg.norm(pos - center) > 0.5 else np.array([0, 0, 0])
            )

        planet.add_updater(lambda m: m.move_to([
            2 * np.cos(t.get_value()+PI/2),
            2 * np.sin(t.get_value()),
            np.sin(t.get_value() * 2)
        ]))

        vector_field.add_updater(lambda m: m.become(ArrowVectorField(
            get_grav_func(),
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-3, 3, 1],
            opacity=0.9,
            vector_config={
                "stroke_width": 3
            }
        )))

        self.play(t.animate.set_value(TAU), run_time=6, rate_func=smooth)
        self.stop_ambient_camera_rotation()
        self.wait(1)


class TEST(Scene):
    def construct(self):
        func = lambda pos: (((pos[0] * UR + pos[1] * LEFT) - pos)/4) 
        field = ArrowVectorField(func)
        self.add(field)

