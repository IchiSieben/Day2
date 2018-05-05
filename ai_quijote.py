archivo = open('quijote.txt')
contenido = archivo.read().lower().split()
archivo.close()

# {'a': 100, 'b': 333, 'c':...}

palabras = {}
c
for palabra in contenido:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1

for palabra, cantidad in palabras.items():
    print('letra: {} cantidad: {}'.format(palabra, cantidad))