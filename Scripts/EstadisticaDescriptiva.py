import pandas as pd
import numpy as np
import seaborn as sns
import researchpy as rp
import scipy.stats as st
from scipy.stats import f_oneway
from scipy.stats import ttest_ind

names = ['ID', 'anio', 'mes', 'Sexo', 'Edad', 'region','PEA','Desempleo','Salario']
url = "Datos\ECH_2022 - BD Proyecto Final PyE 2023.csv"
ech = pd.read_csv(url, names=names, delimiter=";",skiprows=1)
print(ech.head())
