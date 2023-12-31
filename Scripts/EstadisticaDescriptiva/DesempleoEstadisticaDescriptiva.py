import matplotlib.pyplot as plt
import sys
sys.path.append("Scripts")
from DatosCsv import ech

def calcularTasaDesempleo(personasDesempleadas,PEA):
    return round((personasDesempleadas / PEA),4)

def graficarTasaDesempleo():
    totalPersonasRango1 = len(ech.query('Edad>=14 & Edad<=17')['Edad'])
    desempleadas1 = len(ech.query('Edad>=14 & Edad<=17')[ech['Desempleo']== 1])
    valor1 = calcularTasaDesempleo(desempleadas1,totalPersonasRango1)

    totalPersonasRango2 = len(ech.query('Edad>=18 & Edad<=25')['Edad'])
    desempleadas2 = len(ech.query('Edad>=18 & Edad<=25')[ech['Desempleo']== 1])
    valor2 = calcularTasaDesempleo(desempleadas2,totalPersonasRango2)

    totalPersonasRango3 = len(ech.query('Edad>=26 & Edad<=40')['Edad'])
    desempleadas3 = len(ech.query('Edad>=26 & Edad<=40')[ech['Desempleo']== 1])
    valor3 = calcularTasaDesempleo(desempleadas3,totalPersonasRango3)

    totalPersonasRango4 = len(ech.query('Edad>40')['Edad'])
    desempleadas4 = len(ech.query('Edad>40')[ech['Desempleo']== 1])
    valor4 = calcularTasaDesempleo(desempleadas4,totalPersonasRango4)
    
    plt.suptitle("Tasa de desempleo por rango de edad")
    ejeX = ["Entre 14 y 17","Entre 18 y 25","Entre 26 y 40","Mayores de 40"]
    ejeY = [valor1,valor2,valor3,valor4]
    plt.subplot().bar(ejeX,ejeY)
    plt.show()

graficarTasaDesempleo()
print("La tasa de desempleo en el uruguay es: "+str(calcularTasaDesempleo(len(ech[ech['Desempleo'] == 1]),len(ech[ech['PEA'] == 1]))))