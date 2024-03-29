import random
import numpy as np
from no import No

class QuebraCabecaDe4:
  def __init__(self):
    self.estado_objetivo = np.array(["1", "2", "3", "_"])
    self.estado_inicial = np.array(["_", "1", "2", "3"])
    np.random.shuffle(self.estado_inicial)
    
  def tem_solucao(self, estado):
      # Contar o número de inversões
      inversoes = 0
      for i in range(len(estado)):
          for j in range(i+1, len(estado)):
              if estado[i] != 0 and estado[j] != 0 and estado[i] > estado[j]:
                  inversoes += 1

      # Verifica se tem solução se o número de inversões for par
      blank_row = 0
      for row_index, row in enumerate(estado):
          if "_" in row:
              blank_row = row_index
              break
      if blank_row % 2 == 0:
          return inversoes % 2 == 0
      else:
          return inversoes % 2 == 1

  def iniciar(self):
    np.random.shuffle(self.estado_inicial)

    while(not self.tem_solucao(self.estado_inicial)):
      np.random.shuffle(self.estado_inicial)

    self.no_raiz = No(self.estado_inicial)
    return self.no_raiz

  def define_estado_inicial(self, estado):
    self.estado_inicial = estado

  def iniciar(self):
    self.no_raiz = No(self.estado_inicial)
    return self.no_raiz

  # Função auxiliar para imprimir no formato:
  # | 3 | 1 |
  # | _ | 4 |
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

    expansoes = []
    if no.aresta == "⬅️":
      expansoes = [self._esquerda, self._cima, self._baixo]
    elif no.aresta == "⬆️":
      expansoes = [self._direita, self._esquerda, self._cima]
    elif no.aresta == "⬇️":
      expansoes = [self._direita, self._esquerda, self._baixo]
    elif no.aresta == "➡️":
      expansoes = [self._direita, self._cima, self._baixo]
    else:
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