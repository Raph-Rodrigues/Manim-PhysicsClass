from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Seja bem-vindo ao seu Pior Pesadelo", font_size=42)
        self.play(Write(title))
        self.wait(2)

        self.play(title.animate.scale(0.5).to_edge(UP))
        self.wait(1)

        obs = Text("Of coursemente, somente se você for de humanas huahuahua", font_size=22)
        self.play(FadeIn(obs))
        self.wait(0.6)
        self.play(obs.animate(lag_ratio=0, run_time=1.6).next_to(title, DOWN))
        self.wait(0.8)
        self.play(Wiggle(obs))

        subtitle = Text("Aula 1: Introdução à Física", font_size=44)
        self.play(subtitle.animate(lag_ratio=0, run_time=0.8).scale(1.5))
        self.play(subtitle.animate(lag_ration=0, run_time=1.5).shift(UP * 2))
        self.wait(2)
        msgTxt = Text("CHUPA HUMANAS que não conseguem criar animações direito", font_size=16).scale(0.8)
        self.play(FadeIn(msgTxt))
        self.wait(0.5)
        self.play(msgTxt.animate().shift(LEFT * 4))
        self.wait(1)
        self.play(FadeOut(msgTxt))
        self.wait(1.2)
        msg = Text("Espero que sobreviva a experiência", font_size=32)
        self.play(GrowFromCenter(msg))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(obs), FadeOut(subtitle), FadeOut(msg))
        self.wait(1)