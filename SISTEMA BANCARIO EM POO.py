from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = Conta()

class Conta:
    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.limite = 500
        self.numero_saques = 0
        self.LIMITE_SAQUE = 3
        self.transacoes_diarias = []
        self.LIMITE_TRANSACOES = 10

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.extrato += f"Depósito: R${valor:.2f} em {data_hora}\n"
            self.transacoes_diarias.append(data_hora)
        else:
            print("Valor inválido! Tente novamente.")

    def sacar(self, valor):
        excedeu_limite = valor > self.limite
        excedeu_saldo = valor > self.saldo
        excedeu_numero_saques = self.numero_saques >= self.LIMITE_SAQUE
        excedeu_transacoes = len(self.transacoes_diarias) >= self.LIMITE_TRANSACOES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Excedeu o limite de saque.")
        elif excedeu_numero_saques:
            print("Operação falhou! Excedeu o número de saques.")
        elif excedeu_transacoes:
            print("Operação falhou! Você excedeu o número de transações permitidas para hoje.")
        elif valor > 0:
            self.saldo -= valor
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.extrato += f"Saque: R${valor:.2f} em {data_hora}\n"
            self.transacoes_diarias.append(data_hora)
            self.numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n====== EXTRATO =======")
        print("Sem movimentação." if not self.extrato else self.extrato)
        print(f"\nSaldo: R${self.saldo:.2f}")

def main():
    clientes = []
    menu = """
    [1] Criar Conta
    [2] Depósito
    [3] Saque
    [4] Extrato
    [5] Sair
    """

    while True:
        opcao = str(input(menu))

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            print(f"Conta criada com sucesso para {nome}.")

        elif opcao in ["2", "3", "4"]:
            if not clientes:
                print("Nenhum cliente cadastrado. Por favor, crie uma conta primeiro.")
                continue

            cpf = input("Digite o CPF do cliente: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)

            if not cliente:
                print("Cliente não encontrado.")
                continue

            if opcao == "2":
                valor = float(input("Digite o valor que deseja depositar: "))
                cliente.conta.depositar(valor)

            elif opcao == "3":
                valor_saque = float(input("Digite o valor para saque: "))
                cliente.conta.sacar(valor_saque)

            elif opcao == "4":
                cliente.conta.exibir_extrato()

        elif opcao == "5":
            print("Obrigado por usar o sistema.")
            break

        else:
            print("Tente novamente!")

if __name__ == "__main__":
    main()
