'''
Tentativa de criação de um sistema bancário e aprimorar com o tempo
'''
# Imports
import pdb
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Variáveis Globais
saldo = 0
conta_criada = False
login = False
extrato = ''
username = ''
senha = ''
opcao = 10
nome = ''
contas = {} # Dicionário feito para armazenas contas e ser possível realizar transferencia.

# Funções
def menu_inicial():
    print(' ')
    print(' ')
    print('=' * 50)
    print(' ')
    print(' '*15 + '🏦 Bem-Vindo ao Banco 🏦')
    print(' ')
    print(' '*10 + 'Somos um banco feito pelo povo e para o povo!')
    print(' ')
    print('=' * 50)
    print(' ')
    print(' 1️⃣  - Criar Conta')
    print(' 2️⃣  - Entrar na conta')
    print(Fore.RED + ' 0️⃣  - Sair')
    print(' ')
    print('=' * 50)

def menu_principal():
    print('=' * 50)
    print(' ')
    print(' '*15 + '🏦 Menu Principal 🏦')
    print(' ')
    print(' 3️⃣  - Realizar Depósito')
    print(' 4️⃣  - Realizar Saque')
    print(' 5️⃣  - Ver extrato')
    print(' 6️⃣  - Transferência de Fundos')
    print(' 7️⃣  - Mudar Senha')
    print(' 8️⃣  - Sair da Conta')
    print(' 0️⃣  - Sair')
    print(' ')
    print('=' * 50)

def criar_conta():
    global username
    global senha
    global conta_criada
    global nome
    print(f'Olá. Vamos iniciar a criação de sua Conta! 😊')
    username = input('Digite aqui seu Username: ')
    while True:
        senha = input('Digite aqui sua senha: ')
        if len(senha) >= 4:
            break
        else:
            print('--- A senha deve possuir no mínimo 4 caracteres. ---')
            print(' ')

    contas[username] = {'nome': nome, 'senha': senha, 'saldo': 0, 'extrato': ''}
    conta_criada = True
    print('')
    print(Fore.GREEN + 'Conta criada com sucesso! 😄')
    return

def entrar_conta():
    global username
    global senha
    global conta_criada
    global login
    if not login:
        teste_usuario = input('Digite o username: ')
        teste_senha = input('Digite aqui sua senha: ')
        if teste_usuario in contas and contas[teste_usuario]['senha'] == teste_senha:
            username = teste_usuario
            login = True
            print(Fore.GREEN + '--- Login realizado com sucesso! 😄 ---')
            return
        else:
            print(Fore.RED + '--- Usuário ou senha Incorretos! 💀' )
            return
    else:
        print(Fore.RED + 'Você já está logado!')
        return

def realizar_deposito():
    global contas, username, login

    if login:
        print('Uhul! Vamos realizar um depósito!')
        while True:
            try:
                valor = float(input('Digite aqui o valor do depósito: '))
                break
            except ValueError:
                print(Fore.RED + 'O valor digitado não é um número válido. 💀 ')

        contas[username]['saldo'] += valor
        contas[username]['extrato'] += f'Depósito: R$ {valor:.2f}\n'

        print('')
        print(Fore.GREEN + 'Confirmando...')
        print('----- DEPÓSITO -----')
        print(f'Depósito Feito com sucesso 😄. Foi depositado na conta o valor R$ {valor:.2f}. 🤑')
        print('--------------------')
        return
    else:
        print(Fore.RED + 'Faça Login ou Crie uma Conta primeiro. 💀 ')
        return

def realizar_saque():
    global contas, username, login

    if login:
        print('Vamos realizar um Saque.')
        while True:
            try:
                valor = float(input('Digite o valor a ser sacado: R$ '))
                break
            except ValueError:
                print(Fore.RED + 'Valor inválido. Digite apenas números válidos.')

        if valor > contas[username]['saldo']:
            print(Fore.RED + 'Saldo insuficiente para realizar o saque. 💀')
        else:
            contas[username]['saldo'] -= valor
            contas[username]['extrato'] += f'Saque: R$ {valor:.2f}\n'
            print(Fore.WHITE + f'Saque de R$ {valor:.2f} realizado com sucesso.')
            print(f'Saldo atual: R$ {contas[username]["saldo"]:.2f}')
    else:
        print(Fore.RED + 'Faça Login ou crie uma conta primeiro. 💀 ')

