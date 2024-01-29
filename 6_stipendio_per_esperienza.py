#Analisi dello stipendio medio per esperienza di lavoro
import pandas as pd 
import matplotlib.pyplot as plt
#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file)
print(dataset) #testo se l'import è avvenuto correttamente

#calcolo il salario in base al livello di esperienza
salario_esperienza = dataset.groupby('experience_level')['salary_in_usd'].mean().reset_index() #.reset_index() permette di avere come nomi delle colonne quelli originali
#ordino in senso discendente il salario per esperienza
salario_esperienza_ordinato = salario_esperienza.sort_values(by="salary_in_usd", ascending=False)
print(salario_esperienza_ordinato)
#come prevedibile, a livelli di esperienza maggiori corrispondono salari maggiori

#Grafico a barre del salario in base all'esperienza
plt.bar(salario_esperienza_ordinato['experience_level'], 
        salario_esperienza_ordinato['salary_in_usd'])
plt.title('Salario per esperienza')
plt.xlabel('Livello di esperienza')
plt.ylabel('Salario in USD')
plt.xticks(rotation=90)
plt.show()

