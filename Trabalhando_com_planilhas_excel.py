#Importando a biblioteca pandas
import pandas as pd
#Carrega um arquivo e o atribui a uma variável
a = pd.read_excel('C:/Users/User/Python/datasets/Aracaju.xlsx')
b = pd.read_excel('C:/Users/User/Python/datasets/Fortaleza.xlsx')
c = pd.read_excel('C:/Users/User/Python/datasets/Natal.xlsx')
d = pd.read_excel('C:/Users/User/Python/datasets/Recife.xlsx')
e = pd.read_excel('C:/Users/User/Python/datasets/Salvador.xlsx')
#Anexa todos os arquivos selecionados
x = pd.concat([a,b,c,d,e])
#Mostra as 5 primeiras linhas
x.head()
#Mostra as 5 últimas linhas
x.tail()
#Mostra uma amostra com 1 linha
x.sample()
#Mostra o tipo de dado de cada coluna
x.dtypes
#Alterando o tipo de dado de uma coluna (int) para (object)
x['LojaID'] = x['LojaID'].astype('object')
#Consulta de linhas com dados faltantes (O arquivo original não tinha nenhum dado faltante, mas na
#apresentação do desafio o arquivo é mostrado com 7 itens faltantes, portanto excluí manualmente 7 itens
#aleatórios da planilha Salvador)
x.isnull().sum()
#Média da coluna vendas
x['Vendas'].mean()
#Substituir os itens faltantes pela média
x['Vendas'].fillna(x['Vendas'].mean(), inplace=True)
#Substituir os itens faltantes por 0
x['Vendas'].fillna(0,inplace=True)
#Apagar itens com valores nulos
x.dropna(inplace=True)
#Apagar itens com valores nulos de uma coluna específica
x.dropna(subset=['Vendas'],inplace=True)
#Apaga itens que tenha valores nulos em TODAS as colunas
x.dropna(how='all',inplace=True)
#Criando uma coluna nova
x['Receita'] = x['Vendas'].mul(x['Qtde'])
#Maior valor da coluna receita
x['Receita'].max()
#Menor valor da coluna receita
x['Receita'].min()
#Retorna uma quantidade X de linhas com os maiores valores de uma coluna específica
x.nlargest(3,'Receita')
#Retorna uma quantidade X de linhas com os menores valores de uma coluna específica
x.nsmallest(3,'Receita')
#Agrupamento de valores por critério
#Neste caso, será somado todos os valores de receitas de cada cidade
x.groupby('Cidade')['Receita'].sum()
#Ordenar conjunto de dados
x.sort_values('Receita', ascending=False).head(10)








