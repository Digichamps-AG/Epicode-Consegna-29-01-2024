#Analisi delle percentuali di tipo di presenza e tipo di impiego
import pandas as pd 
import matplotlib.pyplot as plt

#file = "./data_science_salaries.csv"
file = "https://raw.githubusercontent.com/Digichamps-AG/Epicode-Consegna-29-01-2024/main/data_science_salaries.csv"
#scrivo l'indirizzo del dataset da importare
#file = "./data_science_salaries.csv"

#importo il file con pandas
dataset = pd.read_csv(file) 
print(dataset) #testo se l'import è avvenuto correttamente

#calcolo le percentuali del tipo di presenza
tipo_di_presenza = dataset['work_models'].value_counts()
percentuali_tipo_presenza = [i for i in tipo_di_presenza/tipo_di_presenza.sum()*100]
#creo una lista con tutti i tipi di presenza sfruttando il metodo .unique()
lista_presenze = [i for i in dataset['work_models'].unique()]

#creo con pandas un dataframe che mostri le percentuali dei tipi di presenza
df_tipo_presenza = pd.DataFrame({'Percentuale Presenza': percentuali_tipo_presenza}, index=lista_presenze)
print(df_tipo_presenza)


#calcolo le percentuali dei tipi di impiego (full-time, part-time, ecc)
tipo_di_impiego = dataset['employment_type'].value_counts()
percentuali_tipo_impiego = [i for i in tipo_di_impiego/tipo_di_impiego.sum()*100]
#creo una lista con tutti i tipi di impiego sfruttando il metodo .unique()
lista_impiego = [i for i in dataset['employment_type'].unique()]

#creo con pandas un dataframe che mostri le percentuali dei tipi di impiego
df_tipo_impiego = pd.DataFrame({'Percentuale Impiego': percentuali_tipo_impiego}, index=lista_impiego)
print(df_tipo_impiego)


#Creo un grafico a torta per esprimere le percentuali dei tipi di presenza
plt.pie(df_tipo_presenza['Percentuale Presenza'], 
        labels=df_tipo_presenza.index)
plt.title('Percentuale di tipo di presenza')
plt.show()

#Creo un grafico a torta per esprimere le percentuali dei tipi di impiego
plt.pie(df_tipo_impiego['Percentuale Impiego'], 
        labels=df_tipo_impiego.index)
plt.title('Percentuale di tipo di presenza impiego')
plt.show()

