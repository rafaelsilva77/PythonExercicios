palavras = ("PROGRAMACAO", "PYTHON", "TUPLA", "LISTA", "DICIONARIO",
            "DADOS", "ESTRUTURA", "ALGORITMO", "COMPUTACAO", "LOGICA")

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end = ' ')