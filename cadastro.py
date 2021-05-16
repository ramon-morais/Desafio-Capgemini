import time
from datetime import date

def calcular_valor_investido():
    valor = float(input("Digite o valor, em reais, que deseja investir: \n"))
    total = (valor * 21.6) * 4 + (valor * 30)
    return total

def gerenciador():
    cad_anuncios = []
    while 1 == 1:
        print("Escolha uma opção:")
        print("1 <-> Cadastro de anúncio")
        print("2 <-> Relatório de anúncio cadastrado")
        print("3 <-> Buscar anúncio")
        print("4 <-> Sair do programa")

        opcao_digitada = int(input("?"))
        if opcao_digitada == 1:
            nome = input("Informe o nome do anúncio: ")
            cliente = input("Informe o nome do cliente: ")
            print("Quando iniciará o investimento? \n")
            dia = int(input("Dia: "))
            mes = int(input("Mes: "))
            ano = int(input("Ano: "))
            print("\n Quando será finalizado o investimento? \n")
            dia_final = int(input("Dia: "))
            mes_final = int(input("Mes: "))
            ano_final = int(input("Ano: "))
            valor_investido = float(input("Digite o valor, em reais, que deseja investir: \n"))
            dias_contados = (date(year=ano_final, month=mes_final, day=dia_final) - date(year=ano, month=mes, day=dia))
            total_investido = float(dias_contados.days * valor_investido)
            numero_views = float((total_investido * 21.6) * 4 + (total_investido * 30))
            total_cliques = float(dias_contados.days * 3.6 * valor_investido)
            total_compartilhado = float(dias_contados.days * 0.54 * valor_investido)
            cad_anuncios.append((nome, cliente, valor_investido, dia, mes, ano, dia_final, mes_final, ano_final, total_investido, numero_views, total_cliques, total_compartilhado))
            print('\n')
        elif opcao_digitada == 2:
            for anuncio in cad_anuncios:
                nome, cliente, valor_investido, dia, mes, ano, dia_final, mes_final, ano_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                print(f'Nome do anúncio: {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f" % total_investido}'
                      f'\nTotal de cliques: {"%.2f" % total_cliques}\nTotal de compartilhamento: {"%.2f" % total_compartilhado}\n'
                      f'Visualizações: {"%.2f" % numero_views}\n')

        elif opcao_digitada == 3:
            print("1. Procurar por cliente"
                  "\n2. Procurar por período")

            opcao = int(input("Opção: \n"))

            if opcao == 1:
                cliente_desejado = input("Nome do cliente: ")
                for anuncio in cad_anuncios:
                    nome, cliente, valor_investido, dia, mes, ano, dia_final, mes_final, ano_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                    if cliente == cliente_desejado:
                        print(
                            f'Nome:  {nome}\nCliente: {cliente}\nTotal investido: R$ {"%.2f" % total_investido}\n'
                            f'Visualizações: {"%.2f" % numero_views}\nTotal de cliques: {"%.2f" % total_cliques}\nTotal de compartilhamento: {"%.2f" % total_compartilhado}')
                        print("\n" * 2)
                    else:
                        print("Cliente não encontrado")
                        break

            elif opcao == 2:
                dia_periodo = int(input("DIA: "))
                mes_periodo = int(input("MES: "))
                ano_periodo = int(input("ANO: "))
                for anuncio in cad_anuncios:
                    nome, cliente, valor_investido, dia, mes, ano, dia_final, mes_final, ano_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio
                if date(day=dia_periodo, month=mes_periodo, year=ano_periodo) >= date(year=ano, month=mes,
                                                                                      day=dia) and date(
                        day=dia_periodo, month=mes_periodo, year=ano_periodo) <= date(year=ano_final, month=mes_final,
                                                                                      day=dia_final):
                    for anuncio in cad_anuncios:
                        nome, cliente, valor_investido, dia, mes, ano, dia_final, mes_final, ano_final, total_investido, numero_views, total_cliques, total_compartilhado = anuncio

                        print(

                            f'Nome:  {nome}\nCliente: {cliente}\nValor investido: R$ {"%.2f" % valor_investido}\nTotal investido: R$ {"%.2f" % total_investido}\n'
                            f'Visualizações: {"%.2f" % numero_views}\nTotal de cliques: {"%.2f" % total_cliques}\nTotal de compartilhamento: {"%.2f" % total_compartilhado}')

                        print("\n" * 2)
                else:
                    print("cliente não encontrado: ")
            else:
                print("Opção Inválida")
        elif opcao_digitada == 4:
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida")

gerenciador()
