import random
from dfs import dfs
from aux import vertice_caminho, no_caminho
from no import No

class QuebraCabeca:
  def __init__(self, estado):
    self.estado = estado

  def iniciar(self):
    # estamos usando tuplas porque podemos usar dentro de conjuntos
    # não é possível usar listas [] em Sets {}
    self.estado = ["_", "1", "2", "3", "4", "5", "6", "7", "8"]
    random.shuffle(self.estado)
    return tuple(self.estado)

  def imprime(self, estado):
    return "| " + estado[0] + " | " + estado[1] + " | " + estado[2] + " |\n| " + estado[3] + " | " + estado[4] + " | " + estado[5] + " |\n| " + estado[6] + " | " + estado[7] + " | " + estado[8] + " |"

  def testar_objetivo(self, estado):
    return estado == ("1", "2", "3", "4", "5", "6", "7", "8", "_")

  # movimento do quadrado vazio
  def gerar_sucessores(self, estado_atual):
    sucessores = []

    # encontra a posição do _
    posicao = estado_atual.index("_")

    # movimento para cima
    ## Não gera se estiver no topo
    if posicao not in [0, 1, 2]:
      # peça de baixo sobe
      sucessor_cima = list(estado_atual)
      sucessor_cima[posicao] = sucessor_cima[posicao - 3]
      sucessor_cima[posicao - 3] = "_"
      estado_vertice = (tuple(sucessor_cima), "⬆️")
      sucessores.append(estado_vertice)

    # movimento para baixo
    ## Não gera se estiver no fundo
    if posicao not in [6, 7, 8]:
      # peça de baixo desce
      sucessor_baixo = list(estado_atual)
      sucessor_baixo[posicao] = sucessor_baixo[posicao + 3]
      sucessor_baixo[posicao + 3] = "_"
      estado_vertice = (tuple(sucessor_baixo), "⬇️")
      sucessores.append(estado_vertice)

    # movimento para direita
    ## Não gera se estiver na direita
    if posicao not in [2, 5, 8]:
      # peça de baixo desce
      sucessor_direita = list(estado_atual)
      sucessor_direita[posicao] = sucessor_direita[posicao + 1]
      sucessor_direita[posicao + 1] = "_"
      estado_vertice = (tuple(sucessor_direita), "➡️")
      sucessores.append(estado_vertice)

    # movimento para esquerda
    if posicao not in [0, 3, 6]:
      # peça de baixo desce
      sucessor_esquerda = list(estado_atual)
      sucessor_esquerda[posicao] = sucessor_esquerda[posicao - 1]
      sucessor_esquerda[posicao - 1] = "_"
      estado_vertice = (tuple(sucessor_esquerda), "⬅️")
      sucessores.append(estado_vertice)
    return sucessores

q = QuebraCabeca(None)
no_solucao = dfs(q.iniciar(), q.testar_objetivo, q.gerar_sucessores, q.imprime)
#no_solucao = dfs(("1", "2", "3", "4", "5", "6", "7", "8", "_"), q.testar_objetivo, q.gerar_sucessores, q.imprime)

if(no_solucao is None):
  print("Não houve solução ao problema")
else:
  #caminho = no_caminho(no_solucao)
  caminho = vertice_caminho(no_solucao)
  print(caminho)