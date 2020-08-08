from pilha import Pilha
from no import No

# Depth-First Search - Busca em Profundidade
# no_raiz => Instância de No
# testar_objetivo => função que verifica se o estado atual é aceito
# gerar_sucessores => Gera os nós sucessores de acordo com a regra do problema
def dfs(no_raiz, testar_objetivo, gerar_sucessores):
  pilha = Pilha()
  pilha.push(No(no_raiz, None))
  visitados = {no_raiz} # Conjuntos (Sets) em python e {1, 2, 3}

  while not pilha.esta_vazio():
    no_atual = pilha.pop()
    estado_atual = no_atual.estado
    # faz o teste objetivo conforme a função `teste_objetivo`
    if(testar_objetivo(estado_atual)):
      return no_atual
    
    # verifico os nos filhos e os adiciono na pilha
    # função sucessores define os nós seguintes de 
    for no_filho in gerar_sucessores(estado_atual):
      if no_filho in visitados:
        continue
      visitados.add(no_filho)
      pilha.push(No(no_filho, no_atual))

    return None