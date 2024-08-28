# Backend - Baião Tech Calendar API

![FastAPI Banner](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

![FastAPI](https://img.shields.io/badge/FastAPI-0.112.2-teal)
![Python](https://img.shields.io/badge/Python-3.12.5-blue)
![Status](https://img.shields.io/badge/Status-Development-orange)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A **Baião Tech Calendar API** é um componente crucial do backend que permite gerenciar e organizar eventos de forma eficiente. Construída utilizando **FastAPI**, uma das frameworks mais rápidas e robustas para Python, esta API oferece operações CRUD avançadas para manipulação de eventos, proporcionando uma solução escalável e extensível para diversas necessidades.

## Sobre o Projeto

Este projeto é parte integrante do backend para a API de calendário do Baião Tech, uma plataforma que facilita a gestão de eventos para a comunidade tech. A API permite a criação, leitura, atualização e exclusão de eventos, com funcionalidades desenhadas para atender a diversas especificações de usuário. Cada evento possui os seguintes atributos:

- **Título do evento**: Identificação única do evento.
- **Data do evento**: A data exata em que o evento ocorrerá.
- **Horário do evento**: O horário de início do evento.
- **Descrição do evento**: Detalhes adicionais sobre o evento.
- **Organizadores do evento**: Lista de pessoas ou entidades responsáveis pelo evento.
- **Local do evento**: O endereço ou local virtual onde o evento ocorrerá.
- **URL do site do evento**: Um link opcional para informações adicionais.

## Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Um framework web moderno e de alto desempenho para a construção de APIs com Python.
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Utilizado para validação e modelagem de dados, garantindo a integridade dos dados da API.
- **Python 3.12.5** - Linguagem de programação, conhecida por sua simplicidade e robustez.

## Pré-requisitos

Antes de iniciar, verifique se você possui o Python 3.12.5 instalado. Confira a versão do Python com o seguinte comando:

```bash
python --version
```

## Instalação

Siga estas etapas para configurar o ambiente de desenvolvimento local:

1. Clone o repositório:

   ```bash
   git clone https://github.com/Baiao-Tech/Backend
   cd Backend
   ```

2. Crie um ambiente virtual para isolamento de dependências:

   ```bash
   python -m venv env
   source env/bin/activate  # No Ruindows use `env\Scripts\activate`
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Executando a Aplicação

Para iniciar o servidor de desenvolvimento da API:

```bash
uvicorn app.main:app --reload
```

A aplicação estará rodando em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Documentação da API

Explore a documentação interativa da API (Swagger UI) para testar as rotas e funcionalidades em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Estrutura do Projeto

```
backend/
│
├── app/
│   ├── __init__.py  # Inicialização do pacote
│   └── main.py      # Código principal da aplicação FastAPI
├── README.md        # Documentação do projeto
├── requirements.txt # Dependências do projeto
└── __pycache__/     # Arquivos compilados do Python
```

## Contribuindo

Contribuições são extremamente valiosas e encorajadas! Para sugerir melhorias ou corrigir bugs, por favor, abra um *issue* ou envie um *pull request*.

## Licença

Distribuído sob a licença MIT. Consulte `LICENSE` para mais informações.