# Sistema de pedidos antecipados do restaurante universitário

Este documento fornece um *overview* do sistema construído no trabalho final da disciplina de Design de Software.

## Diagramação

Os diagramas produzidos pela equipe se encontram em `docs/diagramas`, com cada tipo de diagrama tendo seu subdiretório.

### Diagrama de classes

O diagrama de classes abaixo:

![diag-classes](./diagramas/classes/Diagrama%20de%20Classes.png)

Representa as interações entre as principais entidades do sistema, bem como suas respectivas multiplicidades e composições. A partir deste diagrama, surgiram os próximos.

### Diagramas de sequência

Foram pensados três casos de uso relevantes: Alterar Cardápio, Fazer Pedido (caso de uso principal) e Fazer *Login*. Para cada caso de uso, foi feito um diagrama de sequência correspondente. Acionadores de caso de uso (entidades `Controller`) e interfaces de comunicação com `Usuario` estão implícitas, a fim de simplificar os diagramas, e também porque o caso de uso é explícito. A seguir, uma breve descrição de cada diagrama, nas quais os possíveis fluxos serão descritos separadamente.

### Alterar Pedido

![diag-seq-alterar-pedido](./diagramas/sequencia/Alterar%20Cardápio/Diagrama%20de%20Sequência%20-%20Alterar%20Cardápio.png)

Fluxo principal (`Usuario` é um administrador do sistema, então pode alterar o cardápio):

1. `Usuario` se autentica através de `RULogin`
2. `RULogin` devolve um `Token` de sessão (por simplicidade, assumimos que o *login* foi bem-sucedido) para `Usuario`
3. `alterarCardapio()` é acionado em `RUCardapioService` pela requisição do `Usuario`
4. `RUCardapioService` chama `Cardapio` para realizar alguma alteração no cardápio
5. `Cardapio` devolve uma confirmação a `RUCardapioService`
6. `RUCardapioService` chama `RUNotificator` para emitir uma notificação de confirmação
7. `RUNotificator` notifica `Usuario` de que a tabela foi atualizada
8. `RUCardapioService` chama `Log` para registrar a alteração feita no cardápio
9. `Log` devolve uma confirmação do registro para `RUCardapioService`

Fluxo alternativo (`Usuario` não é um administrador do sistema, então seu acesso é negado):

1. `Usuario` se autentica através de `RULogin`
2. `RULogin` devolve um `Token` de sessão (por simplicidade, assumimos que o *login* foi bem-sucedido) para `Usuario`
3. `RUCardapioService` chama `RUNotificator` para emitir uma notificação de acesso negado
4. `RUNotificator` notifica `Usuario` de que sua ação não é permitida ou que seu acesso foi negado
5. `RUCardapioService` chama `Log` para registrar a tentativa de alteração no cardápio
6. `Log` devolve uma confirmação do registro para `RUCardapioService`

### Autores

Sofia Barbosa Candiotto, Eduarda Saibert, Caio Eduardo Ferreira de Miranda, Kawai Barzotto.
