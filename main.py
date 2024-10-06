import pandas as pd
from utils import data


# Adicionando a tabela a uma váriavel

table: pd.DataFrame = pd.read_excel("./table/clients.xlsx")

#formatando a coluna de datas caso ela não esteja formatada


table['date'] = pd.to_datetime(table['date'], format='%d-%m/Y', yearfirst=False)


# Removendo possíveis linhas vazias

table: pd.DataFrame = table.dropna()

#chamando a função resume
data.resume(table, data.getProfit(table), data.getVisitors(table), "./result/resume.txt")

