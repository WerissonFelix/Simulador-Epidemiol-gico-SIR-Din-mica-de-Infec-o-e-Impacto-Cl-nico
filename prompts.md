# 🧠 Prompts Utilizados no Projeto

Este documento reúne os principais prompts utilizados no desenvolvimento deste projeto com auxílio de Inteligência Artificial.

## 📌 Objetivo

Garantir transparência, reprodutibilidade e documentação do processo de desenvolvimento assistido por IA.

---

## 1. Prompt Inicial – Geração do Sistema

```text
Você é um engenheiro de software sênior especializado em modelagem matemática e desenvolvimento de aplicações científicas em Python.

Seu objetivo é desenvolver uma aplicação simples, didática e funcional para modelar o espalhamento de doenças infectocontagiosas, acessível a usuários sem experiência em programação.

### Requisitos técnicos:

1. MODELO MATEMÁTICO:
- Utilize o modelo epidemiológico SIR (Suscetíveis, Infectados, Recuperados)
- Implemente as equações diferenciais discretizadas
- Permita ajuste dos parâmetros:
  - taxa de transmissão (beta)
  - taxa de recuperação (gamma)
  - população total
  - número inicial de infectados

2. EXTENSÃO CLÍNICA:
Inclua uma camada adicional que modele:
- Hospitalizados
- Recuperados
- Fatalidades

Com base em parâmetros como:
- taxa de mortalidade
- tempo médio de recuperação
- taxa de hospitalização

3. TECNOLOGIA:
- Use:
  - NumPy → cálculos numéricos
  - Pandas → organização dos dados
  - Matplotlib → visualização
  - Streamlit → interface web acessível via link

4. INTERFACE:
- Interface simples com sliders para parâmetros
- Botão para rodar simulação
- Gráficos em tempo real mostrando:
  - evolução do SIR
  - evolução clínica (hospitalizados, mortes, recuperados)

5. ESTRUTURA DO CÓDIGO:
- Código bem organizado em funções:
  - simulação SIR
  - simulação clínica
  - geração de gráficos
- Comentários explicativos (nível iniciante)
- Código completo pronto para execução

6. OBJETIVO EDUCACIONAL:
- O código deve ser simples o suficiente para iniciantes entenderem
- Explique brevemente o funcionamento ao final
- Evite complexidade desnecessária

7. ENTREGA:
- Código completo em Python
- Instruções para rodar localmente
- Instruções para deploy usando Streamlit Cloud
```

---

## 2. Prompt – Geração do Artigo Científico

```text
Agora, você é um pesquisador sênior na área de modelagem computacional e epidemiologia.

Sua tarefa é escrever um texto no formato de artigo científico explicando o projeto feito que modela o espalhamento de doenças infectocontagiosas.

OBJETIVO:
Explicar de forma clara e técnica o funcionamento do código, as escolhas de implementação e o papel das bibliotecas utilizadas.

ESTRUTURA OBRIGATÓRIA:

1. Título
2. Resumo 
3. Introdução
   - Contextualização sobre doenças infectocontagiosas
   - Importância da modelagem computacional

4. Metodologia
   - Descrição do modelo SIR
   - Explicação da lógica do código
   - Estrutura do programa (funções principais)
   - Parâmetros utilizados (taxa de transmissão, recuperação, etc.)

5. Tecnologias Utilizadas
   - Explicar o papel de cada biblioteca:
     - NumPy (cálculo numérico)
     - Pandas (estruturação de dados)
     - Matplotlib (visualização)
     - Streamlit (interface e deploy)

6. Resultados e Visualizações
   - Explicação dos gráficos gerados
   - Interpretação dos resultados da simulação

7. Discussão
   - Limitações do modelo
   - Possíveis melhorias
   - Comparação com modelos mais complexos

8. Conclusão

REQUISITOS:
- Linguagem formal e acadêmica
- Clareza para leitores iniciantes em programação
- Não inventar dados irreais ou referências falsas
- Explicar conceitos técnicos de forma didática
- Manter coerência científica

CONTEXTO:
O projeto foi desenvolvido com auxílio de inteligência artificial, com o objetivo de demonstrar que pessoas sem experiência prévia podem criar aplicações funcionais e educativas.
```

---

## 3. Prompt – README

```text
Você é um engenheiro de software e redator técnico experiente em documentação de projetos.

Sua tarefa é gerar conteúdos para um repositório GitHub de um projeto em Python que modela o espalhamento de doenças infectocontagiosas.

Siga EXATAMENTE os passos abaixo:



 1. TÍTULO DO PROJETO
- Crie um nome claro, técnico e atrativo
- Deve refletir modelagem epidemiológica e simulação

---

 2. DESCRIÇÃO DO REPOSITÓRIO
- Escreva uma descrição curta (1–3 frases)
- Linguagem clara e objetiva
- Deve explicar o propósito do projeto



 3. README (em Markdown)

Gere um README completo em Markdown contendo:

Visão Geral
Explique o que o projeto faz de forma simples

 Funcionalidades
Liste as principais funcionalidades:
- Simulação do modelo SIR
- Visualização de gráficos
- Parâmetros ajustáveis
- Dinâmica clínica (hospitalizados, mortes, recuperados)

Tecnologias Utilizadas
Explique o papel de cada biblioteca:
- NumPy
- Pandas
- Matplotlib
- Streamlit

 Como Executar
Passo a passo simples:
1. Instalar dependências
2. Rodar o projeto
3. Acessar no navegador

 Objetivo do Projeto
Explique que o projeto demonstra como IA pode ajudar iniciantes a criar sistemas complexos

 REGRAS IMPORTANTES:
- Use linguagem clara e profissional
- Evite jargões desnecessários
- README deve ser bem formatado e organizado
- Não invente tecnologias não mencionadas
- Seja didático, pois o público inclui iniciantes
```

---

## 4. Prompt – Melhorias e Refinamentos

```text
No markdown, adicione um tópico para um link artigo científico .
```

---

## 🛠 Observações

* Os prompts foram estruturados utilizando técnicas de engenharia de prompt
* O objetivo foi obter código funcional e documentação didática
* Pequenos ajustes manuais podem ter sido realizados após a geração

---

## 📚 Nota

Este projeto demonstra como a utilização de IA pode auxiliar no desenvolvimento de aplicações científicas, mesmo por usuários sem experiência prévia em programação.
