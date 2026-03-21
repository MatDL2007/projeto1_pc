import math
import random
import datetime
import statistics
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#entradas
capital = float(input('Capital Inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int (input('Prazo (meses): '))
cdi_anual = float (input ('Cdi Anual(%): ' ))/100
percentual_cdb = float(input ('Percental do CDI(%): '))/100
percentual_lci = float(input ('Percentual do LCI(%): '))/100
taxa_fii = float (input ('Rentabilidade Mensal do FII(%): '))/100
meta = float (input ('Meta financeira: (R$): '))

#conversãocdi
cdi_mensal = math.pow ((1+cdi_anual), 1/12) -1

#totalinvestido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * percentual_cdb
montante_cdb = (capital * math.pow ((1 + taxa_cdb), meses) + (aporte * meses ))
lucro_cdb = montante_cdb - total_investido 
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * percentual_lci
montante_lci = (capital * math.pow ((1 + taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow ((1+taxa_poupanca), meses) + (aporte * meses))

#FII - Simulações
simulacao1 = (capital * math.pow((1 + taxa_fii + random.uniform(-0.03,0.03)), meses) + (aporte * meses))
simulacao2 = (capital * math.pow((1 + taxa_fii + random.uniform(-0.03,0.03)), meses) + (aporte * meses))
simulacao3 = (capital * math.pow((1 + taxa_fii + random.uniform(-0.03,0.03)), meses) + (aporte * meses))
simulacao4 = (capital * math.pow((1 + taxa_fii + random.uniform(-0.03,0.03)), meses) + (aporte * meses))
simulacao5 = (capital * math.pow((1 + taxa_fii + random.uniform(-0.03,0.03)), meses) + (aporte * meses))


valoresFII = [simulacao1, simulacao2, simulacao3, simulacao4, simulacao5]

media_fii = statistics.mean(valoresFII)
mediana_fii = statistics.median (valoresFII)
desviopadrao_fii = statistics.stdev(valoresFII)

valorfinal_fii = media_fii


#Datas

datasimulacao = datetime.datetime.now()
diasresgate = meses * 30
dataresgate = datasimulacao + datetime.timedelta(days=diasresgate)

#MetaFinanceira

metaatingida = valorfinal_fii >= meta

#Formatação

capitalf = locale.currency(capital, grouping=True)
total_investidof = locale.currency(total_investido, grouping=True)

CDBF = locale.currency(montante_cdb_liquido, grouping=True)
LCIF = locale.currency(montante_lci, grouping=True)
poupancaF = locale.currency(montante_poupanca, grouping=True)
FIIF = locale.currency(valorfinal_fii, grouping=True)

media_fiif = locale.currency(media_fii, grouping=True)
mediana_fiif = locale.currency(mediana_fii, grouping=True)
desvio_fiif = locale.currency(desviopadrao_fii, grouping=True)

#GráficosASCII 

blocos_cdb = int(montante_cdb_liquido / 1000)
blocos_lci = int(montante_lci / 1000)
blocos_poupanca = int(montante_poupanca / 1000)
blocos_fii = int(valorfinal_fii / 1000)

grafico_cdb = "█" * blocos_cdb
grafico_lci = "█" * blocos_lci
grafico_poupanca = "█" * blocos_poupanca
grafico_fii = "█" * blocos_fii

#Relatório

print("\nRELATÓRIO FINAL")

print("\nData da simulação:", datasimulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", dataresgate.strftime("%d/%m/%Y"))

print("\nTotal investido:", total_investidof)

print("\nValores finais:")
print("CDB:", CDBF)
print("LCI:", LCIF)
print("Poupança:", poupancaF)
print("FII:", FIIF)

print("\nEstatísticas do FII:")
print("Média:", media_fiif)
print("Mediana:", mediana_fiif)
print("Desvio padrão:", desvio_fiif)

print("\nMeta financeira atingida:", metaatingida)

print("\nGRÁFICOS (cada bloco = R$1000)")

print("CDB:", grafico_cdb)
print("LCI:", grafico_lci)
print("Poupança:", grafico_poupanca)
print("FII:", grafico_fii)
