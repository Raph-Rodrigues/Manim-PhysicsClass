from manim import *


class IntroIII(Scene):
    def construct(self):
        s = Text("Existem grandezas vetoriais e escalares", font_size=32)
        s.save_state()
        # mais rápido e suave
        self.play(Write(s, reverse=True, remover=False), run_time=0.9)
        self.wait(0.6)
        self.play(
            s.animate.set_color(PURPLE).set_opacity(0.5).shift(2 * LEFT).scale(3),
            run_time=0.9,
            rate_func=smooth,
        )
        self.play(s.animate.shift(5 * DOWN).rotate(PI / 4), run_time=0.9, rate_func=smooth)

        vet = Tex(r'Vetoriais:', tex_template=TexFontTemplates.french_cursive, font_size=80)
        # entrada mais rápida
        self.play(Write(vet), run_time=0.8)
        self.wait(0.4)
        self.play(vet.animate().shift(3 * UP), run_time=0.9, rate_func=smooth)
        # restaurar breve
        self.play(Restore(s), run_time=1.0, rate_func=smooth)
        self.wait(0.4)

        explainVet = Text("Possuem direção, sentido e módulo", font_size=28)
        self.play(Transform(s, explainVet), run_time=0.9, rate_func=smooth)
        self.wait(0.8)

        esc = Tex(r'Escalares:', tex_template=TexFontTemplates.french_cursive, font_size=80)
        # transformar vet -> esc com arco
        esc.move_to(vet.get_center())
        self.play(Transform(vet, esc, path_arc=PI / 2), run_time=1.0)
        self.play(ApplyWave(esc, rate_func=linear, ripples=4), run_time=0.8)
        self.wait(0.4)
        self.play(esc.animate().shift(3 * UP), run_time=0.9, rate_func=smooth)
        self.wait(0.6)

        explainEsc = Text("Possuem apenas módulo", font_size=28)
        # transformar explainVet -> explainEsc com arco
        explainEsc.move_to(explainVet.get_center())
        self.play(Transform(explainVet, explainEsc, path_arc=PI / 3), run_time=0.9)
        self.wait(0.8)
        self.play(FadeOut(explainEsc), FadeOut(esc), run_time=0.6)
        self.wait(0.6)

        exVetTitle = Text("Exemplos de grandezas vetoriais:", font_size=32)
        exVetTxt = Text("Velocidade, Força, Aceleração, Deslocamento", font_size=26, slant=ITALIC)
        exVet = VGroup(exVetTitle, exVetTxt)
        self.play(Write(exVet, reverse=True, remover=False), run_time=0.9)
        self.play(exVet.animate.arrange(DOWN).shift(UP), run_time=0.8, rate_func=smooth)
        self.wait(0.6)
        self.play(Indicate(exVetTxt, color=RED), run_time=0.6)
        self.wait(0.4)

        exEscTitle = Text("Exemplos de grandezas escalares:", font_size=32)
        exEscTxt = Text("Massa, Temperatura, Energia, Tempo", font_size=26, slant=ITALIC)
        exEsc = VGroup(exEscTitle, exEscTxt)
        self.play(Write(exEsc, reverse=False, remover=True), run_time=0.8)
        self.play(exEsc.animate.arrange(DOWN).next_to(exVet, DOWN, buff=0.5), run_time=0.8, rate_func=smooth)
        self.wait(0.6)
        self.play(Indicate(exEscTxt, color=BLUE), run_time=0.6)
        self.wait(0.8)

        grandsGroup = VGroup(exVet, exEsc)
        self.play(FadeOut(grandsGroup), run_time=0.7)
        self.wait(0.4)

        quest = Text("O que ocorre com grandezas com módulos muito elevados ou pequenos?", font_size=24)
        self.play(Write(quest), run_time=0.6)
        self.play(quest.animate.to_edge(UP), run_time=0.6)
        self.wait(0.6)
        self.play(Indicate(quest), run_time=0.5)
        self.wait(0.4)
        expQuest = Text("Utilizamos a notação científica, para facilitar a escrita e a leitura", font_size=22)
        self.play(Write(expQuest, reverse=True, remover=False), run_time=0.8)
        self.play(expQuest.animate.next_to(quest, DOWN), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(quest), FadeOut(expQuest), run_time=0.6)
        self.wait(0.6)

        exNotCient = Text("Como por exemplo a velocidade da luz no vácuo:", font_size=28)
        valNotCient = Tex(
            r"$300000000 = 3 \times 10^8$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=80,
        )
        self.add(exNotCient)
        self.play(GrowFromCenter(exNotCient), run_time=0.7)
        self.wait(0.5)
        self.play(exNotCient.animate.to_edge(UP), run_time=0.7)
        self.wait(0.4)
        self.play(DrawBorderThenFill(valNotCient), run_time=0.9)
        self.wait(0.8)
        self.play(Indicate(valNotCient), run_time=0.6)
        self.wait(0.6)
        self.play(Unwrite(exNotCient, reverse=False, remover=True), Unwrite(valNotCient, reverse=False, remover=True), run_time=0.8)
        self.wait(0.8)

        obs = MarkupText(f'<span underline="double" underline_color="green">Observe que na notação científica</span> utilizamos <span fgcolor="{YELLOW}">SEMPRE na base 10</span>',
                         font_size=26)
        self.play(SpinInFromNothing(obs, angle=2 * PI), run_time=0.8)
        self.wait(0.6)
        self.play(ApplyWave(obs, rate_func=linear, ripples=2), run_time=0.9)
        self.wait(0.6)
        self.play(obs.animate.shift(UP * 2.25), run_time=0.6)
        exNotCient2 = Text("Para números dentro do intervalo de 0 e 1, utilizamos expoente negativo", font_size=22)
        self.play(FadeIn(exNotCient2), run_time=0.7)
        self.play(exNotCient2.animate.next_to(obs, DOWN, buff=1.2), run_time=0.6)
        self.wait(0.6)
        exCarga = Text("Ex: Carga Elementar", font_size=30)
        self.play(Write(exCarga, reverse=False, remover=True), run_time=0.8)
        self.play(exCarga.animate.next_to(exNotCient2, DOWN, buff=1.2), run_time=0.6)
        cargEle = Tex(
            r"$1.6 \times 10^{-19}$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=80,
        )
        self.play(Write(cargEle), run_time=0.9)
        self.play(exCarga.animate.shift(LEFT * 2.45), run_time=0.6)
        self.play(cargEle.animate.next_to(exCarga, RIGHT, buff=0.8), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(obs), FadeOut(exNotCient2), FadeOut(exCarga), FadeOut(cargEle), run_time=0.8)

        ordGrand = MarkupText(f'Temos também a <span fgcolor="{YELLOW}">Ordem de Grandeza</span> para aproximar uma medida com a <span underline="double" underline_color="red">potência mais próxima desta medida</span>', 
                              font_size=22).scale(0.95)
        self.play(GrowFromCenter(ordGrand), run_time=0.7)
        self.play(ordGrand.animate.to_edge(UP, buff=0.85), run_time=0.6)
        ordGrandExp = Text("Utilizando a notação científica teremos o valor sempre compreendida no intervalo:", font_size=25, slant=ITALIC)
        self.play(Write(ordGrandExp), ordGrand.animate.scale(0.8), run_time=0.8)
        self.play(ordGrandExp.animate.next_to(ordGrand, DOWN, buff=1.2), run_time=0.6)
        self.play(ordGrandExp.animate.scale(0.75), run_time=0.5)
        ordGrandIntrv = Tex(r"$10^{e} \leq c \times 10^{e} < 10{e} + 1$",
                            tex_template=TexFontTemplates.french_cursive,
                            font_size=66)
        self.play(SpinInFromNothing(ordGrandIntrv, angle=2 * PI), run_time=0.8)
        self.play(ordGrandIntrv.animate.next_to(ordGrandExp, DOWN, buff=0.75), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(ordGrand), FadeOut(ordGrandExp), FadeOut(ordGrandIntrv), run_time=0.6)