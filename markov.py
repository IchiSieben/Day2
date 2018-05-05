import random
file =open ("quijote.txt",'r')
content = file.read().lower()
file.close()


content = content.replace('\n', ' ').replace('   ', ' ').replace('.','').replace(',','').replace(';','').replace('   ',' ').replace('  ', ' ').split()

palabras = {}

for posicion, palabra in enumerate (content[:-1]):

    if palabra not in palabras:

        palabras[palabra]=[]

    palabras[palabra].append(content[posicion + 1])


palabra_inicial = input("escribe una plabra: ")

oracion = [palabra_inicial]

for _ in range(15):
    ultima_palabra=oracion[-1]
    siguiente_palabra = random.choice(palabras[ultima_palabra])
    oracion.append((siguiente_palabra))
print(" ".join(oracion))