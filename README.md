# Minimum Travel

**Número da Lista**: 37  
**Conteúdo da Disciplina**: Grafos 2  

## Alunos

| Matrícula   | Aluno                          |
| ----------- | ------------------------------ |
| 221037975   | Natália Rodrigues de Morais    |
| 221021975   | Gabriel Santos Monteiro        |

## Sobre

O Minimum Travel é um projeto que utiliza conceitos de Grafos 2, focando na aplicação do algoritmo de Prim para encontrar a árvore geradora mínima (Minimum Spanning Tree - MST) em um grafo. O projeto implementa uma interface gráfica interativa que permite aos usuários selecionar esquinas em um mapa e calcular a rota mínima entre elas.

### Uso de Grafos

O projeto implementa os seguintes conceitos de teoria dos grafos:

1. **Representação de Mapa**: O mapa do jogo é modelado como um grafo, onde as esquinas são representadas por nós e as ruas por arestas.

2. **Algoritmo de Prim**: Uma implementação manual do algoritmo de Prim é utilizada para encontrar a árvore geradora mínima do grafo.

3. **Caminhos Mínimos**: O projeto calcula os caminhos mínimos entre esquinas selecionadas usando o algoritmo de caminho mais curto.

4. **Subgrafos**: São criados subgrafos contendo apenas os caminhos relevantes entre as esquinas selecionadas pelo usuário.

## Screenshots

| Tela de Introdução                         | Tela de Jogo                               |
| ------------------------------------------ | ------------------------------------------ |
| Intro                    | Game                      |

| Tela de Início do Jogo                     | Tela de Fim de Jogo                        |
| ------------------------------------------ | ------------------------------------------ |
| Start                    | End                        |

## Instalação 

**Linguagem**: Python  
**Framework**: Tkinter, PIL, NetworkX

### Pré-requisitos

1. Python 3.x instalado.
2. Instale as bibliotecas necessárias usando:
   ```bash
   pip install tkinter pillow networkx
   ```

### Rodando o projeto

Para executar o projeto, navegue até o diretório do projeto e execute o arquivo principal:

```bash
python main.py
```

## Uso

1. Ao iniciar o programa, você verá um mapa interativo.
2. Clique em até 5 esquinas no mapa para selecioná-las.
3. Após selecionar as esquinas, o programa calculará e exibirá a rota mínima entre elas.
4. Use o botão de reset para limpar as seleções e começar novamente.

### Controles

- Clique do mouse: Selecionar esquinas
- Botão de reset: Limpar seleções e rota

## Apresentação

- [Vídeo de apresentação Grafos 2]()