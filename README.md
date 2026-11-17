# trab-design-restaurante
Projeção de uma solução de software para o problema do restaurante universitário. Trabalho feito para a disciplina de design de software.

**Contexto do sistema:** É um sistema para lidar com pedidos antecipados do restaurante universitário. Alunos e funcionários da universidade podem consultar o cardápio disponibilizado pelo restaurante e realizar pedidos antecipados de combinações de itens disponíveis, bem como cancelá-los. Existem administradores para monitorar a fila de pedidos e que têm acesso aos *logs* e registros de auditoria.

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
uvicorn app.main:app --reload
```

Visualize os `endpoints` por meio do `swagger`:
```bash
http://127.0.0.1:8000/docs
```

# Estrutura
```bash
.

├── README.md
│
├── docs                            // Documentação dos requisitos, ASRs, etc...
│   ├── adr
│   │   ├── ADR-001.md
│   │   ├── ADR-002.md
│   │   └── ADR-003.md
│   ├── diagramas
│   │   ├── classes
│   │   │   ├── Diagrama de Classes.drawio
│   │   │   ├── Diagrama de Classes.png
│   │   └── sequencia
│   │       ├── Alterar Cardápio
│   │       │   ├── Diagrama de Sequência - Alterar Cardápio.drawio
│   │       │   └── Diagrama de Sequência - Alterar Cardápio.png
│   │       ├── Caso de Uso Principal
│   │       │   ├── Diagrama de Sequência - Caso de Uso Principal.drawio
│   │       │   └── Diagrama de Sequência - Caso de Uso Principal.png
│   │       └── Login
│   │           ├── Diagrama de Sequência - Login.drawio
│   │           └── Diagrama de Sequência - Login.png
│   ├── arquitetura.md
│   ├── requisitos.md
│   └── tradeoffs.md
│
└── src
    ├── database                    // Repositories
    │   ├── CardapioRepository.py
    │   ├── database.py             // Conexão com o MySQL 
    │   └── PedidoRepository.py
    ├── interfaces                  // Interfaces
    │   ├── IAuthService.py
    │   ├── ICardapioService.py
    │   └── IPedidoService.py
    ├── main.py
    ├── models                      // Entidades do domínio
    │   ├── Cardapio.py
    │   ├── Item.py
    │   └── Pedido.py
    ├── router.py                   // Controller
    └── services                    // Serviços da Aplicação
        ├── CardapioService.py
        ├── LoginService.py
        └── PedidoService.py

```