def wagner_whitin(d, s, h):
    
    N = len(d) 

    # Prefix sum de h para acelerar
    H = [0] * (N + 1)
    for i in range(N):
        H[i+1] = H[i] + h[i]

    # F[t] = custo mínimo até t
    F = [0] * N
    parent = [0] * N

    # Função custo correto
    def cost(j, t):
        total = s[j]
        for k in range(j+1, t+1):
            holding = H[k] - H[j]  # custo acumulado de h[j] até h[k-1]
            total += d[k] * holding
        return total

    # DP
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

def read_data():
    with open("ABS1_50_6_copy.dat", "r") as f:
        linhas = f.readlines()

    d = list(map(int, linhas[0].split()))
    
    s = list(map(int, linhas[1].split()))
    
    return d, s

d = []
s = []

d, s = read_data()

h = [1] * len(d)

custo, pedidos = wagner_whitin(d, s, h)

print("Custo total:", custo)
print("Pedidos:", pedidos)