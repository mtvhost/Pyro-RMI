from platform import python_branch
import re
import math
import Pyro4
from Pyro4.core import Daemon

# python -m Pyro4.naming # name server start in windows 10

# Expressao regular para validar email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

@Pyro4.expose
class Mine(object):
    def check_email(self, email):
        if(re.match(regex, email)):
            return("Email valido")
        else:
            return("Email invalido")


    def inss_taxes(self, salary):
        # primeira faixa salarial
        taxes = 0
        salary = float(salary)
        if(salary <= 1038.99):
            taxes = salary * 0.075
            return str(taxes)

        taxes += 1038.99 * 0.075

        # segunda faixa salarial
        if(salary <= 2098.60):
            taxes += (salary - 1038.99) * 0.09
            return str(taxes)

        taxes += (2098.60 - 1038.99) * 0.09

        # terceira faixa salarial
        if(salary <= 3134.40):
            taxes += (salary - 2098.60) * 0.12
            return str(taxes)

        taxes += (3134.40 - 2098.60) * 0.12

        # quarta faixa salarial
        if(salary <= 6101.06):
            taxes += (salary - 3134.40) * 0.14
            return str(taxes)

        # valor fixo
        taxes = 604.44
        return str(taxes)


    def permutation(self, number):
        return str(math.factorial(int(number)))


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Mine)
    print("Objeto servidor publicado.")
    print(uri)

    ns = Pyro4.locateNS()
    ns.register("MatheusEsteves", uri)
    print("Objeto registrado no serviço de nome.")

    daemon.requestLoop()


if __name__ == "__main__":
    main()