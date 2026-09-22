# Day2

Coursework from an introductory Python class (~2018): a loose collection of standalone
scripts, not a single application. Includes Fizz-Buzz, basic function/lambda examples, a
letter-frequency counter and a simple Markov-chain word generator, both run against the
bundled `quijote.txt`. Some files (`calculos.py`, `carro.py`) are unfinished/broken —
left as-is, since this is class practice, not production code.

## How to run

Requires Python 3. Each script is standalone:

```
python fizz_buzz.py        # works
python ai_quijote.py        # works, prints word frequency
python markov.py            # works interactively, prompts for a starting word
python functions.py         # works
python calculos.py          # broken: NameError on undefined PI (left unfixed, coursework)
python carro.py             # broken: .format() called on print()'s return value (left unfixed)
```

Verified against Python 3.12 on 2026-09-22.

## Author

Yoichi Palacios Tanaka (IchiSieben) · ichisieben.dev

## Licence

Apache-2.0 (see `LICENSE`).

## Español

Ejercicios de un curso introductorio de Python (~2018): una colección de scripts sueltos,
no una sola aplicación. Incluye Fizz-Buzz, ejemplos básicos de funciones/lambdas, un
contador de frecuencia de letras y un generador de texto por cadenas de Markov, ambos
sobre el `quijote.txt` incluido. Algunos archivos (`calculos.py`, `carro.py`) quedaron
incompletos o rotos — se dejan tal cual, por ser práctica de clase y no código de producción.

### Cómo correrlo

Requiere Python 3. Cada script es independiente:

```
python fizz_buzz.py        # funciona
python ai_quijote.py        # funciona, imprime frecuencia de palabras
python markov.py            # funciona en modo interactivo, pide una palabra inicial
python functions.py         # funciona
python calculos.py          # roto: NameError por PI sin definir (se deja sin corregir)
python carro.py             # roto: .format() sobre el valor de retorno de print() (se deja sin corregir)
```

Verificado con Python 3.12 el 2026-09-22.

### Autor

Yoichi Palacios Tanaka (IchiSieben) · ichisieben.dev

### Licencia

Apache-2.0 (ver `LICENSE`).
