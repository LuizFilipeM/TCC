import leitura
import IRP_WW
import pyVRP


#Leitura dos dados
clientes, N, T = leitura.data()

#Inicialização de variáveis
demanda_ww = []
custo_setup_ww = clientes[0].s

for i in range(0,T):
    aux = 0

    for j in clientes[1:N+1]:
        aux += j.d[i]        

    demanda_ww.append(aux)


def main():
    custo, pedidos = IRP_WW.main(demanda_ww, clientes[0].s, clientes[0].h)


    # Chamada do pyVRP

    #pyVRP.main(clientes[0], clientes[1:N+1], pedidos, T)

    #ADICIONAR CUSTO TOTAL (PRODUCAO + SETUP + TRANSPORTE) E CUSTO DE ARMAZENAMENTO (HOLDING COST)
        
main()
demanda_ww = []