#include "aluno.h"
#include <stdio.h>

/*
 * aluno.c — Implementação do módulo Aluno
 *
 * Contém os detalhes internos das funções declaradas em aluno.h.
 * O programa cliente não precisa conhecer este arquivo: ele apenas
 * inclui aluno.h e liga o executável à biblioteca compilada.
 */

#define MEDIA_APROVACAO     7.0f
#define MEDIA_RECUPERACAO   5.0f

void calcularMedia(Aluno *aluno) {
    float soma = 0.0f;

    for (int i = 0; i < QTD_NOTAS; i++) {
        soma += aluno->notas[i];
    }

    aluno->media = soma / QTD_NOTAS;

#ifdef DEBUG
    printf("[DEBUG] calcularMedia: RGA=%d soma=%.2f media=%.2f\n",
           aluno->rga, soma, aluno->media);
#endif
}

const char *calcularSituacao(const Aluno *aluno) {
#ifdef DEBUG
    printf("[DEBUG] calcularSituacao: RGA=%d media=%.2f\n",
           aluno->rga, aluno->media);
#endif

    if (aluno->media >= MEDIA_APROVACAO) {
        return "Aprovado";
    } else if (aluno->media >= MEDIA_RECUPERACAO) {
        return "Recuperacao";
    } else {
        return "Reprovado";
    }
}

void imprimirAluno(const Aluno *aluno) {
    printf("\n========================================\n");
    printf("         DADOS DO ALUNO\n");
    printf("========================================\n");
    printf("RGA      : %d\n", aluno->rga);
    printf("Nome     : %s\n", aluno->nome);

    printf("Notas    : ");
    for (int i = 0; i < QTD_NOTAS; i++) {
        printf("%.2f ", aluno->notas[i]);
    }
    printf("\n");

    printf("Media    : %.2f\n", aluno->media);
    printf("Situacao : %s\n", calcularSituacao(aluno));
    printf("========================================\n");
}
