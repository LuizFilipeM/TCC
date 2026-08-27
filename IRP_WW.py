def wagner_whitin(d, s, h):
    
    T = len(d) 
    H = [0] * (T + 1)
    
    for i in range(T):
        H[i+1] = H[i] + h # Trata o custo de armazenamento somente na planta

    # F[t] = custo mínimo até t
    F = [0] * T
    parent = [0] * T
    
    for t in range(T):
        F[t] = float('inf')
        for j in range(t + 1):
            if j == 0:
                c = cost(0, t, d, s, H)
            else:
                c = F[j-1] + cost(j, t, d, s, H)

            if c < F[t]:
                F[t] = c
                parent[t] = j

    # reconstrução
    pedidos = [0] * T
    t = T - 1

    while t >= 0:
        j = parent[t]
        pedidos[j] = sum(d[k] for k in range(j, t+1))
        t = j - 1

    return F[T-1], pedidos

# Função custo
def cost(j, t, d, s, H):
    total = s
    for k in range(j+1, t+1):
        holding = H[k] - H[j]
        total += d[k] * holding
    return total

def main(d, s, h):

    print("INICIANDO WW...\n\n")

    custo, pedidos = wagner_whitin(d, s, h)

    print("Custo total:", custo)
    print("Pedidos:", pedidos)

    print("\n\nWW FINALIZADO COM SUCESSO\n\n")

    return custo, pedidos
