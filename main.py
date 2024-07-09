#Desenvolvido um sistema bancario com as operações : sacar, depositar e visualizar o extrato.
#Os saques não podem ser maiores de 500, e só poder ser 3 por dia.
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



def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITES_SAQUES = 3
    
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
             
                        

        elif opcao == 'q':
            print('Fim do programa!!!!')
            break
    

main()