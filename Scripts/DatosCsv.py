names = ['ID', 'anio', 'mes', 'Sexo', 'Edad', 'region','PEA','Desempleo','Salario']
url = "Datos\ECH_2022 - BD Proyecto Final PyE 2023.csv"
ech = pd.read_csv(url, names=names, delimiter=";",skiprows=1)