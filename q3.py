# OBS. O SITE NAO DISPONIBILIZOU DADOS ENTAO CRIEI ALEATORIAMENTE
# Dado um vetor que guarda o valor de
# faturamento diário de uma distribuidora

# 30 dias
# 0 sao finais de semana o feriados
FATURAMENTO = [10527.8, 48579.07, 49787.5, 44176.61, 44432.24, 0, 0, 
               39831.84, 10950.16, 34845.97, 15068.99, 31488.34, 0, 0, 
               44389.92, 0, 32030.28, 47219.69, 23282.5, 0, 0, 
               24121.13, 46331.35, 38784.38, 0, 25629.51, 0, 0, 
               42686.76, 45198.53]

def obter_dias_uteis(mes):
    return len(mes) - mes.count(0)

dias_uteis = obter_dias_uteis(FATURAMENTO)

print('Dias úteis ->', dias_uteis)

min_valor_mensal = max(FATURAMENTO)
max_valor_mensal = max(FATURAMENTO)
media_mensal = sum(FATURAMENTO)/dias_uteis

dias_gt_media = 0

for valor in FATURAMENTO:
    if valor == 0: continue
    if valor < min_valor_mensal:
        min_valor_mensal = valor
    if valor > media_mensal:
        dias_gt_media+=1

print('O menor valor de faturamento ocorrido em um dia do mês =', min_valor_mensal)
print('O maior valor de faturamento ocorrido em um dia do mês =', max_valor_mensal)
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal =', dias_gt_media)

