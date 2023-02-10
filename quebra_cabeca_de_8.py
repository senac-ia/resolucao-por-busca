import random
import numpy as np
from no import No

class QuebraCabecaDe8:
  def __init__(self):
    self.estado_objetivo = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "_"])
    self.estado_inicial = np.array(["_", "1", "2", "3", "4", "5", "6", "7", "8"])

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
    self.estado_inicial = np.array(["_", "1", "2", "3", "4", "5", "6", "7", "8"])
    np.random.shuffle(self.estado_inicial)

    while(not self.tem_solucao(self.estado_inicial)):
      np.random.shuffle(self.estado_inicial)

    self.no_raiz = No(self.estado_inicial)
    return self.no_raiz

  # Função auxiliar para imprimir no formato:
  # | 3 | 7 | 2 |
  # | _ | 4 | 5 |
  # | 8 | 1 | 6 |
  def imprimir(self, no):
    estado = no.estado
    return "| " + estado[0] + " | " + estado[1] + " | " + estado[2] + " |\n| " + estado[3] + " | " + estado[4] + " | " + estado[5] + " |\n| " + estado[6] + " | " + estado[7] + " | " + estado[8] + " |"

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

    expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
    random.shuffle(expansoes)
    for expansao in expansoes:
      no_sucessor = expansao(posicao, no)
      if no_sucessor is not None: nos_sucessores.append(no_sucessor)

    return nos_sucessores

  def _esquerda(self, posicao, no):
    # movimento para esquerda
    if posicao not in [0, 3, 6]:
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
    if posicao not in [0, 1, 2]:
      # peça de baixo sobe
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao - 3]
      sucessor[posicao - 3] = "_"
      return No(sucessor, no, "⬆️")
    else:
      None

  def _baixo(self, posicao, no):
    # movimento para baixo
    ## Não gera se estiver no fundo
    if posicao not in [6, 7, 8]:
      # peça de baixo desce
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao + 3]
      sucessor[posicao + 3] = "_"
      return No(sucessor, no, "⬇️")
    else:
      None

  def _direita(self, posicao, no):
    # movimento para direita
    ## Não gera se estiver na direita
    if posicao not in [2, 5, 8]:
      # peça de baixo desce
      sucessor = np.copy(no.estado)
      sucessor[posicao] = sucessor[posicao + 1]
      sucessor[posicao + 1] = "_"
      return No(sucessor, no, "➡️")
    else:
      None

  # Heurística 1: Checar se os valores 
  # esta heurística não é admissível, pois, pode dificultar 
  # a chegada de um resultado final
  def heuristica(self, estado):
    resultado = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]
    return sum(1 for i in range(len(resultado)) if resultado[i] == estado[i])

  # Heurística 2: Distância para o resultado espero
  # Heurística adminissível, pois, sempre o resultado chega mais perto
  # Transformei o array em matriz para fazer cálculo de distância
  def heuristica2(self, estado):
    resultado = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "_"]]
    estado_matriz = [estado[0:3], estado[3:6], estado[6:9]]

    soma = 0

    for i in range(len(resultado)):
      for j in range(len(resultado[i])):
        valor = resultado[i][j]
        soma = soma + self._distancia_manhattan(valor, estado_matriz, i, j)

    return soma

  # Distância de Manhattan: d = |xi-xj| + |yi-yj|
  def _distancia_manhattan(self, valor, estado, i, j):
    for k in range(len(estado)):
      for h in range(len(estado[k])):
        if valor == estado[k][h]: return abs(i-k)+abs(j-h)
    
  # Função de custo: Quando custa mover de um 
  # estado_origem para estado_destino. No Quebra Cabeça 
  # de 8, este custo é fixo e arbitrariamente será 1.
  def custo(self, estado_origem, estado_destino):
    return 1