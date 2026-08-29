def wagner_whitin(d, clientes, T):
    #holding coit for each client
    H = [[0 for j in range(T+1)] for i in range(len(clientes))]
    for i in range(1, len(clientes)):
        for j in range(T):
            H[i][j+1] = H[i][j] + clientes[i].h
    

    # F[t] = custo mínimo até t
    F = [0] * T
    parent = [0] * T
    for t in range(T):
        F[t] = float('inf')

        j_min = max(0, t - limit_L(clientes, T, 0) + 1) 
        #garantido para horizonte de pedido identico
        # conferir compatibilidade com horizonte de pedidos que variam
        print("j_min:", j_min)
        for j in range(j_min, t + 1):
            if j == 0:
                c = cost(0, t, d, H, clientes)
            else:
                c = F[j-1] + cost(j, t, d, H, clientes)
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
def cost(l, t, d, H, clientes):
    N = len(clientes)
    total = clientes[0].s
    total += clientes[0].u * sum(d[k] for k in range(l, t+1))

    for cliente in range(1, N):
        for k in range(l+1, t+1):
            holding = H[cliente][k] - H[cliente][l]
            total += clientes[cliente].d[k] * holding

    return total

def limit_L(clientes, T, start):   
    max_L = 0
    min_L = T
    aux_d = 0
    for i in range(1, len(clientes)):
        for j in range(start, T):
            
            aux_d += clientes[i].d[j]
            if aux_d <= clientes[i].L + clientes[i].d[start]:
                max_L += 1
            else:
                break
        if max_L < min_L:
            min_L = max_L
        aux_d = 0
        max_L = 0
    print("Limite L:", min_L,start)
    return min_L


def main(d, clientes):
    T = len(d)
    
    print("INICIANDO WW...\n\n")
 
    custo, pedidos = wagner_whitin(d, clientes, T)

    print("Custo total:", custo)
    print("Pedidos:", pedidos)

    print("\n\nWW FINALIZADO COM SUCESSO")

    return custo, pedidos

