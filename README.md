Selection Sort (ordenação por seleção)

Estavel? Não
Memória extra? Baixa

Vantagens:
Simples de entender e implementar.
Pouca memória extra necessária (in-place).

Desvantagens:
Muito lento para grandes listas (O(n²)).
Ineficiente mesmo em listas parcialmente ordenadas.

Bubble Sort

Estavel? sim
Memória extra? Baixa

Vantagens:
Fácil de implementar.
Bom para listas pequenas ou quase ordenadas.

Desvantagens:
Muito ineficiente para grandes volumes (O(n²)).
Realiza muitas comparações desnecessárias.

Insertion Sort (ordenação por inserção)

Estavel? Sim
Memória extra? Baixa

Vantagens:
Excelente para listas pequenas.
Muito eficiente para listas quase ordenadas.

Desvantagens:
Desempenho ruim em listas grandes (O(n²)).

Merge Sort (ordenação por intercalação)

Estavel? sim
Memória extra? Alta

Vantagens:
Muito eficiente (O(n log n)).
Estável (mantém a ordem relativa).

Desvantagens:
Requer memória extra.
Mais difícil de implementar manualmente.

Quick Sort (ordenação rápida)

Estavel? Não
Memória extra? Baixa

Vantagens:
Um dos mais rápidos na prática (O(n log n) em média).
In-place (se implementado com ponteiros).

Desvantagens:
Desempenho pode cair para O(n²) no pior caso.
Não é estável por padrão.

Heap Sort

Estavel? Não
Memória extra? Baixa

Vantagens:
Complexidade O(n log n).
Não precisa de memória extra significativa.

Desvantagens:
Não é estável.
Mais lento que Quick Sort na média.

Counting Sort

Estavel? Sim
Memória extra? Alta

Vantagens:
Extremamente rápido para números inteiros pequenos.
Complexidade O(n + k).

Desvantagens:
Requer conhecer o valor máximo.
Ineficiente para grandes intervalos de valores.

Radix Sort

Estavel? Sim
Memória extra? ]alta

Vantagens:
Muito eficiente para números inteiros.
Complexidade quase linear (O(nk)).

Desvantagens:
Requer memória adicional.
Só funciona bem com inteiros.

Bucket Sort

Estavel? Sim
Memória extra? Alta

Vantagens:
Excelente desempenho com dados uniformemente distribuídos.
Pode ser mais rápido que o Quick Sort.

Desvantagens:
Requer função de distribuição adequada.
Complexidade pode variar muito.
