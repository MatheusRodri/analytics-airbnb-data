# Dash Airbnb

> Este projeto contém 2 análises interativas:
> - Análise de Vendas, utilizando a biblioteca Pygwalker em um Jupyter Notebook.
> - Dashboard sobre o Airbnb no Rio de Janeiro, utilizando Pygwalker e Streamlit.



## Sumário

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar](#como-rodar)
  - [Pré-requisitos](#pré-requisitos)
- [Como Usar](#como-usar)
- [Como Contribuir](#como-contribuir)


## Funcionalidades

- Análise interativa de dados de vendas de um e-commerce.
- Dashboard interativo sobre o Airbnb no Rio de Janeiro usando pygwalker e Streamlit.

## Tecnologias Utilizadas

- Anaconda
- Python
    - Pandas
    - Pygwalker
    - Streamlit

## Como Rodar
### Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:
- Python 3.10 ou superior
- Anaconda
- Editor de texto ou IDE de sua preferência (Visual Studio Code, PyCharm, etc.)

## Como rodar
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

## Como Contribuir

- Entre em contato comigo pelo [LinkedIn](https://www.linkedin.com/in/matheus-rodrigues-mrj/)
- Faço fork do repositório