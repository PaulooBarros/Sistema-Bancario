Sistema Bancário em Python

Este é um projeto de um sistema bancário simples desenvolvido em Python durante práticas de Programação Orientada a Objetos (OO). O sistema permite criar contas bancárias, realizar depósitos, saques, transferências de fundos, mudar a senha, visualizar extratos e fazer login/logout.

Funcionalidades

- Criar Conta: Permite criar uma nova conta bancária com um username, senha e nome do usuário.
- Entrar na Conta: Permite fazer login em uma conta existente usando o username e senha.
- Realizar Depósito: Permite depositar um valor na conta logada.
- Realizar Saque: Permite sacar um valor da conta logada, desde que haja saldo suficiente.
- Ver Extrato: Exibe o extrato das operações realizadas na conta logada.
- Transferência de Fundos: Permite transferir um valor para outra conta usando o username do destinatário.
- Mudar Senha: Permite alterar a senha da conta logada.
- Logout: Permite sair da conta logada.

Estrutura do Código

Classe `ContaBancaria`

Representa uma conta bancária individual. Possui os seguintes métodos:

- `__init__(self, username, senha, nome='')`: Inicializa uma nova conta bancária.
- `depositar(self, valor)`: Realiza um depósito na conta.
- `sacar(self, valor)`: Realiza um saque na conta, se houver saldo suficiente.
- `ver_extrato(self)`: Exibe o extrato da conta.
- `mudar_senha(self, nova_senha)`: Altera a senha da conta.

 Classe `Banco`

Gerencia várias contas bancárias. Possui os seguintes métodos:

- `__init__(self)`: Inicializa o banco.
- `criar_conta(self, username, senha, nome='')`: Cria uma nova conta bancária.
- `entrar_conta(self, username, senha)`: Permite o login em uma conta existente.
- `logout(self)`: Faz logout da conta logada.
- `transferir(self, destinatario_username, valor)`: Realiza uma transferência entre contas.
- `realizar_deposito(self, valor)`: Realiza um depósito na conta logada.
- `realizar_saque(self, valor)`: Realiza um saque na conta logada.
- `ver_extrato(self)`: Exibe o extrato da conta logada.
- `mudar_senha(self, nova_senha)`: Altera a senha da conta logada.
- `menu_inicial(self)`: Exibe o menu inicial do banco.
- `menu_principal(self)`: Exibe o menu principal do banco.
- `executar(self)`: Executa o loop principal do programa, exibindo os menus e respondendo às ações do usuário.
