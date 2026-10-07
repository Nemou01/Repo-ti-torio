
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
def uw():
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

uw()
#pe()
#dsa_calcula_imc()
#quadrado()
#n()
#b()
