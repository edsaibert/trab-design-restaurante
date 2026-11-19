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

### Fazer Pedido

![diag-seq-fazer-pedido](./diagramas/sequencia/Caso%20de%20Uso%20Principal/Diagrama%20de%20Sequencia%20-%20Caso%20de%20Uso%20Principal.png)

Fluxo principal (`Usuario` faz seu pedido com todos os itens disponíveis):

1. `Usuario` faz uma consulta ao cardápio, enviando a requisição para `PedidoService`
2. `PedidoService` chama `Cardapio` para realizar a consulta
3. `Cardapio` devolve o cardápio para `PedidoService`
4. `PedidoService` exibe o cardápio obtido para `Usuario`
5. Enquanto `Usuario` continuar escolhendo itens:
    5.1. `Usuario` seleciona um item
    5.2. `PedidoService` chama `Cardapio` para consultar a disponibilidade do item selecionado
    5.3. `Cardapio` devolve que o item selecionado está disponível
    5.4. `PedidoService` chama `Pedido` para adicionar o item ao pedido de `Usuario`
    5.5. `Pedido` devolve a `PedidoService` a confirmação de que o item foi adicionado
    5.6. `PedidoService` notifica `Usuario`, localmente, de que o item foi adicionado ao pedido
6. `Usuario` chama `PedidoService` para realizar o pedido
7. `PedidoService` chama `Pedido` para registrar o pedido
8. `PedidoService` chama `Log` para registrar o *log* do pedido
9. `Log` devolve uma confirmação do registro para `PedidoService`
10. `PedidoService` chama `RUNotificator` para emitir uma notificação da confirmação do pedido
11. `RUNotificator` devolve a notificação para `PedidoService`
12. `PedidoService` repassa a notificação para `Usuario`

Fluxo alternativo (`Usuario` faz seu pedido, mas ao menos 1 item se encontra indisponível):

1. `Usuario` faz uma consulta ao cardápio, enviando a requisição para `PedidoService`
2. `PedidoService` chama `Cardapio` para realizar a consulta
3. `Cardapio` devolve o cardápio para `PedidoService`
4. `PedidoService` exibe o cardápio obtido para `Usuario`
5. Enquanto `Usuario` continuar escolhendo itens:
    5.1. `Usuario` seleciona um item
    5.2. `PedidoService` chama `Cardapio` para consultar a disponibilidade do item selecionado
    5.3. Se o item estiver disponível, `Cardapio` devolve que o item selecionado está disponível, e que está indisponível caso contrário
    5.4. `PedidoService` chama `Pedido` para adicionar o item ao pedido de `Usuario`, caso ele esteja disponível
    5.5. `Pedido` devolve a `PedidoService` a confirmação de que o item foi adicionado; notifica localmente o usuário acerca da indisponibilidade do item caso este não esteja disponível
    5.6. `PedidoService` notifica `Usuario`, localmente, de que o item foi adicionado ao pedido
6. `Usuario` chama `PedidoService` para realizar o pedido
7. `PedidoService` chama `Pedido` para registrar o pedido
8. `PedidoService` chama `Log` para registrar o *log* do pedido
9. `Log` devolve uma confirmação do registro para `PedidoService`
10. `PedidoService` chama `RUNotificator` para emitir uma notificação da confirmação do pedido
11. `RUNotificator` devolve a notificação para `PedidoService`
12. `PedidoService` repassa a notificação para `Usuario`

### Fazer *Login*

![diag-seq-fazer-login](./diagramas/sequencia/Login/Diagrama%20de%20Sequencia%20-%20Login.png)

Fluxo principal (autenticação ocorreu sem falhas):

1. `Usuario` informa suas credenciais na Tela da Aplicação
2. A Tela da Aplicação realiza requisição de *login* para `RULogin`
3. `RULogin` chama `AuthService` para autenticar as credenciais
4. `AuthService` devolve um *token*
5. `RULogin` devolve o *token* para a Tela da Aplicação
6. A Tela da Aplicação autentica o usuário

Fluxo alternativo (autenticação falhou):

1. `Usuario` informa suas credenciais na Tela da Aplicação
2. A Tela da Aplicação realiza requisição de *login* para `RULogin`
3. `RULogin` chama `AuthService` para autenticar as credenciais
4. `AuthService` devolve uma negativa de *login*
5. `RULogin` devolve a negativa de *login* para a Tela da Aplicação
6. A Tela da Aplicação notifica o usuário de que a autenticação falhou

### Diagrama de componentes

O diagrama de componentes abaixo:

![diag-componentes](./diagramas/componentes/componentes.drawio.png)

Expõe os componentes do sistema e os contratos expostos por cada um para que ocorra a comunicação entre eles. É importante que sejam destacados alguns pontos:

- `CardapioService` dispõe de comunicação bidirecional com o Banco de Dados para indicar leitura e escrita
- O serviço de autenticação é um componente externo, então é mostrado separadamente

### Diagrama de comunicação

### Autores

Sofia Barbosa Candiotto, Eduarda Saibert, Caio Eduardo Ferreira de Miranda, Kawai Barzotto.
