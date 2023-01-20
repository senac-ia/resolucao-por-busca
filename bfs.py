from no import No
from aux import imprime_atual, imprime_atual, imprime_sucessores

# Breadth-First Search - Busca em Largura
def bfs(problema):
  estado_inicial = problema.iniciar()

  fila = Fila()
  fila.push(No(estado_inicial))

  visitados = Visitados(estado_inicial)
  iteracoes = 0

  while not fila.esta_vazio():
    no = fila.pop()
    estado = no.estado
    visitados.adicionar(estado)

    # faz o teste objetivo conforme a função `teste_objetivo`
    # para a execução se achou o objetivo
    if(testar_objetivo(problema, no)): return no
    
    # função sucessores define os Nós sucessores
    nos_sucessores = gerar_sucessores(problema, no)

    # para cada sucessor, se armazena se ainda não visitado
    for no_sucessor in nos_sucessores:
      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor.estado): fila.push(no_sucessor)

    iteracoes+=1
    if iteracoes%1000 == 0: print(f"Interação: {iteracoes}, estados visitados: {visitados.tamanho()}")
  return None

def testar_objetivo(problema, no):
  return problema.testar_objetivo(no.estado)

def gerar_sucessores(problema, no):
  sucessores = problema.gerar_sucessores(no.estado)
  nos_sucessores = [No(estado, no, aresta) for (estado, aresta) in sucessores]
  return nos_sucessores

class Visitados:
  def __init__(self, estado_inicial):
    # Conjuntos (Sets) em python e {1, 2, 3}
    # necessita ser uma tupla por ser comparável com ==
    self.visitados = set({tuple(estado_inicial)})
  
  def adicionar(self, estado):
    self.visitados.add(tuple(estado))
  
  def foi_visitado(self, estado):
    return tuple(estado) in self.visitados

  def tamanho(self):
    return len(self.visitados)

class Fila:
  def __init__(self):
    self.fila = []
  
  def push(self, item):
    self.fila.append(item)
  
  def pop(self):
    if(self.esta_vazio()):
        return None
    else:
        return self.fila.pop(0)

  def esta_vazio(self):
    return len(self.fila) == 0