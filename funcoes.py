
'''
import pandas as pd
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
'''

def criar_lista_de_acoes():
    pass
    """Função que busca o arquivo csv baixado do site da B3 e lê as ações que compõe e índice retornando a lista"""
    # acoes = pd.read_csv('ibov.csv', encoding='ISO-8859-1', sep=';')
    # lista_acoes = acoes['IBOV - Carteira do Dia 31/07/24'].loc[:][1:-2]
    # lista_acoes = list(lista_acoes)
    # return lista_acoes

def baixar_arquivos(ativo='CPLE6', periodo=2):
    pass
    # """Baixa os dados do yfinance pedindo o código do ativo e o período"""
    # codigo = yf.Ticker(f'{ativo.upper()}.SA')
    # df = codigo.history(f'{periodo}y')
    #
    # return df

def criar_bandas_bollinger(ativo='VALE3', periodo=5):
    pass
    # """Cria bandas de bollinger usando a função baixar arquivos"""
    # # faz o cálculo das bandas de bollinger
    # df = baixar_arquivos(ativo, periodo)
    # df['Media'] = df['Close'].rolling(window=20).mean()
    # df['Desvio'] = df['Close'].rolling(window=20).std()
    #
    # df['Banda Superior'] = df['Media'] + 2 * df['Desvio']
    # df['Banda Inferior'] = df['Media'] - 2 * df['Desvio']
    # df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    # df = df.dropna()
    # gatilhos = df[df['Close'] <= df['Banda Inferior']]
    #
    # fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Cotação')])
    # #fig = go.Figure(go.Scatter(x=df.index, y=df['Close'], line_color='black', name='Fechamento'))
    # fig.add_trace(go.Scatter(x=df.index, y=df['Banda Superior'], name="Banda Superior", line_color='green'))
    # fig.add_trace(go.Scatter(x=df.index, y=df['Banda Inferior'], name='Banda Inferior', line_color='green'))
    # fig.add_trace(go.Scatter(x=df.index, y=df['Media'], name='Média 20', line_color='orange'))
    # fig.add_trace(go.Scatter(x=gatilhos.index, y=gatilhos['Close'], line_color='purple', name='Compra', mode='markers'))
    # fig.update_layout(title_text=f"Indicador Bandas de Bollinger de {ativo}", xaxis_rangeslider_visible=False)
    # st.plotly_chart(fig)
    #
    # st.text_area(
    #     "Uma breve explicação sobre as bandas de Bollinger: :sunglasses:",
    #     "Nossas queridas Bandas de Bollinger são compostas de uma média móvel de 20 períodos e 2 desvios  também de 20 períodos "
    #     "onde a méida é a linha laranja do meio e os desvios são são as bandas superior e inferior."
    #     "\nRepare que o preço tem alta probabilidade de se movimentar próximo as bandas!"
    #     "\nImagine quanto dinheiro não podemos ganhar unindo nossas Bandas de Bollinger com outros indicadores de preço e volume?!")

