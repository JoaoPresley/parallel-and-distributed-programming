#4: MPI — Filtro de Limiar (Threshold) em Vetores
#Contexto: O Scatter divide um array original e o distribui em pedaços iguais. O mestre então espera os dados calculados de volta usando Gather.
#Tarefa: Escreva um script MPI em que o Rank 0 cria um vetor ordenado com 20 elementos (números inteiros de 1 a 20) e o distribui igualmente para 4 processos de trabalho (cada processo receberá 5 elementos).
#Regra de Implementação: Cada processo deve percorrer seu buffer local e aplicar um filtro de limiar: qualquer número dentro do seu buffer local que for maior que 10 deve ser substituído por -1. Após a alteração, use a função comm.Gather() para recolher o vetor modificado de volta no Rank 0 e imprima o vetor completo modificado.

from mpi4py import MPI
import numpy as np

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Garante que seja executado apenas 4 processos
    #  mpiexe -n 4 python Filtro_limiar.py
    if size != 4:
        print('[ERRO] Execute apenas 4 processos simultaneos')
        return

    # 1. Prepara o array de 1 a 20
    if rank == 0:
        lista = np.arange(1, 21)
    else:
        lista = None

    # 2. Distribui o array em 5 processos
    buffer = np.empty(5, dtype=int) #lista local de cada processo
    comm.Scatter(lista, buffer, root=0) #distribuição

    # 3. Lógica de cada processo
    #  Se o valor da lista for maior que 10 deve ser substituido por -1
    buffer[buffer > 10] = -1

    print(f"[Processo {rank}], meu buffer modificado: {buffer}")

    # 4. Reune a lista nova
    resultado = comm.gather(buffer, root=0)
    resultado = np.array(resultado).flatten() #Trata para uma lista unidimensional

    # 5. O mestre mostra o resultado
    if rank == 0:
        resultado = np.array(resultado).flatten()
        print("Lista pos processos: ", resultado)

if __name__ == "__main__":
    main()