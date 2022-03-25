## Ambiente Web para reduzir isolamento provocado pelo pandemia

Neste exercício-programa simularemos algoritmos implementados em sítios Web para formação de "pares", em nosso caso para incentivar conversas digitais para contornar o isolamento provocado pela pandemia provocada pela Covid-19.

Geralmente esses sítios solicitam que o usuário responda um questionário indicando algumas de suas preferências (como estilo de filmes preferidos e esportes praticados, dentre outros), que são representadas por um vetor de características (denominaremos apenas por característica). A partir desses dados o sítio calcula as afinidades entre cada par de usuários em sua base de dados utilizando alguma métrica de distância (como a distância euclidiana ou outra, como o que chamaremos de número da afinidade).

Esse modelo será bastante simplificado aqui, para começar trocaremos o vetor por um único número natural, que será aqui denominado por característica do usuário. Outra simplificação é que não buscaremos os usuários mais "próximos", apenas imprimiremos a "proximidade" (afinidade) entre pares de usuário. Além disso, usaremos como critério para determinar a afinidade entre duas pessoas uma heurística, que chamaremos de número da afinidade.

O número da afinidade de um indivíduo com característica K será o resultado das somas de seus dígitos até chegar a um único dígito. Por exemplo, para calcular o número da afinidade do valor 9024, são necessárias duas iterações: na iteração 1 soma todos seus dígitos resultando 15 (pois 9+0+2+4 = 15), como 15 tem mais que um dígito, itera novamente; 15 resulta em 6 (1+5 = 6) que é um único dígito, logo o número da afinidade de 9024 é 6.
Se o número da afinidade de dois usuários coincidir, diremos que eles são compatíveis, indicando que eles poderiam iniciar uma conversa remota.

Para simular os dados de características usaremos funções fornecidas. Assim, é essencial que as use corretamente. O modo 1 foi desenhado para você testar a geração dos números pseudo-aleatórios e os modos 2 e 3 para testar o cálculo do número de afinidade. Os demais estão em ordem crescente de complexidade, sendo que o modo k usa algo do modo k-1 (para k > 0).

No início do jogo seu programa deve imprimir a mensagem Digite o modo do jogo: para o usuário deve escolher o modo de jogo (digitando 1, 2, 3, 4 ou 5). Então seu programa invoca o procedimento ("função" que nada devolve) que implementa esse particular modo (vide as seções 2, 3, 4, 5 e 6 com a descrição de cada um deles).

### Modo 1: dada uma semente, gerar a sequência pseudo-aleatória iniciada por essa semente
Para entrar nesse modo o jogador deve ter digitado inicialmente modo 1.
Seu programa deve solicitar que o usuário digite um número natural (que será a semente do processo de geração de pseudo-aleatórios), em seguida deve solicitar um natural k, então seu programa deverá imprimir k valores da sequência pseudo-aleatória produzida pela função _proximo_pseudo(.). Lembre-se que o primeiro elemento da sequência será a semente.

### Modo 2: gerar características e imprimir a soma de seus dígitos
Para entrar nesse modo o jogador deve ter digitado inicialmente modo 2.
Em seguida seu programa deve solicitar que o usuário digite um número natural representando a característica de uma pessoa, então ele deverá calcular a soma de seus dígitos e imprimir esse valor.

### Modo 3: gerar número característico e imprimir seu "número de afinidade"
Para entrar nesse modo o jogador deve ter digitado inicialmente modo 3.
Neste modo de jogo, o usuário deve digitar um número natural (que será a semente do processo), então seu programa deverá gerar um valor pseudo-aleatório (invocando, com a semente, a função _proximo_pseudo(.)) representando (simulando) a característica do usuário. Em seguida seu programa deverá computar e imprimir o número de afinidade associado à característica gerada para o usuário.

### Modo 4: gerar características para 2 pessoas e imprimir se são ou não compatíveis
Para entrar nesse modo o jogador deve ter digitado inicialmente modo 4.
Neste modo de jogo, o usuário deverá digitar dois valores naturais representando as características de duas pessoas, então seu programa deverá computar os números de afinidade associado a cada um e imprimir se são compatíveis ou não (como indicado nos exemplos 8 e 9).

### Modo 5: gerar característica do usuário, depois gerar característica de N possíveis candidatos à compatibilidade
Neste modo, você deve digitar um número para semente, que será utilizado como sua característica. Depois, você digitar um natural k e em seguida seu programa deverá gerar os próximos k números da sequência pseudo-aleatória (a partir da semente), usando a função dada _proximo_pseudo(.) (deve ser a mesma sequência do modo 1).
A seguir seu programa deve, para cada uma das k características geradas (simulação de k pessoas), imprimir se são ou não compatíveis com sua característica, de acordo com os exemplos 10 e 11.