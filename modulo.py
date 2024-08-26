from datetime import date

#função exibir o menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{"="*20} BANCO ANACONDA | {dia}/{mes}/{ano}{"="*20}\n')
    print('1 - Criar conta')
    print('2 - Entrar na conta')
    print('3 - Exibir correntistas')
    print('4 - Excluir conta')
    print('5 - Encerrar programa ')

# função exibir operações 
def exibir_operacoes():
    print('\nOPERAÇÃOES\n')
    print('1 - Consulta saldo')
    print('2 - Depositar valor')
    print('3 - Sacar valor')
    print('4 - Voltar')

#função exibir dados do correntista
def exibir_dados(nome, i, saldo):
    print(f'ID: {i}')
    print(f'nome: {nome}')
    print(f'Agência: 1001')
    print(f'Conta: 1001{i}')
    print(f'Saldo: R$ {saldo}')

    #função de  deposito 
def depositar_valor (saldo, valor):
  saldo += valor
  return saldo
#função sacar valor
def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo
    