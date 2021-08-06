import Pyro4
import sys


def main():
    MatheusEsteves = Pyro4.Proxy("PYRONAME:MatheusEsteves")

    try:
        MatheusEsteves._pyroBind()
    except Pyro4.errors.CommunicationError:
        print("Objeto remoto não encontrado. Encerrando execução.")
        sys.exit(1)

    while(True):
        # Lendo uma mensagem
        print("Opções:")
        print("a - Verificar email")
        print("b - Desconto do inss")
        print("c - Quantidade de permutações")
        print("Qualquer outra letra - Encerra execução")
        print("Entre com uma opção:")
        command = input()
        # Verificação da função escolhida
        if(command == "a"):
            print("Verificar email")
            print("Entre com o email:")
            email = input()
            print(MatheusEsteves.check_email(email))
        elif(command == "b"):
            print("Desconto do inss")
            print("Entre com o salário:")
            salario = input()
            print(MatheusEsteves.inss_taxes(salario))
        elif(command == "c"):
            print("Quantidade de permutações")
            elementos = input()
            print(MatheusEsteves.permutation(elementos))
        else:
            print("Qualquer outra letra")
            break


if __name__ == "__main__":
    main()
