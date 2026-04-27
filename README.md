# Modelos Estruturais para Pavimentos - ECC840

Este repositório contém o trabalho acadêmico da disciplina **ECC840 – Análise Estrutural I**, do Programa de Pós-Graduação em Engenharia Civil e Ambiental da Universidade Federal de Santa Maria (UFSM).

## 📄 Sobre o Trabalho

O estudo aborda a análise de pavimentos em concreto armado utilizando diferentes métodos de modelagem estrutural:

- Modelos clássicos (tabelas de lajes)
- Modelos de grelha equivalente (Modelo 01 e Modelo 02)
- Análise matricial com softwares educacionais
- Modelagem por elementos finitos no **ANSYS** (elementos BEAM4 e BEAM188)

## 🎯 Objetivos

- Calcular momentos fletores (positivos e negativos) e flecha máxima de uma laje retangular armada em duas direções
- Calibrar os coeficientes `α1` e `α2` (relação entre inércia torcional e flexional) para equalizar resultados com as tabelas clássicas
- Comparar a influência da rigidez das vigas de contorno no comportamento estrutural

## 🧰 Ferramentas Utilizadas

| Ferramenta                     | Finalidade                          |
| ------------------------------ | ----------------------------------- |
| `Grelha_Molas_2009_GAUSS.exe`  | Análise matricial de grelhas (FORTRAN) |
| Mastan2                        | Análise matricial educacional       |
| ANSYS (Mechanical APDL)        | Análise por elementos finitos       |
| Tabelas de Pinheiro (2007)     | Referência clássica para lajes      |

## 📁 Estrutura do Repositório
.
├── APDL/ # Arquivos de entrada ANSYS APDL
│ ├── 1_grelha_M1_BEAM4_D.txt # Modelo 1 - BEAM4 (flecha)
│ ├── 1_grelha_M1_BEAM4_M.txt # Modelo 1 - BEAM4 (momento)
│ ├── 1_grelha_M1_BEAM4.txt # Modelo 1 - BEAM4 (sem calibração)
│ ├── 2_grelha_M2_BEAM4_D.txt # Modelo 2 - BEAM4 (flecha)
│ ├── 2_grelha_M2_BEAM4_M.txt # Modelo 2 - BEAM4 (momento)
│ ├── 2_grelha_M2_BEAM4.txt # Modelo 2 - BEAM4 (sem calibração)
│ ├── 3_grelha_M1_BEAM188-D.txt # Modelo 1 - BEAM188 (flecha)
│ ├── 3_grelha_M1_BEAM188-M.txt # Modelo 1 - BEAM188 (momento)
│ ├── 3_grelha_M1_BEAM188.txt # Modelo 1 - BEAM188 (sem calibração)
│ ├── 4_grelha_M2_BEAM188-D.txt # Modelo 2 - BEAM188 (flecha)
│ ├── 4_grelha_M2_BEAM188-M.txt # Modelo 2 - BEAM188 (momento)
│ ├── 4_grelha_M2_BEAM188.txt # Modelo 2 - BEAM188 (sem calibração)
│ ├── 5_grelha_M2_2_BEAM188_ASEC.txt # Modelo 2-2 - BEAM188 (seção arbitrária)
│ ├── 5_grelha_M2_2_BEAM188_REC.txt # Modelo 2-2 - BEAM188 (seção retangular)
│ ├── 5_grelha_M2_2_BEAM4_D.txt # Modelo 2-2 - BEAM4 (flecha)
│ ├── 5_grelha_M2_2_BEAM4_M.txt # Modelo 2-2 - BEAM4 (momento)
│ ├── 5_grelha_M2_2_BEAM4.txt # Modelo 2-2 - BEAM4 (sem calibração)
│ └── RESULTS/ # Resultados das simulações ANSYS
│ ├── MODELO 1 - BEAM188/
│ ├── MODELO 1 - BEAM4/
│ ├── MODELO 2-2 - BEAM188/
│ ├── MODELO 2-2 - BEAM4/
│ ├── MODELO 2-2 BEAM4 - D/
│ ├── MODELO 2-2 BEAM4-M/
│ ├── MODELO 2 - BEAM188/
│ └── MODELO 2 - BEAM4/
│
├── EXCEL/ # Planilhas com dados e cálculos
│ ├── MODELO01.xlsx
│ ├── MODELO02-02.xlsx
│ └── MODELO02.xlsx
│
├── GRELHA_MOLAS/ # Arquivos do software Grelha_Molas
│ ├── MODELO1/ # Modelo 1 (sem calibração)
│ ├── MODELO1_D/ # Modelo 1 calibrado por flecha
│ ├── MODELO1_M/ # Modelo 1 calibrado por momento
│ ├── MODELO2_1/ # Modelo 2 (sem calibração)
│ ├── MODELO2_1_D/ # Modelo 2 calibrado por flecha
│ ├── MODELO2_1_M/ # Modelo 2 calibrado por momento
│ ├── MODELO2_2/ # Modelo 2 com viga (sem calibração)
│ ├── MODELO2_2_D/ # Modelo 2 com viga calibrado por flecha
│ └── MODELO2_2_M/ # Modelo 2 com viga calibrado por momento
│
├── MASTAN2/ # Arquivos do software Mastan2
│ ├── grelha_M1_D.mat
│ ├── grelha_M1.mat
│ ├── grelha_M1_M.mat
│ ├── grelhaM2_2_D.mat
│ ├── grelhaM2_2.mat
│ ├── grelhaM2_2_M.mat
│ ├── grelha_M2_D.mat
│ ├── grelha_M2.mat
│ ├── grelha_M2_M.mat
│ └── results/ # Resultados das análises Mastan2
│ ├── results_M1_D.txt
│ ├── results_M1_M.txt
│ ├── results_M1.txt
│ ├── results_M2_2_D.txt
│ ├── results_M2_2_M.txt
│ ├── results_M2_2.txt
│ └── results_M2.txt
│
├── Salome/ # Arquivos do software Salome
│ ├── barras.txt
│ ├── grelha-m1_Files/
│ ├── grelha-m1.hdf
│ ├── import.py
│ ├── mesh.med
│ └── nodes.txt
│
├── NOMENCLATURA.txt # Convenções de nomenclatura utilizadas
├── TRABALHO_01_ECC840_2025_01-REV02.pdf # Relatório completo do trabalho
├── README.md # Este arquivo
└── .gitignore # Arquivos e pastas ignorados pelo Git


