'''
prob 1-numar prim
'''


def is_prime(nr):
    e_prim = 1
    for i in range(2, nr // 2 + 1):
        if nr % i == 0 or nr == 1 or nr == 0:
            return False
            e_prim = 0

    if e_prim:
        return True


'''
prob 2-produsul a n numere
'''


def get_product(lst):
    p = 1
    for i in lst:
        p = p * lst [ i ]
    return p


'''
prob 3-cmmdc
'''


def get_cmmdc(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def read_list():
    given = input("Dati numere separate prin virgula:")
    int_list = given.split(',')
    list = [ ]
    for int_lst in int_list:
        list.append(int(int_lst))
    return list

def print_menu():
    print('1.Citirea unei liste.')
    print('2.numar prim(prob 1)')
    print('3.produsul a n numere(prob 2)')
    print('4.cmmdc(prob 3)')

def main():
    lst = []
    while True:
        print_menu()
        op = input("Alegeti o optiune: ")
        if op=='1':
            lst= read_list()
        if op == '2':
            n = int(input("n = "))
            print(is_prime(n))
        if op == '3':
            print(get_product(lst))
        if op == '4':
            a = int(input("a = "))
            b = int(input("b = "))
            print(get_cmmdc(a, b))

main()