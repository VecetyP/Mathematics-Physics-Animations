from manim import *


class ProjectileDerivationMath(Scene):
    def construct(self):
        # This will hold our saved boxes at the bottom
        saved_items = VGroup()

        # Helper function to create an explanation + equation line consistently
        def create_line(exp_string, math_string, reference_mob=None):
            exp = Text(exp_string, font_size=20, color=LIGHT_GREY)
            eq = MathTex(math_string, font_size=36)
            line = VGroup(exp, eq).arrange(DOWN, buff=0.2)
            if reference_mob:
                line.next_to(reference_mob, DOWN, buff=0.4)
            return exp, eq, line

        # ==========================================
        # STEP 1: Calculate Gravity
        # ==========================================
        title1 = Text("1. Calculate gravity (A to B)", color=YELLOW, font_size=32).to_edge(UP)
        self.play(Write(title1))

        exp1_1, eq1_1, line1_1 = create_line("Using the kinematic equation:", "v_{yB} = v_{yA} + g \\Delta t", title1)
        self.play(Write(line1_1))
        self.wait(0.8)

        exp1_2, eq1_2, line1_2 = create_line("Substitute known values (apex velocity is 0):", "0 = 98 + g(1.3)", line1_1)
        self.play(Write(line1_2))
        self.wait(0.8)

        exp1_3, eq1_3, line1_3 = create_line("Solve for the gravity constant:", "g = -75.4 \\text{ studs/s}^2", line1_2)
        self.play(Write(line1_3))
        self.wait(1)

        # Box the final value
        box1 = SurroundingRectangle(eq1_3, color=WHITE)
        self.play(Create(box1))
        self.wait(2)

        # Group the box and equation, then fade everything else
        saved_1 = VGroup(eq1_3, box1)
        self.play(
            FadeOut(title1), FadeOut(exp1_1), FadeOut(eq1_1), 
            FadeOut(exp1_2), FadeOut(eq1_2), FadeOut(exp1_3)
        )
        
        # Move the saved value to the bottom left
        self.play(saved_1.animate.scale(0.7).to_edge(DOWN).shift(LEFT * 4))
        saved_items.add(saved_1)

        # ==========================================
        # STEP 2: Total Time A to C
        # ==========================================
        title2 = Text("2. Total time from A to C (T)", color=YELLOW, font_size=32).to_edge(UP)
        self.play(Write(title2))

        exp2_1, eq2_1, line2_1 = create_line("Using the displacement formula:", "\\Delta s = u \\Delta t + \\frac{1}{2} a \\Delta t^2", title2)
        self.play(Write(line2_1))
        self.wait(0.8)

        exp2_2, eq2_2, line2_2 = create_line("Δs = 5,   a = -75.4,   Δt = T,   u = 98:", "5 = 98T + \\frac{1}{2}(-75.4)T^2", line2_1)
        self.play(Write(line2_2))
        self.wait(0.8)

        exp2_3, eq2_3, line2_3 = create_line("Rearrange into a quadratic equation:", "377T^2 - 980T + 50 = 0", line2_2)
        self.play(Write(line2_3))
        self.wait(1)

        box2 = SurroundingRectangle(eq2_3, color=WHITE)
        self.play(Create(box2))
        self.wait(2)

        saved_2 = VGroup(eq2_3, box2)
        self.play(
            FadeOut(title2), FadeOut(exp2_1), FadeOut(eq2_1), 
            FadeOut(exp2_2), FadeOut(eq2_2), FadeOut(exp2_3)
        )
        
        # Move to bottom, next to the first saved value
        self.play(saved_2.animate.scale(0.7).to_edge(DOWN).next_to(saved_1, RIGHT, buff=0.5))
        saved_items.add(saved_2)

        # ==========================================
        # STEP 3: Quadratic Formula
        # ==========================================
        title3 = Text("3. Apply the Quadratic Formula", color=YELLOW, font_size=32).to_edge(UP)
        self.play(Write(title3))

        exp3_1, eq3_1, line3_1 = create_line("Standard quadratic formula:", "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}", title3)
        self.play(Write(line3_1))
        self.wait(0.8)

        exp3_2, eq3_2, line3_2 = create_line("Substitute a,   b,   c,   and  x:", "T = \\frac{-(-980) \\pm \\sqrt{(-980)^2 - 4(377)(50)}}{2(377)}", line3_1)
        self.play(Write(line3_2))
        self.wait(0.8)

        # Construct line 3 manually so we can split the equation into 3 parts:
        # [0] is "T ="  |  [1] is the messy fraction and 0.05  |  [2] is "2.54"
        exp3_3 = Text("Simplify and select the valid landing time:", font_size=20, color=LIGHT_GREY)
        eq3_3 = MathTex("T = ", "\\frac{490 \\pm 25\\sqrt{354}}{377} \\approx 0.05 , \\; ", "2.54", font_size=36)
        line3_3 = VGroup(exp3_3, eq3_3).arrange(DOWN, buff=0.1).next_to(line3_2, DOWN, buff=0.25)
        
        self.play(Write(line3_3))
        self.wait(0.8)

        # Box ONLY the "2.54" part (which is eq3_3[2]) in GREEN
        box3 = SurroundingRectangle(eq3_3[2], color=GREEN)
        self.play(Create(box3))
        self.wait(2)

        # Create the final clean version to move to the bottom
        final_eq3 = MathTex("T = 2.54 \\text{ s}", font_size=36).move_to(eq3_3)
        final_box3 = SurroundingRectangle(final_eq3, color=WHITE)
        saved_3 = VGroup(final_eq3, final_box3)

        # Clean up the screen: fade out the middle junk, merge 'T =' and '2.54' together
        self.play(
            FadeOut(title3), FadeOut(line3_1), FadeOut(line3_2), FadeOut(exp3_3), 
            FadeOut(eq3_3[1]), # Fades out the fraction and 0.05
            ReplacementTransform(VGroup(eq3_3[0], eq3_3[2]), final_eq3),
            ReplacementTransform(box3, final_box3)
        )
        
        self.play(saved_3.animate.scale(0.7).to_edge(DOWN).next_to(saved_2, RIGHT, buff=0.5))
        saved_items.add(saved_3)

        # ==========================================
        # STEP 4: Time from B to C
        # ==========================================
        title4 = Text("4. Calculate time from B to C", color=YELLOW, font_size=32).to_edge(UP)
        self.play(Write(title4))

        exp4_1, eq4_1, line4_1 = create_line("Subtract ascent time from total time:", "\\Delta t_{B \\to C} = T - t_{A \\to B}", title4)
        self.play(Write(line4_1))
        self.wait(0.8)

        exp4_2, eq4_2, line4_2 = create_line("Substitute calculated values:", "\\Delta t_{B \\to C} = 2.54 - 1.3", line4_1)
        self.play(Write(line4_2))
        self.wait(0.8)

        exp4_3, eq4_3, line4_3 = create_line("Final Answer:", "\\Delta t_{B \\to C} = 1.24 \\text{ s}", line4_2)
        eq4_3.set_color(GREEN)
        self.play(Write(line4_3))
        self.wait(1)

        # Clean the screen one last time, keeping only the final equation
        self.play(
            FadeOut(title4), FadeOut(line4_1), FadeOut(line4_2), FadeOut(exp4_3),
            eq4_3.animate.scale(1.5).move_to(ORIGIN)
        )
        
        # Box and highlight the final answer in the center
        highlight = BackgroundRectangle(eq4_3, color=LIGHT_PINK, fill_opacity=0.2, buff=0.2)
        box4 = SurroundingRectangle(eq4_3, color=RED, buff=0.2)
        self.play(FadeIn(highlight),Create(box4))
        
        self.wait(3)
        
        

