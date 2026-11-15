# trab-design-restaurante
Projeção de uma solução de software para o problema do restaurante universitário. Trabalho feito para a disciplina de design de software.

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
├── docs                            // Documentação dos requisitos, ASRs, etc...
├── README.md
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