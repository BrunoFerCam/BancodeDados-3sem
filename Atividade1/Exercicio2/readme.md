# Pontos Fortes e Fracos

Modelo Relacional:

Pontos Fortes:

Boa estrutura para manter integridade referencial entre livros, autores e empréstimos.
Ideal para operações que exigem transações e integridade de dados rigorosa.
Facilita a realização de consultas complexas através de JOINs entre tabelas.

Pontos Fracos:

Pode ser complexo e demorado para modelar e normalizar dados em grandes bibliotecas.
Menor flexibilidade para mudanças de schema ou adição de novos tipos de dados.
Pode ter problemas de escalabilidade e desempenho em operações intensivas de leitura/escrita.

Modelo Não Relacional:

Pontos Fortes:

Alta flexibilidade para evoluir a estrutura de dados, permitindo armazenar diferentes tipos de documentos sem grandes mudanças.
Melhor performance em consultas e manipulações de dados que envolvem poucos relacionamentos complexos.
Adequado para armazenamento de grandes volumes de dados e consultas rápidas, especialmente em dados semi-estruturados.

Pontos Fracos:

Manter integridade referencial e consistência de dados pode ser mais difícil.
Não é ideal para operações transacionais complexas que exigem consistência forte.
Pode resultar em duplicidade de dados e inconsistências se não for bem gerenciado.
