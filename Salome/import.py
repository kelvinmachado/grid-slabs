import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
import math

geompy = geomBuilder.New()

# Caminho dos arquivos
caminho_nos = r"C:/Users/kelvi/OneDrive/Documentos/1PERSONAL/4MASTER/UFSM/3SUBJECTS/Análise estrutural I/TRABALHO - GRELHA/Salome/nodes.txt"
caminho_barras = r"C:/Users/kelvi/OneDrive/Documentos/1PERSONAL/4MASTER/UFSM/3SUBJECTS/Análise estrutural I/TRABALHO - GRELHA/Salome/barras.txt"

# === 1. Lê os nós e cria pontos ===
pontos = []

with open(caminho_nos, "r") as f:
    linhas = f.readlines()

for linha in linhas:
    if not linha.strip():
        continue
    partes = linha.strip().split(",")
    if len(partes) < 3:
        continue
    try:
        x = float(partes[0])
        y = float(partes[1])
        z = float(partes[2])
        ponto = geompy.MakeVertex(x, y, z)
        pontos.append(ponto)
    except ValueError:
        continue

# === 2. Lê as barras e cria linhas ===
barras = []

with open(caminho_barras, "r") as f:
    linhas = f.readlines()

for linha in linhas:
    if not linha.strip():
        continue
    partes = linha.strip().split(",")
    if len(partes) < 3:
        continue
    try:
        id_barra = int(partes[0])
        i = int(partes[1]) - 1  # index começa em 0
        j = int(partes[2]) - 1
        linha_geom = geompy.MakeLineTwoPnt(pontos[i], pontos[j])
        barras.append(linha_geom)
    except Exception as e:
        print("Erro na barra:", linha, " ->", e)
        continue

# === 3. Adiciona ao estudo ===
grupo_pontos = geompy.MakeCompound(pontos)
grupo_barras = geompy.MakeCompound(barras)

geompy.addToStudy(grupo_pontos, "Nos_Importados")
geompy.addToStudy(grupo_barras, "Barras_Importadas")

for i, p in enumerate(pontos):
    geompy.addToStudyInFather(grupo_pontos, p, f"No_{i+1}")

for i, b in enumerate(barras):
    geompy.addToStudyInFather(grupo_barras, b, f"Barra_{i+1}")
