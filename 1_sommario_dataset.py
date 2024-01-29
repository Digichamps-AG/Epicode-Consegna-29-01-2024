#Analisi base del dataset scelto
import pandas as pd 

#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"

file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente



#creo un sommario delle colonne numeriche del dataset (escluso l'anno, per cui non avrebbe senso)
sommario_dataset = dataset[["salary", "salary_in_usd"]].describe()
print(sommario_dataset)

#aggiungo la moda, visto che .describe() non la calcola
moda = dataset[["salary", "salary_in_usd"]].mode()
print(moda)



