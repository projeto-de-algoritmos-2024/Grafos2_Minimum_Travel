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
    if icon_button.cget('bg') == "blue":
        icon_button.config(bg="SystemButtonFace")  # Troca a cor para o padrão (cor normal)
    else:
        icon_button.config(bg="blue")  # Caso contrário, torna verde

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

# Executando a interface gráfica
root.mainloop()
