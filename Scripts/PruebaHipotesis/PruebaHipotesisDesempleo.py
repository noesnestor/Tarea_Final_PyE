import scipy.stats as st

testT = st.ttest_1samp(0.0761, 0.07, alternative='greater')
print(testT.pvalue) # La diferencia es tan baja que scipy pierde precisión y otorga NaN

if testT.pvalue < 0.05:
    print("Con la muestra actual, podemos confirmar que la tasa de desempleo es mayor que lo que era en 2021.")
else:
    print("Con la muestra actual, no podemos confirmar que la tasa de desempleo es mayor que lo que era en 2021.")


