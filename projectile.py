from manim import *
import numpy as np


class ProjectileMotion(Scene):
    def construct(self):

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True}
        ).add_coordinates()
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        plane = NumberPlane(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            x_length=10,
            y_length=6,
            background_line_style={
                "stroke_width": 1,
                "stroke_color": BLUE_D,
                "stroke_opacity": 0.5,
                }
        )
        plane.move_to(axes.c2p(5, 3))



        v0 = 16.0
        theta = 70 * DEGREES
        g = 20
        
        vx = v0 * np.cos(theta)
        vy = v0 * np.sin(theta)
        t_final = (2 * vy) / g


        def get_pos(t):
            x = vx * t
            y = vy * t - 0.5 * g * (t**2)
            return axes.c2p(x, y)

        
        def get_vel_vector(t):
            v_y_current = vy - g * t
            return np.array([vx * 0.3, v_y_current * 0.3, 0])

        
        t_tracker = ValueTracker(0)
        
        
        path = ParametricFunction(
            lambda t: get_pos(t), 
            t_range=[0, t_final], 
            color=YELLOW
        )

        ball = Dot(color=RED).move_to(get_pos(0))
        

        vel_arrow = always_redraw(lambda: Arrow(
            start=ball.get_center(),
            end=ball.get_center() + get_vel_vector(t_tracker.get_value()),
            buff=0,
            color=BLUE,
            stroke_width=4
        ))

        vel_arrow_x = always_redraw(lambda: Arrow(
            start=ball.get_center(),
            end=ball.get_center() + np.array([vx * 0.3, 0, 0]),
            buff=0,
            color=GREEN,
            stroke_width=4
        ))

        vel_arrow_y = always_redraw(lambda: Arrow(
            start=ball.get_center(),
            end=ball.get_center() + np.array([0, (vy - g*t_tracker.get_value())*0.3, 0]),
            buff=0,
            color=RED,
            stroke_width=4
        ))


        pos_formula = MathTex(
            r"\vec{s}(t) = \begin{bmatrix} v_x t \\ v_y t - \frac{1}{2}gt^2 \end{bmatrix}",
            color=YELLOW
        ).scale(0.7).to_corner(UR).shift(LEFT * 0.5)

        vel_formula = MathTex(
            r"\vec{v}(t) = \frac{d\vec{s}}{dt} = \begin{bmatrix} v_x \\ v_y - gt \end{bmatrix}",
            color=BLUE,
        ).scale(0.7).next_to(pos_formula, DOWN, buff=0.5)


        self.play(Write(axes), Write(labels), Write(plane))
        self.play(FadeIn(pos_formula), FadeIn(vel_formula))
        self.add(ball)
        self.play(Create(vel_arrow), Create(vel_arrow_x), Create(vel_arrow_y))
        

        ball.add_updater(lambda m: m.move_to(get_pos(t_tracker.get_value())))


        self.play(
            Create(path),
            t_tracker.animate.set_value(t_final),
            run_time=4,
            rate_func=linear
        )
        
        ball.clear_updaters()
        self.play(FadeOut(vel_arrow), FadeOut(vel_arrow_x), FadeOut(vel_arrow_y), time_width=0.2)
        self.wait(2)



