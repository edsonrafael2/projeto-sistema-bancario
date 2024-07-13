#Desenvolvido um sistema bancario com as operações : sacar, depositar e visualizar o extrato.
#Os saques não podem ser maiores de 500, e só poder ser 3 por dia.

'''
Obs. criar tres novas funcoes , criar usuario, criar conta e lista de contas
Regras: armazenar os usuarios em uma lista
'''
import os
print()
print('='*25)
print(' SISTEMA BANCARIO')
print('='*25)

def escolha():
        menu = str(input(
    '''
    [ d ] - Depositar 
    [ s ] - Sacar 
    [ e ] - Extrato 
    [ u ] - Novo Cliente(Usuário)
    [ c ] - Nova conta
    [ l ] - Lista de contas
    [ q ] - Sair
    [ * ] - Digite uma opção: ''')).lower()
        
        return menu
    

def depositar(saldo,valor,extrato,/):
        if valor > 0:
           saldo += valor
           extrato.append(f'Deposito R$: {valor:.2f}')
           print('Deposito efetuado com sucesso.')
        else:
            print("Valor informado esta incorreto!!")
                 
        return saldo, extrato

def sacar(saldo,valor,extrato,limite,saques_diarios,limite_saques_diarios,/):
    if valor > limite:
          print("O Valor do saque excede o limite! ")
    elif valor > saldo:
          print("Saldo insuficiente para saque!")
    elif saques_diarios >= limite_saques_diarios:
          print(" Limite de saques diarios execedido!")
    elif valor > 0:
          saldo -= valor
          extrato.append(f'Saque R$: {valor:.2f}')
          saques_diarios +=1
          print('Saque efetuado com sucesso!!')
    else:
          print("ATENÇÃO!!!, o Valor informado esta incorreto.")

    return saldo , extrato , saques_diarios              
      


def extrato_conta(saldo,/,*,extrato):
     os.system('clear')
     print("="*25)
     for i in extrato:
         print(f'{(i)}') 
     print("***")    
     print(f'Saldo da conta R$:{saldo:.2f}')
     print("="*25)

def criar_usuario(usuarios):
     cpf = input('Digite o CPF, apenas números: ')
     usuario = filtrar_usuario(cpf,usuarios)
     if usuario:
          print("Já existe usuario com esta conta...")
          return

     nome = input('Digite o nome: ')
     data_nasc = input('Digite a data de nascimento neste formato dd-mm-yyyy: ')
     endereco = input('Digite o endereço Logradouro - nro - bairro - cidade/Estado: ')
     usuarios.append({'nome':nome, 'data': data_nasc, 'CPF': cpf,'Endereço':endereco})
     print('Usuario criado com sucesso!!!')

def filtrar_usuario(cpf,usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None




def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITES_SAQUES = 3
    usuarios  = []
    lista_contas = []
    
    while True:

        opcao = escolha()
        if opcao == 'd':
             valor = int(input("Digite o valor a depositar:  "))
             saldo,extrato=depositar(saldo,valor,extrato)

        elif opcao == 's':
             valor = int(input(" Digite o valor a ser sacado: "))
             saldo,extrato,numero_saques = sacar(saldo,valor,extrato,limite,numero_saques,LIMITES_SAQUES)

        elif opcao == 'e':
             extrato_conta(saldo,extrato=extrato)
             
        elif opcao == 'u':
             criar_usuario(usuarios)          

        elif opcao == 'q':
            print('Fim do programa!!!!')
            break
    

main()