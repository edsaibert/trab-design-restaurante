# Alternativas e Trade-Offs

---

## Alternativa A: Cliente-Servidor Monolítico

A arquitetura Cliente-Servidor é a mais intuitiva para nosso problema pois as interações são no geral estilo requisição-resposta. O monólito também é a primeira alternativa para um sistema qualquer que seja simples e pequeno o suficiente pois dispensa maiores abstrações e governanças necessárias para manejar outras arquiteturas mais complexas. Os clientes são leves, a segurança e os dados são centralizados, a implementação inicial é bem simples e o custo inicial é baixo.

**Problema:** O servidor é crítico para o desempenho e a disponibilidade do sistema então caso este esteja congestionado, todos os usuários são afetados e caso ele falhe, todo o sistema cai. Além disso crescer e modificar esse sistema se torna uma dor de cabeça, como não há preocupação em isolar os componentes, uma modificação simples ou aumento notável na demanda de usuários pode necessitar uma mudança geral do sistema, e isso é muito custoso.

___

## Alternativa B: Hexagonal

Uma arquitetura Hexagonal cria um ambiente mais modificável. Com o núcleo independente de saídas e a implementação de portas e adaptadores, estes podem ser desenvolvidos de maneira autônoma. Além da modificabilidade, a arquitetura hexagonal também auxilia na escalabilidade, permitindo os componentes crescerem sozinhos desde que respeitem os contratos e testabilidade do sistema pois é possível testar os componentes isolados.

**Problema:**  A equipe de implementação é pequena e as demandas do sistema são simples. O sistema demanda poucos casos de uso e todos eles partem de uma requisição síncrona feita pelos usuários, sejam eles clientes ou funcionários. A implementação de uma arquitetura hexagonal pode ser complicada demais e causar muitas abstrações que não valham a pena para um sistema de pequeno porte.

___

## Alternativa C: Microsserviços

Os microsserviços podem ser muito bons para o desempenho e escalabilidade da solução pois sobrecarga de um serviço não afeta outro e eles conseguem crescer de maneira independente. Além disso, o desenvolvimento de cada parte pode ser feita de maneira completamente separada, possibilitando autonomia entre as equipes envolvidas.

**Problema:** Os microsserviços implicam em uma complexidade altíssima no sistema, além de abstrações e contratos para a boa comunicação entre partes, é necessário cuidado com a rede, consistência de dados e observabilidade distribuída. Tudo isso pode valer a pena caso hajam equipes o suficiente, serviços o suficiente e demanda o suficiente para justificar tal escolha, mas este não é nosso caso.

___

## Comparativos

A principal motivação da escolha da alternativa A foi baseada em simplicidade. A presença de uma equipe pequena e poucos casos de uso faz da escolha de um Cliente-Servidor Monolítico a mais intuitiva e rápida. 
Apesar de pequeno, o sistema pode escalar para atender mais universidades/estudantes. Caso isso aconteça, o sistema pode ser transicionado para uma Arquitetura Hexagonal que preserva muitos dos benefícios de modularidade e de requisição do Cliente-Servidor.\\
O escopo do sistema faz a escolha de microsserviços confusa. Apesar da necessidade de modularidade entre comunicadores e regras de negócio, o sistema não possui diversos serviços diferentes ocorrendo de maneira assíncrona. A implementação de microsserviços causaria uma carga de trabalho grande que não seria aproveitada pelas funcionalidades implementadas do sistema.