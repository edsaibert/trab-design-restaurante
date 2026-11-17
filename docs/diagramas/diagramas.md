# Diagramas de Arquitetura

## Diagrama de Classes
As classes construtoras que utilizam as interfaces de `CardapioRepository`, `PedidoRepository`, `LogRepository` e `RULogin` não foram consideradas no diagrama para facilitar a visualização. No sistema atual, foi proposta apenas uma implementação concreta para cada classe.

![diagrama_classes](./classes/Diagrama%20de%20Classes.png)

## Diagramas de Sequência
Nos diagramas de sequência, a classe `Controller` ficou de fora pois só é responsável pelo roteamento entre os serviços, sem implementar regras de negócio complexas.

### Caso de Uso 1: Alterar Cardápio
![diagrama_sequencia_alterar_cardapio](./sequencia/Alterar%20Cardápio/Diagrama%20de%20Sequência%20-%20Alterar%20Cardápio.png)


### Caso de Uso 2: Fazer Pedido
![diagrama_sequencia_fazer_pedido](./sequencia/Caso%20de%20Uso%20Principal/Diagrama%20de%20Sequencia%20-%20Caso%20de%20Uso%20Principal.png)


### Caso de Uso 3: Fazer Login
![diagrama_sequencia_fazer_login](./sequencia/Login/Diagrama%20de%20Sequencia%20-%20Login.png)

## Diagramas de Comunicação
Os componentes `Tela da Aplicação`e `Controller` foram dispensados dos diagramas de comunicação para facilitar a visualização do fluxo da requisição do usuário ao sistema. O `Controller` apenas recebe a requisição e a interpreta para o serviço correspondente, sem implementar regras de negócio complexas.

---
### Caso de Uso 1: Alterar Cardápio

![diagrama_comuicacao_alterar_cardapio](./comunicacao/alterar_cardapio_comunicacao.png)
---
### Caso de Uso 2: Fazer Pedido

![diagrama_comunicacao_fazer_pedido](./comunicacao/fazer_pedido_comunicacao.png)
---

## Diagrama de Componentes
![diagrama_componentes](./componentes/componentes.drawio.png)