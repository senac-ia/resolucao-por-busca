from dfs import dfs
from bfs import bfs
from a_estrela import a_estrela
from aux import vertice_caminho, no_caminho
from quebra_cabeca import QuebraCabeca


if __name__ == "__main__":
    q = QuebraCabeca()
    estado_inicial = q.iniciar()

    no_solucao = dfs(estado_inicial, q.testar_objetivo, q.gerar_sucessores)
    # no_solucao = a_estrela(estado_inicial, 
    #                         q.testar_objetivo, 
    #                         q.gerar_sucessores, 
    #                         q.heuristica2,
    #                         q.custo,
    #                         q.imprimir)

    if(no_solucao is None):
        print("Não houve solução ao problema")
    else:
        print("Solução:")
        #caminho = no_caminho(no_solucao)
        caminho = vertice_caminho(no_solucao)
        print(caminho)

        print("Estado Inicial:")
        print(q.imprimir(estado_inicial))