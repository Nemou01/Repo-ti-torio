
def b():
    a = int(input("de um numero "))
    for i in range(1,11):
        print(a*i)

def n():
    a = [{"nome": "beatriz", "nota": 6}, {"nome": "joao", "nota": 3}, {"nome": "maria", "nota": 9}, {"nome": "pedro", "nota": 5}]
    for i in range(len(a)):
        if a[i]["nota"] >= 7:
            print(a[i]["nome"], "aprovado")
        else:
            print(a[i]["nome"], "reprovado")
def quadrado():
    a = [1,2,3,4,5,6,7,8,9,10]
    for i in a:
        print(i**2)
def dsa_calcula_imc():
    p = float(input("seu peso "))  
    a = float(input("sua altura "))
    print(f"seu imc é {p/(a**2):.2f}")
def pe():
    pessoas = [
            {"idade": 22, "nome": "beatriz"},
            {"idade": 25, "nome": "joao"},
            {"idade": 30, "nome": "maria"},
            {"idade": 35, "nome": "pedro"},
            {"idade": 14, "nome": "ana"},
            {"idade": 57, "nome": "carlos"}
        ]
    ordem = sorted(pessoas, key=lambda u: u['idade'])
    print(ordem)

import random
def uwu():
    a =[]
    n = []
    r=[]
    for i in range(10):
        b = random.randint(1,100)
        if b%2 ==0:
            n.append(b)
        else:
            a.append(b)
        r.append(b)
    print(len(n),"pares")
    print(len(a),"impares")
    print(r)

def ol():
    x = str(input("Python é oq?"))
    x = x.upper()
    print(x,"PYTHON")

def jogo():
    import random
    a = random.randint(1,21)
    i = 0
    while  i != 5:
        b = int(input("adivinhe um numeo de 1 a 20 lil bro"))
        
        if b < a:
            print("e maior lil bro")
        elif b > a:
            print("Its little")
        else:
            print("na mosca")
            break
        i+=1
        print(f"tentativa {i} de 5")

def trinaguloguloso():
    a = int(input("lado 1 "))
    b = int(input("lado 2 "))
    c = int(input("lado 3 "))
    if a == b and b == c:
        print("equilatero")
    elif a == b or b == c or a == c:
        print("isoceles")
    else:
        print("escaleno")


def gmail():
    a = [
        "lanadelrei@gmail.com",
        "flavio2026@hotmail.com",
        "lulalindinhodebunito@gmail.com"
    ]
    pe= "@gmail.com"
    re = [p for p in a if p.endswith(pe)]
    return print(re)
print("a")
#gmail()
#trinaguloguloso()
#jogo()
#ol()
#uwu()
#pe()
#dsa_calcula_imc()
#quadrado()
#n()
#b()
