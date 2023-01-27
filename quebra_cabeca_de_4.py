import random
import numpy as np
from no import No

class QuebraCabecaDe4:
  def __init__(self):
    self.estado_objetivo = np.array(["1", "2", "3", "_"])
    self.estado_inicial = np.array(["_", "1", "2", "3"])
    np.random.shuffle(self.estado_inicial)
    
  def define_estado_inicial(self, estado):
    self.estado_inicial = estado

  def iniciar(self):
    self.no_raiz = No(self.estado_inicial)
    return self.no_raiz

  # Função auxiliar para imprimir no formato:
  # | 3 | 7 | 2 |
  # | _ | 4 | 5 |
  # | 8 | 1 | 6 |
  def imprimir(self, no):
    estado = no.estado
    return "| " + estado[0] + " | " + estado[1] + " |\n| " + estado[2] + " | " + estado[3] + " | "

  # Função booleana que verifica se o estado atual
  # é o estado objetivo do problema
  def testar_objetivo(self, no):
    return np.array_equal(no.estado, self.estado_objetivo)

  # Função que gera os sucessores válidos 
  # a partir de um estado válido
  def gerar_sucessores(self, no):
    estado = no.estado
    nos_sucessores = []

    # encontra a posição do _
    posicao = np.where(estado == "_")[0][0]
    print(posicao)

    expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
    random.shuffle(expansoes)
    for expansao in expansoes:
      no_sucessor = expansao(posicao, no)
      if no_sucessor is not None: nos_sucessores.append(no_sucessor)

    return nos_sucessores

  def _esquerda(self, posicao, no):
    # movimento para esquerda
    if posicao not in [0, 2]:
      # peça de baixo desce
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao - 1]
      sucessor[posicao - 1] = "_"
      return No(sucessor, no, "⬅️")
    else:
      None
    
  def _cima(self, posicao, no):
    # movimento para cima
    ## Não gera se estiver no topo
    if posicao not in [0, 1]:
      # peça de baixo sobe
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao - 2]
      sucessor[posicao - 2] = "_"
      return No(sucessor, no, "⬆️")
    else:
      None

  def _baixo(self, posicao, no):
    # movimento para baixo
    ## Não gera se estiver no fundo
    if posicao not in [2, 3]:
      # peça de baixo desce
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao + 2]
      sucessor[posicao + 2] = "_"
      return No(sucessor, no, "⬇️")
    else:
      None

  def _direita(self, posicao, no):
    # movimento para direita
    ## Não gera se estiver na direita
    if posicao not in [1, 3]:
      # peça de baixo desce
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao + 1]
      sucessor[posicao + 1] = "_"
      return No(sucessor, no, "➡️")
    else:
      None