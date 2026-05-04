import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. MODELO MATEMÁTICO (SIR)
# ==========================================
def simular_sir(populacao_total, infectados_iniciais, beta, gamma, dias):
    """
    Simula o modelo SIR usando o método de Euler para discretizar as equações.
    S = Suscetíveis, I = Infectados, R = Resolvidos (Recuperados + Óbitos)
    """
    # Inicializando arrays para guardar os dados de cada dia
    S = np.zeros(dias)
    I = np.zeros(dias)
    R = np.zeros(dias)
    
    # Condições iniciais (Dia 0)
    S[0] = populacao_total - infectados_iniciais
    I[0] = infectados_iniciais
    R[0] = 0
    
    # Loop de simulação dia a dia
    for t in range(dias - 1):
        # Quantidade de pessoas que se infectam no dia 't'
        novos_infectados = (beta * S[t] * I[t]) / populacao_total
        
        # Quantidade de pessoas que deixam de estar infectadas (se recuperam ou falecem)
        resolvidos = gamma * I[t]
        
        # Atualizando os valores para o dia seguinte (t+1)
        # Evitamos números negativos usando a função max()
        S[t+1] = max(0, S[t] - novos_infectados)
        I[t+1] = max(0, I[t] + novos_infectados - resolvidos)
        R[t+1] = min(populacao_total, R[t] + resolvidos)
        
    return S, I, R

# ==========================================
# 2. CAMADA CLÍNICA
# ==========================================
def simular_clinica(I, R, taxa_hospitalizacao, taxa_mortalidade):
    """
    Deriva os dados clínicos a partir dos resultados do modelo SIR base.
    """
    # Hospitalizados são uma proporção dos infectados ativos em um dado dia
    hospitalizados = I * taxa_hospitalizacao
    
    # Dos casos "Resolvidos" (R do modelo SIR), uma parte sobrevive e outra falece
    mortes = R * taxa_mortalidade
    recuperados_reais = R * (1 - taxa_mortalidade)
    
    return hospitalizados, recuperados_reais, mortes

# ==========================================
# 3. INTERFACE DE USUÁRIO (Streamlit)
# ==========================================
st.set_page_config(page_title="Simulador Epidemiológico", layout="wide")

st.title("🦠 Simulador de Doenças Infectocontagiosas")
st.markdown("Uma aplicação interativa baseada no modelo matemático **SIR** (Suscetíveis, Infectados, Recuperados).")

# Sidebar para os controles (Parâmetros)
st.sidebar.header("Parâmetros da Simulação")

# Sliders para capturar input do usuário
populacao = st.sidebar.number_input("População Total", min_value=1000, value=100000, step=1000)
inf_iniciais = st.sidebar.number_input("Infectados Iniciais", min_value=1, value=5, step=1)
dias_simulacao = st.sidebar.slider("Dias de Simulação", 10, 365, 100)

st.sidebar.subheader("Parâmetros de Transmissão")
beta = st.sidebar.slider("Taxa de Transmissão (β)", 0.0, 1.0, 0.3, help="Probabilidade de transmissão ao contato.")
dias_recuperacao = st.sidebar.slider("Dias até recuperação", 1, 30, 10)
gamma = 1.0 / dias_recuperacao  # Taxa de recuperação (γ)

st.sidebar.subheader("Parâmetros Clínicos")
taxa_hosp = st.sidebar.slider("Taxa de Hospitalização (%)", 0.0, 100.0, 5.0) / 100
taxa_mort = st.sidebar.slider("Taxa de Mortalidade (%)", 0.0, 20.0, 2.0) / 100

# Botão para executar
if st.sidebar.button("Rodar Simulação", type="primary"):
    
    # 1. Executa os cálculos matemáticos
    S, I, R_sir = simular_sir(populacao, inf_iniciais, beta, gamma, dias_simulacao)
    
    # 2. Executa a camada clínica
    H, Rec, Mortes = simular_clinica(I, R_sir, taxa_hosp, taxa_mort)
    
    # 3. Organiza os dados usando Pandas
    dias_array = np.arange(dias_simulacao)
    df_sir = pd.DataFrame({'Dia': dias_array, 'Suscetíveis': S, 'Infectados': I, 'Resolvidos': R_sir})
    df_clinico = pd.DataFrame({'Dia': dias_array, 'Hospitalizados': H, 'Recuperados': Rec, 'Mortes': Mortes})
    
    # ==========================================
    # 4. VISUALIZAÇÃO (Matplotlib)
    # ==========================================
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dinâmica de Infecção (Modelo SIR)")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.plot(df_sir['Dia'], df_sir['Suscetíveis'], label='Suscetíveis', color='blue')
        ax1.plot(df_sir['Dia'], df_sir['Infectados'], label='Infectados ativos', color='red')
        ax1.plot(df_sir['Dia'], df_sir['Resolvidos'], label='Casos Resolvidos', color='green')
        ax1.set_xlabel("Dias")
        ax1.set_ylabel("Número de Pessoas")
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig1)

    with col2:
        st.subheader("Desdobramento Clínico")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.plot(df_clinico['Dia'], df_clinico['Recuperados'], label='Recuperados (Saudáveis)', color='lime')
        ax2.plot(df_clinico['Dia'], df_clinico['Hospitalizados'], label='Hospitalizados (Ativos)', color='orange')
        ax2.plot(df_clinico['Dia'], df_clinico['Mortes'], label='Óbitos', color='black')
        ax2.set_xlabel("Dias")
        ax2.set_ylabel("Número de Pessoas")
        ax2.legend()
        ax2.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig2)
        
    # Exibir resumo em cards
    st.divider()
    st.subheader("Resumo Final (Dia %d)" % dias_simulacao)
    c1, c2, c3 = st.columns(3)
    c1.metric("Pico de Infectados Simultâneos", f"{int(max(I))}")
    c2.metric("Total de Óbitos", f"{int(Mortes[-1])}")
    c3.metric("Pessoas que não pegaram a doença", f"{int(S[-1])}")

else:
    st.info("Ajuste os parâmetros na barra lateral e clique em **Rodar Simulação** para visualizar os gráficos.")