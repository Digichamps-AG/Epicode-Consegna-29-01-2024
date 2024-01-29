#Analisi per calcolare lo stipendio medio di ogni anno
import pandas as pd 
import matplotlib.pyplot as plt
#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente

#usando il metodo .groupby(), calcolo lo stipendio medio (in usd) per ogni anno
stipendio_medio_per_anno = dataset.groupby('work_year')['salary_in_usd'].mean()
print(stipendio_medio_per_anno)
#nel tempo c'è tendezialmente un incremento dei salari medi

#creo un grafico a linee per vedere l'andamento medio degli stipendi nel tempo
plt.plot(stipendio_medio_per_anno.index, 
         stipendio_medio_per_anno.values)
plt.title('Stipendio medio per anno')
plt.xlabel('Anno')
plt.ylabel('Stipendio medio in USD')
plt.show()