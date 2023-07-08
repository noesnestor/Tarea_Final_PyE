import sys
sys.path.append("Scripts")
from DatosCsv import ech
import pandas as pd
import scipy.stats as st


def estimarDesempleoTotal(datos : pd.DataFrame) -> float: #revisar

    suma_desempleados = len(datos[(datos['Desempleo'] == 1) & (datos['PEA'] == 1)])
    suma_pea = len(datos[(datos['PEA'] == 1)])

    desempleados_muestra = suma_desempleados / suma_pea

    pea_total = 1757161
    des_total =  pea_total * desempleados_muestra

    return des_total


estim = estimarDesempleoTotal(ech)

testT = st.ttest_1samp(0.0761, 0.07, alternative='greater')
print(testT.pvalue) # La diferencia es tan baja que scipy pierde precisión y otorga NaN

if testT.pvalue < 0.05:
    print("Con la muestra actual, podemos confirmar que la tasa de desempleo es mayor que lo que era en 2021.")
else:
    print("Con la muestra actual, no podemos confirmar que la tasa de desempleo es mayor que lo que era en 2021.")


