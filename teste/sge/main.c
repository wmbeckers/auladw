#include "aluno.h"
#include <stdio.h>

/*
 * main.c — Programa cliente
 *
 * Observe que este arquivo inclui apenas "aluno.h". Ele não conhece
 * (nem precisa conhecer) o conteúdo de aluno.c: a implementação foi
 * compilada separadamente e será ligada via libaluno.a na etapa de
 * linkedição (-L -l).
 */

static void cadastrarExemplo(Aluno *aluno, int rga, const char *nome,
                              float n1, float n2, float n3, float n4) {
    aluno->rga = rga;
    snprintf(aluno->nome, sizeof(aluno->nome), "%s", nome);
    aluno->notas[0] = n1;
    aluno->notas[1] = n2;
    aluno->notas[2] = n3;
    aluno->notas[3] = n4;
}

int main(void) {
#ifdef DEBUG
    printf("[DEBUG] Modo de depuracao ativado\n");
#endif

    Aluno turma[2] = {0};

    cadastrarExemplo(&turma[0], 1001, "Ana Souza", 8.0f, 7.5f, 9.0f, 8.5f);
    cadastrarExemplo(&turma[1], 1002, "Bruno Lima", 4.0f, 5.5f, 6.0f, 4.5f);

    for (int i = 0; i < 2; i++) {
        calcularMedia(&turma[i]);
        imprimirAluno(&turma[i]);
    }

    return 0;
}
