dados = [
    ('SP', 67836.43),
    ('RJ', 36678.66),
    ('MG', 29229.88),
    ('ES', 27165.48),
    ('Outros', 19849.53)]

total = 0

for _, valor in dados:
    total += valor

for estado, valor in dados:
    percentual = valor/total*100
    print(f'{estado}\t-> {percentual:.2f}%')



# saida
# SP      -> 37.53%
# RJ      -> 20.29%
# MG      -> 16.17%
# ES      -> 15.03%
# Outros  -> 10.98%