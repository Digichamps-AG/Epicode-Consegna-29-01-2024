#Analisi del tipo di ruolo mediamente meglio pagato
import pandas as pd 

#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente

#calcolo la media del salario per ogni tipo di lavoro
media_salario_posizione = dataset.groupby('job_title')['salary_in_usd'].mean().reset_index()

#calcolo il ruolo con lo stipendio mediamente meglio pagato
ruolo_piu_pagato = media_salario_posizione.loc[media_salario_posizione['salary_in_usd'].idxmax()]
print("Il ruolo piu' pagato è:")
print(ruolo_piu_pagato)
#Il ruolo mediamente più pagato è quello di Analytics Engineering Manager