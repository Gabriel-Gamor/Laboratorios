1. Crie um sistema de cálculo distribuído simples com apenas 2 processos:
• O Rank 0 (Cliente) define um número inteiro (ex: 80), envia esse número para o Rank 1 e fica esperando uma resposta.
• O Rank 1 (Servidor) recebe o número, divide por 2 e envia o resultado de volta para o Rank 0.
• O Rank 0 recebe a resposta e imprime: “O servidor me respondeu: [Resultado]”.

2. Você está desenvolvendo o sistema de comunicação de um Satélite Militar. Para enviar um "Código de Lançamento", não basta apenas jogar o dado na rede. E necessário um protocolo rigoroso de 4 passos (four way handshake) para garantir que nada foi perdido. Implemente essa comunicação usando send e recv. Cada processo deve imprimir o que enviou e o que recebeu em cada etapa.

3. Desafio - A Eleição do Novo Rei (Algoritmo de Chang-Roberts): Cada processo só conhece o "endereço" do seu vizinho da direita. Eles não sabem o tamanho total da rede nem quem são os outros. Como descobrir quem tem o maior Rank circulando apenas mensagens?
Escreva um código utilizando MPI para a eleição do Novo rei, simulando o não conhecimendo dos indices.

4. Desafio - Exclusão Mutua Distribuída: Uma impressora em rede deve ser utilizada por qualquer dispositivo na rede. No entanto, caso dois aparelhos enviem impressões simultaneamente, o papel sairá borrado. Como garantir que apenas um use a impressora por vez, sem ter um servidor central controlando? Resolva esse problema usando MPI e apenas send e recv.

5. O Problema dos Generais Bizantinos (Consenso Simplificado): Um General (Rank 0) envia uma ordem para seus Tenentes: ’ATACAR’ ou ’RECUAR’. Por´em, o General pode ser um Traidor e enviar ordens diferentes para tenentes diferentes (para causar confusão). Como os tenentes podem conversar entre si para descobrir se o General é confiável?

