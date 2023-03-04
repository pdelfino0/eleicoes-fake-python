
cid = "PORTO ALEGRE"
vagas = 36

partidos = {}
votos = {}
totalGeral = 0

with open("sampledata/eleicoes-fake.csv") as csv:
    csv.readline()
    for linha in csv:
        dados = linha[:-1].split(",")
        aux = {'nome': dados[1], 'votos':  0, 'vagas': 0, 'media': 0}
        partidos[dados[0]] = aux

with open("sampledata/eleicoes-municipais-fake.csv") as csv:
    csv.readline()
    for linha in csv:
        dados = linha[:-1].split(",")
        cidade = dados[1]
        sigla = dados[2]
        cargo = dados[3]
        nome = dados[4]
        totalDeVotos = int(dados[5])
        if cidade != cid or cargo != "VEREADOR":
            continue
        if nome not in votos:
            votos[nome] = {"sigla": sigla, "votos": 0}
        votos[nome]["votos"] += totalDeVotos
        partidos[sigla]["votos"] += totalDeVotos
        totalGeral += totalDeVotos

qe = totalGeral // vagas
print(f"Total geral de votos: {totalGeral}")
print(f"Vagas: {vagas}")
print(f"QE: {qe}")

somaVagas = 0

for sigla, dados in partidos.items():
    qp = dados['votos'] // qe
    if qp> 0:
        dados['vagas'] = qp
        somaVagas += qp

print()
print(f"Total de vagas já ocupadas: {somaVagas} ")
print()

for siglas, dados in partidos.items():
    me = dados['votos']/(dados['vagas'] + 1)
    dados['media'] = me
    print(sigla, dados)

for sigla, dados in sorted(partidos.items(), key=lambda x:x[1]['media'], reverse=True):
    if somaVagas< vagas:    
        dados['vagas'] += 1
        somaVagas +=1 

print()
print(f"Total de vagas ocupadas: {somaVagas}")
print()

salvaVagas = {}
for p in partidos:
    salvaVagas[p] = partidos[p]['vagas']

for nome, dados in sorted(votos.items(), key=lambda x: x[1]['votos'],reverse=True):
    sigla = dados['sigla']
    if partidos[sigla]['vagas'] > 0:
         print(sigla, nome, dados)
         partidos[sigla]['vagas'] -= 1


print()
print(salvaVagas)

totalFinalVagas = 0
nomes = []
valores = []
for p in salvaVagas:
    if salvaVagas[p]> 0:
        nomes.append(p)
        valores.append(salvaVagas[p])


import matplotlib.pylab as plt

plt.figure(figsize=(10,4))
plt.xticks(rotation= 30, ha='right')
plt.bar(nomes,valores)
plt.show()
         


