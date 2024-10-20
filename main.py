from funcoes import *
import streamlit as st

#st.set_option('deprecation.showPyplotGlobalUse', False)

lista_de_acoes = criar_lista_de_acoes()

################## página principal #####################################
st.title(f"Ganhe R$ com estatística com :blue[IBOV] ")
st.markdown("By J.Brutus :sunglasses:")
st.error('Tive um problema com a base de dados, logo estarei corrigindo essa falha...')
########################## Sidebar ######################################
st.sidebar.subheader('Selecione o ativo para análise:')
acao = st.sidebar.selectbox(f'Selecione uma ação da lista das {len(lista_de_acoes)} do IBOV:', (lista_de_acoes),
                            help="Foi buscada no site da B3 as ações atuais que compões o índice...")
anos = st.sidebar.slider("Selecione o tempo para análise:", 0, 10, 1)

df = baixar_arquivos(ativo=acao, periodo=anos)
########################################################################################################################
st.sidebar.success('Marque para exibir ou não o estudo! :wave:')
estudo = st.sidebar.checkbox("Estudo Estatístico", value=True)
if estudo:
    estudo_variacao_precos(acao, anos)

########################################################################################################################
grafico_selecionado = st.sidebar.radio(
    "Selecione um indicador de sua preferência:",
    ["Bandas de Bollinger", "IFR"],
    help='Logo vou colocar gráfico iterativos para facilitar o estudo, pois sei que é melhor e em breve estará pronto.')


if grafico_selecionado == 'Bandas de Bollinger':
    fig2 = criar_bandas_bollinger(acao, anos)
    st.sidebar.write('Bandas de Bollinger calculadas...')

if grafico_selecionado == 'IFR':
    fig3 = criar_ifr(acao, anos)
    st.sidebar.write('IFR calculado e postado...')

st.sidebar.success('Área de previsões de preços :heart:')

reg_lin = st.sidebar.checkbox('Previsão com Regressão Linear')
if reg_lin:
    st.sidebar.info('Recomendo pelo menos 5 anos de análise')
    previsao_regressao_linear(acao, anos)
    st.error('Atenção: Se tiver muito divergente a previsão, significa que é erro na base de dados do Yfinance. '
             'Não atualizaram ainda e geralmente corrigem próximo ao iníncio do pregão!')

rn = st.sidebar.checkbox('Previsão com Redes Neurais')
if rn:
    st.sidebar.error('Aguenta só mais um pouquinho, Calabrezo, já faço o deploy')
#pprint