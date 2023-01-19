from no import No
from aux import imprime_atual, imprime_atual, imprime_sucessores

# Breadth-First Search - Busca em Largura
# no_raiz => Instância de No
# testar_objetivo => função que verifica se o estado atual é aceito
# gerar_sucessores => Gera os nós sucessores de acordo com a regra do problema
# imprimir => função de formatação para imprimir o estado
# stepEstado => imprime o estado atual
# stepSucessores => imprime os sucessores de cada passo
def bfs(estado_inicial, testar_objetivo, gerar_sucessores, imprimir=str, stepEstado=False, stepSucessores=False):
  fila = Fila()
  fila.push(No(estado_inicial))
  visitados = {tuple(estado_inicial)} # Conjuntos (Sets) em python e {1, 2, 3}
  i = 0

  while not fila.esta_vazio():
    no_atual = fila.pop()
    estado_atual = no_atual.estado
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
      if tuple(estado_filho) in visitados: # pula estado_filho se já foi expandido
        continue
      visitados.add(tuple(estado_filho))
      fila.push(No(estado_filho, no_atual, vertice))
    
    i+=1
    if i%1000 == 0: print(f"Interação:{i} , estados visitados: {len(visitados)}")
  return None

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