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


if __name__ == "__main__":
    # 1. Configuração do Cluster Local
    # n_workers: quantos processos (nós) queremos simular
    cluster = LocalCluster(n_workers=4, threads_per_worker=1)
    client = Client(cluster)

    print(f"\n--- Cluster Ativo ---")
    print(f"Console para  Monitoramento: {client.dashboard_link}")
    print(f"----------------------\n")

    # 2. Lista de tarefas (Trabalho a ser feito)
    numeros = [2, 3, 4, 5, 6, 7, 8, 9]  # base
    expoentes = [1, 2, 3, 4, 5, 6, 7, 8]  # expoentes

    print("Enviando tarefas para o cluster...")

    # 3. Mapeamento Distribuído
    # O Client envia as tarefas para os workers de forma equilibrada
    # futuros = client.map(calcular_potencia, numeros, [3]*8)# Calcula a potência de cada número elevado a 3
    futuros = client.map(calcular_potencia, numeros,
                         expoentes)  # Calcula a potência de cada número elevado ao seu respectivo expoente
    # 4. Recolha de resultados
    resultados = client.gather(futuros)

    print("\n=== RESULTADOS FINAIS ===")
    for valor, pid in resultados:
        print(f"Resultado: {valor} | Processado pelo PID: {pid}")

    # Pausa para os alunos verem o Dashboard antes de fechar
    input("\nPressione Enter para encerrar o cluster...")
    client.close()
    cluster.close()