import random
import numpy as np

class QuebraCabeca:
  def iniciar(self):
    self.estado_objetivo = np.array(["1", "2", "3", "4", "5", "6", "7", "8", "_"])
    estado_inicial = np.array(["_", "1", "2", "3", "4", "5", "6", "7", "8"])
    np.random.shuffle(estado_inicial)
    return estado_inicial

  # Função auxiliar para imprimir no formato:
  # | 3 | 7 | 2 |
  # | _ | 4 | 5 |
  # | 8 | 1 | 6 |
  def imprimir(self, estado):
    return "| " + estado[0] + " | " + estado[1] + " | " + estado[2] + " |\n| " + estado[3] + " | " + estado[4] + " | " + estado[5] + " |\n| " + estado[6] + " | " + estado[7] + " | " + estado[8] + " |"

  # Função booleana que verifica se o estado atual
  # é o estado objetivo do problema
  def testar_objetivo(self, estado):
    return np.array_equal(estado, self.estado_objetivo)

  # Função que gera os sucessores válidos 
  # a partir de um estado válido
  def gerar_sucessores(self, estado):
    sucessores = []

    # encontra a posição do _
    posicao = np.where(estado == "_")[0][0]

    expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
    random.shuffle(expansoes)
    for expansao in expansoes:
      sucessor = expansao(posicao, estado)
      if sucessor is not None: sucessores.append(sucessor)

    return sucessores

  def _esquerda(self, posicao, estado_atual):
    # movimento para esquerda
    if posicao not in [0, 3, 6]:
      # peça de baixo desce
      sucessor = np.copy(estado_atual)
      sucessor[posicao] = sucessor[posicao - 1]
      sucessor[posicao - 1] = "_"
      return (sucessor, "⬅️")
    
  def _cima(self, posicao, estado_atual):
    # movimento para cima
    ## Não gera se estiver no topo
    if posicao not in [0, 1, 2]:
      # peça de baixo sobe
      sucesso = np.copy(estado_atual)
      sucesso[posicao] = sucesso[posicao - 3]
      sucesso[posicao - 3] = "_"
      return (sucesso, "⬆️")

  def _baixo(self, posicao, estado_atual):
    # movimento para baixo
    ## Não gera se estiver no fundo
    if posicao not in [6, 7, 8]:
      # peça de baixo desce
      sucessor = np.copy(estado_atual)
      sucessor[posicao] = sucessor[posicao + 3]
      sucessor[posicao + 3] = "_"
      return (sucessor, "⬇️")

  def _direita(self, posicao, estado_atual):
    # movimento para direita
    ## Não gera se estiver na direita
    if posicao not in [2, 5, 8]:
      # peça de baixo desce
      sucessor = np.copy(estado_atual)
      sucessor[posicao] = sucessor[posicao + 1]
      sucessor[posicao + 1] = "_"
      return (sucessor, "➡️")