def criar_ifr(ativo='CPLE6', periodo=1):
    pass
    # df = baixar_arquivos(ativo, periodo)
    # df['retornos'] = df['Close'].pct_change()
    # df = df.dropna()
    # # separar os retornos positivos dos negativos
    # df['retornos_positivos'] = df['retornos'].apply(lambda x: x if x > 0 else 0)
    # df['retornos_negativos'] = df['retornos'].apply(lambda x: abs(x) if x < 0 else 0)
    # # calcular a média dos retornos positivos e negativos dos ultimos 22 dias
    # df['media_retornos_positivos'] = df['retornos_positivos'].rolling(window=22).mean()
    # df['media_retornos_negativos'] = df['retornos_negativos'].rolling(window=22).mean()
    # df = df.dropna()
    # # passo 6 - Calcular o RSI
    # df['RSI'] = (100 - 100 / (1 + df['media_retornos_positivos'] / df['media_retornos_negativos']))
    #
    # # Cria gráfico do IFR
    # fig_ifr = make_subplots(
    #     rows=3, cols=2,
    #     specs=[[{"rowspan": 2, "colspan": 2}, None],
    #            [None, None], [{'colspan': 2}, None]],
    # )
    # fig_ifr.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Cotação'), row=1, col=1)
    # #fig_ifr.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Fechamento", line_color='black'), row=1, col=1)
    # fig_ifr.add_trace(go.Scatter(x=df.index, y=df['RSI'], name="IFR", line_color='orange'), row=3, col=1)
    # fig_ifr.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
    # fig_ifr.add_hline(y=30, line_dash="dash", line_color="blue", row=3, col=1)
    #
    # fig_ifr.update_layout(title_text=f"Indicador IFR de {ativo}", xaxis_rangeslider_visible=False)
    # st.plotly_chart(fig_ifr)
    # st.text_area(
    #     "Uma breve explicação sobre as o IFR: :sunglasses:",
    #     "Nosso querido indicador IFR é calculado com os retornos do períodos e uma média da janela de 20 períodos "
    #     "feito algumas divisões."
    #     "\nO Game com o IFR é comprar próximo a linha vermelha e vender róximo a linha azul."
    #     "\nAchou difícil? Posso te mostrar como ganhamos dinheiro com ele?!")

def estudo_variacao_precos(ativo='vale3', periodo=5):
    pass
    """Função que cira indicadores e cria também um gráfico em matplotlib para estudo de comportamento do preços"""
    # df = baixar_arquivos(ativo, periodo)
    # df = df.drop(['Dividends', 'Stock Splits'], axis=1)
    # df['Close_change'] = df['Close'].pct_change()
    # df = df.dropna()
    # df['Close_change'].describe()
    # p25, p75 = df['Close_change'].describe()[['25%', '75%']]
    #
    # pmin = max(min(df['Close_change']), p25 - 1.5 * (p75 - p25))
    # pmax = min(max(df['Close_change']), p75 + 1.5 * (p75 - p25))
    #
    # st.text_area(
    #     "Informação sobre o método (role para baixo para ver o estudo):",
    #     "Aqui é onde analisaremos o comportamento dos preços... observe a linha azul que é onde compraremos! "
    #     "Na linha vermelha é onde devemos efetuar a venda com lucro, lógico que algumas operações vamos alongar nossas"
    #     " operações...", )
    #
    # fig_e = make_subplots(
    #     rows=2, cols=2,
    #     specs=[[{"colspan": 2}, None], [{}, {}]],
    #
    #     subplot_titles=(f"Variação do Preço Real em R$ do ativo {ativo}", "Box Plot de Variação", f"Variação % do preço "))
    #
    # fig_e.add_trace(go.Scatter(x=df.index, y=df['Close_change'], line_color='black'),
    #               row=2, col=1)
    # fig_e.add_hline(y=pmin, line_dash="dash", line_color="blue")
    # fig_e.add_hline(y=pmax, line_dash="dash", line_color="red")
    # fig_e.add_trace(go.Box(y=df['Close_change']),
    #               row=2, col=2)
    # fig_e.add_hline(y=pmin, line_dash="dash", line_color="blue")
    # fig_e.add_hline(y=pmax, line_dash="dash", line_color="red")
    # fig_e.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
    #                                name='Cotação'), row=1, col=1)
    #
    # fig_e.update_layout(showlegend=False, xaxis_rangeslider_visible=False,
    #                     title_text=f"Estudo da Variação de preço do ativo {ativo} por {periodo} ano(s),")
    # st.plotly_chart(fig_e)

