from dataclasses import dataclass, field
from typing import List

def data():
    
    @dataclass
    class ClientePRP:
        x: float                  # Coordenada x
        y: float                  # Coordenada y
        I0: float                 # Estoque inicial
        h: float                  # Custo de inventário
        L: float                  # Limite de estoque
        C: float                  # Capacidade de produção
        s: float                  # Custo fixo de produção
        u: float                  # Custo unitário de produção
        s1: float                 # Tempo de serviço
        B: float                  # Penalidade de atraso
        d: List[float] = field(default_factory=list)  # Demanda


    # Lê todas as linhas do arquivo
    with open("Instancias/ABS1_50_6.dat", "r") as f:
        linhas = f.readlines()

    # Converte os dados para float
    dados = [list(map(float, linha.split())) for linha in linhas]

    # ======================= PARÂMETROS =======================
    N = int(dados[0][0])   # número de clientes
    T = int(dados[1][0])   # períodos
    P = int(dados[2][0])   # número de produtos
    K = int(dados[3][0])   # número de veículos

    # Vetor de clientes
    clientes = [None] * (N + 2)

    contador = 0

    # Ignora o custo de ativação do veículo
    Q = []

    for i in range(K):
        contador = 4 + i
        Q.append(dados[contador][0])  # 

    contador = 5 + K

    # clientes[0] indica a facilidade/fábrica
    clientes[0] = ClientePRP(
        x = dados[contador][0],
        y = dados[contador][1],
        I0 = dados[contador][2],
        h = dados[contador][3],
        L = dados[contador][4],
        C = dados[contador][5],
        s = dados[contador][6],
        u = dados[contador][7],
        s1 = 0.0,
        B = 0.0,
        d = [0.0] * T
    )

    contador += 1

    # clientes[1] até clientes[N] indicam os clientes
    for i in range(1, N + 1):
        clientes[i] = ClientePRP(
            x = dados[contador][0],
            y = dados[contador][1],
            I0 = dados[contador][3],
            h = dados[contador][4],
            L = dados[contador][5],
            C = 0.0,
            s = 0.0,
            u = 0.0,
            s1 = 0.0,
            B = dados[contador][6],
            d = [0.0] * T
        )

        contador += 1

    # Cópia da fábrica como nó de retorno
    clientes[N + 1] = clientes[0]

    # Leitura das demandas
    for i in range(1, N + 1):
        for t in range(T):
            clientes[i].d[t] = dados[contador][t]

        contador += 1

    return clientes, N, T