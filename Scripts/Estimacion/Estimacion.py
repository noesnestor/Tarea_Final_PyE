import sys
sys.path.append("Scripts")
from DatosCsv import ech
import pandas as pd
import scipy.stats as st
import math

def estimarDesempleoTotal(datos : pd.DataFrame):
    desempleados_muestra = len(datos[(datos['Desempleo'] == 1)])
    pea_muestra = len(datos[(datos['PEA'] == 1)])
    
    tasa_desempleados_muestra = desempleados_muestra / pea_muestra

    pea_total = 1757161
    desempleo_total =  pea_total * tasa_desempleados_muestra

    return desempleo_total

def IntervaloDeConfianza(datos : pd.DataFrame):
    desempleo_total = estimarDesempleoTotal(datos)
    desempleados_muestra = len(datos[(datos['Desempleo'] == 1)])
    pea_muestra = len(datos[(datos['PEA'] == 1)])
    
    tasa_desempleados_muestra = desempleados_muestra / pea_muestra

    confianza = 0.95
    error_estandar = math.sqrt((tasa_desempleados_muestra * (1 - tasa_desempleados_muestra)) / pea_muestra)
    intervalo_confianza = st.norm.interval(confianza, loc=desempleo_total, scale=error_estandar)

    return intervalo_confianza

print("El desempleo total es: "+str(estimarDesempleoTotal(ech)))
print("Los valores del Intervalo de confianza con certeza del 95 porciento: "+str(IntervaloDeConfianza(ech)))