def previsao_regressao_linear(ativo, periodo):
    pass
    """Essa funçção utiliza machine learning para prever o preço de um ativo do tia posterior"""
    # df = baixar_arquivos(ativo, periodo)
    # # tratamento dos dados e criação de média
    # df['mm9'] = df['Close'].rolling(window=9).mean()
    # df['mm21'] = df['Close'].rolling(window=21).mean()
    # df['Close'] = df['Close'].shift(-1)
    # df.reset_index(inplace=True)
    # ultimo_dado = df.iloc[-1:]
    # df.dropna(inplace=True)
    #
    # # tamanho dos dados
    # total = len(df)
    # treino = len(df) - int((0.7*len(df)))
    # teste = len(df) - 15
    #
    # # definindo features e labels
    # x_features = df.drop(['Date', 'Close', 'Volume', 'Dividends', 'Stock Splits'], axis=1)
    # x_features_list = list(x_features.columns)
    #
    # y_label = df['Close']
    #
    # # separando x e y de treino e teste
    # x_train, x_test = x_features[:treino], x_features[treino:teste]
    # y_train, y_test = y_label[:treino], y_label[treino:teste]
    #
    # # Rodar a regressão
    #
    # lr = LinearRegression()
    # lr.fit(x_train, y_train)
    # y_predito = lr.predict(x_test)
    # coef = r2_score(y_test, y_predito)
    # mensagem = f'O Coeficiente é de {coef * 100:.2f}% de expliação dos dados'
    #
    # # dados de validação:
    # prever = x_features[teste:total]
    # data = df['Date'][teste:total]
    # fechamento = df['Close'][teste:total]
    #
    # y_previsto = lr.predict(prever)
    #
    # dados = pd.DataFrame({'Data': data, 'Fechamento': fechamento, 'Previsto': y_previsto})
    # dados['Fechamento'] = dados['Fechamento'].shift(+1)
    # dados['Erro'] = dados['Previsto'] - dados['Fechamento']
    # dados = dados.round(2).dropna()
    #
    # fig, ax = plt.subplots(figsize=(16, 8))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    # ax.xaxis.set_tick_params(rotation=30)
    #
    # ax.set_title(f'\nDesempenho do modelo com o ativo {ativo} nos ultimos 15 pregões.\n',
    #              fontsize=24)
    # ax.set_xlabel(f'\nPeríodo de {periodo} anos. {mensagem}\nGRÁFICO FIGURA B', fontsize=16)
    # ax.set_ylabel(f'Variação do preço do ativo', fontsize=16)
    # ax.plot(dados['Data'], dados['Fechamento'], color='blue', label='Cotação Real', marker='o')
    # ax.plot(dados['Data'], dados['Previsto'], color='red', label='Cotação Prevista', marker='o')
    # plt.legend()
    # plt.grid()
    #
    # data = ultimo_dado['Date']
    # prever = ultimo_dado.drop(['Date', 'Close', 'Volume', 'Dividends', 'Stock Splits'], axis=1)
    #
    # y_amanha = lr.predict(prever)
    #
    # fig, ax = plt.subplots(figsize=(16, 8))
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
    # ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    # ax.xaxis.set_tick_params(rotation=30)
    # ax.set_title(
    #     f'\nDesempenho do modelo de {ativo} nos ultimos 15 pregões e Previsão.\nPrevisão para o próximo fechamento: R$ {str(y_amanha.round(2)).replace("[", "").replace("]", "").replace(".", ",")}',
    #     fontsize=24)
    # ax.set_xlabel(f'\nPeríodo de {periodo} ano(s). {mensagem}', fontsize=22)
    # ax.set_ylabel(f'Variação do preço do ativo', fontsize=16)
    # ax.plot(dados['Data'], dados['Fechamento'], color='blue', label='Cotação Real', marker='o')
    # ax.plot(dados['Data'], dados['Previsto'], color='red', label='Cotação Prevista', marker='o')
    #
    # ax.plot(data, y_amanha,
    #         color='green',
    #         label=f'Previsão para amanhã: R$ {str(y_amanha.round(2)).replace("[", "").replace("]", "").replace(".", ",")}',
    #         marker='X')
    #
    # plt.legend()
    # plt.grid()
    # plt.show()
    # st.pyplot(fig)
    # st.info('Para uma previsão mais precisa, recomendo fazer essa análise com pelo menos 5 anos!')
