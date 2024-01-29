#Analisi dello stipendio di un Data Engineer (DE)
import pandas as pd 
import matplotlib.pyplot as plt
#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente

#credo un nuovo dataset per fare dei calcoli solo sul Data Engineer(DE), cioè il lavoro con più occupazione
dataset_de = dataset[dataset['job_title'] == 'Data Engineer'][['job_title', 'work_year', "salary_in_usd", "company_location"]]


#calcolo lo stipendio medio del DE per anno
stipendio_medio_per_anno = dataset_de.groupby('work_year')['salary_in_usd'].mean()
print(stipendio_medio_per_anno)

#calcolo lo stipendio medio del DE per luogo dell'azienda, per capire che zone sono più profittevoli per un DE
#e lo faccio per il 2023, per vedere come sono gli stipendi dell'ultimo anno

#creo un nuovo dataset filtrando per lavoro (DE) e anno (2023)
dataset_de = dataset[(dataset["job_title"] == "Data Engineer") & (dataset["work_year"]==2023)]
#ora calcolo lo stipendio medio per luogo dell'azienda
stipendio_medio_per_luogo = dataset_de.groupby('company_location')['salary_in_usd'].mean()
#ordino gli stipendi medi in ordine discendente
stipendio_per_luogo_ordinato = stipendio_medio_per_luogo.sort_values(ascending=False)
#stampo i primi 10 valori, per conoscere le prime 10 location
#in cui i DE prendono gli stipendi medi maggiori
print(stipendio_per_luogo_ordinato.head(10))

#creo un grafico a barre per vedere la distribuzione media degli stipendi
#dei DE nel 2023 per ogni area geografica
plt.bar(stipendio_per_luogo_ordinato.index, 
        stipendio_per_luogo_ordinato.values)
plt.xticks(rotation=90) #ruoto le etichette sull'asse delle X di 90° per poterle leggere
plt.xlabel('Paese compagnia')
plt.ylabel('Salario in USD')
plt.title('Salario medio del DE per luogo della compagnia (2023)')
plt.show()