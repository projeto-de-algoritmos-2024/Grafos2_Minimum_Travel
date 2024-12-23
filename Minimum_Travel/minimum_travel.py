import tkinter as tk
from PIL import Image, ImageTk
import networkx as nx

import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk
import subprocess

arvore_gerada = False

def mostrar_erro(titulo, mensagem):
    janela_erro = tk.Toplevel(root)
    janela_erro.title(titulo)
    janela_erro.geometry("300x150")

    label_erro = tk.Label(janela_erro, text=mensagem, wraplength=250, justify="center")
    label_erro.pack(expand=True)

    botao_ok = tk.Button(janela_erro, text="OK", command=janela_erro.destroy)
    botao_ok.pack(pady=10)

    # Carregar e exibir a imagem de erro
    imagem_erro = Image.open("caminho_para_imagem_de_erro.png")
    imagem_erro = imagem_erro.resize((50, 50), Image.LANCZOS)
    imagem_erro_tk = ImageTk.PhotoImage(imagem_erro)
    label_imagem = tk.Label(janela_erro, image=imagem_erro_tk)
    label_imagem.image = imagem_erro_tk  # Manter uma referência
    label_imagem.pack(pady=10)

class TelaInicial:
    def __init__(self, master):
        self.master = master
        self.master.title("Minimum Travel - Início")
        self.master.geometry("800x600")

        # Variáveis para controlar as janelas abertas
        self.janela_info = None
        self.janela_controles = None

        # Carregar e redimensionar a imagem de fundo
        imagem_fundo = Image.open("./inicio.png")
        imagem_fundo = imagem_fundo.resize((800, 600), Image.LANCZOS)
        self.fundo = ImageTk.PhotoImage(imagem_fundo)

        # Criar canvas e adicionar imagem de fundo
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.fundo, anchor="nw")

        # Subtítulo
        subtitulo_font = tkfont.Font(family="Helvetica", size=18)
        self.canvas.create_text(400, 160, text="Encontre a rota mínima entre esquinas", font=subtitulo_font, fill="white")

        # Botão Começar
        botao_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        botao_comecar = tk.Button(
            self.master, 
            text="Começar", 
            font=botao_font, 
            command=self.iniciar_projeto, 
            bg="tan"
        )
        botao_comecar_window = self.canvas.create_window(400, 300, anchor="center", window=botao_comecar)

        # Botão Informações
        botao_info = tk.Button(
            self.master,
            text="Informações",
            font=botao_font,
            command=self.mostrar_informacoes,
            bg="tan"
        )
        botao_info_window = self.canvas.create_window(300, 400, anchor="center", window=botao_info)

        # Botão Controles
        botao_controles = tk.Button(
            self.master,
            text="Controles",
            font=botao_font,
            command=self.mostrar_controles,
            bg="tan"
        )
        botao_controles_window = self.canvas.create_window(500, 400, anchor="center", window=botao_controles)

    def iniciar_projeto(self):
        self.master.destroy()
        subprocess.run(["python", "main.py"])

    def mostrar_informacoes(self):
        if self.janela_info is None or not self.janela_info.winfo_exists():
            self.janela_info = tk.Toplevel(self.master)
            self.janela_info.title("Informações do projeto")
            self.janela_info.geometry("400x300")
            
            info_text = tk.Text(self.janela_info, wrap=tk.WORD, padx=10, pady=10)
            info_text.pack(expand=True, fill="both")
            
            info_text.insert(tk.END, "Minimum Travel é um projeto que utiliza conceitos de Grafos 2, focando na aplicação do algoritmo de Prim para encontrar a árvore geradora mínima em um grafo.\n\n")
            info_text.insert(tk.END, "O objetivo é selecionar até 5 esquinas no mapa e encontrar a rota mínima entre elas.\n\n")
            info_text.insert(tk.END, "O projeto implementa conceitos como representação de mapa como grafo, algoritmo de Prim, cálculo de caminhos mínimos e criação de subgrafos.")
            
            info_text.config(state=tk.DISABLED)
        else:
            self.janela_info.lift()

    def mostrar_controles(self):
        if self.janela_controles is None or not self.janela_controles.winfo_exists():
            self.janela_controles = tk.Toplevel(self.master)
            self.janela_controles.title("Controles do projeto")
            self.janela_controles.geometry("400x300")
            
            controles_text = tk.Text(self.janela_controles, wrap=tk.WORD, padx=10, pady=10)
            controles_text.pack(expand=True, fill="both")
            
            controles_text.insert(tk.END, "Controles do Minimum Travel:\n\n")
            controles_text.insert(tk.END, "- Clique do mouse: Selecionar esquinas (até 5)\n")
            controles_text.insert(tk.END, "- Teclas de seta: Mover a visualização do mapa\n")
            controles_text.insert(tk.END, "- Botão 'Calcular Árvore Geradora Mínima': Calcular e exibir a rota mínima\n")
            controles_text.insert(tk.END, "- Botão 'Resetar': Limpar seleções e rota calculada")
            
            controles_text.config(state=tk.DISABLED)
        else:
            self.janela_controles.lift()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaInicial(root)
    root.mainloop()
    

