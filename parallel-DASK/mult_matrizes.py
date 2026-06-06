# Tarefa:
#   Implemente um script que multiplique uma constante por uma matriz.
#   Realize dois testes de carga:
#       Teste A: Matriz 1000x1000 multiplicada pela constante 2.
#       Teste B: Matriz 5000x5000 multiplicada pela constante 2.5.
#   Execute cada teste variando o número de trabalhadores (Workers) no LocalCluster: 2, 4 e 8 nós (ou o limite da sua máquina).
#   Análise Requerida:
#       Utilize o Dashboard do Dask (Aba Task Stream).
#       Compare o tempo de conclusão: O aumento de nós reduziu o tempo proporcionalmente?
#       Observe o gráfico de memória: Houve picos excessivos no Teste B?

# =========== importações ===================
from dask.distributed import Client, LocalCluster
import numpy as np

# Função distribuida para calcular matriz de 1000x1000 * 2
def mult_1000x1000(matriz, client):
    #distribui a multiplicação da matriz
    ft = client.map(lambda x: x*2, matriz)
    return client.gather(ft)

# Função distribuida para calcular matriz de 5000x5000 * 2,5
def mult_5000x5000(matriz, client):

    #ditrivui a multiplicação da matriz
    ft = client.map(lambda x: x*2.5, matriz)
    return client.gather(ft)

# ============= MAIN ===========================
if __name__ == "__main__":
    #ALTERE O n_workers para 2, 4, 8 e minha potente maquina 12 rsrsr
    cluster = LocalCluster(n_workers=4, threads_per_worker=1)
    client = Client(cluster)

    print(f"\nConsole para monitoramento {client.dashboard_link}\n")

    # cria muma matriz 1000x1000 ordenada
    matriz1000x1000 = np.arange(0, 1000000).reshape(1000, 1000)
    matriz5000x5000 = np.arange(0, 25000000).reshape(5000, 5000)

    #multiplica a matriz 1000x1000 por 2 e mostra os 10 primeiros valores da primeira linha
    print("\nMatriz 1000x1000, primeiros 10 valores: ", mult_1000x1000(matriz1000x1000, client)[0][:10])

    input("\nAperte enter para passar para a próxima task\n")

    #multiplica a matriz 5000x5000 por 2,5 e mostra os 10 primeiros valores da primeira linha
    print("\nMatriz 5000x5000, primeiros 10 valores: ", mult_5000x5000(matriz5000x5000, client)[0][:10])

    #pausa para ver o dashboard
    input("Aperte enter para fechar\n")
    client.close()
    cluster.close()


