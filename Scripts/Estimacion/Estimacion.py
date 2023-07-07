import sys
sys.path.append("Scripts")
from DatosCsv import ech
import pandas as pd
import scipy.stats as st

def estimarDesempleoTotal(datos : pd.DataFrame):
    desempleados_muestra = len(datos[(datos['Desempleo'] == 1)])
    pea_muestra = len(datos[(datos['PEA'] == 1)])
    
    tasa_desempleados_muestra = desempleados_muestra / pea_muestra

    pea_total = 1757161
    desempleo_total =  pea_total * tasa_desempleados_muestra

    return desempleo_total

def IntervaloDeConfianza(datos : pd.DataFrame):
    desempleo_total = estimarDesempleoTotal(datos)

    confianza = 0.95  
    grados_libertad = len(datos[(datos['PEA'] == 1)]) - 1
    error_estandar = st.sem(datos.query('PEA == 1')['Desempleo'])
    intervalo_confianza = st.t.interval(confianza, grados_libertad, loc=desempleo_total, scale=error_estandar)

    return intervalo_confianza

print(estimarDesempleoTotal(ech))
print(IntervaloDeConfianza(ech))