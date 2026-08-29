def wagner_whitin(d, clientes, N, T):

    # Custo de inventário por cliente
    H = [[0 for j in range(T+1)] for i in range(len(clientes))]
    for i in range(1, len(clientes)):
        for j in range(T):
            H[i][j+1] = H[i][j] + clientes[i].h


    # F[t] = custo mínimo até t
    F = [float('inf')] * T
    parent = [0] * T
    for t in range(T):
        for j in range(t + 1):
            if not lote_viavel(j, t, clientes, N):
                continue
            if j == 0:
                c = cost(0, t, d, H, clientes)
            else:
                c = F[j-1] + cost(j, t, d, H, clientes)
            if c < F[t]:
                F[t] = c
                parent[t] = j


    # Reconstrução 
    pedidos = [0] * T
    t = T - 1
    while t >= 0:
        j = parent[t]
        pedidos[j] = sum(d[k] for k in range(j, t+1))
        t = j - 1

    return F[T-1], pedidos

def cost(l, t, d, H, clientes):
    N = len(clientes)
    total = clientes[0].s
    total += clientes[0].u * sum(d[k] for k in range(l, t+1))

    for cliente in range(1, N):
        for k in range(l+1, t+1):
            holding = H[cliente][k] - H[cliente][l]
            total += clientes[cliente].d[k] * holding

    return total

# Considera que a demanda do periodo atual não consome estoque
def lote_viavel(l, t, clientes, N):
    for i in range(1, N + 1):
        cli = clientes[i]
        pico = sum(cli.d[k] for k in range(l+1, t + 1))
        if cli.L is not None and pico > cli.L:
            return False
    return True

def main(d, clientes, N):
    T = len(d)

    print("INICIANDO WW...\n\n")

    custo, pedidos = wagner_whitin(d, clientes, N, T)

    print("Custo total:", custo)
    print("Pedidos:", pedidos)

    print("\n\nWW FINALIZADO COM SUCESSO")

    return custo, pedidos