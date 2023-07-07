import sys
sys.path.append("Scripts")
from DatosCsv import ech
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts

def histograma_salarios():
    plt.title("Histograma Salarios")
    salarios_filtrados = ech.query('0<Salario<=100000')['Salario']
    plt.hist(salarios_filtrados)
    plt.show()

def boxplot_salarios():
    plt.title("Box-plot salarios totales")
    salarios = ech.query('0<Salario')['Salario']
    plt.boxplot(salarios,whis=350)
    plt.show()

    plt.title("Box-plot salarios masculinos y femeninos")
    salarios_masc = ech.query('Sexo == 1 & Salario>0')['Salario']
    salarios_fem = ech.query('Sexo == 2 & Salario>0')['Salario']
    plt.boxplot([salarios_masc,salarios_fem],whis=350,labels=["Masculino","Femenino"])
    plt.show()

    plt.title("Box-plot salarios de capital y del interior")
    salarios_capital = ech.query('region == 1 & Salario>0')['Salario']
    salarios_interior = ech.query('(region == 2 | region == 3) & Salario>0')['Salario']
    plt.boxplot([salarios_capital,salarios_interior],whis=350,labels=["Montevideo","Interior"])
    plt.show()

def estadisticas():
    salarios_filtrados = ech.query('0<Salario')['Salario']
    return {
            'Moda': sts.mode(salarios_filtrados, keepdims=False).mode,
            'Promedio': np.mean(salarios_filtrados),
            'Mínimo' : salarios_filtrados.min(),
            '1er Quartil': np.quantile(salarios_filtrados,0.25),
            'Mediana/2do Quartil': str(np.median(salarios_filtrados)),
            '3er Quartil': np.quantile(salarios_filtrados,0.75),
            'Máximo' : salarios_filtrados.max()
        }

histograma_salarios()
print(estadisticas())
boxplot_salarios()
