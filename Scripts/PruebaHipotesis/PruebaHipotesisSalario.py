import sys
sys.path.append("Scripts")
from DatosCsv import ech
import pandas as pd
import researchpy as rp


testRtable, testRres = rp.ttest(group1=ech[ech['Sexo'] == 1]['Salario'], group2=ech[ech['Sexo'] == 2]['Salario'],group1_name="Hombres", group2_name="Mujeres")

print(testRres)
p_value = testRres.values[3][1]

if p_value < 0.01:
    print("Con la muestra actual, podemos confirmar que la diferencia de salarios entre hombres y mujeres es significativa")
else:
    print("Con la muestra actual, no podemos confirmar que la diferencia de salarios entre hombres y mujeres es significativa")
