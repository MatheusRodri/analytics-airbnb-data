# Dash Airbnb

Este projeto contém 2 análises interativas:
- Análise de Vendas, utilizando a biblioteca Pygwalker em um Jupyter Notebook.
- Dashboard sobre o Airbnb no Rio de Janeiro, utilizando Pygwalker e Streamlit.

## Tecnologias Usadas
- Anaconda: Para gerenciamento de ambiente e pacotes.
- Python:
  - Pandas: Para manipulação e análise de dados.
  - Pygwalker: Para criação de visualizações de dados interativas.
  - Streamlit: Para a construção do dashboard web.

## Requisitos

- Anaconda ou Miniconda 
- Python 3.8 ou superior
- Editor de código (ex: VSCode, PyCharm, Jupyter Notebook)

## Como rodar o projeto:

- Clone ou baixe o repositório
- Entrar na pasta do projeto pelo terminal
- Executar o seguinte comando no terminal: ``conda env create -f environment.yml``
    - Nota sobre o Nome do Ambiente 
        O nome padrão para este ambiente, definido no arquivo environment.yml, é dash_airbnb_rj. Se você já tiver um ambiente com este nome em sua máquina, o comando acima falhará.
        Para resolver, você pode criar o ambiente com um nome diferente de sua escolha, usando o seguinte comando:
        ``conda env create -f environment.yml -n nome_do_seu_ambiente``
- Ativar o ambiente criado:
    - No Windows: ``conda activate dash_airbnb_rj``
    - No MacOS/Linux: ``source activate dash_airbnb_rj``
- Abra o projeto no seu editor de código preferido.
- Pronto para rodar os notebooks e o dashboard!
- Para rodar o dashboard, no terminal, estando na pasta do projeto e com o ambiente ativado, execute:
    ``streamlit run dash_airbnb.py``
