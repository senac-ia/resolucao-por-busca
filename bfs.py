from no import No
from aux import Visitados

# Breadth-First Search - Busca em Largura
def bfs(problema):
  no = problema.iniciar()

  fila = Fila()
  fila.push(no)

  visitados = Visitados()

  while not fila.esta_vazio():
    no = fila.pop()
    estado = no.estado
    visitados.adicionar(no)

    # faz o teste objetivo. Se chegou no resultado final
    # retorna o No correspondente
    if(testar_objetivo(problema, no)):
      print(f"Estados visitados: {visitados.tamanho()}")
      return no
    
    # função sucessores define os Nós sucessores
    nos_sucessores = gerar_sucessores(problema, no)

    # para cada sucessor, se armazena se ainda não visitado
    for no_sucessor in nos_sucessores:
      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor): fila.push(no_sucessor)

  print(f"Estados visitados: {visitados.tamanho()}")
  return None

def testar_objetivo(problema, no):
  return problema.testar_objetivo(no.estado)

def gerar_sucessores(problema, no):
  sucessores = problema.gerar_sucessores(no.estado)
  nos_sucessores = [No(estado, no, aresta) for (estado, aresta) in sucessores]
  return nos_sucessores

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