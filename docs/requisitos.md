# Requisitos funcionais do sistema:


- **RF01** O sistema deve permitir a consulta ao cardápio do restaurante universitário
- **RF02** O sistema deve permitir a realização de pedidos antecipados
- **RF03** O sistema deve informar sobre a disponibilidade de algum item ao usuário
- **RF04** O sistema deve permitir o cancelamento de pedidos antecipados
- **RF05** O sistema deve dispor a retirada das refeições em ordem de realização
- **RF06** O sistema deve indicar que uma combinação de itens está indisponível sempre que ao menos um dos itens na combinação se encontrar indisponível
- **RF07** O sistema deve permitir três tipos de acesso: usuário, funcionário e administrador.
- **RF08** O sistema deve liberar ao funcionário o acesso à lista de pedidos.
- **RF09** O sistema deve permitir ao funcionário alterar o cardápio do dia (Adição, remoção e alteração de itens).

# Restrições do sistema:

- **RN01** O sistema deve usar o sistema institucional da universidade para autenticar os usuários.
- **RN02** O sistema deve obter a entrada do usuário apenas por seleção induzida autocompletada, isto é, o usuário deve entrar apenas com *strings* bem definidas em um conjunto finito de entradas que são relevantes para o contexto, que são dadas pelo sistema ao usuário (*e.g.* usuário escolhe "Bife", "Arroz" e "Feijão", pois todas estas são *strings* relevantes ao contexto)
- **RN03** O sistema deve barrar o acesso de usuários não autenticados pelo serviço institucional da universidade
- **RN04** O sistema deve impedir realizar pedidos 30 minutos antes dos horários de refeição.