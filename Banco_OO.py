import colorama
from colorama import Fore

colorama.init(autoreset=True)

# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, username, senha, nome=''):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.saldo = 0
        self.extrato = ''

    def depositar(self, valor):
        self.saldo += valor
        self.extrato += f'Depósito: R$ {valor:.2f}\n'
        print(Fore.GREEN + f'Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f} 🤑')

    def sacar(self, valor):
        if valor > self.saldo:
            print(Fore.RED + 'Saldo insuficiente para realizar o saque. 💀')
        else:
            self.saldo -= valor
            self.extrato += f'Saque: R$ {valor:.2f}\n'
            print(Fore.WHITE + f'Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}')

    def ver_extrato(self):
        print('\n----- EXTRATO 💰 -----')
        print(f'Seu saldo atual é: R$ {self.saldo:.2f}')
        if self.extrato:
            print('Operações realizadas:')
            print(self.extrato)
        else:
            print('Nenhuma operação foi realizada.')
        print('--------------------')

    def mudar_senha(self, nova_senha):
        self.senha = nova_senha
        print(Fore.GREEN + 'Senha alterada com sucesso!')

# Classe que representa o banco
class Banco:
    def __init__(self):
        self.contas = {}
        self.usuario_logado = None

    def criar_conta(self, username, senha, nome=''):
        if username in self.contas:
            print(Fore.RED + 'Username já existe. Tente outro username.')
            return
        self.contas[username] = ContaBancaria(username, senha, nome)
        print(Fore.GREEN + 'Conta criada com sucesso! 😄')

    def entrar_conta(self, username, senha):
        conta = self.contas.get(username)
        if conta and conta.senha == senha:
            self.usuario_logado = conta
            print(Fore.GREEN + '--- Login realizado com sucesso! 😄 ---')
        else:
            print(Fore.RED + '--- Usuário ou senha incorretos! 💀 ---')

    def logout(self):
        if self.usuario_logado:
            print('Você foi deslogado!')
            self.usuario_logado = None
        else:
            print(Fore.RED + 'Nenhum usuário está logado. 💀')

    def transferir(self, destinatario_username, valor):
        if not self.usuario_logado:
            print(Fore.RED + 'Faça login primeiro. 💀')
            return

        destinatario = self.contas.get(destinatario_username)
        if not destinatario:
            print(Fore.RED + 'Conta destinatária não encontrada. 💀')
            return

        if self.usuario_logado.saldo < valor:
            print(Fore.RED + 'Saldo insuficiente para realizar a transferência. 💀')
            return

        self.usuario_logado.saldo -= valor
        destinatario.saldo += valor
        self.usuario_logado.extrato += f'Transferência enviada para {destinatario_username}: R$ {valor:.2f}\n'
        destinatario.extrato += f'Transferência recebida de {self.usuario_logado.username}: R$ {valor:.2f}\n'
        print(Fore.GREEN + f'Transferência de R$ {valor:.2f} para {destinatario_username} realizada com sucesso! 😄')

    def realizar_deposito(self, valor):
        if self.usuario_logado:
            self.usuario_logado.depositar(valor)
        else:
            print(Fore.RED + 'Faça login primeiro. 💀')

    def realizar_saque(self, valor):
        if self.usuario_logado:
            self.usuario_logado.sacar(valor)
        else:
            print(Fore.RED + 'Faça login primeiro. 💀')

    def ver_extrato(self):
        if self.usuario_logado:
            self.usuario_logado.ver_extrato()
        else:
            print(Fore.RED + 'Faça login primeiro. 💀')

    def mudar_senha(self, nova_senha):
        if self.usuario_logado:
            self.usuario_logado.mudar_senha(nova_senha)
        else:
            print(Fore.RED + 'Faça login primeiro. 💀')

# Função para exibir o menu inicial
def menu_inicial():
    print('\n' + '=' * 50)
    print('\n' + ' '*15 + '🏦 Bem-Vindo ao Banco 🏦')
    print('\n' + ' '*10 + 'Somos um banco feito pelo povo e para o povo!')
    print('\n' + '=' * 50)
    print('\n 1️⃣  - Criar Conta')
    print(' 2️⃣  - Entrar na conta')
    print(Fore.RED + ' 0️⃣  - Sair')
    print('\n' + '=' * 50)

# Função para exibir o menu principal
def menu_principal():
    print('\n' + '=' * 50)
    print('\n' + ' '*15 + '🏦 Menu Principal 🏦')
    print('\n 3️⃣  - Realizar Depósito')
    print(' 4️⃣  - Realizar Saque')
    print(' 5️⃣  - Ver extrato')
    print(' 6️⃣  - Transferência de Fundos')
    print(' 7️⃣  - Mudar Senha')
    print(' 8️⃣  - Sair da Conta')
    print(' 0️⃣  - Sair')
    print('\n' + '=' * 50)

# Função principal para executar o sistema bancário
def executar():
    banco = Banco()
    while True:
        if banco.usuario_logado:
            menu_principal()
        else:
            menu_inicial()

        try:
            opcao = int(input('Digite aqui a opção desejada: '))
        except ValueError:
            print(Fore.RED + 'Deve-se digitar um número inteiro. Tente novamente.')
            continue

        if opcao == 1 and not banco.usuario_logado:
            username = input('Digite seu Username: ')
            senha = input('Digite sua senha: ')
            nome = input('Digite seu nome (opcional): ')
            banco.criar_conta(username, senha, nome)
        elif opcao == 2 and not banco.usuario_logado:
            username = input('Digite seu Username: ')
            senha = input('Digite sua senha: ')
            banco.entrar_conta(username, senha)
        elif opcao == 3 and banco.usuario_logado:
            valor = float(input('Digite o valor do depósito: R$ '))
            banco.realizar_deposito(valor)
        elif opcao == 4 and banco.usuario_logado:
            valor = float(input('Digite o valor do saque: R$ '))
            banco.realizar_saque(valor)
        elif opcao == 5 and banco.usuario_logado:
            banco.ver_extrato()
        elif opcao == 6 and banco.usuario_logado:
            destinatario_username = input('Digite o username do destinatário: ')
            valor = float(input('Digite o valor da transferência: R$ '))
            banco.transferir(destinatario_username, valor)
        elif opcao == 7 and banco.usuario_logado:
            nova_senha = input('Digite a nova senha: ')
            banco.mudar_senha(nova_senha)
        elif opcao == 8 and banco.usuario_logado:
            banco.logout()
        elif opcao == 0:
            print(Fore.RED + 'Saindo...')
            break
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')

if __name__ == '__main__':
    executar()
