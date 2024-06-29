#Desenvolvido um sistema bancario com as operações : sacar, depositar e visualizar o extrato.
#Os saques não podem ser maiores de 500, e só poder ser 3 por dia.
import os
print()
print('*'*25)
print(' SISTEMA BANCARIO')
print('*'*25)
print()



saldo = 0
limite = 500
extrato = dict()
numero_saques = 0
LIMITES_SAQUES = 3
saque = 0
deposito = []
saques = []
quant_saque = 0
while True:
    print()
    menu = str(input(
'''[ d ] - Depositar 
[ s ] - Sacar 
[ e ] - Extrato 
[ q ] - Sair
[ * ] - Digite uma opção: ''')).lower()
    
    if menu == 'd':
        while 1:
            deposito.append(int(input('Digite o valor a ser depositado: ')))
            extrato['depositos'] = deposito
            for i in deposito:
                if i <= 0:
                     print('ATENÇÃO!!!!Não é possível o deposito de valores negativos')
                     deposito.remove(i)
            saldo +=i               
            res = input('\nDeseja fazer outro deposito [ Sim ] S - [ Não ] - N: ').upper()
            if res in 'N':
                break  
            #saldo += i  
    elif menu == 's':

        saque = int(input('Digite o valor que você quer sacar: '))
        if quant_saque >= LIMITES_SAQUES:
            print('Limite de saques diarios acedido....')
        elif saque > saldo:
            print(f"Valor disponivel insuficiente, saldo na conta de R${saldo:.2f}")
        elif saque > limite:
            print(f'Limite de saque diario execedito, VALOR DIARIO é de R$:{limite:.2f}')
        elif saque <= saldo:
            print(f'Saque de R${saque:.2f}, efetuado com sucesso!!!')
            quant_saque +=1
            saldo -= saque
            saques.append(saque)

        
    elif menu == 'e':
         os.system('clear')
         print('='*50)
         total_deposito = 0
         print("Valores Depositados:")
         for key, value in extrato.items():
                for y in value:
                    print(f'R$:{(y):.2f}')  

         print('Saques Efetuados: ')
         for i in saques:
             print(f'R$:{i:.2f}')

         print(f"Saldo Total em conta R$:{saldo:.2f}")
         print('='*50)

    elif menu == 'q':
        break
    else:
        print('Opção incorreta , Tente novamente!!!')



print()


