# Projeto Festa Julina

Este é um projeto em Django e GCP para criar um sistema de comandas para uma festa julina. O sistema permite que cada comanda seja associada a um cliente e que cada barraquinha tenha um conjunto de itens disponíveis.

## Funcionalidades

- Registro de pedidos: Os atendentes podem registrar os pedidos dos clientes nas comandas, com base nos itens disponíveis em cada barraquinha.
- Associação de clientes: Cada comanda é associada a um cliente, permitindo um controle mais preciso das vendas.
- Acerto no caixa: No final, os clientes podem passar no caixa e acertar o valor total da comanda.

## Tecnologias utilizadas

- Django: Um framework web em Python para o desenvolvimento rápido de aplicações.
- Google Cloud Platform (GCP): Uma plataforma de computação em nuvem que fornece recursos escaláveis e confiáveis para hospedar e executar aplicativos.

## Configuração do ambiente

1. Clone o repositório do projeto: `git clone https://github.com/seu-usuario/festajulina.git`
2. Acesse o diretório do projeto: `cd festajulina`
3. Crie e ative um ambiente virtual: `python -m venv venv` e `source venv/bin/activate`
4. Instale as dependências do projeto: `pip install -r requirements.txt`
5. Configure as variáveis de ambiente necessárias, como as credenciais do GCP.
6. Execute as migrações do banco de dados: `python manage.py migrate`
7. Inicie o servidor de desenvolvimento: `python manage.py runserver`

## Contribuição

Os contribuidores são:
- [RafaelDiasCmp](https://github.com/RafaelDiasCmp)
- [jrtedeschi](https://github.com/jrtedeschi)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).