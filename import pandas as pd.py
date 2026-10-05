import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta
 
def gera_dados_ficticios(num_registro = 600):
    """
    Gera um DataFrame do Pandas com dados fictícios.
    """
    
    print(f"\nIniciando a geração de {num_registro} registro de venda...")
    
    produtos = {
        'Laptop Gamer':{'categoria':'Eletrônicos', 'preco':7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }
    
    lista_produtos = list(produtos.keys())
    
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }
    
    lista_cidades = list(cidades_estados.keys())
    
    dados_vendas = []
    
    data_inicial = datetime(2026, 1, 1)
    
    for i in range(num_registro):
        produto_nome = random.choice(lista_produtos)
        cidade = random.choice(lista_cidades)
        quantidade = np.random.randint(1,8)
        data_pedido = data_inicial + timedelta(days= int(i/5), hours= random.randint(0, 23))
        
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']
            
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })

    print("Geração de dados concluída.\n")
    return pd.DataFrame(dados_vendas)
    
df_vendas = gera_dados_ficticios(500) 
#type(df_vendas)
#print(df_vendas.shape)
#print(df_vendas.head())
#df_vendas.tail()
#df_vendas.info()
#df_vendas.describe()
#df_vendas.dtypes

df_vendas['data_pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])
df_vendas['faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']    
df_vendas['Status_Entrega']= df_vendas['Estado'].apply(lambda estado: 'rapida' if estado in ["SP","RJ","MG"] else 'normal')
#print(df_vendas.info())
#print(df_vendas.head())

top_10_produtoss = df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)
#print(top_10_produtoss)

sns.set_style('whitegrid')
plt.figure(figsize=(12,7))
top_10_produtoss.sort_values(ascending=True).plot(kind='barh', color='skyblue')
plt.title("Top 10 produtos", fontsize=20)
plt.xlabel('Quantidade Vendida', fontsize = 12)
plt.ylabel('Produto', fontsize=12)

#print(plt.tight_layout())
#print(plt.show())

df_vendas['Mes']= df_vendas['Data_Pedido'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['faturamento'].sum()
faturamento_mensal.index = faturamento_mensal.index.strftime('%Y%m')
#print(faturamento_mensal.map('R$ {:,.2f}'.format))

plt.figure(figsize=(12,6))
faturamento_mensal.plot(kind="line", marker='o', linestyle='-',color='green')
plt.title('faturamento mensal', fontsize=20)
plt.xlabel('Mes', fontsize = 12)
plt.ylabel('faturamento', fontsize=12)
plt.xticks(rotation = 45)
plt.grid(True,which='both',linestyle= '--',linewidth = 0.5)
#print(plt.tight_layout())
#print(plt.show())


vape = df_vendas.groupby('cidade_estados{SP}')
print(vape)