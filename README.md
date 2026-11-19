# trab-design-restaurante
Projeção de uma solução de software para o problema do restaurante universitário. Trabalho feito para a disciplina de design de software.

**Contexto do sistema:** É um sistema para lidar com pedidos antecipados do restaurante universitário. Alunos e funcionários da universidade podem consultar o cardápio disponibilizado pelo restaurante e realizar pedidos antecipados de combinações de itens disponíveis, bem como cancelá-los. Existem administradores para monitorar a fila de pedidos e que têm acesso aos *logs* e registros de auditoria.


# Configurando o Banco de Dados (Ubuntu)
Instalar o mysql
```bash
sudo apt install mysql-server
```

Iniciar o serviço:
```bash
sudo systemctl start mysql
sudo systemctl enable mysql
```

Acessar como administrador:
```bash
sudo mysql
```

Criar database para o projeto:
```bash
CREATE DATABASE restaurante;
```

Criar usuário e senha (alterar em `database.py`):
```bash
CREATE USER 'admin'@'localhost'
IDENTIFIED BY 'admin';
```

Conceder permissões:
```bash
GRANT ALL PRIVILEGES ON restaurante.* 
TO 'admin'@'localhost';
```

Flush:
```bash
FLUSH PRIVILEGES;
```

Para criação das tabelas de salvamento MySQL, rode:
```bash
python -m src.database.create_tables
```


# Rodando a Aplicação
- Se já não criada, crie um ambiente virtual usando o comando python:
```bash
python -m venv .venv
```

Ative o ambiente virtual com:
```bash
source .venv/bin/activate
```

Baixe os requisitos do `pip`:
```bash
pip install -r requirements.txt
```

Caso precise adicionar uma nova dependência ao `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Rode a aplicação dentro do ambiente virtual, com o comando abaixo:
```bash
uvicorn src.main:app --reload
```

Visualize os `endpoints` por meio do `swagger`:
```bash
http://127.0.0.1:8000/docs
```


# Estrutura
```bash
.
├── docs
│   ├── adr
│   │   ├── ADR-001.md
│   │   ├── ADR-002.md
│   │   └── ADR-003.md
│   ├── arquitetura.md
│   ├── diagramas
│   │   ├── classes
│   │   │   ├── Diagrama de Classes 3.drawio
│   │   │   └── Diagrama de Classes.png
│   │   ├── componentes
│   │   │   └── componentes.drawio.png
│   │   ├── comunicacao
│   │   │   ├── alterar_cardapio_comunicacao.png
│   │   │   └── fazer_pedido_comunicacao.png
│   │   ├── diagramas.md
│   │   └── sequencia
│   │       ├── Alterar Cardápio
│   │       │   ├── Diagrama de Sequência - Alterar Cardápio.drawio
│   │       │   └── Diagrama de Sequência - Alterar Cardápio.png
│   │       ├── Caso de Uso Principal
│   │       │   ├── Diagrama de Sequencia - Caso de Uso Principal(2).drawio
│   │       │   └── Diagrama de Sequencia - Caso de Uso Principal.png
│   │       └── Login
│   │           ├── Diagrama de Sequencia - Login.drawio
│   │           └── Diagrama de Sequencia - Login.png
│   ├── requisitos.md
│   └── tradeoffs.md
├── README.md
└── src
    ├── database
    │   ├── create_tables.py
    │   ├── database.py
    │   ├── interfaces
    │   │   ├── CardapioRepository.py
    │   │   ├── LogRepository.py
    │   │   └── PedidoRepository.py
    │   ├── SQLAlchemyCardapioRepository.py
    │   ├── SQLAlchemyLogRepository.py
    │   └── SQLAlchemyPedidoRepository.py
    ├── interfaces
    │   ├── IAuthService.py
    │   ├── ICardapioService.py
    │   └── IPedidoService.py
    ├── main.py
    ├── models
    │   ├── Cardapio.py
    │   ├── ItemCardapio.py
    │   ├── ItemPedido.py
    │   └── Pedido.py
    ├── requirements.txt
    ├── router.py
    ├── schemas
    │   ├── CardapioSchema.py
    │   ├── ItemCardapioSchema.py
    │   ├── ItemPedidoSchema.py
    │   └── PedidoSchema.py
    └── services
        ├── CardapioService.py
        ├── LoginService.py
        └── PedidoService.py

```
