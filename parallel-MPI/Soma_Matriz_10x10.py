from mpi4py import MPI
import numpy as np

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    # Configuração: Matriz 10x10 (100 elementos) para 4 processos
    if size != 4:
        if rank == 0:
            print("Erro: Execute com exatamente 4 processos.")
        return

    # Passo 1: Preparação no Mestre (Rank 0)
    if rank == 0:
        matriz = np.arange(1, 101, dtype='i').reshape(10, 10)#dados de 1 a 101 e coloca no formato de matriz 10x10
        dados_planos = matriz.flatten()#coloca os dados em linha unica
    else:
        dados_planos = None

    # Passo 2: Alocação do buffer local (cada um recebe 25 elementos)
    buffer_local = np.empty(25, dtype='i')

    # Passo 3: Distribuição (Scatter)
#Nesta etapa o MPI distribui automaticamente os dados entre os processos locais 25 elementos para cada(4x25). root=0 indica que o no mestre esta com as informações.
#Todos executam esta linha o no 1 envia os dados para os nos 2,3 e 4.
    comm.Scatter(dados_planos, buffer_local, root=0)

    # Passo 4: Cálculo Local
    soma_local = np.sum(buffer_local)
    print(f"[Processo {rank}] Soma parcial calculada.")

    # Passo 5: Redução Global (Reduce)
    soma_total = comm.reduce(soma_local, op=MPI.SUM, root=0)

    # Passo 6: Exibição no Mestre
    if rank == 0:
        print(f"\n>>> Resultado Final da Soma: {soma_total}")

if __name__ == "__main__":
    main()