def ver_extrato():
    global contas, username, login

    if login:
        print('\n----- EXTRATO 💰 -----')
        print(f'Seu saldo atual é: R$ {contas[username]["saldo"]:.2f}')

        # Exibindo extrato do usuário logado
        if contas[username]['extrato']:
            print('Operações realizadas:')
            print(contas[username]['extrato'])
        else:
            print('Nenhuma operação foi realizada.')

        print('--------------------')
    else:
        print(Fore.RED + 'Faça login ou crie uma conta primeiro. 💀 ')

def logout():
    global login
    if login and conta_criada:
        login = False
        print('Você foi deslogado!')
        return
    else:
        print(Fore.RED + 'Faça login primeiro. 💀 ')
        return

def mudar_senha():
    global senha, username, contas

    if login:
        teste_senha = input('Digite aqui sua senha atual: ')
        if teste_senha == contas[username]['senha']:
            while True:
                nova_senha = input('Digite sua nova senha (mínimo 4 caracteres): ')
                if len(nova_senha) >= 4:
                    contas[username]['senha'] = nova_senha
                    senha = nova_senha  # Atualiza a variável global senha
                    print(Fore.GREEN + 'Senha alterada com sucesso!')
                    break
                else:
                    print(Fore.LIGHTYELLOW_EX + 'A senha deve possuir no mínimo 4 caracteres.')
        else:
            print(Fore.RED + 'Senha incorreta. 💀')
    else:
        print('Faça primeiro o login. 💀')

def transferencia():
    global contas, username, login

    if login:
        destinatario = input('Digite o USERNAME da conta de Destino: ')

        if destinatario in contas:
            while True:
                try:
                    valor = float(input('Digite o valor a ser transferido: R$ '))
                    break
                except:
                    print('O valor deve ser um número.')

            if contas[username]['saldo'] >= valor:
                contas[username]['saldo'] -= valor
                contas[destinatario]['saldo'] += valor

                # Atualizando extrato do remetente
                contas[username]['extrato'] += f'Transferência enviada para {destinatario}: R$ {valor:.2f}\n'

                # Atualizando extrato do destinatário
                contas[destinatario]['extrato'] += f'Transferência recebida de {username}: R$ {valor:.2f}\n'

                print(f'Transferência de R$ {valor:.2f} para {destinatario} realizada com sucesso! 😄')
            else:
                print(Fore.RED + 'Saldo insuficiente para realizar a transferência. 💀')
        else:
            print(Fore.RED + 'Conta Destinatária não encontrada. 💀 ')
    else:
        print(Fore.RED + 'Faça Login ou crie uma conta primeiro. 💀 ')

# Função Principal
def main():
    global opcao
    while True:
        if login:
            menu_principal()
        else:
            menu_inicial()
        while True:
            try:
                opcao = int(input('Digite aqui a opção desejada: '))
                break
            except ValueError:
                print(Fore.RED + 'Deve-se digitar um número inteiro. Tente Novamente.')
        if opcao == 1 and not login:
            criar_conta()
        elif opcao == 2 and not login:
            entrar_conta()
        elif opcao == 3 and login:
            realizar_deposito()
        elif opcao == 4 and login:
            realizar_saque()
        elif opcao == 5 and login:
            ver_extrato()
        elif opcao == 6 and login:
            transferencia()
        elif opcao == 7 and login:
            mudar_senha()
        elif opcao == 8 and login:
            logout()
        elif opcao == 0:
            print(Fore.RED + 'Saindo...')
            break
        else:
            print(Fore.RED + 'Opção Inválida. Tente Novamente. ')

main()
