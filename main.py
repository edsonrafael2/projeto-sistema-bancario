# Sistema bancário com operações: sacar, depositar, visualizar o extrato, criar usuário, criar conta e listar contas.
# Regras: os saques não podem ser maiores de 500 e só podem ser 3 por dia. Armazenar os usuários em uma lista.

import os

print()
print('=' * 25)
print(' SISTEMA BANCARIO')
print('=' * 25)

def escolha():
    menu = str(input(
        '''
    [ d ] - Depositar 
    [ s ] - Sacar 
    [ e ] - Extrato 
    [ u ] - Novo Cliente (Usuário)
    [ c ] - Nova conta
    [ l ] - Lista de contas
    [ q ] - Sair
    [ * ] - Digite uma opção: '''
    )).lower()
    
    return menu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f'Deposito R$: {valor:.2f}')
        print('Deposito efetuado com sucesso.')
    else:
        print("Valor informado está incorreto!!")
    
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, saques_diarios, limite_saques_diarios, /):
    if valor > limite:
        print("O Valor do saque excede o limite!")
    elif valor > saldo:
        print("Saldo insuficiente para saque!")
    elif saques_diarios >= limite_saques_diarios:
        print("Limite de saques diários excedido!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f'Saque R$: {valor:.2f}')
        saques_diarios += 1
        print('Saque efetuado com sucesso!!')
    else:
        print("ATENÇÃO!!! Valor informado está incorreto.")
    
    return saldo, extrato, saques_diarios

def extrato_conta(saldo, /, *, extrato):
    os.system('clear')
    print("=" * 25)
    for i in extrato:
        print(f'{i}') 
    print("***")    
    print(f'Saldo da conta R$:{saldo:.2f}')
    print("=" * 25)

def criar_usuario(usuarios):
    cpf = input('Digite o CPF, apenas números: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com este CPF...")
        return

    nome = input('Digite o nome: ')
    data_nasc = input('Digite a data de nascimento no formato dd-mm-yyyy: ')
    endereco = input('Digite o endereço: Logradouro, nro - bairro - cidade/Estado: ')
    usuarios.append({'nome': nome, 'data': data_nasc, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!!!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o número do CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!!!")
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print("Usuário não encontrado...")

def lista_de_contas(contas):
    for conta in contas:
        linha = f'''
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        '''
        print(linha)

def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITES_SAQUES = 3
    usuarios = []
    contas = []
    
    while True:
        opcao = escolha()
        if opcao == 'd':
            valor = float(input("Digite o valor a depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITES_SAQUES)

        elif opcao == 'e':
            extrato_conta(saldo, extrato=extrato)

        elif opcao == 'u':
            criar_usuario(usuarios)

        elif opcao == 'c':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'l':
            lista_de_contas(contas)

        elif opcao == 'q':
            print('Fim do programa!!!!')
            break

main()
