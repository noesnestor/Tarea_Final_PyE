import pandas as pd

names = ['ID', 'anio', 'mes', 'Sexo', 'Edad', 'region','PEA','Desempleo','Salario']
url = "Datos\ECH_2022 - BD Proyecto Final PyE 2023.csv"
ech_unfiltered = pd.read_csv(url, names=names, delimiter=";",skiprows=1)
ech_unfiltered["Salario"] = pd.to_numeric(ech_unfiltered["Salario"],'coerce')
ech = ech_unfiltered.dropna()