from no import No
from aux import imprime_atual, imprime_atual, imprime_sucessores
import heapq

from no import No
from aux import imprime_atual, imprime_atual, imprime_sucessores
import heapq

def a_estrela(estado_inicial, testar_objetivo, gerar_sucessores, heuristica, custo, imprimir=str, stepEstado=False, stepSucessores=False):
  fila = FilaPrioridade()
  fila.push(No(estado_inicial, None, None, 0.0, heuristica(estado_inicial)))
  visitados = {} # Dicionario do Python
  i = 0

  while not fila.esta_vazio():
    no_atual = fila.pop()
    estado_atual = no_atual.estado
    visitados[tuple(estado_atual)] = no_atual.custo

    if stepEstado: imprime_atual(estado_atual, imprimir)

    # faz o teste objetivo conforme a função `teste_objetivo`
    # para a execução se achou o objetivo
    if(testar_objetivo(estado_atual)):
      return no_atual
    
    # verifico os nos filhos e os adiciono na fila
    # função sucessores define os estados seguintes e adiciona os nós seguintes
    estados_vertices_sucessores = gerar_sucessores(estado_atual)
    if stepSucessores: imprime_sucessores(estados_vertices_sucessores, imprimir)

    for estados_vertices_sucessor in estados_vertices_sucessores:
      estado_filho = estados_vertices_sucessor[0]
      vertice = estados_vertices_sucessor[1]
      novo_custo = no_atual.custo + custo(estado_atual, estado_filho)

      # pula estado_filho se já foi expandido
      if tuple(estado_filho) not in visitados or visitados[tuple(estado_filho)] > novo_custo: 
        fila.push(No(estado_filho, no_atual, vertice, novo_custo, heuristica(estado_filho)))

    i+=1
    if i%1000 == 0: print(f"Interação: {i}, estados visitados: {len(visitados)}")
  return None

class Visitados:
  def __init__(self, estado_inicial, custo):
    # Dicionário do Python
    self.visitados = {tuple(estado_inicial): custo}
  
  def adicionar(self, estado, custo):
    self.visitados[tuple(estado)] = custo
  
  def foi_visitado(self, estado, novo_custo):
    return tuple(estado) in self.visitados and self.visitados[tuple(estado)] <= novo_custo

  def tamanho(self):
    return len(self.visitados)

class FilaPrioridade:
  def __init__(self):
    self.fila = []
  
  def push(self, item):
    heapq.heappush(self.fila, item)
  
  def pop(self):
    if(self.esta_vazio()):
        return None
    else:
        return heapq.heappop(self.fila)

  def esta_vazio(self):
    return len(self.fila) == 0