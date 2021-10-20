def test_get_oglindit():
    assert get_oglindit(-31) == -31
    assert get_oglindit(1234) == 4321
    assert get_oglindit(0) == 0
    assert get_oglindit(2) == 2


def test_verifica_element_divide_lista():
    assert verifica_element_divide_lista(12, [1, 2, 3, 4]) is True
    assert verifica_element_divide_lista(23, [1, 3, 23]) is False
    assert verifica_element_divide_lista(14, [1, 2, 7, 0]) is False
    assert verifica_element_divide_lista(-21, [1, 3, 21, -21]) is True


def test_is_palindrom():
    assert is_palindrome("-22") is False
    assert is_palindrome('33') is True
    assert is_palindrome('0') is True
    assert is_palindrome('3') is True
    assert is_palindrome('121') is True
    assert is_palindrome('4334') is True


def test_lungime_multimi():
    assert lungime_multimi([1, 2, 3, 4, 5], [1, 2]) == 2
    assert lungime_multimi([-31, 21, 22], [14, 23, 21, -31, 22]) == 3
    assert lungime_multimi([], [1, 2, 3]) == 0


def test_nr_pare():
    assert nr_pare([1, 2, 3, 4]) == 2
    assert nr_pare([0, 1, 3, 5, 7]) == 1
    assert nr_pare([0, 2, 4, 8, 12]) == 5
    assert nr_pare([-12, 2, 33, 5]) == 2


def get_oglindit(numar):
    """
    Getter de oglindit al unui umar
    :param numar: numarul
    :return: oglinditul numarului sau numarul in sine daca este negativ
    """
    if numar < 0:
        return numar
    numar_str = str(numar)
    numar_str = numar_str[::-1]
    return int(numar_str)


def verifica_element_divide_lista(numar, lista_divizori):
    """
    Verifica daca un numar divide toate elementele unei multimi
    :param numar: numarul care este verificat
    :param lista_divizori: lista de divizori
    :return: True daca divide toate elementele, False in caz contrar
    """
    for i in lista_divizori:
        if i == 0:
            return False
        if numar % i != 0:
            return False
    return True


def mod_lista_oglindit(lista_1, lista_divizori):
    """
    Obtine o lista in care numerele sunt oglindite daca se impart la toate elementele dintr-o lista de divizori
    :param lista_1: lista data
    :param lista_divizori: lista cu divizori
    :return lista_finala: lista finala care are fie numere oglindite prin ea daca un element respecta conditia fie e
    aceeasi cu lista initiala
    """
    lista_finala = []
    for element in lista_1:
        if verifica_element_divide_lista(element, lista_divizori):
            oglindit = get_oglindit(element)
            lista_finala.append(oglindit)
        else:
            lista_finala.append(element)
    return lista_finala


def is_palindrome(element):
    """
    Verifica daca un numar este palindrom
    :param element: numarul verificat
    :return: True daca un numar este palindrom, False in caz contrar
    """
    if int(element) < 0:
        return False
    if element == element[::-1]:
        return True
    else:
        return False


def lungime_multimi(multime_1, multime_2):
    """
    Verifica care dintre doua multimi are mai putine elemente
    :param multime_1: prima multime/lista
    :param multime_2: a doua multime/lista
    :return: lungimea multimii cu mai putine elemente
    """
    if len(multime_1) < len(multime_2):
        return len(multime_1)
    else:
        return len(multime_2)


def palindroame_multimi(lista_1, lista_2):
    """
    Creeaza o lista cu palindroame obtinute prin concatenarea elementelor de pe aceleasi pozitii din doua liste
    :param lista_1: prima lista
    :param lista_2: a doua lista
    :return lista_palindroame: lista cu palindroamele
    """
    lungime = lungime_multimi(lista_1, lista_2)
    lista_palindroame = []
    for i in range(0, lungime):
        element = str(lista_1[i]) + str(lista_2[i])
        if is_palindrome(element):
            lista_palindroame.append(int(element))
    return lista_palindroame


def intersectie_multimi(lista_1, lista_2):
    """
    Creeaza o lista noua cu elementele comune din doua multimi
    :param lista_1: prima multime
    :param lista_2: a doua multime
    :return lista_intersectie: lista cu numerele comune
    """
    lista_intersectie = []
    for elemente_lista_1 in lista_1:
        for elemente_lista_2 in lista_2:
            if elemente_lista_1 == elemente_lista_2:
                lista_intersectie.append(elemente_lista_1)
    return lista_intersectie


def nr_pare(lista):
    """
    Verifica cate numere pare sunt intr-o lista
    :param lista: lista data
    :return nr_elemente_pare: numarul de elemente pare
    """
    nr_elemente_pare = 0
    for i in lista:
        if i % 2 == 0:
            nr_elemente_pare += 1
    return nr_elemente_pare


def citire_lista():
    """
    Citeste o lista
    :return: lista citita
    """
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(" ")

    for string_element in string_elemente:
        element = int(string_element)
        result_list.append(element)

    return result_list


def main():
    lista_1 = []
    lista_2 = []
    while True:
        print("""
1. Citire date
2. Afisare daca cele doua liste au acelasi numar de elemente pare
3. Afisare lista intersectie a doua multimi
4. Afisare multime palindroame obtinute prin concatenarea elementelor din lista de pe aceleasi pozitii
5. Afisare prima si a doua lista cu elemente inlocuite cu oglinditul lor 
   daca sunt divizibile cu toate elementele dintr-o lista citita de la tastatura
x. Iesire""")
        command = input("Introduceti comanda: ")
        if command == 'x':
            break
        elif command == '1':
            lista_1 = citire_lista()
            lista_2 = citire_lista()
        elif command == '2':
            if nr_pare(lista_1) == nr_pare(lista_2):
                print("Cele doua liste au acelasi numar de elemente pare")
            else:
                print("Cele doua liste NU au acelasi numar de elemente pare")
        elif command == '3':
            lista_intersectie = intersectie_multimi(lista_1, lista_2)
            if not lista_intersectie:
                print("Nu exista elemente comune in cele doua multimi")
            else:
                print(f'Elementele comune ale celor doua multimi sunt:{lista_intersectie}')
        elif command == '4':
            lista_palindroame = palindroame_multimi(lista_1, lista_2)
            if not lista_palindroame:
                print("Nu exista elemente care sa satisfaca cerinta")
            else:
                print(f'Palindroamele care satisfac cerinta sunt{lista_palindroame}')
        elif command == '5':
            lista_divizori = citire_lista()
            lista_1 = mod_lista_oglindit(lista_1, lista_divizori)
            lista_2 = mod_lista_oglindit(lista_2, lista_divizori)
            print(f"Listele sunt: {lista_1} si {lista_2}")
        else:
            print("Comanda invalida!")


test_is_palindrom()
test_nr_pare()
test_get_oglindit()
test_lungime_multimi()
test_verifica_element_divide_lista()
main()
