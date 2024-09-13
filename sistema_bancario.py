saldo = 0
LIMITE_VALOR_SAQUES = 1500
valor_total_saques = 0
LIMITE_VALOR_POR_SAQUE = 500
LIMITE_SAQUES = 3
quantidade_saques = 0
SISTEMA = True
historico_transacoes = []

menu_de_opcoes = """
    [D] Depositar
    [E] Extrato
    [S] Sacar
    [Q] Sair
"""

def verificar_transacao(resposta):
    match resposta:
        case "D":
            depositar()
        case "E":
            extrato()
        case "S":
            sacar()
        case "Q":
            sair()
        case _:
            print("Operação inválida!\n")

def depositar():
    global saldo
    try:
        resposta = float(input("Digite o valor que deseja depositar: "))
        if resposta > 0:
            saldo += resposta
            registrar_extrato("DEPOSITAR", f"{resposta:.2f}", saldo)
            print("Depósito realizado com sucesso.\n")
        else:
            print("O valor do depósito deve ser positivo.\n")
    except ValueError:
        print("Entrada inválida. Digite um número válido.\n")

def registrar_extrato(transacao, resposta, saldo):
    transacao = {
        "tipo": transacao,
        "valor": resposta,
        "saldo": saldo
    }
    historico_transacoes.append(transacao)

def extrato():
    if historico_transacoes:
        for transacao in historico_transacoes:
            print(f"Tipo: {transacao['tipo']}, Valor: R$ {transacao['valor']}, Saldo: R$ {transacao['saldo']}\n")
    else:
        print("Nenhuma transação registrada.\n")

def sacar():
    global saldo, quantidade_saques, valor_total_saques
    try:
        resposta = float(input("Digite o valor que deseja sacar: "))

        if resposta <= 0:
            print("O valor do saque deve ser positivo.\n")
            return

        if resposta > saldo:
            print("Saldo insuficiente.\n")
            return

        if quantidade_saques >= LIMITE_SAQUES:
            print("Você ultrapassou a quantidade de saques permitida.\n")
            return

        if resposta > LIMITE_VALOR_POR_SAQUE:
            print("Você ultrapassou o valor por saque permitido.\n")
            return
        
        if valor_total_saques + resposta > LIMITE_VALOR_SAQUES:
            print("Você ultrapassou o valor de saques permitido por dia.\n")
            return

        saldo -= resposta
        quantidade_saques += 1
        valor_total_saques += resposta
        registrar_extrato("SACAR", f"{resposta:.2f}", saldo)
        print("Saque realizado com sucesso.\n")
        
    except ValueError:
        print("Entrada inválida. Digite um número válido.\n")

def sair():
    global SISTEMA
    SISTEMA = False

def main():
    global SISTEMA
    while SISTEMA:
        try:
            resposta = input(menu_de_opcoes).upper()
            verificar_transacao(resposta)
        except Exception as e:
            print(f"Ocorreu um erro: {e}\n")

    print("Obrigado pela preferência!\n")

if __name__ == "__main__":
    main()
