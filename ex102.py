def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
fac = int(input('Digite um número: '))
print(fatorial(fac, show=True))
# help(fatorial)
