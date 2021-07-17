#importando a biblioteca Pandas
#import → Comando para importar; pandas → Nome da biblioteca; pd → Abreviação da biblioteca
import pandas as pd
#Importando o arquivo com os dados que serão utilizados na análise
a = pd.read_csv("C:/Users/User/OneDrive/Documentos/GitHub/Python/Arquivos desafio/datasets/"
                "Gapminder.csv", sep = ';')
#Renomeando as colunas
a = a.rename(columns={'country':'País','continent':'Continente','year':'Ano','lifeExp':'Expectativa de vida',
                  'pop':'População','gdpPercap':'PIB'})
#Total de linhas e Colunas
a.shape
#Mostra as colunas existentes
a.columns
#Mostra os tipos de cada coluna
a.dtypes
#Mostra as 5 últimas linhas
a.tail()
#Retorna informações estatísticas sobre o conjunto de dados, como média, mínimo, máximo, quartís, dentre outros
a.describe()
#Retorna valores únicos de uma coluna
a['Continente'].unique()
#Filtro de dados localizando termos específicos com o comando loc
Oceania = a.loc[a['Continente'] == 'Oceania']
#Agrupamento de países diferentes por continente; Quantos países diferentes existem na Asia? 41
a.groupby('Continente')['País'].nunique()
#Qual a expectativa média de cada ano?
a.groupby('Ano')['Expectativa de vida'].mean()
#Média de valores de uma coluna
a['PIB'].mean()
#Soma de valores de uma coluna
a['PIB'].sum()



