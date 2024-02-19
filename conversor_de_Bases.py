def converte_decimal(valor: int, base: int):
    """
    :param valor: recebe um valor inteiro
    :param base: recebe um valor igual a 2, 8, ou 16
    :return: retorna a converção numérica de um valor decimal para a base escolhida
    """
    if valor >= 0 and type(valor) == int:
        if base == 2 or base == 8 or base == 16 and type(base) == int:
            valor_convertido = []
            letras_hexadecimais = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            dividendo = valor
            divisor = base
            while True:
                dividendo /= divisor
                resto_div = int((dividendo * divisor) - (int(dividendo) * divisor))
                if base == 16 and resto_div > 9:
                    resto_div = letras_hexadecimais[resto_div]
                valor_convertido.append(f'{resto_div}')
                if int(dividendo) == 0:
                    break
            for n in valor_convertido[::-1]:
                print(n, end='')
            return valor_convertido
        else:
            # gera uma exceção caso a variavel 'base' receba um valor diferente de 2, 8, ou 16
            raise Exception('The Base should be integer and equal to 2, 8, or 16')
    else:
        # gera uma exceção caso a variavel 'valor' receba um valor que não seja um inteiro
        raise Exception('The value should be integer end greater than or equal to zero')


def converte_binario(valor: str, base: int):
    """
    :param valor: recebe um valor binário
    :param base: recebe um valor igual a 8, 10 ou 16
    :return: retorna a converção numérica de um valor binário para base escolhida
    """
    list_exp = [1, 2, 4, 8]
    letras_hexadecimais = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    sum = 0
    cont = 0
    list_resp = []
    for i in valor:
        if i != '0' and i != '1':
            # gera uma exceção caso seja inserido um valor não binário
            raise Exception('Invalid binary value')
    if base == 8:
        for i, v in enumerate(valor[::-1]):
            if i % 3 != 0 or i == 0:
                if v == '1':
                    sum += list_exp[cont]
            else:
                list_resp.append(sum)
                cont = 0
                sum = 0
                if v == '1':
                    sum += list_exp[cont]
            cont += 1
            if len(valor) == i+1 and sum != 0:
                list_resp.append(sum)
    elif base == 10:
        for i, v in enumerate(valor[::-1]):
            sum += int(v) * (2 ** i)
        list_resp.append(sum)
    elif base == 16:
        for i, v in enumerate(valor[::-1]):
            if i % 4 != 0 or i == 0:
                if v == '1':
                    sum += list_exp[cont]
            else:
                list_resp.append(sum)
                cont = 0
                sum = 0
                if v == '1':
                    sum += list_exp[cont]
            cont += 1
            if len(valor) == i+1 and sum != 0:
                list_resp.append(sum)
    else:
        # gera uma exceção caso a variavel 'base' seja diferente de 8, 10 ou 16
        raise Exception('The Base should be integer and equal to 8, 10, or 16')

    for i, v in enumerate(list_resp):
        if v > 9:
            list_resp.pop(i)
            list_resp.insert(i, letras_hexadecimais[v])
    for i, v in enumerate(list_resp[::-1]):
        print(v, end='')


def converte_octal(valor: str, base: int):
    """
    :param valor: recebe um valor octal
    :param base: recebe um valor igual a 2, 10 ou 16
    :return: retorna a conversão numérica de um valor octal para a base escolhida
    """
    sum = 0
    if '8' not in valor and '9' not in valor and valor.isdigit():
        if base == 2:
            for i, v in enumerate(valor[::-1]):
                sum += int(v) * (8 ** i)
            converte_decimal(sum, 2)
        elif base == 10:
            for i, v in enumerate(valor[::-1]):
                sum += int(v) * (8 ** i)
            print(sum)
        elif base == 16:
            for i, v in enumerate(valor[::-1]):
                sum += int(v) * (8 ** i)
            converte_decimal(sum, 16)
        else:
            # gera uma exceção caso a variavel base 'seja' diferente de 2, 10 ou 16
            raise Exception('The Base should be integer and equal to 2, 10, or 16')
    else:
        # gera uma exceção caso seja digitado um valor não octal
        raise Exception('Incorrect value')


def converte_hexadecimal(valor: str, base: int):
    """
    :param valor: recebe um valor hexadecimal
    :param base: recebe um valor igual a 2, 8 ou 10
    :return: retorna a conversão numérica de um valor octal para a base escolhida
    """

    letras_hexadecimais = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    sum = 0
    string = ''
    for i in valor:
        if i in '-' or i in 'GHIJKLMNOPQRSTUVXWYZ':
            # gera uma exceção caso seja inserido um valor não hexadecimal
            raise Exception('Invalid value')
    if base == 10:
        for i, v in enumerate(valor[::-1]):
            if v in 'ABCDEF':
                v = letras_hexadecimais[v]
            sum += int(v) * (16 ** i)
        return sum
    elif base == 2 or base == 8:
        divisor = 2
        if base == 8:
            divisor = 8
        v1 = converte_hexadecimal(valor, 10)
        while v1 > 0:
            digit = v1 % divisor
            string += str(digit)
            v1 //= divisor
        return string[::-1]
    else:
        # gera uma exceção caso a variavel base 'seja' diferente de 2, 8 ou 10
        raise Exception('The Base should be integer and equal to 2, 8, or 10')