def mover_imagem(event):
    if event.keysym == 'Left':  # Move para a esquerda
        canvas.xview_scroll(-1, "units")
    elif event.keysym == 'Right':  # Move para a direita
        canvas.xview_scroll(1, "units")
    elif event.keysym == 'Up':  # Move para cima
        canvas.yview_scroll(-1, "units")
    elif event.keysym == 'Down':  # Move para baixo
        canvas.yview_scroll(1, "units")

# Criando a janela principal
root = tk.Tk()
root.title("Minimum Travel")

# Carregando a imagem do mapa
imagem_mapa = Image.open("./caminho_para_o_mapa.jpg")
largura_imagem, altura_imagem = imagem_mapa.size

# Definindo o tamanho da janela
largura_janela = 600  
altura_janela = 400  

# Convertendo a imagem para o formato que o Tkinter pode exibir
imagem_tk = ImageTk.PhotoImage(imagem_mapa)

# Criando o Canvas para desenhar a imagem
canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
canvas.pack()

# Adicionando a imagem ao canvas
canvas.create_image(0, 0, anchor="nw", image=imagem_tk)

# Configurando o canvas para permitir rolagem (scroll)
canvas.config(scrollregion=(0, 0, largura_imagem, altura_imagem))

# Bind das teclas de navegação
root.bind("<Left>", mover_imagem)
root.bind("<Right>", mover_imagem)
root.bind("<Up>", mover_imagem)
root.bind("<Down>", mover_imagem)

# Criando um Label para exibir mensagens
mensagem_label = tk.Label(root, text="", fg="red")
mensagem_label.pack()

# Função para trocar a cor do ícone
def mudar_cor(icon_button):
    if icon_button.cget('bg') == "green":
        icon_button.config(bg="SystemButtonFace")  # Troca a cor para o padrão (cor normal)
    else:
        icon_button.config(bg="green")  # Caso contrário, torna verde

# Função para registrar a escolha da aresta
esquinas_selecionadas = []
def selecionar_esquina(icon_button, nome):
    global arvore_gerada

    if arvore_gerada:
        mostrar_erro("Resetar", "Você deve resetar antes de selecionar novas esquinas.")
        return
    # Verifica se o botão está verde (selecionado)
    if icon_button.cget('bg') == "green":
        esquinas_selecionadas.remove(nome)  # Remove da lista de selecionadas
    else:
        if len(esquinas_selecionadas) < 5:
            esquinas_selecionadas.append(nome)  # Adiciona à lista de selecionadas
        else:
            mensagem_label.config(text="Você já selecionou 5 esquinas!")  # Exibe a mensagem de aviso
            return
    mudar_cor(icon_button)  # Muda a cor do botão
    mensagem_label.config(text=f"Esquinas selecionadas: {len(esquinas_selecionadas)}")  # Atualiza o contador


