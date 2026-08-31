import leitura as leitura
import IRP_WW as IRP_WW
import pyVRP as pyVRP


#Leitura dos dados
clientes, N, T = leitura.data()

#Inicialização de variáveis
demanda_ww = []

for i in range(0,T):
    aux = 0

    for j in clientes[1:N+1]:
        aux += j.d[i]

    demanda_ww.append(aux)


def main():
    #custo, pedidos = IRP_WW.main(demanda_ww, clientes)
    IRP_WW.main(demanda_ww, clientes, N)

    # Chamada do pyVRP

    #pyVRP.main(clientes[0], clientes[1:N+1], pedidos, T)

    #ADICIONAR CUSTO TOTAL (PRODUCAO + SETUP + TRANSPORTE) E CUSTO DE ARMAZENAMENTO (HOLDING COST)
        
main()
demanda_ww = []