# 🦠 Simulador Epidemiológico SIR: Dinâmica de Infecção e Impacto Clínico

## 📖 Visão Geral
Este projeto é uma aplicação interativa que simula como uma doença infectocontagiosa se espalha por uma população ao longo do tempo. Baseado no modelo matemático **SIR** (Suscetíveis, Infectados, Recuperados), o sistema calcula diariamente a transição de pessoas saudáveis para infectadas, e posteriormente para recuperadas. Além da matemática pura, o projeto aplica uma "lente clínica" sobre os dados, permitindo visualizar o impacto real em um sistema de saúde, como a quantidade de leitos hospitalares necessários e o número de óbitos projetados.

## 📄 Artigo Científico

Para um aprofundamento teórico sobre as escolhas técnicas e a modelagem matemática deste projeto, confira o artigo acadêmico completo que acompanha este repositório. 

O documento detalha:
* A fundamentação do modelo compartimental SIR.
* A metodologia de discretização das equações diferenciais.
* A lógica por trás da camada clínica (hospitalizações e mortalidade).
* A interpretação detalhada dos gráficos e limitações do modelo.

👉 **[Leia o artigo científico completo aqui](https://docs.google.com/document/d/1tb4FNjxOTjalmlIiRyjYBKaDPT8bSVxsvByDldeT9Wk/edit?usp=sharing)**

## ✨ Funcionalidades
* **Simulação do Modelo SIR:** Cálculo passo a passo da transição entre indivíduos Suscetíveis, Infectados e Resolvidos.
* **Dinâmica Clínica:** Estimativa em tempo real do número de pacientes hospitalizados, fatalidades e pacientes totalmente recuperados com base na curva de infecção.
* **Parâmetros Ajustáveis:** Interface intuitiva com *sliders* para modificar a população total, taxa de transmissão (infecção), tempo de recuperação, taxa de hospitalização e taxa de mortalidade.
* **Visualização de Gráficos:** Geração instantânea de gráficos que comparam a curva matemática de contágio com o desdobramento clínico esperado.

## 🛠️ Tecnologias Utilizadas
O projeto foi construído inteiramente em Python, utilizando um ecossistema de bibliotecas focadas em dados e visualização:

* **NumPy:** Responsável pelos cálculos numéricos rápidos e pela manipulação das matrizes (arrays) que guardam os dados de cada dia da simulação.
* **Pandas:** Utilizado para organizar os resultados matemáticos brutos em tabelas estruturadas (*DataFrames*), facilitando a leitura e o alinhamento dos dias com as estatísticas.
* **Matplotlib:** A biblioteca gráfica que transforma as tabelas de dados nos gráficos de linhas visuais, essenciais para interpretar as curvas da epidemia.
* **Streamlit:** Framework que converte o script Python em uma página web interativa. Ele é o responsável por criar os botões, menus e gerenciar o site sem a necessidade de escrever código em HTML ou JavaScript.

## 🚀 Como Executar

Siga os passos abaixo para configurar o ambiente e rodar o simulador no seu computador:

### 1. Preparar o ambiente
Certifique-se de ter o **Python 3.7+** instalado. É recomendável criar um ambiente virtual, mas você pode prosseguir diretamente no terminal.

### 2. Instalar as dependências via `requirements.txt`
Em vez de instalar cada biblioteca individualmente, utilize o arquivo de requisitos para garantir que todas as versões corretas sejam instaladas de uma só vez. No terminal, dentro da pasta do projeto, execute:
```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação
Com as dependências instaladas, inicie o servidor do Streamlit rodando o comando
```bash
stream lit run app.py
```

### 4. Acessar no navegador 
Após o cmando acima, o terminal exibirá um endereço local (geralmente um localhost:8501). O navegador deve abrir automaticamente, mas caso não abra, basta copiar e colar esse endereço na sua barra de navegação.
