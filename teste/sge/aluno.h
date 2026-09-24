#ifndef ALUNO_H
#define ALUNO_H

/*
 * aluno.h — Interface pública do módulo Aluno
 *
 * Este cabeçalho define o contrato do módulo: os tipos e as
 * funções que um programa cliente pode utilizar. Os detalhes de
 * implementação ficam em aluno.c e não precisam ser conhecidos
 * por quem apenas usa a biblioteca.
 */

#define QTD_NOTAS 4

typedef struct {
    int rga;
    char nome[100];
    float notas[QTD_NOTAS];
    float media;
} Aluno;

/* Calcula a média das notas do aluno e armazena em aluno->media. */
void calcularMedia(Aluno *aluno);

/*
 * Calcula a situação do aluno a partir da média já calculada.
 * Retorna uma string constante: "Aprovado", "Recuperacao" ou "Reprovado".
 */
const char *calcularSituacao(const Aluno *aluno);

/* Exibe os dados do aluno (RGA, nome, notas, média e situação). */
void imprimirAluno(const Aluno *aluno);

#endif /* ALUNO_H */
