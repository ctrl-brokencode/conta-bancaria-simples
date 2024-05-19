from os import system, name
def limpar_terminal():
    system('cls' if name == 'nt' else 'clear')


def exibir_menu():
    limpar_terminal()
    print('-=-'*5 + ' PyBanco! ' + '-=-'*5)
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver extrato')
    print('4 - Exibir menu')
    print('5 - Encerrar')
    print('-=-'*13)


class Banco:
    def __init__(self) -> None:
        self.saldo = 0
        self.saques_diarios = 0
        self.transacoes = []


    def __str__(self) -> str:
        return str(self.saldo)


    def depositar(self):
        try:
            valor = float(input('> Digite o valor que deseja depositar: '))
        except ValueError:
            print('> Valor inválido!')
        else:
            self.saldo += valor
            self.transacoes.append(f'+ R$ {valor:>8.2f}')
            print(f'Foi depositado R$ {valor:.2f} na sua conta.')


    def sacar(self):
        if self.saques_diarios >= 3:
            print('Você já fez 3 saques hoje.')
            return
        try:
            valor = float(input('> Digite o valor que deseja depositar: '))
        except ValueError:
            print('> Valor inválido!')
            return
        if valor > self.saldo:
            print('Você não tem saldo suficiente para realizar esse saque.')
        elif valor > 500:
            print('O valor máximo para saque é de R$ 500.')
        else:
            self.saldo -= valor
            self.transacoes.append(f'- R$ {valor:>8.2f}')
            self.saques_diarios += 1
            print(f'Foi sacado R$ {valor:.2f} da sua conta.')


    def ver_extrato(self):
        print('Extrato:')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Seu total é de {self.saldo:.2f}')


if __name__ == '__main__':
    conta = Banco()
    exibir_menu()
    while True:
        escolha = input('\n> Digite sua escolha: ')

        match escolha:
            case '1':
                conta.depositar()
            case '2':
                conta.sacar()
            case '3':
                conta.ver_extrato()
            case '4':
                exibir_menu()
            case '5':
                print('Obrigado por utilizar o PyBanco!')
                break
            case _:
                print('Opção inválida.')
