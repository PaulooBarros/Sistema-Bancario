import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont

# Variáveis Globais
saldo = 0
conta_criada = False
login = False
extrato = ''
current_user = ''
senha = ''
opcao = 10
nome = ''
contas = {}  # Dicionário para armazenar contas e possibilitar transferências.
id_counter = 1


# Funções
def mostrar_menu_inicial():
    limpar_tela()

    label = ttk.Label(root, text="🏦 Bem-Vindo ao Banco 🏦", font=header_font)
    label.pack(pady=10)

    button_criar_conta = ttk.Button(root, text="Criar Conta", command=mostrar_tela_criar_conta)
    button_criar_conta.pack(pady=5)

    button_entrar_conta = ttk.Button(root, text="Entrar na Conta", command=mostrar_tela_entrar_conta)
    button_entrar_conta.pack(pady=5)

    button_sair = ttk.Button(root, text="Sair", command=root.quit)
    button_sair.pack(pady=5)


def mostrar_menu_principal():
    limpar_tela()

    label = ttk.Label(root, text="🏦 Menu Principal 🏦", font=header_font)
    label.pack(pady=10)

    button_deposito = ttk.Button(root, text="Realizar Depósito", command=mostrar_tela_deposito)
    button_deposito.pack(pady=5)

    button_saque = ttk.Button(root, text="Realizar Saque", command=mostrar_tela_saque)
    button_saque.pack(pady=5)

    button_extrato = ttk.Button(root, text="Ver Extrato", command=ver_extrato)
    button_extrato.pack(pady=5)

    button_transferencia = ttk.Button(root, text="Transferência de Fundos", command=mostrar_tela_transferencia)
    button_transferencia.pack(pady=5)

    button_mudar_senha = ttk.Button(root, text="Mudar Senha", command=mostrar_tela_mudar_senha)
    button_mudar_senha.pack(pady=5)

    button_informacoes_conta = ttk.Button(root, text="Informações da Conta", command=mostrar_tela_informacoes_conta)
    button_informacoes_conta.pack(pady=5)

    button_sair_conta = ttk.Button(root, text="Sair da Conta", command=logout)
    button_sair_conta.pack(pady=5)


def mostrar_tela_criar_conta():
    limpar_tela()

    label_nome = ttk.Label(root, text="Digite seu nome:")
    label_nome.pack(pady=5)

    global entry_nome
    entry_nome = ttk.Entry(root)
    entry_nome.pack(pady=5)

    label_username = ttk.Label(root, text="Digite seu username:")
    label_username.pack(pady=5)

    global entry_username
    entry_username = ttk.Entry(root)
    entry_username.pack(pady=5)

    label_senha = ttk.Label(root, text="Digite sua senha (mínimo 4 caracteres):")
    label_senha.pack(pady=5)

    global entry_senha
    entry_senha = ttk.Entry(root, show='*')
    entry_senha.pack(pady=5)

    button_confirmar_criacao = ttk.Button(root, text="Confirmar", command=criar_conta)
    button_confirmar_criacao.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_inicial)
    button_voltar.pack(pady=5)


def mostrar_tela_entrar_conta():
    limpar_tela()

    label_username = ttk.Label(root, text="Digite seu username:")
    label_username.pack(pady=5)

    global entry_login_username
    entry_login_username = ttk.Entry(root)
    entry_login_username.pack(pady=5)

    label_senha = ttk.Label(root, text="Digite sua senha:")
    label_senha.pack(pady=5)

    global entry_login_senha
    entry_login_senha = ttk.Entry(root, show='*')
    entry_login_senha.pack(pady=5)

    button_confirmar_login = ttk.Button(root, text="Entrar", command=entrar_conta)
    button_confirmar_login.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_inicial)
    button_voltar.pack(pady=5)


def mostrar_tela_deposito():
    limpar_tela()

    label_deposito = ttk.Label(root, text="Digite o valor do depósito:")
    label_deposito.pack(pady=5)

    global entry_deposito
    entry_deposito = ttk.Entry(root)
    entry_deposito.pack(pady=5)

    button_confirmar_deposito = ttk.Button(root, text="Confirmar", command=realizar_deposito)
    button_confirmar_deposito.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def mostrar_tela_saque():
    limpar_tela()

    label_saque = ttk.Label(root, text="Digite o valor do saque:")
    label_saque.pack(pady=5)

    global entry_saque
    entry_saque = ttk.Entry(root)
    entry_saque.pack(pady=5)

    button_confirmar_saque = ttk.Button(root, text="Confirmar", command=realizar_saque)
    button_confirmar_saque.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def mostrar_tela_transferencia():
    limpar_tela()

    label_transferencia_destinatario = ttk.Label(root, text="Digite o username ou ID do destinatário:")
    label_transferencia_destinatario.pack(pady=5)

    global entry_transferencia_destinatario
    entry_transferencia_destinatario = ttk.Entry(root)
    entry_transferencia_destinatario.pack(pady=5)

    label_transferencia_valor = ttk.Label(root, text="Digite o valor da transferência:")
    label_transferencia_valor.pack(pady=5)

    global entry_transferencia_valor
    entry_transferencia_valor = ttk.Entry(root)
    entry_transferencia_valor.pack(pady=5)

    button_confirmar_transferencia = ttk.Button(root, text="Confirmar", command=transferencia)
    button_confirmar_transferencia.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def mostrar_tela_mudar_senha():
    limpar_tela()

    label_senha_atual = ttk.Label(root, text="Digite sua senha atual:")
    label_senha_atual.pack(pady=5)

    global entry_senha_atual
    entry_senha_atual = ttk.Entry(root, show='*')
    entry_senha_atual.pack(pady=5)

    label_nova_senha = ttk.Label(root, text="Digite sua nova senha:")
    label_nova_senha.pack(pady=5)

    global entry_nova_senha
    entry_nova_senha = ttk.Entry(root, show='*')
    entry_nova_senha.pack(pady=5)

    button_confirmar_mudar_senha = ttk.Button(root, text="Confirmar", command=mudar_senha)
    button_confirmar_mudar_senha.pack(pady=5)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def mostrar_tela_informacoes_conta():
    global contas, current_user

    conta = contas[current_user]

    limpar_tela()

    label_informacoes_conta = ttk.Label(root, text="Informações da Conta", font=header_font)
    label_informacoes_conta.pack(pady=10)

    text_informacoes = f"Nome: {conta['nome']}\nUsername: {current_user}\nID: {conta['id']}\nSaldo: R$ {conta['saldo']:.2f}"
    label_informacoes = ttk.Label(root, text=text_informacoes)
    label_informacoes.pack(pady=10)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def criar_conta():
    global id_counter, contas

    nome = entry_nome.get()
    username = entry_username.get()
    senha = entry_senha.get()

    if not nome or not username or not senha:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return

    if len(senha) < 4:
        messagebox.showwarning("Atenção", "A senha deve ter no mínimo 4 caracteres!")
        return

    if username in contas:
        messagebox.showwarning("Atenção", "Username já existe!")
        return

    contas[username] = {'nome': nome, 'senha': senha, 'saldo': 0, 'extrato': '', 'id': id_counter}
    id_counter += 1

    messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
    mostrar_menu_inicial()


