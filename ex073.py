times =("Flamengo", "Palmeiras", "Atlético-MG", "Fortaleza", "Bragantino",
    "Corinthians", "Internacional", "Grêmio", "São Paulo", "Fluminense",
    "América-MG", "Ceará", "Athletico-PR", "Santos", "Atlético-GO",
    "Bahia", "Sport Recife", "Juventude", "Chapecoense", "Cuiabá")
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os últimos 4 são: {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1} na posição')