# Criando botões de ícones para cada esquina
esquinas = {
    "A": (262, 62),  
    "B": (314, 45),
    "C": (366, 26),
    "D": (418, 11),
    "E": (454, 1),
    "G": (373, 218),
    "H": (354, 163),
    "I": (423, 202),
    "J": (404, 146),
    "K": (390, 98),
    "L": (474, 183),
    "M": (453, 126),
    "N": (441, 80),
    "O": (516, 175),
    "P": (524, 158),
    "Q": (494, 111),
    "R": (477, 58),
    "S": (530, 218),
    "T": (283, 129),
    "U": (301, 181),
    "V": (317, 234),
    "W": (335, 286),
    "X": (270, 302),
    "Y": (251, 251),
    "Z": (203, 269),
    "F": (187, 220),
    "A1": (693, 47),
    "B1": (573, 141),
    "C1": (709, 95),
    "D1": (583, 202),
    "E1": (633, 183),
    "F1": (659, 173),
    "G1": (685, 166),
    "H1": (730, 149),
    "I1": (620, 311),
    "J1": (670, 295),
    "K1": (720, 279),
    "L1": (771, 260),
    "M1": (635, 358),
    "N1": (686, 338),
    "O1": (733, 317),
    "P1": (779, 296),
    "Q1": (769, 370),
    "R1": (680, 399),
    "S1": (671, 366),
    "T1": (354, 335),
    "U1": (587, 391),
    "V1": (566, 327),
    "W1": (546, 274),
    "X1": (598, 425),
    "Y1": (517, 449),
    "Z1": (501, 405),
    "A2": (581, 375),
    "B2": (666, 191),
    "C2": (581, 161),
    "D2": (718, 387),
    "E2": (620, 420),
    "F2": (729, 421),
    "G2": (634, 453),
    "H2": (534, 484),
    "I2": (526, 469),
    "J2": (741, 464),
    "K2": (650, 498),
    "L2": (759, 508),
    "M2": (404, 491),
    "N2": (347, 509),
    "O2": (293, 517),
    "P2": (390, 458),
    "Q2": (337, 475),
    "R2": (286, 493),
    "S2": (236, 508),
    "T2": (203, 520),
    "U2": (345, 350),
    "V2": (300, 365),
    "W2": (318, 416),
    "X2": (265, 433),
    "Y2": (250, 384),
    "Z2": (199, 401),
    "A3": (370, 390),
    "B3": (386, 442),
    "C3": (281, 303),
    "D3": (230, 321),
    "F3": (178, 338),
    "G3": (146, 348),
    "H3": (150, 359),
    "I3": (162, 405),
    "J3": (179, 454),
    "K3": (198, 505),
    "L3": (9, 454),
    "M3": (21, 505),
    "N3": (68, 494),
    "O3": (102, 425),
    "P3": (1, 411),
    "Q3": (129, 292),
    "R3": (111, 241),
    "S3": (95, 192),
    "T3": (235, 202),
    "U3": (217, 151),
    "V3": (58, 82),
    "W3": (38, 22),
    "X3": (92, 73),
    "Y3": (144, 56),
    "Z3": (194, 36),
    "A4": (74, 17),
    "B4": (115, 475),

    #NEW
    "C4": (271, 90),
    "D4": (251, 31),
    "E4": (204, 47),
    "F4": (222, 106),
    "G4": (352, 280),
    "H4": (345, 251),
    "I4": (331, 253),
    "J4": (364, 228),
    "K4": (385, 288),
    "L4": (427, 274),
    "M4": (407, 213),
    "N4": (415, 238),
    "O4": (433, 207),
    "P4": (451, 256),

    

}

# Criando um dicionário para armazenar os botões
botões = {}
for nome, (x, y) in esquinas.items():
    botões[nome] = tk.Button(root,command=lambda nome=nome: selecionar_esquina(botões[nome], nome), width=1, font=("Arial", 3))
    canvas.create_window(x, y, window=botões[nome])

