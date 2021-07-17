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
#Transformando o tipo de uma coluna no tipo 'Data'
x['Data'] = pd.to_datetime(x['Data'])
#Agrupamento da coluna 'Receita' utilizando apenas o ano da data
x.groupby(x['Data'].dt.year)['Receita'].sum()
#Criar uma coluna nova utilizando apenas o ano da coluna 'Data'
x['Ano_venda'] = x['Data'].dt.year
#Criar colunas com os valores do mês e do dia da coluna 'Data'
x['mes_venda'], x['dia_venda'] = (x['Data'].dt.month, x['Data'].dt.day)
#Retornar a data mais antiga
x['Data'].min()
#Calcular a diferença entre datas
x['diferenca_dias'] = x['Data'] - x['Data'].min()
#Criar uma coluna nova que receberá o valor referente ao trimestre da coluna 'Data'
x['trimestre_venda'] = x['Data'].dt.quarter
#Filtrar as vendas ocorridas no mês de março do ano de 2019
vendas_marco_19 = x.loc[(x['Data'].dt.year == 2019) & (x['Data'].dt.month ==3)]


