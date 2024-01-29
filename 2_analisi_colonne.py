#Analisi delle colonne singole (testuali) più interessanti
import pandas as pd 
import matplotlib.pyplot as plt
#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"


#importo il file con pandas
dataset = pd.read_csv(file)

#calcolo quali sono i lavori più frequenti (data analyst? data engineer? ecc)
#il metodo .value_counts() mi ordina anche già i risultati in ordine crescente
tipo_di_lavoro = dataset['job_title'].value_counts()
print(tipo_di_lavoro.head(5))
#i 5 lavori più frequenti sono, in ordine:
# Data Engineer, Data Scientist, Data Analyst, Analytics Engineer


#calcolo quali sono i tipi di impiego (full-time, parti-time, ecc) più frequenti
tipo_di_impiego = dataset['employment_type'].value_counts()
print(tipo_di_impiego)
#la stragrande maggioranza dei lavoratori sono full-time


#calcolo quali sono i tipi di presenza (remoto, online, ibrido) più frequenti
tipo_di_presenza = dataset['work_models'].value_counts()
print(tipo_di_presenza)
#la maggior parte dei lavoratori è in presenza (on-site)


#creo un grafico a barre dei lavori più frequenti
plt.bar(tipo_di_lavoro.head(5).index, 
        tipo_di_lavoro.head(5).values)
plt.xlabel('Lavori')
plt.ylabel('Frequenza')
plt.title('Tipi dei lavori più frequenti')
plt.xticks(rotation=90) #ruoto di 90° le etichette per renderle leggibili, altrimenti si sovrappongono
plt.show()

#creo un grafico a barre per i tipi di impiego più frequenti
plt.bar(tipo_di_impiego.index, 
        tipo_di_impiego.values,
        color = "r")
plt.title('Tipi di impiego più frequenti')
plt.xlabel('Tipi di impiego')
plt.ylabel('Frequenza')
plt.show()

#creo un grafico a barre per i tipi di presenza più frequenti
plt.bar(tipo_di_presenza.index, 
        tipo_di_presenza.values,
        color = "g")
plt.title('Tipi di presenza più frequenti')
plt.xlabel('Tipi di presenza')
plt.ylabel('Frequenza')
plt.show()