class ProjectileVisuals(Scene):
    def construct(self):
        # ==========================================
        # SETUP: Axes, The Curve, and Initial Points
        # ==========================================

        axes = Axes(
            x_range=[-0.2, 3.2, 0.5],
            y_range=[-10, 80, 20],
            x_length=10,
            y_length=5.5,
            axis_config={"color": WHITE, "font_size": 12},
        )
        
        visual_h = 15 
        
        # Function for the curve: y = 98t - 37.7t^2
        def height_func(t): 
            return 98 * t - 37.7 * (t ** 2)

        x_label = axes.get_x_axis_label("Distance")
        y_label = axes.get_y_axis_label("Height (studs)")
        y_label.shift(LEFT * 1.8).shift(UP * 0.15)
        
        # Define Point A (Start) and Point B (Apex)
        pt_A = axes.coords_to_point(0, 0)
        pt_B = axes.coords_to_point(1.3, height_func(1.3))
        pt_C = axes.coords_to_point(2.44, visual_h)
        
        
        landing_box = Rectangle(
            width=1.5, 
            height=0.9, 
            fill_opacity=0.5, 
            fill_color=GREY, 
            color=WHITE
        )
        # Position the box so its TOP surface is exactly at pt_C
        # pt_C was defined at (2.44, visual_h)
        landing_box.move_to(pt_C, aligned_edge=UP).shift(RIGHT*0.6)

        self.play(Create(axes), run_time=1)
        self.play(Write(x_label), Write(y_label), run_time=1.5)
        self.play(FadeIn(landing_box))
        # ---> THE ACTUAL CURVE <---
        graph = axes.plot(height_func, color=BLUE, x_range=[0, 2.44])
        self.play(Create(graph), run_time=2)


        dot_A = Dot(pt_A, color=GREEN)
        label_A = Text("A", font_size=24).next_to(dot_A, DL)
        
        dot_B = Dot(pt_B, color=RED)
        label_B = Text("B (Apex)", font_size=24).next_to(dot_B, UP)

        # ==========================================
        # UPDATED VISUAL STEP 1: Motion from A to B with Vectors
        # ==========================================
        # 1. Show Point A and its initial vertical velocity
        v_y_initial_text = MathTex("v_{yA} = 98", font_size=24, color=GREEN).next_to(dot_A, LEFT, buff=0.3).shift(UP * 0.4)
        self.play(FadeIn(dot_A, label_A), Write(v_y_initial_text))
        self.wait(0.8)

        # 2. Setup the moving parts
        t_tracker = ValueTracker(0)

        # Helper function for vertical velocity
        def get_vy(t):
            return 98 - 75.4 * t

        # Arbitrary horizontal speed for the visual arc
        vx_val = 1.5 

        # The moving point
        moving_dot = always_redraw(lambda: Dot(
            axes.coords_to_point(t_tracker.get_value(), height_func(t_tracker.get_value())),
            color=WHITE
        ))

        # Vertical velocity arrow (scaled down by 30 so it fits nicely on screen)
        vy_arrow = always_redraw(lambda: Arrow(
            moving_dot.get_center(),
            moving_dot.get_center() + UP * (get_vy(t_tracker.get_value()) / 30),
            buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.2
        ))

        # Horizontal velocity arrow
        vx_arrow = always_redraw(lambda: Arrow(
            moving_dot.get_center(),
            moving_dot.get_center() + RIGHT * vx_val,
            buff=0, color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.2
        ))
        
        vy_arrow_fixed = Arrow(
            moving_dot.get_center(),
            moving_dot.get_center() + UP * (get_vy(t_tracker.get_value()) / 30),
            buff=0, color=GREEN, stroke_width=4, max_tip_length_to_length_ratio=0.2
        )
        
        vx_arrow_fixed = Arrow(
            moving_dot.get_center(),
            moving_dot.get_center() + RIGHT * vx_val,
            buff=0, color=RED, stroke_width=4, max_tip_length_to_length_ratio=0.2
        )

        # Dynamic text tracking the current v_y
        vy_dynamic_text = always_redraw(lambda: MathTex(
            f"v_y = {max(0, get_vy(t_tracker.get_value())):.1f}", font_size=20, color=GREEN
        ).next_to(vy_arrow, UP, buff=0.1))

        self.play(FadeIn(moving_dot), FadeIn(vy_dynamic_text), FadeIn(vy_arrow), FadeIn(vx_arrow), FadeIn(vy_arrow_fixed), FadeIn(vx_arrow_fixed))

        # 3. Animate the flight to the apex (t=1.3)
        self.play(t_tracker.animate.set_value(1.3), run_time=3, rate_func=linear)
        self.remove(vy_dynamic_text)
        self.wait(0.5)

        # 4. Show Point B, its final vertical velocity, AND the t=1.3 line
        v_y_final_text = MathTex("v_{yB} = 0", font_size=24, color=GREEN).next_to(dot_B, UP * 1.1, buff=0.7)
        
        t_B_line = axes.get_vertical_line(pt_B, color=YELLOW, line_func=DashedLine)
        t_B_label = MathTex("t = 1.3", font_size=24).next_to(axes.coords_to_point(1.3, 0), DOWN)

        # Fade out the dynamic text, show the final v_y, and drop the dashed line down to the axis
        self.play(
            FadeIn(dot_B, label_B), 
            Write(v_y_final_text),
            Create(t_B_line),
            Write(t_B_label)
        )
        self.wait(0.8)
        
        vinitialBox = SurroundingRectangle(v_y_initial_text, color=WHITE, fill_opacity=0.1)
        vfinalBox = SurroundingRectangle(v_y_final_text, color=WHITE, fill_opacity=0.1)
        timeBox = SurroundingRectangle(t_B_label, color=WHITE, fill_opacity=0.1)
        self.play(Create(vinitialBox), Create(vfinalBox), Create(timeBox), run_time=1)
        self.wait(1)

        # 5. Show the math calculation to find g
        calc_group = VGroup(
            MathTex("\\Delta v_y = v_{yB} - v_{yA} = 0 - 98 = -98", font_size=24),
            MathTex("\\Delta t = 1.3 \\text{ s}", font_size=24),
            MathTex("g = \\frac{\\Delta v_y}{\\Delta t} = \\frac{-98}{1.3} = -75.4 \\text{ studs/s}^2", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.2).to_corner(UR, buff=0.5)

        calc_box = SurroundingRectangle(calc_group, color=WHITE, fill_opacity=0.1)

        self.play(Write(calc_group), run_time=3)
        self.wait(1)
        self.play(Create(calc_box), run_time=1)
        self.wait(3)

        # 6. Clean up the screen to prepare for Step 2
        # Notice we DO NOT fade out t_B_line or t_B_label here, so they stay for the brace later!
        self.play(
            FadeOut(moving_dot), FadeOut(vx_arrow), FadeOut(vy_arrow),
            FadeOut(v_y_initial_text), FadeOut(v_y_final_text),
            FadeOut(calc_group), FadeOut(calc_box),
            FadeOut(vinitialBox), FadeOut(vfinalBox), FadeOut(timeBox),
            FadeOut(vx_arrow_fixed), FadeOut(vy_arrow_fixed)
        )
        self.wait(0.5)
        

        # ==========================================
        # VISUAL STEP 2 & 3: The "Middle Ground" y=15 line
        # ==========================================
        
        h_tracker = ValueTracker(0) # Starts at y=0

        # 1. The moving pink line
        y5_line = always_redraw(lambda: axes.get_horizontal_line(
            axes.coords_to_point(2.4, h_tracker.get_value()), 
            color=PINK, 
            line_func=DashedLine
        ))

        # 2. The Highlight Area (The "Space Underneath")
        # We use a Rectangle that grows as the tracker increases
        dy_highlight = always_redraw(lambda: Rectangle(
            width=axes.coords_to_point(2.4, 0)[0] - axes.coords_to_point(0, 0)[0],
            height=abs(axes.coords_to_point(0, h_tracker.get_value())[1] - axes.coords_to_point(0, 0)[1]),
            fill_color=PINK,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.coords_to_point(0, 0), aligned_edge=DL))

        # 3. The Dynamic Label (Counts from 0 to 5)
        y5_label = always_redraw(lambda: MathTex(
            # We divide by 3 to map the visual_h (15) back to the math value (5)
            f"\\Delta y = {h_tracker.get_value() / 3:.1f}", 
            color=PINK, 
            font_size=24
        ).next_to(axes.coords_to_point(0, h_tracker.get_value()), LEFT, buff=0.2))

        # Show second root (Point C) (labeled as math result 2.54)
        dot_C = Dot(pt_C, color=GREEN)
        label_C = Text("C", font_size=24).next_to(dot_C, UR, buff=0.1)

        # --- ANIMATION ---
        self.play(FadeIn(dy_highlight, y5_line, y5_label, dot_C, label_C))
        
        
        # Move from 0 to 15 (visual_h)
        self.play(h_tracker.animate.set_value(visual_h), run_time=2, rate_func=smooth)
        self.wait(1)

        # Coordinates solved to sit perfectly on the curve at y=15
        pt_root1 = axes.coords_to_point(0.16, visual_h) 

        dot_root1 = Dot(pt_root1, color=YELLOW)
        
        
        # Show first root (labeled as math result 0.05)
        self.play(FadeIn(dot_root1))
        root1_label = MathTex("t \\approx 0.05", font_size=20).next_to(dot_root1, UP)
        self.play(Write(root1_label))


        root2_label = MathTex("T = 2.54", font_size=30, color=GREEN).next_to(label_C, RIGHT, buff=0.2)
        self.play(Write(root2_label))
        self.wait(1)

        self.play(FadeOut(dot_root1), FadeOut(root1_label))

        # ==========================================
        # VISUAL STEP 4: Time from B to C (The Brace)
        # ==========================================
        # Connect apex (1.3) to our visual Point C (2.44)
        brace = BraceBetweenPoints(
            axes.coords_to_point(1.3, 0), 
            axes.coords_to_point(2.44, 0), 
            direction=DOWN, 
            color=ORANGE
        )
        brace.shift(DOWN*0.5)
        brace_text = brace.get_tex("\\Delta t = 1.24\\text{ s}").scale(0.8)
        
        self.play(FadeIn(brace), Write(brace_text))
        
        # Highlight final segment from Apex to Point C
        arc_segment = axes.plot(height_func, color=ORANGE, x_range=[1.3, 2.44])
        self.play(Create(arc_segment), run_time=1.5)
        self.wait(2)
        

