import tkinter as tk
from PIL import Image, ImageTk
import networkx as nx

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
imagem_mapa = Image.open("caminho_para_o_mapa.jpg")
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
}

# Criando um dicionário para armazenar os botões
botões = {}
for nome, (x, y) in esquinas.items():
    botões[nome] = tk.Button(root, text=nome, command=lambda nome=nome: selecionar_esquina(botões[nome], nome))
    canvas.create_window(x, y, window=botões[nome])

# Função para desenhar a árvore geradora mínima no mapa
def desenhar_arestas(arvore_minima):
    for (n1, n2, data) in arvore_minima.edges(data=True):
        x1, y1 = esquinas[n1]  # Pega a posição de n1
        x2, y2 = esquinas[n2]  # Pega a posição de n2
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="linha")  # Desenha a linha entre n1 e n2

def calcular_rota():
    grafo = nx.Graph()

    #A
    grafo.add_edge("A", "B", weight=5)
    grafo.add_edge("A", "T", weight=7)

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

    #G
    grafo.add_edge("G", "H", weight=5)
    grafo.add_edge("G", "I", weight=5)
    grafo.add_edge("G", "V", weight=5)

    #H

    #I
    grafo.add_edge("I", "J", weight=5)
    grafo.add_edge("I", "L", weight=5)

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

    #Q
    grafo.add_edge("Q", "R", weight=5)

    #R

    #S
    
    #T
    grafo.add_edge("T", "U", weight=5)

    #U
    grafo.add_edge("U", "V", weight=5)

    #V
    grafo.add_edge("V", "Y", weight=5)
    grafo.add_edge("V", "W", weight=5)

    #W
    grafo.add_edge("W", "X", weight=5)

    #X
    grafo.add_edge("X", "Y", weight=5)

    #Y
    grafo.add_edge("Y", "Z", weight=5)

    #Z

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

    # Calcula a árvore geradora mínima do subgrafo
    arvore_minima = nx.minimum_spanning_tree(subgrafo, weight="weight")

    # Cria um subgrafo final apenas com os caminhos necessários
    subgrafo_final = nx.Graph()
    
    # Identificar os nós úteis: todos que estão em trajetos entre esquinas selecionadas
    nos_uteis = set()
    for i, origem in enumerate(esquinas_selecionadas):
        for destino in esquinas_selecionadas[i + 1:]:
            try:
                caminho = nx.shortest_path(arvore_minima, source=origem, target=destino, weight="weight")
                nos_uteis.update(caminho)
            except nx.NetworkXNoPath:
                continue

    # Adiciona apenas arestas entre nós úteis ao subgrafo final
    for u, v, data in arvore_minima.edges(data=True):
        if u in nos_uteis and v in nos_uteis:
            subgrafo_final.add_edge(u, v, weight=data["weight"])

    mensagem_label.config(text="")
    desenhar_arestas(subgrafo_final)

# Botão para calcular a árvore geradora mínima
calcular_btn = tk.Button(root, text="Calcular Árvore Geradora Mínima", command=calcular_rota)
calcular_btn.pack()

# Função para resetar as seleções e rota
def resetar_selecoes():
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
