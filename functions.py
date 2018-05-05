def suma1 (a: int, b:int)-> int:
    return a+b

print (suma1(2,5))
print (suma1("holo","5"))
help(suma1)

suma2 = lambda x ,y : x+y
print (suma2(2,3))

def suma3 (*numeros):
    return numeros

print (suma3(1,2,3,4))
print (suma1(b=3,a=2))

sumandos = [6,7]
print (suma1(*sumandos))


def suma4 (**numeros):
    print (numeros)

suma4(a=1,b=2,c=3,d=4)