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
#Criando uma coluna nova
x['Receita'] = x['Vendas'].mul(x['Qtde'])
#Criar uma coluna nova utilizando apenas o ano da coluna 'Data'
x['ano_venda'] = x['Data'].dt.year
#Criar colunas com os valores do mês e do dia da coluna 'Data'
x['mes_venda'], x['dia_venda'] = (x['Data'].dt.month, x['Data'].dt.day)
#Filtrar o ID das lojas e colocar em ordem decrescente de acordo com a quantidade de vendas
x['LojaID'].value_counts(ascending=False)
#Criar um gráfico de barras
x['LojaID'].value_counts(ascending=False).plot.bar()
#Criar um gráfico de barras horizontais
x['LojaID'].value_counts(ascending=False).plot.barh()
#Criar um gráfico de barras horizontais ordenados de forma decrescente
x['LojaID'].value_counts(ascending=True).plot.barh()
#Criar um gráfico de pizza
x.groupby(x['Data'].dt.year)['Receita'].sum().plot.pie()
#Total de vendas por cidade
x['Cidade'].value_counts()
#Adicionar título e alterar o nome dos eixos
import matplotlib.pyplot as plt
x['Cidade'].value_counts().plot.bar(title = 'Total vendas por cidade')
plt.xlabel('Cidade')
plt.ylabel('Total Vendas');
#Alterar a cor do gráfico
x['Cidade'].value_counts().plot.bar(title='Total vendas por cidade', color='red')
plt.xlabel('Cidade')
plt.ylabel('Total Vendas')
#Alterar o estilo do gráfico
plt.style.use('ggplot')
#Filtrar a quantidade de vendas por mes
x.groupby(x['mes_venda'])['Qtde'].sum()
#Selecionar apenas as vendas de 2019
x_2019 = x[x['ano_venda'] == 2019]
#Total de produtos vendidos por mês
x_2019.groupby(x_2019['mes_venda'])['Qtde'].sum().plot(marker = 'o')
plt.xlabel('Mês')
plt.ylabel('Total de produtos vendidos');
plt.legend()
#Criar um histograma
plt.hist(x['Qtde'],color='orangered');
#Criar um gráfico de dispersão
plt.scatter(y = x_2019['dia_venda'], z = x_2019['Receita']);
#Salvar em png
x_2019.groupby(x_2019['mes_venda'])['Qtde'].sum().plot(marker = 'v')
plt.title('Quantidade de produtos vendiso x mes')
plt.xlabel('Mês')
plt.ylabel('Total produtos vendidos')
plt.legend()
plt.savefig('grafico QTDE x MES.png')


