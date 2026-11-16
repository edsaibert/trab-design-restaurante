# Visão Geral e Organização
O sistema implementa uma arquitetura **Cliente-Servidor Monolítica Modular**. Essa arquitetura traz facilidade de implementação e manutenibilidade do software por se tratar de um deploy único e um sistema que não demanda complexidade. Sua simplicidade é especialmente útil dada a presença de uma equipe pequena e inexperiente com outros tipos de solução que utilizam comunicação via rede e outros conceitos. Uma arquitetura Cliente-Servidor é intuitiva dado o caráter do sistema, que necessita de requisições de pedidos ou alterações de cardápio para tratar seus casos de uso. Por fim, as requisições são majoritariamente repetidas e a estrutura de uma arquitetura Monolítica Modular contribui para a implementação de um sistema de Cache

---

# Principais Componentes e Responsabilidades

| Componente / Módulo | Responsabilidades |
| :--- | :--- |
| **Aplicação Web (Frontend)** | Renderizar a interface do usuário, captar credenciais de login, exibir o cardápio e enviar requisições de pedidos ou alterações, a depender do tipo de usuário. |
| **CardapioService** |  |
| **PedidoService** |  |
| **LoginService** | Gerenciar o fluxo de autenticação na aplicação, atuando como adaptador entre o roteamento interno e o provedor externo de identidade (`RULogin`). |
| **Camada de Persistência (Repositories)** | Abstrair consultas SQL, gerenciando a conexão com o **MySQL** e a persistência das classes `Cardapio`, `Item`, `Pedido`, `Usuario` e `Log`. |
| **Log** |  |
| **Notificador (`RUNotificator`)** |  |
| **Serviço de Autenticação (`RULogin`)** |  |

---

# Interfaces Relevantes
Os componentes comunicam-se por meio de contratos que reduzem o acoplamento:

* **`ICardapioService`:** Interface exposta por `CardapioService` e consumida tanto por `Controller` quanto por `PedidoService`.
* **`IPedidoService`:** Interface exposta pelo `PedidoService` e consumida pelo `Controller`.
* **`IAuthService` (`RULogin`):** Contrato de integração com o serviço externo de autenticação, implementando operações como `autenticar(credenciais)` para validação de usuário.

---

# Mecanismos de Comunicação
* **Comunicação Externa:** Ocorre de forma síncrona sobre o protocolo **HTTP/HTTPS**, utilizando o estilo **REST** com troca de mensagens em formato **JSON**.
* **Comunicação Interna:** A comunicação entre `Controller`, `CardapioService`, `PedidoService` e entidades de domínio ocorre via chamadas de métodos diretas, através de interfaces (`ICardapioService`, `IPedidoService`).

---

# Decisões de Comunicação
* **Utilização de Cache:** A requisição de consulta ao cardápio ocupa o maior volume de todo o sistema. Posicionar o `CacheService` entre a `Aplicação Web` e o `Controller` evita consultas repetitivas ao banco e desafoga o servidor, que é essencial para uma arquitetura Cliente-Servidor.
* **Autenticação:** Toda requisição que chega ao `Controller` é validada junto ao `AuthService` antes de acionar os serviços de negócio. Para operações sensíveis como alterar o cardápio, se verifica a flag `isAdmin`, bloqueando acessos não autorizados antes de qualquer alteração.

---

# Persistência e Integrações Externas
* **Persistência:**
  * 
* **Integrações Externas:**
  *

---

# Documentação de API
Os principais contratos estão descritos abaixo:

| Método | Endpoint | Descrição | Corpo / Parâmetros | Respostas Esperadas | Acesso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST` | `/api/auth/login` | Autentica o usuário no `RULogin` (`AuthService`). | `{ "usuario", "senha" }` | `200 OK` (retorna Token) / `401 Unauthorized` (negativa de login) | Público |