# Função para desenhar a árvore geradora mínima no mapa
def desenhar_arestas(arvore_minima):
    for (n1, n2, data) in arvore_minima.edges(data=True):
        x1, y1 = esquinas[n1]  # Pega a posição de n1
        x2, y2 = esquinas[n2]  # Pega a posição de n2
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="linha")  # Desenha a linha entre n1 e n2

def calcular_rota():
    global arvore_gerada
    
    if arvore_gerada:
        mostrar_erro("Resetar", "Você deve resetar antes de selecionar novas esquinas.")
        return

    if len(esquinas_selecionadas) < 2:
        mensagem_label.config(text="Selecione pelo menos duas esquinas!")
        return
    grafo = nx.Graph()

    #A
    grafo.add_edge("A", "B", weight=5)
    grafo.add_edge("A", "T", weight=7)
    grafo.add_edge("A", "C4", weight=2)
    grafo.add_edge("A", "D4", weight=2)

    #B
    grafo.add_edge("B", "C", weight=5)
    grafo.add_edge("B", "H", weight=12)

    #C
    grafo.add_edge("C", "D", weight=5)
    grafo.add_edge("C", "K", weight=7)

    #D
    grafo.add_edge("D", "E", weight=5)
    grafo.add_edge("D", "N", weight=7)

    #E
    grafo.add_edge("E", "R", weight=5)

    #F
    grafo.add_edge("F", "U", weight=10)
    grafo.add_edge("F", "Z", weight=5)
    grafo.add_edge("F", "R3", weight=7)
    grafo.add_edge("F", "T3", weight=5)

    #G
    grafo.add_edge("G", "H", weight=5)
    grafo.add_edge("G", "I", weight=5)
    grafo.add_edge("G", "V", weight=5)
    grafo.add_edge("G", "J4", weight=1)
    grafo.add_edge("G", "M4", weight=3)

    #H

    #I
    grafo.add_edge("I", "J", weight=5)
    grafo.add_edge("I", "L", weight=5)
    grafo.add_edge("I", "M4", weight=1)
    grafo.add_edge("I", "O4", weight=1)

    #J
    grafo.add_edge("J", "K", weight=5)

    #K
    
    #L
    grafo.add_edge("L", "M", weight=5)
    grafo.add_edge("L", "O", weight=5)

    #M
    grafo.add_edge("M", "N", weight=5)

    #N

    #O
    grafo.add_edge("O", "P", weight=1)
    grafo.add_edge("O", "Q", weight=5)
    grafo.add_edge("O", "S", weight=5)

    #P
    grafo.add_edge("P", "B1", weight=5)

    #Q
    grafo.add_edge("Q", "R", weight=5)
    grafo.add_edge("Q", "A1", weight=20)

    #R

    #S
    grafo.add_edge("S", "D1", weight=5)
    grafo.add_edge("S", "W1", weight=5)
    
    #T
    grafo.add_edge("T", "U", weight=5)
    grafo.add_edge("T", "U3", weight=6)
    grafo.add_edge("T", "C4", weight=2)

    #U
    grafo.add_edge("U", "V", weight=5)
    grafo.add_edge("U", "T3", weight=6)

    #V
    grafo.add_edge("V", "Y", weight=5)
    grafo.add_edge("V", "W", weight=5)
    grafo.add_edge("V", "I4", weight=2)
    grafo.add_edge("V", "J4", weight=5)

    #W
    grafo.add_edge("W", "C3", weight=5)
    grafo.add_edge("W", "T1", weight=5)
    grafo.add_edge("W", "G4", weight=2)
    grafo.add_edge("W", "I4", weight=3)

    #X
    grafo.add_edge("X", "Y", weight=5)
    grafo.add_edge("X", "C3", weight=1)

    #Y
    grafo.add_edge("Y", "Z", weight=5)

    #Z
    grafo.add_edge("Z", "Q3", weight=7)

    #A1
    grafo.add_edge("A1", "C1", weight=5)

    #B1
    grafo.add_edge("B1", "C2", weight=1)
    grafo.add_edge("B1", "C1", weight=15)

    #C1
    grafo.add_edge("C1", "H1", weight=5)

    #D1
    grafo.add_edge("D1", "E1", weight=5)
    grafo.add_edge("D1", "I1", weight=10)

    #E1
    grafo.add_edge("E1", "J1", weight=10)
    grafo.add_edge("E1", "F1", weight=3)

    #F1
    grafo.add_edge("F1", "G1", weight=3)
    grafo.add_edge("F1", "B2", weight=5)
    
    #G1
    grafo.add_edge("G1", "H1", weight=5)
    grafo.add_edge("G1", "K1", weight=10)

    #H1
    grafo.add_edge("H1", "L1", weight=10)

    #I1
    grafo.add_edge("I1", "J1", weight=5)
    grafo.add_edge("I1", "M1", weight=5)

    #J1
    grafo.add_edge("J1", "N1", weight=5)

    #K1
    grafo.add_edge("K1", "L1", weight=5)
    grafo.add_edge("K1", "O1", weight=5)

    #L1
    grafo.add_edge("L1", "P1", weight=5)

    #M1
    
    #N1
    grafo.add_edge("N1", "S1", weight=3)

    #O1

    #P1
    grafo.add_edge("P1", "Q1", weight=7)

    #Q1
    grafo.add_edge("Q1", "R1", weight=7)
    grafo.add_edge("Q1", "D2", weight=4)

    #R1
    grafo.add_edge("R1", "X1", weight=7)
    grafo.add_edge("R1", "S1", weight=3)
    grafo.add_edge("R1", "D2", weight=3)
    grafo.add_edge("R1", "E2", weight=5)

    #S1
    
    #T1
    grafo.add_edge("T1", "W1", weight=20)
    grafo.add_edge("T1", "U2", weight=1)
    grafo.add_edge("T1", "A3", weight=5)

    #U1
    grafo.add_edge("U1", "X1", weight=3)
    grafo.add_edge("U1", "A2", weight=1)

    #V1
    grafo.add_edge("V1", "W1", weight=5)
    grafo.add_edge("V1", "A2", weight=5)
    grafo.add_edge("V1", "A3", weight=20)

    #W1

    #X1
    grafo.add_edge("X1", "Y1", weight=7)
    grafo.add_edge("X1", "E2", weight=1)
    grafo.add_edge("X1", "U1", weight=3)

    #Y1
    grafo.add_edge("Y1", "Y1", weight=5)
    grafo.add_edge("Y1", "I2", weight=1)
    grafo.add_edge("Y1", "Z1", weight=5)
    grafo.add_edge("Y1", "M2", weight=7)

    #Z1
    grafo.add_edge("Z1", "A2", weight=5)
    grafo.add_edge("Z1", "B3", weight=10)

    #A2
    
    #B2

    #C2

    #D2
    grafo.add_edge("D2", "F2", weight=3)

    #E2
    grafo.add_edge("E2", "G2", weight=3)

    #F2
    grafo.add_edge("F2", "G2", weight=10)
    grafo.add_edge("F2", "J2", weight=5)

    #G2
    grafo.add_edge("G2", "K2", weight=5)
    grafo.add_edge("G2", "H2", weight=10)

    #H2
    grafo.add_edge("H2", "I2", weight=1)

    #I2

    #J2
    grafo.add_edge("J2", "K2", weight=5)
    grafo.add_edge("J2", "L2", weight=5)

    #K2

    #L2

    #M2
    grafo.add_edge("M2", "P2", weight=3)
    grafo.add_edge("M2", "N2", weight=4)

    #N2
    grafo.add_edge("N2", "O2", weight=4)
    grafo.add_edge("N2", "Q2", weight=2)

    #O2
    grafo.add_edge("O2", "R2", weight=2)

    #P2
    grafo.add_edge("P2", "Q2", weight=4)
    grafo.add_edge("P2", "B3", weight=1)

    #Q2
    grafo.add_edge("Q2", "R2", weight=4)
    grafo.add_edge("Q2", "W2", weight=5)

    #R2
    grafo.add_edge("R2", "S2", weight=4)
    grafo.add_edge("R2", "X2", weight=5)

    #S2
    grafo.add_edge("S2", "T2", weight=2)
    grafo.add_edge("S2", "Z2", weight=10)

    #T2
    grafo.add_edge("T2", "K3", weight=1)

    #U2
    grafo.add_edge("U2", "V2", weight=4)

    #V2
    grafo.add_edge("V2", "W2", weight=5)
    grafo.add_edge("V2", "C3", weight=5)

    #W2
    grafo.add_edge("W2", "X2", weight=4)

    #X2
    grafo.add_edge("X2", "Y2", weight=5)

    #Y2
    grafo.add_edge("Y2", "Z2", weight=4)

    #Z2
    grafo.add_edge("Z2", "F3", weight=5)
    grafo.add_edge("Z2", "S2", weight=10)

    #A3
    grafo.add_edge("A3", "B3", weight=5)

    #B3

    #C3

    #D3

    #F3
    grafo.add_edge("F3", "D3", weight=5)
    grafo.add_edge("F3", "G3", weight=2)

    #G3
    grafo.add_edge("G3", "H3", weight=1)
    grafo.add_edge("G3", "Q3", weight=5)

    #H3
    grafo.add_edge("H3", "P3", weight=10)
    grafo.add_edge("H3", "I3", weight=5)

    #I3
    grafo.add_edge("I3", "O3", weight=6)
    grafo.add_edge("I3", "J3", weight=5)

    #J3
    grafo.add_edge("J3", "N3", weight=7)
    grafo.add_edge("J3", "K3", weight=5)

    #K3

    #L3
    grafo.add_edge("L3", "O3", weight=7)

    #M3
    grafo.add_edge("M3", "N3", weight=5)

    #N3
    grafo.add_edge("N3", "B4", weight=5)

    #O3
    grafo.add_edge("O3", "B4", weight=5)

    #P3

    #Q3
    grafo.add_edge("Q3", "R3", weight=5)

    #R3
    grafo.add_edge("R3", "F", weight=5)
    grafo.add_edge("R3", "S3", weight=5)

    #S3
    grafo.add_edge("S3", "U3", weight=7)
    grafo.add_edge("S3", "V3", weight=8)

    #T3
    grafo.add_edge("T3", "U3", weight=5)

    #U3

    #V3
    grafo.add_edge("V3", "X3", weight=3)
    grafo.add_edge("V3", "W3", weight=6)

    #W3

    #X3
    grafo.add_edge("X3", "A4", weight=6)
    grafo.add_edge("X3", "Y3", weight=6)

    #Y3
    grafo.add_edge("Y3", "Z3", weight=6)

    #Z3

    #C4
    grafo.add_edge("C4", "F4", weight=5)

    #D4
    grafo.add_edge("D4", "E4", weight=5)

    #E4
    grafo.add_edge("E4", "F4", weight=6)

    #F4

    #G4
    grafo.add_edge("G4", "H4", weight=3)

    #H4
    grafo.add_edge("H4", "I4", weight=1)

    #I4

    #J4
    grafo.add_edge("J4", "K4", weight=6)

    #K4
    grafo.add_edge("K4", "L4", weight=4)

    #L4

    #M4
    grafo.add_edge("M4", "N4", weight=3)

    #N4

    #O4
    grafo.add_edge("O4", "P4", weight=5)





    # Valida se há arestas selecionadas
    if len(esquinas_selecionadas) < 2:
        mensagem_label.config(text="Selecione pelo menos duas esquinas!")
        return

    # Cria um subgrafo contendo apenas os caminhos mínimos entre as arestas selecionadas
    subgrafo = nx.Graph()
    for i, origem in enumerate(esquinas_selecionadas):
        for destino in esquinas_selecionadas[i + 1:]:
            try:
                # Calcula o menor caminho entre origem e destino
                caminho = nx.shortest_path(grafo, source=origem, target=destino, weight="weight")
                # Adiciona ao subgrafo apenas as arestas do menor caminho
                for u, v in zip(caminho[:-1], caminho[1:]):
                    peso = grafo[u][v]["weight"]
                    subgrafo.add_edge(u, v, weight=peso)
            except nx.NetworkXNoPath:
                # Ignora se não houver caminho entre as esquinas
                mensagem_label.config(text=f"Sem caminho entre {origem} e {destino}")

    arvore_gerada = True

    # Implementação manual do algoritmo de Prim
    def prim_algoritmo_manual(grafo):
        # Conjuntos de nós visitados e não visitados
        visitados = set()
        nao_visitados = set(grafo.nodes)
        arestas_resultantes = []

        # Começa por um nó arbitrário
        no_atual = next(iter(grafo.nodes))
        visitados.add(no_atual)
        nao_visitados.remove(no_atual)

        # Enquanto houver nós não visitados
        while nao_visitados:
            menor_aresta = None
            menor_peso = float('inf')

            # Percorre as arestas conectando nós visitados a não visitados
            for u in visitados:
                for v, atributos in grafo[u].items():
                    if v in nao_visitados and atributos["weight"] < menor_peso:
                        menor_aresta = (u, v)
                        menor_peso = atributos["weight"]

            # Adiciona a menor aresta à solução
            if menor_aresta:
                u, v = menor_aresta
                arestas_resultantes.append((u, v, menor_peso))
                visitados.add(v)
                nao_visitados.remove(v)

        # Retorna o grafo gerado pelas arestas da árvore mínima
        arvore_minima = nx.Graph()
        for u, v, peso in arestas_resultantes:
            arvore_minima.add_edge(u, v, weight=peso)

        return arvore_minima

    # Aplica o algoritmo de Prim no subgrafo
    arvore_minima = prim_algoritmo_manual(subgrafo)

    # Identifica os nós úteis conectados pelas arestas da árvore mínima
    nos_uteis = set()
    for i, origem in enumerate(esquinas_selecionadas):
        for destino in esquinas_selecionadas[i + 1:]:
            try:
                caminho = nx.shortest_path(arvore_minima, source=origem, target=destino, weight="weight")
                nos_uteis.update(caminho)
            except nx.NetworkXNoPath:
                continue

    # Cria o subgrafo final apenas com arestas entre nós úteis
    subgrafo_final = nx.Graph()
    for u, v, data in arvore_minima.edges(data=True):
        if u in nos_uteis and v in nos_uteis:
            subgrafo_final.add_edge(u, v, weight=data["weight"])

    # Atualiza a interface com o grafo final
    mensagem_label.config(text="")
    desenhar_arestas(subgrafo_final)

# Botão para calcular a árvore geradora mínima
calcular_btn = tk.Button(root, text="Calcular Árvore Geradora Mínima", command=calcular_rota)
calcular_btn.pack()

# Função para resetar as seleções e rota
def resetar_selecoes():
    global arvore_gerada
    arvore_gerada = False
    # Limpa a lista de esquinas selecionadas
    esquinas_selecionadas.clear()
    
    # Reseta as cores dos botões
    for botao in botões.values():
        botao.config(bg="SystemButtonFace")  # Volta à cor padrão
    
    # Remove todas as linhas desenhadas no canvas
    canvas.delete("linha")  # Identificador para linhas desenhadas
    
    # Limpa mensagens
    mensagem_label.config(text="Seleções e rota resetadas.")

# Adiciona o botão de resetar na interface
botao_resetar = tk.Button(root, text="Resetar", command=resetar_selecoes)
botao_resetar.pack()

# Executando a interface gráfica
root.mainloop()
