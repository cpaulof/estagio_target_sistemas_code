# obs: uma das formas mais simples é calcular todos os números de 
# fibonacci até N e checar se n pertence a lista. Porém esse método é lento pois é necessário
# calcular todos os elementos até N.
# 
# Outra forma de checar isso é baseado na formula de Binet, em que diz que se N é um número de fibonacci, então
# 5*N^2+4 ou 5*N^2-4 é um quadrado perfeito.

def eh_fibonacci(n):
    a = (5*n**2+4)**0.5 # calcula a raiz quadrada da formula acima
    b = (5*n**2-4)**0.5 # -
    return int(a) == a or int(b) == (b) # checa se a ou b é um quadrado perfeito.

EXEMPLOS = [1, 3, 17, 9, 34, 144, 1600] # exemplos para o teste da funcao.
# resultado esperado para cada elemento deve ser:
# 1 -> True
# 3 -> True
# 17 -> False
# 9 -> False
# 34 -> True
# 144 -> True
# 1600 -> False

for e in EXEMPLOS:
    print(e, '\t->', eh_fibonacci(e))
