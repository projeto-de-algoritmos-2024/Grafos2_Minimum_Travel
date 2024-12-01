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
root.title("Mapa Interativo")

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
    "A": (275, 62),  
    "B": (313, 52),
    "C": (337, 49),
    "D": (363, 37),
    "E": (385, 29),
    "F": (414, 21),
    "G": (447, 17),
    "H": (330, 212),
    "I": (359, 150),
    "J": (379, 201),
    "K": (387, 139),
    "L": (407, 192),
    "M": (397, 78),
    "N": (435, 182),
    "O": (425, 70),
    "P": (460, 173),
    "Q": (458, 102),
    "R": (482, 163),
    "S": (500, 155),
    "T": (256, 119),
    "U": (277, 166),
    "V": (296, 215),
    "W": (313, 270),
    "X": (486, 35),
    "Y": (499, 90),
    "Z": (520, 137),
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
    grafo.add_edge("A", "B", weight=3)
    grafo.add_edge("A", "T", weight=5)
    grafo.add_edge("A", "V", weight=15)
    grafo.add_edge("A", "W", weight=20)
    grafo.add_edge("A", "H", weight=20)
    grafo.add_edge("B", "C", weight=2)
    grafo.add_edge("B", "I", weight=10)
    grafo.add_edge("B", "J", weight=15)
    grafo.add_edge("C", "D", weight=3)
    grafo.add_edge("C", "I", weight=10)
    grafo.add_edge("C", "J", weight=15)
    grafo.add_edge("D", "E", weight=3)
    grafo.add_edge("D", "M", weight=5)
    grafo.add_edge("D", "N", weight=20)
    grafo.add_edge("E", "M", weight=5)
    grafo.add_edge("E", "N", weight=20)
    grafo.add_edge("E", "F", weight=3)
    grafo.add_edge("F", "O", weight=5)
    grafo.add_edge("F", "Q", weight=15)
    grafo.add_edge("F", "P", weight=20)
    grafo.add_edge("F", "R", weight=20)
    grafo.add_edge("G", "S", weight=20)
    grafo.add_edge("G", "X", weight=5)
    grafo.add_edge("G", "Y", weight=15)
    grafo.add_edge("G", "Z", weight=20)
    grafo.add_edge("H", "T", weight=15)
    grafo.add_edge("H", "U", weight=10)
    grafo.add_edge("H", "V", weight=3)
    grafo.add_edge("H", "W", weight=5)
    grafo.add_edge("H", "J", weight=4)
    grafo.add_edge("H", "L", weight=8)
    grafo.add_edge("H", "N", weight=12)
    grafo.add_edge("H", "P", weight=16)
    grafo.add_edge("H", "R", weight=20)
    grafo.add_edge("H", "S", weight=24)
    grafo.add_edge("I", "J", weight=5)
    grafo.add_edge("I", "B", weight=10)
    grafo.add_edge("K", "M", weight=5)
    grafo.add_edge("K", "L", weight=5)
    grafo.add_edge("K", "N", weight=5)
    grafo.add_edge("L", "J", weight=4)
    grafo.add_edge("L", "N", weight=4)
    grafo.add_edge("L", "P", weight=8)
    grafo.add_edge("L", "R", weight=12)
    grafo.add_edge("L", "S", weight=16)
    grafo.add_edge("M", "N", weight=15)
    grafo.add_edge("N", "P", weight=4)
    grafo.add_edge("N", "R", weight=8)
    grafo.add_edge("N", "S", weight=12)
    grafo.add_edge("O", "Q", weight=5)
    grafo.add_edge("O", "R", weight=15)
    grafo.add_edge("O", "P", weight=15)
    grafo.add_edge("P", "R", weight=4)
    grafo.add_edge("P", "S", weight=8)
    grafo.add_edge("R", "S", weight=4)
    grafo.add_edge("S", "Z", weight=1)
    grafo.add_edge("S", "Y", weight=6)
    grafo.add_edge("S", "X", weight=11)
    grafo.add_edge("T", "U", weight=5)
    grafo.add_edge("T", "V", weight=10)
    grafo.add_edge("T", "W", weight=15)
    grafo.add_edge("U", "V", weight=5)
    grafo.add_edge("U", "W", weight=10)
    grafo.add_edge("V", "W", weight=5)
    grafo.add_edge("V", "H", weight=2)
    grafo.add_edge("X", "Y", weight=5)
    grafo.add_edge("X", "Z", weight=10)
    grafo.add_edge("Y", "Z", weight=5)

    # Valida se há arestas selecionadas
    if len(esquinas_selecionadas) < 2:
        mensagem_label.config(text="Selecione pelo menos duas esquinas!")
        return

    # Cria um subgrafo contendo apenas os caminhos mínimos entre as arestas selecionadas
    subgrafo = nx.Graph()
    for i, origem in enumerate(esquinas_selecionadas):
        for destino in esquinas_selecionadas[i+1:]:
            # Calcula o menor caminho entre origem e destino
            caminho = nx.shortest_path(grafo, source=origem, target=destino, weight="weight")
            # Adiciona ao subgrafo apenas as arestas do caminho direto
            for u, v in zip(caminho[:-1], caminho[1:]):
                peso = grafo[u][v]["weight"]
                subgrafo.add_edge(u, v, weight=peso)

    # Calcula a árvore geradora mínima do subgrafo
    arvore_minima = nx.minimum_spanning_tree(subgrafo, weight="weight")

    # Remove qualquer mensagem antiga
    mensagem_label.config(text="")

    # Desenha as arestas da árvore geradora mínima no mapa
    desenhar_arestas(arvore_minima)

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
