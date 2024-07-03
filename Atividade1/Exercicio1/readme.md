# Pontos Fortes e Fracos

Modelo Relacional:

Pontos Fortes:

Consistência dos dados graças a constraints como PK e FK.
Ideal para transações complexas e que exigem ACID (Atomicidade, Consistência, Isolamento, Durabilidade).
Estruturação clara das relações e interdependências entre as tabelas.

Pontos Fracos:

Menor flexibilidade para mudanças de schema.
Pode não ser escalável para grandes volumes de dados distribuídos.
Desempenho pode ser impactado por operações complexas de JOIN em grandes bases de dados.

Modelo Não Relacional:

Pontos Fortes:

Alta flexibilidade de schema e facilidade para evoluir a estrutura de dados.
Melhor performance para operações de leitura e escrita rápidas e para consultas que não envolvem muitos JOINs.
Escalabilidade horizontal mais eficiente para grandes volumes de dados.

Pontos Fracos:

Menor consistência e complexidade para manter integridade referencial.
Dificuldade para realizar consultas que envolvem dados muito inter-relacionados.
Modelo de dados menos estruturado pode levar a duplicidade e inconsistências se não gerenciado adequadamente.
