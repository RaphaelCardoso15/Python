#Importar as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
#Importando o arquivo base e criando o dataframe
a = pd.read_excel('C:/Users/User/Python/datasets/AdventureWorks.xlsx')
x = a
#Apresenta a quantidade de linhas e colunas
x.shape
#Verifica os tipos de dados
x.dtypes
#Qual a receita total?
#5984606.1426
x['Valor Venda'].sum()
#Qual o custo total?
#2486783.05
x['custo'] = x['Custo Unitário'].mul(x['Quantidade'])
round(x['custo'].sum(),2)
#Qual o lucro total?
#3497823.09
x['lucro'] = x['Valor Venda'] - x['custo']
round(x['lucro'].sum(),2)
#Criar uma coluna com o total de dias para enviar o produto
x['Tempo_envio'] = x['Data Envio'] - x['Data Venda']
#Extrair apenas os dias, pois a formatação contém número e texto
x['Tempo_envio'] = (x['Data Envio'] - x['Data Venda']).dt.days
#Conferir se a coluna realmente esta no tipo int
x['Tempo_envio'].dtype
#Calcular média do tempo de envio por marca
x.groupby('Marca')['Tempo_envio'].mean()
#Verificar a existência de valores ausentes na tabela
x.isnull().sum()
#Filtrar o lucro por ano e por marca
##Agrupar ano e marca
x.groupby([x['Data Venda'].dt.year, 'Marca'])['lucro'].sum()
##Formatar apresentação dos números
pd.options.display.float_format = '{:20,.2f}'.format
##Resetar o index
lucro_ano   =   x.groupby([x['Data Venda'].dt.year, 'Marca'])['lucro'].sum().reset_index()
#Qual o total de produtos vendidos?
#25232
x.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
#Gráfico total de produtos vendidos
x.groupby('Produto')['Quantidade'.sum().sort_values(ascending=True).plot.barh(title='Total produtos vendidos')]
plt.xlabel('Total')
plt.ylabel('Produto');
#Lucro por ano
x.groupby(x['Data Venda'].dt.year)['lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita');
#Filtrar apenas as vendas de 2009
x_2009 = x[x['Data Venda'].dt.year == 2009]
#Lucro por mês
x_2009.groupby(x_2009['Data Venda'].dt.month)['lucro'].sum().plot(title = 'Lucro x Mês')
plt.xlabel('Mês')
plt.ylabel('Lucro')
#Lucro por marca
x_2009.groupby('Marca')['lucro'].sum().plot.bar(title = 'Lucro x Marca')
plt.xlabel('Marca')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');
#Lucro por classe
x_2009.groupby('Classe')['lucro'].sum().plot.bar(title = 'Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');
#Análise estatística
x['Tempo_envio'].describe()
#Gráfico de Boxplot
plt.boxplot(x['Tempo_envio']);
#Histograma
plt.hist(x['Tempo_envio'])
#Tempo mínimo de envio
x['Tempo_envio'].min()
#Tempo máximo de envio
x['Tempo_envio'].max()
#Identificando o outlier
x[x['Tempo_envio']==20]
#Salvando em csv
x.to_csv('x_vendas_novo.csv', index=False)







