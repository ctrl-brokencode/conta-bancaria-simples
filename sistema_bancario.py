from os import system, name
def limpar_terminal():
    system('cls' if name == 'nt' else 'clear')


def exibir_menu():
    limpar_terminal()
    print('-=-'*5 + ' PyBanco! ' + '-=-'*5)
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver extrato')
    print('4 - Cadastrar Usuário')
    print('5 - Criar conta')
    print('6 - Listar contas')
    print('7 - Exibir menu')
    print('8 - Encerrar')
    print('-=-'*13)


class Banco:
    def __init__(self) -> None:
        self.saldo = 0
        self.saques_diarios = 0
        self.transacoes = []
        self.clientes = []
        self.contas = []


    def depositar(self):
        try:
            valor = float(input('> Digite o valor que deseja depositar: '))
        except ValueError:
            print('> Valor inválido!')
        else:
            self.saldo += valor
            self.transacoes.append(f'+ R$ {valor:>12.2f}')
            print(f'Foi depositado R$ {valor:.2f} na sua conta.')


    def sacar(self):
        if self.saques_diarios >= 3:
            print('!! Você já fez 3 saques hoje.')
            return
        try:
            valor = float(input('> Digite o valor que deseja depositar: '))
        except ValueError:
            print('!! Valor inválido!')
            return
        if valor > self.saldo:
            print('!! Você não tem saldo suficiente para realizar esse saque.')
        elif valor > 500:
            print('!! O valor máximo para saque é de R$ 500.')
        else:
            self.saldo -= valor
            self.transacoes.append(f'- R$ {valor:>12.2f}')
            self.saques_diarios += 1
            print(f'Foi sacado R$ {valor:.2f} da sua conta.')


    def ver_extrato(self):
        print('Extrato:')
        for transacao in self.transacoes:
            print(transacao)
        print(f'Total - R$ {self.saldo:.2f}')


    def cadastrar_usuario(self):
        cpf = input('> Digite seu CPF (apenas números): ')
        encontrado_cpf = self.buscar_cpf(cpf)
        if encontrado_cpf:
            print('!! Já existe um cliente com esse CPF.')
            return
        nome = input('> Digite seu nome: ')
        data_nasc = input('> Digite sua data de nascimento (dd/mm/aaaa): ')
        endereco = input('> Digite seu endereço: ')

        self.clientes.append({'nome': nome,
                              'data nascimento': data_nasc,
                              'CPF': cpf,
                              'endereço': endereco})

        print('Usuário criado com êxito.')


    def criar_conta(self):
        cpf = input('> Digite o CPF (apenas números): ')
        encontrado_cpf = self.buscar_cpf(cpf)
        if not encontrado_cpf:
            print('!! O CPF mencionado não foi cadastrado.')
            return
        self.contas.append({'numero_conta': len(self.contas)+1,
                            'CPF': cpf})
        print('Conta criada com êxito.')


    def buscar_cpf(self, cpf) -> bool:
        for cliente in self.clientes:
            if cliente['CPF'] == cpf:
                return True
        return False


    def listar_contas(self):
        for conta in self.contas:
            print(f'CPF: {conta['CPF']} -> 0001 {conta['numero_conta']}')


if __name__ == '__main__':
    banco = Banco()
    exibir_menu()
    while True:
        escolha = input('\n> Digite sua escolha: ')

        match escolha:
            case '1':
                banco.depositar()
            case '2':
                banco.sacar()
            case '3':
                banco.ver_extrato()
            case '4':
                banco.cadastrar_usuario()
            case '5':
                banco.criar_conta()
            case '6':
                banco.listar_contas()
            case '7':
                exibir_menu()
            case '8':
                print('Obrigado por utilizar o PyBanco!')
                break
            case _:
                print('Opção inválida.')
