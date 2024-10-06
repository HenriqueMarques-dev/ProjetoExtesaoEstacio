import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict

plt.style.use('ggplot')

def percentagePayments(paymentsMethods: List[int]): 
    
    labels: List[str] = ['Pix', 'Dinheiro', 'Cartão']
    sizes: List[int] = [paymentsMethods[0], paymentsMethods[1], paymentsMethods[2]]

    fig, ax = plt.subplots()

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['green', 'red', 'orange'], 
        wedgeprops={"linewidth": 1, "edgecolor": "white"})
    fig.suptitle('Pagamentos')
    
    return plt.savefig('./result/paymentsGrafic.png')
  
  

def clientFrequency(table: pd.DataFrame): 
    data: Dict[str, int] = table["date"].value_counts().to_dict()

    date: List[str] = list(data.keys())
    frequency: List[int] = list(data.values())

    fig, ax = plt.subplots()

    ax.bar(date, frequency)
    fig.suptitle('Frequência de clientes / 2024')
    return plt.savefig('./result/frequencyGrafic.png')
    
    


