#Contexto: O arquivo teste_local.py distribui o cálculo de potências matemáticas através de listas de tarefas. Vamos usar essa mesma abordagem de computação paralela para processamento de strings.
#Tarefa: Crie um script Dask onde a função distribuída se chame contar_letras(palavra).
#Regra de Implementação:
#A função deve receber uma string, contar quantos caracteres ela possui (usando len()) e retornar uma tupla contendo: (palavra, tamanho, PID_do_processo).
#No escopo principal (__main__), instancie o cluster Dask local e passe a seguinte lista para computação paralela: ["paralela", "distribuida", "sistemas", "nuvem", "socket", "computacao"].
#Colete os resultados usando client.gather() e exiba a contagem detalhada de cada palavra na tela.


import os
import time
from dask.distributed import Client, LocalCluster

# Função que será distribuída (Nó de Processamento)
def calcular_potencia(base, expoente):
    # Identifica o processo para provar a distribuição
    pid = os.getpid()
    print(f"Processando {base}^{expoente} no PID: {pid}")

    time.sleep(1)  # Simula uma tarefa demorada
    return (base ** expoente, pid)

def contar_letras(palavra):
    return (palavra, len(palavra), os.getpid())

if __name__ == "__main__":
    # 1. Configuração do Cluster Local
    # n_workers: quantos processos (nós) queremos simular
    cluster = LocalCluster(n_workers=4, threads_per_worker=1)
    client = Client(cluster)

    print(f"\n--- Cluster Ativo ---")
    print(f"Console para  Monitoramento: {client.dashboard_link}")
    print(f"----------------------\n")

    # 2. Lista de tarefas (Trabalho a ser feito)
    palavras = ["paralela", "distribuida", "sistemas", "nuvem", "socket", "computacao"]

    print("Enviando tarefas para o cluster...")

    # 3. Mapeamento Distribuído
    # O Client envia as tarefas para os workers de forma equilibrada
    # futuros = client.map(calcular_potencia, numeros, [3]*8)# Calcula a potência de cada número elevado a 3
    futuros = client.map(contar_letras, palavras)  # Conta a quantidade de caracteres em cada palavra

    # 4. Recolha de resultados
    resultados = client.gather(futuros)

    print("\n=== RESULTADOS FINAIS ===")
    for palavra, caracteres, pid in resultados:
        print(f"A palavra \"{palavra}\" tem {caracteres} caracteres | Processado pelo PID: {pid}")

    # Pausa para os alunos verem o Dashboard antes de fechar
    input("\nPressione Enter para encerrar o cluster...")
    client.close()
    cluster.close()