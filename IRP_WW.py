def wagner_whitin(d, s, h):
    
    N = len(d) 

    H = [0] * (N + 1)
    
    for i in range(N):
        H[i+1] = H[i] + h # Trata o custo de armazenamento como constante 

    # F[t] = custo mínimo até t
    F = [0] * N
    parent = [0] * N

    # Função custo
    def cost(j, t):
        total = s
        for k in range(j+1, t+1):
            holding = H[k] - H[j]  # custo acumulado de h[j] até h[k-1]
            total += d[k] * holding # mais custo indireto
        return total

    
    for t in range(N):
        F[t] = float('inf')
        for j in range(t + 1):
            if j == 0:
                c = cost(0, t)
            else:
                c = F[j-1] + cost(j, t)

            if c < F[t]:
                F[t] = c
                parent[t] = j

    # reconstrução
    pedidos = [0] * N
    t = N - 1

    while t >= 0:
        j = parent[t]
        pedidos[j] = sum(d[k] for k in range(j, t+1))
        t = j - 1

    return F[N-1], pedidos

def main(d, s, h):

    print("INICIANDO WW...\n\n")

    

    custo, pedidos = wagner_whitin(d, s, h)

    print("Custo total:", custo)
    print("Pedidos:", pedidos)

    print("\n\nWW FINALIZADO COM SUCESSO\n\n")

    return custo, pedidos