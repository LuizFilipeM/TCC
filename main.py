import leitura
import IRP_WW
import pyVRP


clientes, N, T = leitura.data() # Utiliza o modulo de leitura para obter os dados dos clientes

demanda_ww = []

custo_setup_ww = clientes[0].s

for j in range(0,T):
    aux = 0
    
    for i in clientes[1:N+1]:
        aux += i.d[j]    
    
    demanda_ww.append(aux) # Cria um vetor de demanda para o WW a partir dos dados dos clientes
    

custo, pedidos = IRP_WW.main(demanda_ww, custo_setup_ww, i.h)

demanda_ww = [] # Limpa o vetor de demanda para o próximo cliente

    

# Chamada do pyVRP

pyVRP.main(clientes[0], clientes[1:N+1], pedidos, T)

#ADICIONAR CUSTO TOTAL (PRODUCAO + SETUP + TRANSPORTE) E CUSTO DE ARMAZENAMENTO (HOLDING COST)
    