class ProductRuleProof(Scene):
    def construct(self):
        # ── 0. Title ────────────────────────────────────────────────────────
        title = Text("Product Rule", font_size=52, weight=BOLD)
        subtitle = MathTex(r"\frac{d}{dx}[f(x)\,g(x)] = f'(x)\,g(x) + f(x)\,g'(x)",
                           font_size=36)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── 1. Setup: idea text ─────────────────────────────────────────────
        idea = Text("Think of f and g as side lengths of a rectangle.",
                    font_size=28, color=YELLOW).to_edge(UP)
        self.play(FadeIn(idea))
        self.wait(0.8)

        # ── 2. Draw the original rectangle  f × g ───────────────────────────
        # We'll use ValueTrackers so the rectangle can grow later.
        f_val = ValueTracker(2.5)   # initial f
        g_val = ValueTracker(1.8)   # initial g
        df_val = ValueTracker(0.0)  # Δf  (animated to 0.7)
        dg_val = ValueTracker(0.0)  # Δg  (animated to 0.5)

        SCALE = 1.4          # pixel scale factor
        ORIGIN = LEFT * 3.5 + DOWN * 1.2

        def make_rect(w, h, color, opacity=1.0):
            r = Rectangle(width=w * SCALE, height=h * SCALE,
                          color=color, fill_color=color, fill_opacity=opacity)
            r.move_to(ORIGIN, aligned_edge=DL)
            return r

        # Main (original) rectangle — blue
        main_rect = always_redraw(lambda: make_rect(
            f_val.get_value(), g_val.get_value(), BLUE, opacity=0.35))

        # Brace + labels for sides
        f_brace = always_redraw(lambda: Brace(
            make_rect(f_val.get_value(), g_val.get_value(), WHITE, 0),
            direction=DOWN, buff=0.12, color=WHITE))
        g_brace = always_redraw(lambda: Brace(
            make_rect(f_val.get_value(), g_val.get_value(), WHITE, 0),
            direction=LEFT, buff=0.12, color=WHITE))

        f_label = always_redraw(lambda: MathTex("f", color=WHITE, font_size=32)
                                .next_to(f_brace, DOWN, buff=0.15))
        g_label = always_redraw(lambda: MathTex("g", color=WHITE, font_size=32)
                                .next_to(g_brace, LEFT, buff=0.15))

        area_label = always_redraw(lambda: MathTex("A = fg", font_size=30,
                                                    color=BLUE_B)
                                   .move_to(ORIGIN + RIGHT * f_val.get_value()
                                            * SCALE / 2
                                            + UP * g_val.get_value()
                                            * SCALE / 2))

        self.play(FadeIn(idea))
        self.play(Create(main_rect), run_time=0.8)
        self.play(GrowFromCenter(f_brace), GrowFromCenter(g_brace))
        self.play(Write(f_label), Write(g_label), Write(area_label))
        self.wait(0.8)

        # ── 3. Transition text ───────────────────────────────────────────────
        self.play(FadeOut(idea))
        step1 = Text("Now increase f by Δf and g by Δg …",
                     font_size=26, color=YELLOW).to_edge(UP)
        self.play(FadeIn(step1))

        # ── 4. Δg strip (top, GREEN) ─────────────────────────────────────────
        dg_rect = always_redraw(lambda: Rectangle(
            width=f_val.get_value() * SCALE,
            height=dg_val.get_value() * SCALE,
            color=GREEN, fill_color=GREEN, fill_opacity=0.55
        ).move_to(ORIGIN + UP * g_val.get_value() * SCALE, aligned_edge=DL))

        # Δf strip (right, RED)
        df_rect = always_redraw(lambda: Rectangle(
            width=df_val.get_value() * SCALE,
            height=g_val.get_value() * SCALE,
            color=RED, fill_color=RED, fill_opacity=0.55
        ).move_to(ORIGIN + RIGHT * f_val.get_value() * SCALE, aligned_edge=DL))

        # Corner piece (PURPLE) — Δf·Δg
        corner_rect = always_redraw(lambda: Rectangle(
            width=df_val.get_value() * SCALE,
            height=dg_val.get_value() * SCALE,
            color=PURPLE, fill_color=PURPLE, fill_opacity=0.75
        ).move_to(ORIGIN
                  + RIGHT * f_val.get_value() * SCALE
                  + UP * g_val.get_value() * SCALE,
                  aligned_edge=DL))

        self.play(FadeIn(dg_rect), FadeIn(df_rect), FadeIn(corner_rect))

        # Animate the strips growing
        self.play(
            df_val.animate.set_value(0.7),
            dg_val.animate.set_value(0.5),
            run_time=1.8, rate_func=smooth
        )
        self.wait(0.5)

        # ── 5. Label the three new pieces ───────────────────────────────────
        dg_lbl = always_redraw(lambda: MathTex(r"f\,\Delta g", font_size=26,
                                                color=GREEN)
                               .move_to(ORIGIN
                                        + RIGHT * f_val.get_value() * SCALE / 2
                                        + UP * (g_val.get_value()
                                                + dg_val.get_value() / 2)
                                        * SCALE))

        df_lbl = always_redraw(lambda: MathTex(r"\Delta f\,g", font_size=26,
                                                color=RED)
                               .move_to(ORIGIN
                                        + RIGHT * (f_val.get_value()
                                                   + df_val.get_value() / 2)
                                        * SCALE
                                        + UP * g_val.get_value() * SCALE / 2))

        corner_lbl = always_redraw(lambda: MathTex(r"\Delta f\,\Delta g",
                                                    font_size=20, color=PURPLE)
                                   .move_to(ORIGIN
                                            + RIGHT * (f_val.get_value()
                                                       + df_val.get_value() / 2)
                                            * SCALE
                                            + UP * (g_val.get_value()
                                                    + dg_val.get_value() / 2)
                                            * SCALE))

        self.play(Write(dg_lbl), Write(df_lbl), Write(corner_lbl))
        self.wait(1)

        # ── 6. Algebra panel on the right ────────────────────────────────────
        self.play(FadeOut(step1))
        step2 = Text("Total change in area:", font_size=26,
                     color=YELLOW).to_edge(UP)
        self.play(FadeIn(step2))

        eq1 = MathTex(r"\Delta A", "=",
                      r"\underbrace{f\,\Delta g}_{\text{green}}",
                      "+",
                      r"\underbrace{\Delta f\,g}_{\text{red}}",
                      "+",
                      r"\underbrace{\Delta f\,\Delta g}_{\text{purple}}",
                      font_size=28)
        eq1.set_color_by_tex(r"f\,\Delta g", GREEN)
        eq1.set_color_by_tex(r"\Delta f\,g", RED)
        eq1.set_color_by_tex(r"\Delta f\,\Delta g", PURPLE)
        eq1.to_corner(UR).shift(DOWN * 1.0 + LEFT * 0.3)

        self.play(Write(eq1), run_time=1.5)
        self.wait(1)

        # ── 7. Divide by Δx ──────────────────────────────────────────────────
        eq2 = MathTex(
            r"\frac{\Delta A}{\Delta x}", "=",
            r"f\,\frac{\Delta g}{\Delta x}",
            "+",
            r"\frac{\Delta f}{\Delta x}\,g",
            "+",
            r"\frac{\Delta f}{\Delta x}\,\Delta g",
            font_size=28
        )
        eq2.next_to(eq1, DOWN, buff=0.55)

        self.play(TransformMatchingShapes(eq1.copy(), eq2), run_time=1.2)
        self.wait(0.8)

        # ── 8. Take the limit ─────────────────────────────────────────────────
        step3 = Text(r"As Δx → 0, the purple corner vanishes (it's second-order small).",
                     font_size=24, color=YELLOW).to_edge(UP)
        self.play(FadeOut(step2), FadeIn(step3))

        # Shrink the corner piece
        self.play(
            df_val.animate.set_value(0.05),
            dg_val.animate.set_value(0.05),
            run_time=1.5, rate_func=smooth
        )
        self.play(FadeOut(corner_rect), FadeOut(corner_lbl))
        self.wait(0.5)

        eq3 = MathTex(
            r"\frac{d}{dx}[fg]", "=",
            r"f\,\frac{dg}{dx}",
            "+",
            r"\frac{df}{dx}\,g",
            font_size=34, color=YELLOW
        )
        eq3.next_to(eq2, DOWN, buff=0.55)

        self.play(Write(eq3), run_time=1.3)
        self.wait(0.5)

        # ── 9. Final boxed result ─────────────────────────────────────────────
        self.play(FadeOut(step3))
        self.play(FadeOut(eq1), FadeOut(eq2))

        final = MathTex(
            r"(fg)' = f'g + fg'",
            font_size=52, color=YELLOW
        )
        box = SurroundingRectangle(final, color=YELLOW, buff=0.25, corner_radius=0.15)
        final_group = VGroup(final, box).to_corner(UR).shift(DOWN * 1.2 + LEFT * 0.3)

        self.play(Write(final), Create(box), run_time=1.2)

        proven = Text("Q.E.D.", font_size=30, color=GOLD).next_to(final_group, DOWN, buff=0.3)
        self.play(FadeIn(proven, scale=1.5))
        self.wait(2.5)

        # ── 10. Fade out everything ───────────────────────────────────────────
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.2)
        self.wait(0.3)










