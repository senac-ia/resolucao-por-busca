from aux import Visitados
import heapq

def a_estrela(problema):
  no = problema.iniciar()

  fila = FilaPrioridade()
  fila.push(no)

  visitados = Visitados()
  visitados.adicionar(no)

  while not fila.esta_vazio():
    no = fila.pop()
    visitados.adicionar(no)

   # faz o teste objetivo. Se chegou no resultado final
    # retorna o No correspondente
    resultado = problema.testar_objetivo(no)
    if(resultado):
      print(f"Estados visitados: {visitados.tamanho()}")
      return no
    
    # função sucessores define os Nós sucessores
    nos_sucessores = problema.gerar_sucessores(no)

    # para cada sucessor, se armazena se ainda não visitado
    for no_sucessor in nos_sucessores:
      novo_custo = no.custo + problema.custo(no, no_sucessor)

      # pula estado_filho se já foi expandido
      if not visitados.foi_visitado(no_sucessor) or no_sucessor.custo > novo_custo:
        no_sucessor.custo = novo_custo
        no_sucessor.heuristica = problema.heuristica(no_sucessor.estado)
        
        fila.push(no_sucessor)

  print(f"Estados visitados: {visitados.tamanho()}")
  return None

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