## 📊 Resumo dos Resultados

### Deslocamentos máximos (cm)

| Modelo                 | Tabelas Clássicas | BEAM4 | BEAM188 |
| ---------------------- | ----------------- | ----- | ------- |
| Modelo 01              | 0,179             | 0,196 | 0,180   |
| Modelo 02              | 0,179             | 0,189 | 0,169   |
| Modelo 02 com viga     | 0,179             | 0,156 | 0,156   |

### Momentos fletores máximos (kN.m/m)

| Modelo                 | Tabelas Clássicas | BEAM4 | BEAM188 |
| ---------------------- | ----------------- | ----- | ------- |
| Modelo 01              | 8,65              | 9,19  | 8,35    |
| Modelo 02              | 8,65              | 8,90  | 7,89    |
| Modelo 02 com viga     | 8,65              | 7,60  | 7,58    |

## 🔧 Coeficientes Calibrados (BEAM4)

| Coeficiente | Modelo 01 | Modelo 02 |
| ----------- | --------- | --------- |
| α1 (flecha) | 2,87      | 2,44      |
| α2 (momento)| 2,53      | 2,21      |

## 📌 Principais Conclusões

- Os modelos de grelha equivalente apresentaram boa aderência aos resultados clássicos após calibração (diferenças < 1% com BEAM188)
- A inclusão das vigas de contorno reduziu deslocamentos em até 15% e momentos em até 17%
- O elemento BEAM188 mostrou-se mais preciso que o BEAM4 para esta aplicação
- A calibração dos coeficientes de torção é fundamental para a qualidade dos resultados

## 👥 Autores

- Alencar M. Schuster
- Kelvin D. Machado
- Pedro G. Nascimento
- Pedro V. Almeida

## 📅 Período

1º semestre de 2025 – Santa Maria, RS

## 📚 Bibliografia Consultada

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6118**: Projeto de estruturas de concreto. Rio de Janeiro, 2024.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6120**: Ações para o cálculo de estruturas de edificações. Rio de Janeiro, 2019.
- ANSYS, INC. **Element Reference**. Canonsburg, 2009.
- ANSYS, INC. **ANSYS Mechanical APDL Command Reference**. Canonsburg, 2009.
- MCGUIRE, W.; GALLAGHER, R. H.; ZIEMIAN, R. D. **Matrix Structural Analysis**. North Charleston, 2015.
- PINHEIRO, L. M. **Tabelas de lajes**. Apostila. Universidade de São Paulo. São Carlos, 2007.

---

**Nota:** Este repositório contém o PDF do trabalho completo. Os arquivos de entrada dos softwares podem ser adicionados conforme necessidade.