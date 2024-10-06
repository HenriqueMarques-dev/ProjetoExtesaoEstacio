from utils import grafics
from typing import List, Dict, Any
import pandas as pd

# calculando o lucro total, o calculo é feito dentro de uma função. Na função recebemos 
# a tabela como argumento e somamos a coluna "value" e "expense", ao subtrair temos o lucro total. Retorna um dicionário com o valor total, valor de gasto total e o valor de lucro formatados

def getProfit(table: pd.DataFrame) -> Dict[str, int]:
    totalRevenue: int = table["value"].sum()

    totalSpent: int = table["expense"].sum()

    totalProfit: int = totalRevenue - totalSpent

    results:Dict[str, int] = {
        "totalRevenue": totalRevenue,
        "totalSpent": totalSpent,
        "totalProfit" : totalProfit
    }

    return results

#Função para pegar a porcentagem de cada método de pagamento. Retorna uma lista com a quantidade que cada método foi usado.

def getPaymentMethod(table: pd.DataFrame) -> List[int]: 
    paymentCounts = table["payment"].value_counts()
    methods: List[int] = [
        paymentCounts["Pix"],
        paymentCounts["Cartão"],
        paymentCounts["Dinheiro"],
    ]
    return methods

#função para pegar o numero de visitantes e o visitante com mais frequencia

def getVisitors(table: pd.DataFrame)-> Dict[str, int | str]: 
    #Numero total de visitantes
    visitors: int = table["id"].nunique()

    #id com maior frequencia
    mostFrequentVisitor: int | str = table["id"].value_counts().idxmax()
    
    #nome associado a esse id
    mostFrequentVisitorName: str = table[table["id"] == mostFrequentVisitor]["client"].iloc[0]
    
    # frequencia desse visitante
    frequency: int = int(table["id"].value_counts().max())
    
    result: Dict[str, int | str] = {
        "visitors": visitors,
        "frequentVisitorName" : mostFrequentVisitorName,
        "frequency": frequency
    }

    return result


# Função para imprimir o resumo da análise e transformar em um arquivo txt além de criar os graficos

def resume(table: pd.DataFrame, values: Dict[str, int], visits: Dict[str, Any], txtFile: str) -> None: 
    totalRevenue: float = values["totalRevenue"]
    totalSpent: float = values["totalSpent"]
    totalProfit: float = values["totalProfit"]

    visitors: int = visits["visitors"]
    frequentVisitorName: str = visits["frequentVisitorName"]
    frequency: int = visits["frequency"]

    response: Dict[str, str | int] = {
        "Total de Serviços": f'R${totalRevenue:.2f}',
        "Total de Despesas": f'R${totalSpent:.2f}',
        "Lucro": f'R${totalProfit:.2f}',
        "Visitantes Totais": visitors,
        "Visitante Frequente": frequentVisitorName,
        "Resumo": f"O valor total de serviços é de R${totalRevenue:.2f}, com um gasto de R${totalSpent:.2f}. Gerando um lucro de R${totalProfit:.2f}. O comércio teve um total de {visitors} visitantes, o cliente com mais serviços feitos se chama {frequentVisitorName} e conta com {frequency} visitas."
    }

    with open(txtFile, "w") as file: 
        for key, value in response.items():
            file.write(f'{key}: {value}\n')
    
    paymentMethods: List[int] = getPaymentMethod(table)
    print(paymentMethods)
    grafics.percentagePayments(paymentMethods)
    grafics.clientFrequency(table)
                