def entrar_conta():
    global current_user, contas, login

    username = entry_login_username.get()
    senha = entry_login_senha.get()

    if username in contas and contas[username]['senha'] == senha:
        current_user = username
        login = True
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        mostrar_menu_principal()
    else:
        messagebox.showerror("Erro", "Username ou senha incorretos!")


def realizar_deposito():
    global contas, current_user

    try:
        valor = float(entry_deposito.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido!")
        return

    contas[current_user]['saldo'] += valor
    contas[current_user]['extrato'] += f"Depósito: R$ {valor:.2f}\n"

    messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    mostrar_menu_principal()


def realizar_saque():
    global contas, current_user

    try:
        valor = float(entry_saque.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido!")
        return

    if valor > contas[current_user]['saldo']:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return

    contas[current_user]['saldo'] -= valor
    contas[current_user]['extrato'] += f"Saque: R$ {valor:.2f}\n"

    messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
    mostrar_menu_principal()


def transferencia():
    global contas, current_user

    destinatario = entry_transferencia_destinatario.get()
    try:
        valor = float(entry_transferencia_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido!")
        return

    if not destinatario or not valor:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return

    destinatario_encontrado = None
    for user, info in contas.items():
        if user == destinatario or str(info['id']) == destinatario:
            destinatario_encontrado = user
            break

    if not destinatario_encontrado:
        messagebox.showerror("Erro", "Conta destinatária não encontrada!")
        return

    if valor > contas[current_user]['saldo']:
        messagebox.showerror("Erro", "Saldo insuficiente!")
        return

    contas[current_user]['saldo'] -= valor
    contas[destinatario_encontrado]['saldo'] += valor

    contas[current_user]['extrato'] += f"Transferência enviada para {destinatario_encontrado}: R$ {valor:.2f}\n"
    contas[destinatario_encontrado]['extrato'] += f"Transferência recebida de {current_user}: R$ {valor:.2f}\n"

    messagebox.showinfo("Sucesso",
                        f"Transferência de R$ {valor:.2f} para {destinatario_encontrado} realizada com sucesso!")
    mostrar_menu_principal()


def mudar_senha():
    global contas, current_user

    senha_atual = entry_senha_atual.get()
    nova_senha = entry_nova_senha.get()

    if contas[current_user]['senha'] == senha_atual:
        if len(nova_senha) < 4:
            messagebox.showwarning("Atenção", "A nova senha deve ter no mínimo 4 caracteres!")
            return
        contas[current_user]['senha'] = nova_senha
        messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
        mostrar_menu_principal()
    else:
        messagebox.showerror("Erro", "Senha atual incorreta!")


def ver_extrato():
    global contas, current_user

    extrato = contas[current_user]['extrato']
    saldo_atual = contas[current_user]['saldo']

    limpar_tela()

    label_extrato = ttk.Label(root, text=f"Extrato da Conta - Saldo: R$ {saldo_atual:.2f}", font=header_font)
    label_extrato.pack(pady=10)

    text_extrato = tk.Text(root, height=10, width=50)
    text_extrato.insert(tk.END, extrato if extrato else "Nenhuma operação foi realizada.")
    text_extrato.config(state=tk.DISABLED)
    text_extrato.pack(pady=10)

    button_voltar = ttk.Button(root, text="Voltar", command=mostrar_menu_principal)
    button_voltar.pack(pady=5)


def logout():
    global login, current_user
    login = False
    current_user = ''
    messagebox.showinfo("Logout", "Você foi deslogado com sucesso!")
    mostrar_menu_inicial()


def limpar_tela():
    for widget in root.winfo_children():
        widget.destroy()


# Função Principal
def main():
    mostrar_menu_inicial()


# Configuração da Interface Tkinter
root = tk.Tk()
root.title("Sistema Bancário")
root.geometry("400x500")

# Fontes e Estilos
header_font = tkfont.Font(family="Helvetica", size=16, weight="bold")

main()

root.mainloop()
