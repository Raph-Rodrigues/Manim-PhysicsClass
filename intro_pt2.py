from manim import *

class IntroPtII(Scene):
    def construct(self):
        grand = Text("Grandeza:", font_size=36)
        self.play(Write(grand))
        self.wait(1)
        self.play(grand.animate().scale(0.8).shift(LEFT * 5.8))
        self.wait(1)
        self.play(Indicate(grand))
        self.wait(1.4)
        defGrand = Text("tudo que pode ser medido", font_size=32, slant=ITALIC)
        self.play(GrowFromCenter(defGrand), defGrand.animate.next_to(grand, RIGHT, buff=0.8))
        self.wait(2)
        self.play(Unwrite(defGrand), Unwrite(grand, reverse=False))
        self.wait(1)
        med = Text("Medida:", font_size=36)
        self.play(Write(med))
        self.wait(1)
        self.play(med.animate().scale(0.8).shift(LEFT * 6))
        self.wait(1)
        self.play(Indicate(med))
        self.wait(1.4)
        defMed = Text("comparação com uma unidade padrão", font_size=32, slant=ITALIC)
        self.play(GrowFromCenter(defMed), defMed.animate.next_to(med, RIGHT, buff=0.8))
        self.wait(2)
        self.play(Unwrite(defMed), Unwrite(med, reverse=False))
        self.wait(1)

        msg = Text("Existe um conjunto de grandezas que são chamadas de fundamentais", font_size=28)
        self.play(GrowFromCenter(msg))
        self.wait(1)
        self.play(Indicate(msg))
        self.wait(1.5)
        self.play(msg.animate.to_edge(UP, buff=1.0).scale(0.8))
        self.wait(1)
        self.play(FadeOut(msg))
        self.wait(0.5)

        grandezas = [
            ("Comprimento", "metro (m)"),
            ("Massa", "quilograma (kg)"),
            ("Tempo", "segundo (s)"),
            ("Corrente Elétrica", "ampere (A)"),
            ("Temperatura", "kelvin (K)"),
            ("Quantidade de matéria", "mol (mol)"),
            ("Intensidade luminosa", "candela (cd)"),
        ]

        titulo_col1_start = Text("Grandeza Fundamental", font_size=36)
        titulo_col2_start = Text("Unidade de Medida", font_size=36)

        titulo_col1_start.to_edge(UP + LEFT, buff=1.5)
        titulo_col2_start.to_edge(UP + RIGHT, buff=1.5)

        titulo_col1_final = Text("Grandeza Fundamental", font_size=36)
        titulo_col2_final = Text("Unidade de Medida", font_size=36)

        headers_group = VGroup(titulo_col1_final, titulo_col2_final)
        headers_group.arrange(RIGHT, buff=3.0)
        headers_group.to_edge(UP, buff=0.75)

        self.play(Write(titulo_col1_start), Write(titulo_col2_start))
        self.wait(0.4)

        self.play(
            ClockwiseTransform(titulo_col1_start, titulo_col1_final),
            ClockwiseTransform(titulo_col2_start, titulo_col2_final),
            run_time=1.2
        )
        self.wait(0.3)

        col1_texts = VGroup(*[Text(g, font_size=28) for g, _ in grandezas])
        col2_texts = VGroup(*[Text(u, font_size=28) for _, u in grandezas])

        espaco_entre_linhas = 0.6
        col1_texts.arrange(DOWN, aligned_edge=LEFT, buff=espaco_entre_linhas)
        col2_texts.arrange(DOWN, aligned_edge=LEFT, buff=espaco_entre_linhas)

        distancia_titulo_linhas = 0.5
        col1_texts.next_to(titulo_col1_final, DOWN, buff=distancia_titulo_linhas)
        col1_texts.align_to(titulo_col1_final, LEFT)

        espaco_entre_colunas = 4.35
        col2_texts.next_to(col1_texts, RIGHT, buff=espaco_entre_colunas)
        col2_texts.align_to(col1_texts, UP)

        tabela = VGroup(titulo_col1_final, titulo_col2_final, col1_texts, col2_texts)
        tabela.move_to(ORIGIN)

        anims_alternados = []
        duracao_por_anim = 0.22
        for i in range(len(col1_texts)):
            anims_alternados.append(FadeIn(col1_texts[i], shift=LEFT, run_time=duracao_por_anim))
            anims_alternados.append(FadeIn(col2_texts[i], shift=LEFT, run_time=duracao_por_anim))

        
        self.play(Succession(*anims_alternados, rate_func=smooth))
        self.wait(1.0)

        indice_destaque = 0
        rect = SurroundingRectangle(VGroup(col1_texts[0], col2_texts[0]), buff=0.25)
        self.play(Create(rect), run_time=0.6)
        self.wait(0.8)
        for i in range(1, len(col1_texts)):
            target = SurroundingRectangle(VGroup(col1_texts[i], col2_texts[i]), buff=0.25)
            self.play(rect.animate.replace(target), run_time=1.0)
            self.wait(0.8)
        self.play(FadeOut(rect), run_time=0.4)
        self.wait(1)