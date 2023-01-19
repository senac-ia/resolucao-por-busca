from dfs import dfs
from bfs import bfs
from aux import vertice_caminho, no_caminho
from quebra_cabeca import QuebraCabeca

buscar = dfs

if __name__ == "__main__":
    q = QuebraCabeca()
    estado_inicial = q.iniciar()

    no_solucao = buscar(estado_inicial, q.testar_objetivo, q.gerar_sucessores, q.imprimir)

    if(no_solucao is None):
        print("Não houve solução ao problema")
    else:
        print("Solução:")
        #caminho = no_caminho(no_solucao)
        caminho = vertice_caminho(no_solucao)
        print(caminho)

        print("Estado Inicial:")
        print(q.imprimir(estado_inicial))