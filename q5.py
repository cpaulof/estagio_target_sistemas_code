texto1 = "abcde"
texto2 = "chocolate com pimenta"

def inverter_string(s):
    s = list(s)
    last_index = len(s)-1
    mid = len(s)//2

    # i -> inicio, k -> fim da string
    for i in range(mid):
        k = last_index - i
        # trocar as letras na posicao i e k
        temp = s[k]
        s[k] = s[i]
        s[i] = temp
    return ''.join(s)


print(inverter_string(texto1))
print(inverter_string(texto2))
